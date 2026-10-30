#!/usr/bin/env python3
"""Local full-resolution COPC baseline. This is research tooling, not an engine.

Run with .env/bin/python baseline.py --help from this directory.
Reference decoding uses laspy/lazrs; measured decoding uses the PDAL CLI.
"""

import argparse
import csv
import ctypes
from datetime import date
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import statistics
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
# PDAL CLI metadata prints about ten significant digits, not full f64 precision.
ABS_TOL = 1e-7
REL_TOL = 1e-9
MODES = ("full_scan", "copc_bounds")


def fused_decoder():
    # PDAL uses fused multiply/add for scaled coordinates. laspy supplies raw
    # integers, but its ScaledArrayView performs separate NumPy operations.
    fma = ctypes.CDLL(None).fma
    fma.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double]
    fma.restype = ctypes.c_double
    return fma


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def sha256(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def pdal_path():
    executable = Path(sys.executable).parent / "pdal"
    if not executable.is_file():
        raise RuntimeError("Use the pinned environment's Python; sibling pdal is missing")
    return str(executable)


def point_header(path):
    import laspy

    with laspy.open(path) as reader:
        header = reader.header
        crs = header.parse_crs()
        return {
            "point_count": header.point_count,
            "bounds": [header.mins.tolist(), header.maxs.tolist()],
            "scale": header.scales.tolist(),
            "offset": header.offsets.tolist(),
            "crs_wkt": crs.to_wkt() if crs else None,
            "crs_authority": list(crs.to_authority()) if crs and crs.to_authority() else None,
            "projected": crs.is_projected if crs else False,
            "axis_units": [axis.unit_name for axis in crs.axis_info] if crs else [],
        }


def make_cases(header, fixture=False):
    lo, hi = header["bounds"]
    if fixture:
        narrow = [[100, 200, 0], [104, 204, 4]]
        medium = [[99, 199, -1], [106, 206, 6]]
    else:
        def centered(fraction):
            # Keep Z fully constrained to the dataset's native range.
            return [
                [(a + b) / 2 - (b - a) * fraction / 2 if i < 2 else a
                 for i, (a, b) in enumerate(zip(lo, hi))],
                [(a + b) / 2 + (b - a) * fraction / 2 if i < 2 else b
                 for i, (a, b) in enumerate(zip(lo, hi))],
            ]
        narrow, medium = centered(0.05), centered(0.5)
    outside = [[b + max(b - a, 1) for a, b in zip(lo, hi)],
               [b + 2 * max(b - a, 1) for a, b in zip(lo, hi)]]
    result = [
        {"id": "all", "bounds": None, "classification": None},
        {"id": "empty", "bounds": outside, "classification": None},
        {"id": "narrow", "bounds": narrow, "classification": None},
        {"id": "medium", "bounds": medium, "classification": None},
        {"id": "whole_bbox", "bounds": [lo, hi], "classification": None},
        {"id": "narrow_class6", "bounds": narrow, "classification": 6},
        {"id": "medium_class6", "bounds": medium, "classification": 6},
        {"id": "all_class6", "bounds": None, "classification": 6},
    ]
    if fixture:
        result.append({"id": "exact_point", "bounds": [[100, 200, 0], [100, 200, 0]],
                       "classification": None})
    return result


def expression(case):
    conditions = []
    if case["bounds"] is not None:
        for dimension, low, high in zip("XYZ", *case["bounds"]):
            conditions.extend([f"{dimension} >= {low:.17g}", f"{dimension} <= {high:.17g}"])
    if case["classification"] is not None:
        conditions.append(f"Classification == {int(case['classification'])}")
    return " && ".join(conditions)


def pipeline(path, case, mode):
    if mode not in MODES:
        raise ValueError(mode)
    reader = {"type": "readers.las", "filename": str(Path(path).resolve()),
              "threads": 1} if mode == "full_scan" else {
                  "type": "readers.copc", "filename": str(Path(path).resolve()),
                  "requests": 1, "keep_alive": 1}
    if mode == "copc_bounds" and case["bounds"] is not None:
        reader["bounds"] = "(" + ",".join(
            f"[{low:.17g},{high:.17g}]" for low, high in zip(*case["bounds"])) + ")"
    stages = [reader]
    if predicate := expression(case):
        stages.append({"type": "filters.expression", "expression": predicate})
    stages.extend([{"type": "filters.stats", "dimensions": "Z"}, {"type": "writers.null"}])
    return {"pipeline": stages}


def reference(path, cases):
    """One laspy/lazrs scan; independent NumPy predicates and math.fsum means.

    Keep only chunk partial sums, not whole-file coordinates. The reference is
    prepared outside timed trials; it is not a performance competitor.
    """
    import laspy
    import numpy as np

    fma = fused_decoder()
    partials = {case["id"]: [] for case in cases}
    counts = dict.fromkeys(partials, 0)
    with laspy.open(path) as reader:
        for points in reader.chunk_iterator(100_000):
            xyz = [np.fromiter((fma(float(value), float(scale), float(offset)) for value in
                               getattr(points, dimension)), dtype=np.float64, count=len(points))
                   for dimension, scale, offset in zip("XYZ", reader.header.scales, reader.header.offsets)]
            if not all(np.isfinite(values).all() for values in xyz):
                raise ValueError("Non-finite coordinate in benchmark input")
            for case in cases:
                mask = np.ones(len(points), dtype=bool)
                if case["bounds"] is not None:
                    for values, low, high in zip(xyz, *case["bounds"]):
                        mask &= (values >= low) & (values <= high)
                if case["classification"] is not None:
                    mask &= np.asarray(points.classification) == case["classification"]
                selected = xyz[2][mask]
                counts[case["id"]] += len(selected)
                partials[case["id"]].append(math.fsum(selected))
    return {name: {"count": count, "mean_z": math.fsum(partials[name]) / count if count else None}
            for name, count in counts.items()}


def assert_result(actual, expected):
    if actual["count"] != expected["count"]:
        raise AssertionError(f"Count mismatch: {actual} != {expected}")
    if expected["mean_z"] is None:
        if actual["mean_z"] is not None:
            raise AssertionError("Empty SQL AVG must map to null")
    elif actual["mean_z"] is None or not math.isclose(
            actual["mean_z"], expected["mean_z"], rel_tol=REL_TOL, abs_tol=ABS_TOL):
        raise AssertionError(f"Mean mismatch: {actual} != {expected}")


def parse_stats(metadata):
    stats = metadata["stages"]["filters.stats"]["statistic"]
    if isinstance(stats, dict):
        stats = [stats]
    z_stats = [item for item in stats if item["name"] == "Z"]
    if len(z_stats) != 1:
        raise ValueError("Expected exactly one Z statistic")
    count = int(z_stats[0]["count"])
    mean = float(z_stats[0]["average"]) if count else None
    if mean is not None and not math.isfinite(mean):
        raise ValueError("Non-finite PDAL mean")
    return {"count": count, "mean_z": mean}


def run_trial(config, directory):
    directory.mkdir(parents=True, exist_ok=True)
    config_path, metadata_path = directory / "pipeline.json", directory / "metadata.json"
    save(config_path, config)
    if platform.system() != "Darwin":
        raise RuntimeError("This runner measures macOS /usr/bin/time -l RSS in bytes")
    command = ["/usr/bin/time", "-l", pdal_path(), "pipeline", str(config_path),
               "--stream", "--metadata", str(metadata_path)]
    started = time.perf_counter()
    completed = subprocess.run(command, capture_output=True, text=True, timeout=600,
                               env={**os.environ, "OMP_NUM_THREADS": "1"})
    elapsed = time.perf_counter() - started
    (directory / "stderr.txt").write_text(completed.stderr)
    if completed.returncode:
        raise RuntimeError(f"PDAL failed ({completed.returncode}): {completed.stderr}")
    match = re.search(r"(\d+)\s+maximum resident set size", completed.stderr)
    if not match:
        raise ValueError("macOS peak RSS missing")
    result = parse_stats(json.loads(metadata_path.read_text()))
    return {**result, "wall_seconds": elapsed, "peak_rss_bytes": int(match[1]),
            "source_bytes_read": None, "chunks_decoded": None, "chunks_pruned": None}


def prepare():
    import laspy
    import numpy as np
    from pyproj import CRS

    started = time.perf_counter()
    with (ROOT / "fixtures/boundaries.csv").open() as stream:
        rows = list(csv.DictReader(stream))
    header = laspy.LasHeader(point_format=6, version="1.4")
    header.creation_date = date(2026, 10, 30)
    header.scales = np.array([0.125, 0.125, 0.125])
    header.offsets = np.array([100, 200, -5])
    header.add_crs(CRS.from_epsg(32618))
    cloud = laspy.LasData(header)
    for name in "xyz":
        setattr(cloud, name, [float(row[name.upper()]) for row in rows])
    cloud.classification = np.array([int(row["Classification"]) for row in rows], dtype=np.uint8)
    target = ROOT / "data/boundaries.las"
    target.parent.mkdir(parents=True, exist_ok=True)
    cloud.write(target)
    config = {"pipeline": [str(target), {"type": "writers.copc",
              "filename": str(ROOT / "data/boundaries.copc.laz"), "forward": "all"}]}
    save(ROOT / "runs/fixture-pipeline.json", config)
    subprocess.run([pdal_path(), "pipeline", str(ROOT / "runs/fixture-pipeline.json")], check=True)
    manifest = json.loads((ROOT / "datasets.json").read_text())
    prepared = []
    for entry in manifest["datasets"]:
        path = ROOT / entry["path"]
        if not path.is_file():
            raise FileNotFoundError(path)
        digest = sha256(path)
        if entry.get("sha256") and entry["sha256"] != digest:
            raise ValueError(f"Checksum mismatch: {path}")
        info = point_header(path)
        if not info["projected"]:
            raise ValueError("A projected CRS is required")
        cases = json.loads((ROOT / "cases.json").read_text())[entry["id"]]
        results = reference(path, cases)
        if not results["all_class6"]["count"]:
            raise ValueError("Dataset has no classification 6 points")
        if entry["id"] == "boundaries":
            manual = json.loads((ROOT / "fixtures/expected.json").read_text())
            for case in cases:
                expected = manual[case["id"]]
                count = expected["count"]
                assert_result(results[case["id"]], {"count": count,
                              "mean_z": expected["sum_z"] / count if count else None})
        directory = ROOT / "runs/prepared" / entry["id"]
        save(directory / "cases.json", cases)
        save(directory / "reference.json", results)
        for case in cases:
            for mode in MODES:
                save(directory / f"{case['id']}-{mode}.json", pipeline(path, case, mode))
        prepared.append({**entry, **info, "sha256": digest, "size_bytes": path.stat().st_size})
    save(ROOT / "runs/preparation.json", {"seconds": time.perf_counter() - started,
         "includes": "fixture conversion, checksums, independent scans, cases and pipeline generation; excludes download",
         "datasets": prepared})
    print("Prepared and reference-checked both datasets", flush=True)


def run(output):
    output = Path(output).resolve()
    if output.exists():
        raise FileExistsError(f"Choose a new output directory: {output}")
    output.mkdir(parents=True)
    prepared = json.loads((ROOT / "runs/preparation.json").read_text())
    records = []
    for dataset in prepared["datasets"]:
        path = ROOT / dataset["path"]
        if sha256(path) != dataset["sha256"]:
            raise ValueError(f"Input changed since preparation: {path}")
        directory = ROOT / "runs/prepared" / dataset["id"]
        cases = json.loads((directory / "cases.json").read_text())
        expected = json.loads((directory / "reference.json").read_text())
        for case in cases:
            for mode in MODES:
                config = pipeline(path, case, mode)
                # First observed run, one explicit warm-up, five measured repetitions.
                trials = []
                for phase in ("first_observed", "warmup", "measured_1", "measured_2",
                              "measured_3", "measured_4", "measured_5"):
                    result = run_trial(config, output / dataset["id"] / case["id"] / mode / phase)
                    assert_result(result, expected[case["id"]])
                    trials.append({"phase": phase, **result})
                measured = trials[2:]
                record = {"dataset": dataset["id"], "case": case, "mode": mode,
                          "reference": expected[case["id"]], "trials": trials,
                          "selectivity": expected[case["id"]]["count"] / dataset["point_count"],
                          "median_wall_seconds": statistics.median(t["wall_seconds"] for t in measured),
                          "max_peak_rss_bytes": max(t["peak_rss_bytes"] for t in measured)}
                records.append(record)
                save(output / "partial.json", records)
                print(f"PASS {dataset['id']} {case['id']} {mode}: "
                      f"{record['median_wall_seconds']:.3f}s", flush=True)
    report = {
        "schema_version": 1, "date": date.today().isoformat(), "platform": platform.platform(),
        "machine": platform.machine(), "processor": platform.processor(),
        "python": sys.version, "pdal": subprocess.check_output([pdal_path(), "--version"], text=True).strip(),
        "cpu": subprocess.check_output(["/usr/sbin/sysctl", "-n", "machdep.cpu.brand_string"], text=True).strip(),
        "memory_bytes": int(subprocess.check_output(["/usr/sbin/sysctl", "-n", "hw.memsize"], text=True)),
        "environment_lock_sha256": sha256(ROOT / "environment-osx-arm64.lock"),
        "runner_sha256": sha256(ROOT / "baseline.py"),
        "cases_sha256": sha256(ROOT / "cases.json"),
        "tolerance": {"absolute": ABS_TOL, "relative": REL_TOL},
        "measurement": "PDAL child process; CLI startup, reading, filtering, statistics and null writer included; Python reference and fixture preparation excluded",
        "cache": "Uncontrolled OS page cache; first_observed is not cold-cache evidence; full_scan runs before copc_bounds",
        "concurrency": "OMP_NUM_THREADS=1; LAS threads=1; COPC requests=1 and keep_alive=1; stream capacity is PDAL default",
        "unavailable": ["source_bytes_read", "chunks_decoded", "chunks_pruned"],
        "preparation": prepared, "results": records,
    }
    save(output / "report.json", report)
    print(f"Report: {output / 'report.json'}", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("prepare")
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare()
    else:
        run(args.output)


if __name__ == "__main__":
    main()
