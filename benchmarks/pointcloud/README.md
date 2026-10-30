# Local selective-COPC baseline

This directory is research tooling, not a query engine. The Rust library is
unchanged. It compares PDAL sequential LAS/LAZ reading with COPC bounds selection,
then applies the same exact XYZ/classification predicates and Z statistics.

The retained evidence is [results/2026-10-30.json](results/2026-10-30.json).
It includes every first-observed, warm-up and measured result, not just favorable
timings. The [landscape](../../docs/research/point-cloud-query-landscape.md) explains
reuse and the DataFusion feasibility gate. Raw pipelines and full PDAL metadata
are regenerated into ignored `runs/` directories.

## Reproduce on macOS ARM64

From this directory:

```bash
bash setup.sh
.env/bin/python verify_environment.py
.env/bin/python download.py
.env/bin/python baseline.py prepare
.env/bin/python -m unittest discover -p 'test_*.py' -v
.env/bin/python baseline.py run --output runs/my-baseline
.env/bin/python export_evidence.py runs/my-baseline/report.json --output runs/my-evidence.json
```

Network access is needed for setup and the first asset download. `setup.sh` pins
micromamba 2.10.0 with a SHA-256 archive check, then installs exact conda-forge
package URLs/archive hashes from `environment-osx-arm64.lock`. `environment.yml`
describes the main packages; the explicit lock, not a fresh solver run, defines the
tested environment. No system tool, shell configuration or global Python package
is changed. The conda package set is broad because the PDAL distribution includes
optional plugins; no decision to use those plugins in an engine is implied.

The runner requires macOS `/usr/bin/time -l` and permission to query its resource
counters. A restricted sandbox may block those counters; run the benchmark from
an ordinary local terminal in that case. Peak RSS is the PDAL child process's
maximum resident set in **bytes**. The runner deliberately rejects unsupported
platforms rather than mixing Linux KiB and macOS byte measurements. Porting needs
a separately reviewed resource-measurement implementation and environment lock.

`prepare` regenerates the fixture, verifies the public asset checksum, validates a
projected CRS and class 6, and calculates independent references. It loads the
committed `cases.json`; query coordinates do not drift between runs. It writes
concrete per-case PDAL pipeline JSON and references under `runs/prepared/`.
Fixture creation date, scale, offset and source coordinates are fixed. COPC binary
layout may differ across PDAL versions; correctness is checked against the CSV and
hand calculations, not a universal binary checksum.

The reference uses raw laspy/lazrs point records and C fused multiply/add, matching
PDAL's coordinate-decoding arithmetic without using PDAL's reader. NumPy applies
the predicates independently; `math.fsum` computes chunk partial sums and the
final mean. Its runtime is preparation cost, never part of a trial. Invalid
numeric input is rejected. Empty selections use count zero and mean null.

## Data and attribution

- [datasets.json](datasets.json) records URLs, SHA-256, license, attribution and
  preparation. Downloaded point-cloud bytes total **81,123,042**, below 1 GB. Tools
  and package downloads are separate from this point-cloud data budget.
