# Sprint 1 retrospective: selective COPC research and baseline

**Audit date:** October 30, 2026  
**Scope:** the research/benchmark implementation requested in this conversation. Rust learning work is separate and excluded.

## Assessment

**We produced a useful local baseline, but I made the implementation heavier than the decision it needed to support.** Creating isolated tooling was consistent with the approved plan. Choosing a broad 192-package PDAL distribution, adding a second environment, and developing a reusable benchmark toolkit were implementation choices I made. They were not requirements of Rust, DataFusion, RustGIS, or your learning work.

The practical research deliverables were largely achieved: a reuse assessment, a licensed dataset, correct example queries, measured comparisons, and reproducible inputs. The larger strategic question remains open: **what useful capability would a new Rust/DataFusion integration add beyond existing tools?** The measurements do not answer that question affirmatively. They demonstrate existing PDAL functionality, while the SQL probe demonstrates existing DuckDB functionality.

The right response is to review and simplify the proposed ongoing maintenance burden before further implementation. This retrospective makes no cleanup, environment, source-code, staging, or commit changes.

## 1. What the approved plan was trying to accomplish

The plan evolved from a small Rust point-summary exercise into a research-first sprint after you prioritized the point-cloud SQL engine. You explicitly selected research and a baseline instead of implementing the Rust primitive, selective COPC queries, local files first, and a point-cloud download budget below 1 GB.

The final approved scope was:

1. Determine which RustGIS components or underlying libraries could be reused.
2. Investigate existing point-cloud SQL solutions before claiming a gap.
3. Prepare a deterministic fixture and one licensed real COPC asset.
4. Compare a full scan with spatially selective reads using equivalent predicates.
5. Record correctness, timings, memory, provenance, and limitations.
6. Recommend a bounded next step without implementing an engine.

It did **not** require a RustGIS fork, new GIS algorithms, an SQL parser, a DataFusion implementation, Python bindings for the product, a deployed database, an edge service, or changes to your Rust lessons. None of those was implemented. Reading RustGIS and using PDAL as an external baseline are different from adopting either as a production dependency.

## 2. Yes, I created new environments

### Main baseline environment

I downloaded **micromamba 2.10.0**, a standalone manager for conda-format packages, and created:

`benchmarks/pointcloud/.env/`

This is a conda-style environment, despite the generic `.env` directory name. Its Python interpreter and native programs belong to that prefix. The benchmark calls its executables explicitly; it does not require shell activation.

I used conda-forge because PDAL is a native executable with geospatial-library dependencies. A Python virtual environment alone would not supply the PDAL command-line program. Isolating the installation avoided replacing system tools. However, I selected the broad `pdal` package and also explicitly requested `python-pdal`, rather than first finding the smallest package set needed for the CLI baseline.

The installed metadata explains the resulting expansion:

```text
pdal
  → libpdal
    → core + optional Arrow, TileDB, HDF, database and other plugins
      → additional native libraries and their dependencies
  → python-pdal
```

That environment contains **192 conda packages**. Names such as Arrow, PostgreSQL, and cloud SDKs appear because of this distribution's dependency tree. Their installation did not create corresponding project services, cloud accounts, or Rust dependencies.

Two findings make the overprovisioning concrete:

- The installed `libpdal-core` package owns `bin/pdal`.
- None of the final benchmark Python scripts imports the `pdal` Python binding.

Thus the broad metapackage and Python binding were not demonstrated necessities for the final harness. A smaller package selection is worth evaluating if we keep the tooling, but I have not resolved or tested such an alternative in this audit and cannot promise its final dependency count.

### Separate SQL-probe environment

I also created:

`benchmarks/pointcloud/.duckdb-env/`

This is an ordinary Python virtual environment created using the first environment's Python. I installed DuckDB there to test its signed community PDAL extension without upgrading the system DuckDB. The probe tried DuckDB 2.0.0, inspected extension availability for 1.4.5, and ultimately passed with 1.5.6. The final requirements file pins 1.5.6. Extension binaries are stored under `.tools/duckdb-extensions/`.

