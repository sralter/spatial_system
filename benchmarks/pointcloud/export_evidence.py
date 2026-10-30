#!/usr/bin/env python3
"""Export compact, shareable evidence while retaining all numeric trial records."""
import argparse
import json
from pathlib import Path

from baseline import ROOT, save


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = json.loads(args.report.read_text())
    probe = ROOT / "runs/duckdb-probe-1.5.6.json"
    if probe.exists():
        # Normalize only path strings; numeric answers and plan structure stay intact.
        report["duckdb_correctness_probe"] = json.loads(
            probe.read_text().replace(str(ROOT), "<benchmark-root>"))
    failed = ROOT / "runs/duckdb-probe.json"
    if failed.exists():
        report["duckdb_2_0_attempt"] = json.loads(failed.read_text().replace(str(ROOT), "<benchmark-root>"))
    report["export_note"] = "PDAL final run, no concurrent SQL probe; DuckDB path strings normalized for sharing. Different tools were not timed competitively."
    save(args.output, report)
    print("| Autzen case | Count | Full scan median (s) | COPC median (s) | Full / COPC peak MiB |")
    print("|---|---:|---:|---:|---:|")
    grouped = {}
    for record in report["results"]:
        if record["dataset"] == "autzen":
            grouped.setdefault(record["case"]["id"], {})[record["mode"]] = record
    for name, records in grouped.items():
        full, copc = records["full_scan"], records["copc_bounds"]
        print(f"| {name} | {full['reference']['count']:,} | {full['median_wall_seconds']:.3f} | "
              f"{copc['median_wall_seconds']:.3f} | {full['max_peak_rss_bytes']/2**20:.1f} / "
              f"{copc['max_peak_rss_bytes']/2**20:.1f} |")


if __name__ == "__main__":
    main()