- Autzen: Watershed Sciences, Inc. acquisition (2010), Max Sampson/Hobu, Inc.
  classification (2021), distributed by pointcloud.org/PDAL under CC-BY-4.0.
  [Publisher](https://pointcloud.org/datasets/autzen/),
  [license](https://github.com/PDAL/data/blob/main/LICENSE),
  [acquisition/classification notes](https://github.com/PDAL/data/blob/main/autzen/README.md).
  Downloaded asset unchanged; do not infer its data license from a code license.
- Autzen has **10,653,336** points. Horizontal CRS EPSG:2992 uses international
  feet; vertical CRS EPSG:6360 uses US survey feet. Preserve both units.
- The 14-row [synthetic CSV](fixtures/boundaries.csv) is original benchmark data
  under this repository's MIT license. Hand-calculated counts/sums are in
  [expected.json](fixtures/expected.json). It includes duplicates and points on
  and just outside box faces. Scale 0.125 and offsets `[100,200,-5]` are nontrivial
  but exactly representable. EPSG:32618 is synthetic fixture metadata, not an
  assertion that those tiny coordinates represent a surveyed location.
- Millsite is cataloged for follow-up only: its public asset reports 1,445,463,233
  bytes in an October 30 HEAD response. No point bytes were downloaded; exact
  provenance/license must be verified before downloading. Its multipart ETag is
  not a SHA-256 checksum. No second real-data execution or scale trend is claimed.

## What is measured

There are 9 fixture cases and 8 real-data cases. Each runs through both readers:
17 × 2 × (first-observed + one warm-up + five measured trials) = **238 PDAL
executions**. All trial answers must match the reference. Counts are exact; means
allow absolute `1e-7` or relative `1e-9` error because PDAL CLI metadata prints
approximately ten significant digits. The decimal-scale/fused-decoding regression
test prevents hiding boundary-count errors inside an aggregate tolerance.

Full scan: `readers.las`, `threads=1`. Selective scan: `readers.copc`, `requests=1`,
`keep_alive=1`, bounds when present. Both use `filters.expression`, `filters.stats`
on Z and `writers.null`; `--stream` is required, with no resolution or point-count
limit. OpenMP is limited to one thread. Stream capacity remains the PDAL default;
it is not claimed to be a specified cross-version buffer size.

Wall time includes subprocess/CLI startup and all PDAL stages. Peak RSS excludes
the Python parent/reference. Preparation time is recorded separately; first-time
package installation and asset download are not query latency. The final suite
runs without a simultaneous DuckDB probe. It is not a CPU-isolated experiment.

OS cache is uncontrolled and reference preparation has read the file. Full scans
precede selective scans. The first observation is **not** a cold-cache measurement.
Report each trial and use median wall time over the five measured repetitions.

No reliable source-byte or chunk counters are collected. They are explicitly null.
Output count/selectivity does not measure bytes avoided. A measured peak RSS on one
tile is not proof of bounded memory as datasets grow. There are no remote-I/O,
DataFusion, multi-machine, or cross-tool speed results in this report.

## Recorded results — October 30, 2026

Apple M2, 24 GiB RAM, macOS 26.3.1 ARM64, PDAL 2.10.2, Python 3.12.16.
All **238** final PDAL executions passed their reference checks. The reference,
fixture conversion, checksum checks and configuration preparation took **16.743 s**
in the recorded preparation pass, outside query timings.

| Autzen case | Count | Full scan median (s) | COPC median (s) | Full / COPC peak MiB |
|---|---:|---:|---:|---:|
| all | 10,653,336 | 3.794 | 4.100 | 101.3 / 107.2 |
| empty | 0 | 4.249 | 0.090 | 100.2 / 37.9 |
| narrow | 23,550 | 4.094 | 0.254 | 96.0 / 75.7 |
| medium | 2,873,397 | 4.075 | 1.824 | 94.0 / 99.6 |
| whole_bbox | 10,653,336 | 4.135 | 3.896 | 98.1 / 93.0 |
| narrow_class6 | 0 | 4.161 | 0.252 | 99.8 / 73.6 |
| medium_class6 | 135,262 | 4.171 | 1.957 | 94.9 / 90.5 |
| all_class6 | 343,181 | 3.942 | 3.797 | 97.1 / 103.4 |

Peak MiB is the maximum process RSS across the five measured repetitions, not a
median. Narrow-box selectivity is about 0.221%; medium-box selectivity about 26.97%.
The narrow building query is empty; medium and whole-file building queries provide
nonempty attribute-filter cases. Whole-file timings show no consistent reader
advantage; a full-resolution SQL wrapper alone does not create an indexing benefit.
These results demonstrate PDAL's existing selective reader, not a future Rust engine.

Four numerical/fixture contract tests pass. The exact 192-package environment was
verified against its lock, and an explicit-lock restore dry run succeeded. A second
machine and a clean installation from the committed lock were not independently
tested. The initial solved environment is the one used for the measurements.

## Separate DuckDB correctness probe

```bash
.env/bin/python -m venv .duckdb-env
PIP_CACHE_DIR="$PWD/.tools/pip-cache" .duckdb-env/bin/python -m pip install -r duckdb-requirements.txt
.duckdb-env/bin/python duckdb_probe.py
```

This installs/loads the **signed** community PDAL extension in `.tools/duckdb-extensions`;
unsigned loading is not enabled. DuckDB 1.5.6 passed all 17 equivalent SQL cases.
Its extension reports revision `482655f`; its binary hash and EXPLAIN plans are
retained, and the probe rejects a changed binary pending review. The separately inspected upstream README is pinned to a newer revision
and must not be mistaken for the tested binary's exact implementation.

DuckDB 2.0.0's macOS ARM64 PDAL extension returned HTTP 404; the 1.4.5 extension
endpoint also returned 404. Version 1.5.6 was selected after confirming availability.
These are dated compatibility observations, not permanent support statements.
The probe records setup-plus-query time but is **not a comparable latency benchmark**:
its process, options and measurement boundary differ from the timed PDAL runs.

## Review before the next vertical

Walk through one narrow-box pipeline and calculate the fixture count/mean manually.
Explain why a hierarchy-overlapping chunk still needs exact point filtering, why
COUNT must match exactly, and why source units and fused decoding affect the
contract. Then review the DataFusion `Inexact`/residual-filter and Send-future
questions in the landscape note. Propose the next files/API before engine editing.