A second environment was defensible for an isolated compatibility experiment. Keeping it as another permanent project setup is not yet justified.

### What the conda-looking lock file contains

[`environment-osx-arm64.lock`](../../benchmarks/pointcloud/environment-osx-arm64.lock) is **text**, not 192 embedded package archives. It lists exact conda package URLs, builds, and archive MD5 hashes. It records the environment that was installed; it does not establish that every package was needed. MD5 archive identities are also different from the SHA-256 checks used for the bootstrap, dataset, and selected source artifacts.

The actual package binaries are in `.env/`, with package caches/bootstrap tools under `.tools/`. Installation commands targeted workspace-local environments. I did not run `conda init`, edit shell startup files, upgrade system Rust/Python/DuckDB, or change Cargo dependencies.

## 3. Local footprint and Git status

Approximate allocated usage observed with `du` during this audit:

| Location under `benchmarks/pointcloud/` | Usage | Why it exists |
|---|---:|---|
| `.env/` | 735 MB | Main PDAL/Python/native-library environment |
| `.duckdb-env/` | 57 MB | Separate DuckDB Python environment |
| `.tools/` | 514 MB | Micromamba, package caches, downloads, and SQL extension |
| `data/` | 81 MB | Real COPC asset and generated fixture files |
| `runs/` | 11 MB | Preparation outputs, pilots, repeated trials, metadata, and probes |
| `research-cache/` | 744 KB | Downloaded upstream source/metadata snapshots |
| **Whole benchmark directory** | **About 1.4 GB** | Includes the above and versionable inputs/results |

These are approximate filesystem readings, not network-download totals; shared/hardlinked files can affect accounting. The actual public point-cloud asset is **81,123,042 bytes**. We met the **point-cloud data** budget, but that was not a total installation/storage budget. I should have explained the much larger tooling footprint when the dependency solution became visible.

All six local-artifact directories above are ignored by the updated `.gitignore`. The scripts, specifications, fixture source, and selected evidence are eligible for Git tracking. **Ignored does not mean deleted, and untracked does not mean disposable.**

Nothing is staged. The sprint document existed before this work but was ignored; changing the ignore rule makes it appear as a new untracked file. The separate untracked `rust/learn/` work belongs to your parallel learning activity and is not part of this implementation's inventory or any cleanup recommendation.

## 4. Changes made and why

The prior implementation affected **24 versionable artifacts**: 19 benchmark files, two new research/decision documents, and three existing files. The three existing files were `.gitignore`, the literature review, and the formerly ignored sprint specification. This retrospective is the only additional file created by this audit.

| File or group | Change and original purpose | Retrospective judgment |
|---|---|---|
| `.gitignore` | Ignored installations/data/caches and exposed this sprint document to Git. | Appropriate boundary, although it hides substantial local disk usage from ordinary Git status. |
| Existing literature review | Appended the dated second-pass findings and decisions, preserving your observations. | Useful, but some discussion duplicates the landscape note. |
| Existing Sprint 1 specification | Added the revised scope, contract, acceptance record and walkthrough; preserved the original specification in a historical section. | Preserves history, but leaves a long document and an optimistic “implementation complete” status. |
| `docs/research/point-cloud-query-landscape.md` | Added capability comparisons, operation-level reuse decisions, findings, limitations and DataFusion feasibility questions. | The most useful decision-support artifact; it still does not establish an unmet need. |
| `docs/decisions/0001-prioritize-selective-copc-sql.md` | Recorded the engine-first direction and reuse policy. | Reasonable record of direction, not validation of the engine architecture. |
| Benchmark `environment.yml`, `environment-osx-arm64.lock`, `setup.sh`, `verify_environment.py` | Described, pinned, bootstrapped and checked native tooling. | Reproducibility work grew around an unnecessarily broad initial environment choice. |
| Benchmark `datasets.json`, `download.py`, `sources.json` | Recorded license/checksum/source evidence and automated bounded downloading. | Provenance is valuable; a downloader was optional for a single-asset first experiment. |
| Benchmark `fixtures/boundaries.csv`, `fixtures/expected.json`, `cases.json` | Defined hand-checkable data, expected answers and frozen query coordinates. | Strong evidence worth retaining. |
| Benchmark `baseline.py`, `test_baseline.py` | Generated the fixture, computed references, ran trials and tested numerical contracts. | Useful, but a 345-line runner and supporting tests are more infrastructure than the initial decision required. |
| Benchmark `pipelines/fixture-narrow-full_scan.json`, `pipelines/fixture-narrow-copc_bounds.json` | Provided directly inspectable PDAL configurations. | Small, useful explanations of the experiment. |
| Benchmark `duckdb-requirements.txt`, `duckdb_probe.py` | Tested whether existing SQL functionality could answer the same queries. | Strategically important; its separate permanent setup can remain optional. |
| Benchmark `export_evidence.py`, `results/2026-10-30.json`, `README.md` | Retained numeric evidence and documented reproduction and interpretation. | Useful evidence, but the exporter has assumptions that limit general reuse; see below. |

