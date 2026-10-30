#!/usr/bin/env python3
"""Isolated signed DuckDB-PDAL compatibility/correctness probe, not a timing comparison."""
import json
from pathlib import Path
import platform
import time

import duckdb
from baseline import ROOT, assert_result, save, sha256


def main():
    started = time.perf_counter()
    output = ROOT / f"runs/duckdb-probe-{duckdb.__version__}.json"
    extensions = ROOT / ".tools/duckdb-extensions"
    extensions.mkdir(parents=True, exist_ok=True)
    result = {"duckdb": duckdb.__version__, "platform": platform.platform(),
              "unsigned_extensions": False, "status": "not_run", "queries": []}
    try:
        connection = duckdb.connect(":memory:", config={"extension_directory": str(extensions),
                                                       "threads": "1"})
        connection.execute("INSTALL pdal FROM community")
        connection.execute("LOAD pdal")
        result["extension"] = connection.execute(
            "SELECT extension_name, extension_version, installed_from FROM duckdb_extensions() "
            "WHERE extension_name = 'pdal'").fetchall()
        extension_files = list(extensions.rglob("v1.5.6/osx_arm64/pdal.duckdb_extension"))
        expected_hash = "c3d3282c33ed5650e581e6f537d67c86ec14e1157dbe904e49cb127e048db65a"
        if (len(extension_files) != 1 or sha256(extension_files[0]) != expected_hash
                or result["extension"][0][1] != "482655f"):
            raise ValueError("Signed extension changed; review/pin its source and binary before comparing results")
        for dataset in ("boundaries", "autzen"):
            folder = ROOT / "runs/prepared" / dataset
            cases = json.loads((folder / "cases.json").read_text())
            expected = json.loads((folder / "reference.json").read_text())
            path = ROOT / "data" / ("boundaries.copc.laz" if dataset == "boundaries" else "autzen-classified.copc.laz")
            literal = "'" + str(path).replace("'", "''") + "'"
            for case in cases:
                where = []
                if case["bounds"] is not None:
                    where += [f'{d} BETWEEN {low:.17g} AND {high:.17g}'
                              for d, low, high in zip("XYZ", *case["bounds"])]
                if case["classification"] is not None:
                    where.append(f"Classification = {case['classification']}")
                sql = f"SELECT COUNT(*), AVG(Z) FROM PDAL_Read({literal})"
                if where:
                    sql += " WHERE " + " AND ".join(where)
                count, mean = connection.execute(sql).fetchone()
                actual = {"count": count, "mean_z": mean}
                assert_result(actual, expected[case["id"]])
                plan = connection.execute("EXPLAIN " + sql).fetchall()
                result["queries"].append({"dataset": dataset, "case": case["id"],
                                           "sql": sql, **actual, "plan": plan})
                save(output, result)
                print(f"PASS DuckDB {dataset} {case['id']}", flush=True)
        result["status"] = "passed"
        result["extension_files"] = [
            {"path": str(p.relative_to(extensions)), "sha256": sha256(p)}
            for p in extensions.rglob("*.duckdb_extension")]
    except Exception as error:
        result["status"] = "failed"
        result["error"] = str(error)
        raise
    finally:
        result["setup_and_probe_seconds"] = time.perf_counter() - started
        save(output, result)


if __name__ == "__main__":
    main()