The tracked Rust package has no diff against `HEAD`. I did not implement `Point3D`, modify its package version, or integrate RustGIS/DataFusion into it. No source implementation from RustGIS was copied into this project.

## 5. Results: what they establish

I inspected the saved evidence without rerunning pipelines or installations. Its recorded runner, case and environment-lock hashes still match the current files. I rechecked the saved count/mean assertions for all 238 PDAL trials and recomputed their recorded medians. The retained SQL report contains 17 passing cases. The earlier implementation also reported four passing contract tests; this audit read those tests rather than rerunning them.

The **238 executions are repetitions of 17 cases through two reader paths**, not 238 independently designed correctness scenarios. The final recorded PDAL subprocess wall times total about 349 seconds, excluding earlier pilots/runs, setup, downloads, research and documentation.

| Finding | Supported conclusion | Unsupported conclusion |
|---|---|---|
| Narrow Autzen query: 23,550 matches; median full scan 4.094 s versus COPC 0.254 s | Existing PDAL reader paths differ substantially for this selective local workload. | A new Rust engine is faster, or the exact quantity of source I/O avoided is known. |
| Whole-file query: 3.794 s versus 4.100 s | COPC reading offers no universal speed advantage in this experiment. | A general performance ranking across systems or datasets. |
| DuckDB–PDAL answers all 17 SQL cases | This SQL workload already has a functioning implementation. | Its exact chunk-pruning behavior, memory scaling, or comparative speed was established. |
| Fixture and real-data answers match the reference | The selected cases agree under the declared decoded-f64 arithmetic and aggregate tolerance. | All point formats, malformed inputs, CRS cases, or arithmetic models are correct. |
| RustGIS source was assessed | There are useful reuse/reference candidates and a distinction between visualization sampling and exact analytics. | RustGIS was executed, production-qualified, or integrated. |

The fused-decoding discrepancy was a worthwhile discovery: PDAL and ordinary laspy scaling can disagree by a rounding step at an exact boundary. Aligning the reference's arithmetic made the contract explicit, but it also means the reference is conformance to a **chosen decoding model**, not a neutral proof that only that model is correct. The final hand-calculated fixture uses binary-exact scaling; the separate decimal regression checks arithmetic rather than an end-to-end decimal-fixture pipeline.

## 6. Where I overstretched or left work incomplete

1. **Environment breadth:** I should have inspected the package solution before retaining the full PDAL distribution. The Python PDAL binding is unused by the final scripts, and optional plugins brought in substantial unrelated tooling.
2. **Reusable infrastructure before a confirmed need:** setup verification, downloading, evidence exporting, binary pinning and a full repeated matrix accumulated around a first research question. Each has a rationale, but together they increase the material you must understand and maintain. A smaller experiment could have informed the same immediate decision.
3. **Insufficient learning checkpoints:** progress messages were frequent, but I implemented the entire harness in one session. That did not fully honor the intended small, guided steps and human understanding gate. This concern is about this project's handoff; your separate Rust course is not responsible for absorbing the tooling.
4. **Reproducibility was only partly validated:** the installed package metadata matches the explicit lock and a restore dry run succeeded. I did not perform a clean installation from that lock or have another machine/person reproduce the result. “Reproducible inputs and an exercised local procedure” is more accurate than “independently reproduced.” The package verifier compares conda metadata, not every installed binary's contents.
5. **Coverage and instrumentation remain limited:** one real dataset and one machine; uncontrolled cache, fixed reader order, no source-byte/chunk counters, no remote queries, and no DataFusion execution. Peak RSS does not prove bounded memory as inputs grow. These limitations were documented but materially limit the strategic result.
6. **Prototype assumptions remain in the tooling:** `export_evidence.py` labels any supplied report as a final run without a simultaneous SQL probe and attaches a fixed local probe file if present. That label accurately describes the retained final run from this session, but the exporter does not verify it for future runs. The setup script also leaves an existing environment untouched; the README's separate verification step matters. These are reasons to avoid treating the harness as a finished general benchmark framework.
7. **Completion language was too broad:** the sprint's “implementation complete” status describes artifact creation. It should not imply that the human walkthrough, independent reproduction, production dependency selection, or justification for a new engine is complete.

## 7. Did we achieve the goal?

| Goal | Assessment |
|---|---|
| Research RustGIS and avoid reimplementing general GIS functions | **Achieved at source-review level.** No production reuse was implemented or required. |
| Establish a licensed, correct local baseline | **Achieved for the selected data/cases**, with the stated arithmetic and measurement limits. |
| Test existing SQL capability | **Achieved.** DuckDB–PDAL already answers the workload. |
| Supply a readily reviewable, minimal first sprint | **Only partly achieved.** Evidence is inspectable, but setup and maintenance complexity overshot the immediate need. |
| Prove a useful missing Rust/DataFusion capability | **Not achieved.** A possible interoperability investigation was identified, not a validated gap. |
| Deliver the larger engine/platform | **Not attempted**, as required by the approved scope. |

The baseline was a successful experiment. It is not sufficient reason to automatically proceed with an engine. Existing-tool success is a legitimate research outcome and should reduce speculative implementation.

## 8. Recommended disposition before committing

These are recommendations only; no files, environments or caches were removed or changed during this retrospective.

- **Keep the evidence:** the concise landscape/reuse conclusions, dataset/source provenance, small fixture and expected answers, concrete queries/pipelines, and saved results. Preserve the current lock alongside old results if retaining their exact environment provenance.
- **Review the tooling separately:** decide whether the whole harness deserves maintenance or should remain an archived experiment. Do not solve the concern by adding another abstraction layer or silently rewriting the existing evidence.
- **If the benchmark becomes ongoing work:** evaluate a smaller native package set and remove unused bindings/plugins only in a separate, reviewed change. A new environment/lock would describe a new measurement setup; it should not retroactively relabel old results.
- **Treat ignored installations and caches as local artifacts:** the environments and cached tools can be recreated in principle, but removing the main environment can also break the dependent DuckDB virtual environment. No cleanup is necessary to understand or stage the text artifacts, and no cleanup is performed here.
- **Keep learning changes separate:** review any future research commit independently from your untracked `rust/learn/` files. Nothing in this retrospective authorizes staging, moving or deleting those files.
- **Use a smaller next decision:** first identify one concrete DataFusion interoperability requirement that existing maintained tools do not already satisfy. Only then propose one narrowly bounded integration experiment. If there is no such need, an upstream contribution or a clearly labeled learning exercise is a valid outcome.

My main process correction is to make the installation and maintenance cost visible before expanding an experiment, and to stop at the point where the evidence supports the next decision. We now have enough evidence to pause and review; more infrastructure is not needed to complete this retrospective.

## Audit boundaries

This document is based on the approved plan, prior execution history, the current scoped Git diff/status, environment package metadata, filesystem usage, scripts, and saved result records. No new research downloads, package installations, benchmark executions, commits, cleanup operations or Rust-learning edits were performed. The only new file from this audit is this retrospective.
