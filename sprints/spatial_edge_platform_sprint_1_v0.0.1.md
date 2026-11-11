# Sprint 1 — research closeout and the point-cloud engine sequence

Created: Unknown (original local creation time was not recorded; first tracked on 2026-10-30T22:02:19Z)

Last updated: 2026-11-10T21:57:35Z

**Status:** Plan rewritten; human review and Sprint 1 acceptance pending.

**Current assignment:** Review this plan, then agree on checkpoint 1A.

**First project objective:** A Rust point-cloud SQL query engine using Apache DataFusion.

**Scheduling:** Capability-sized sprints; no calendar duration or deadline has been agreed.

**Version:** The filename is historical; this plan does not assign a package version or release tag.

## 1. Purpose and current state

Build a small, understandable query engine that demonstrates professional engineering
and becomes reusable in later edge, distributed, and hybrid experiments. Learning,
portfolio quality, correctness, and downstream usefulness justify this work. Existing
OSS implementations are references and potential dependencies; proving a market gap
or beating them is not an entry requirement.

The [architecture rule](../.rules/architecture.mdc) is authoritative for project
boundaries. [ADR 0001](../docs/decisions/0001-prioritize-selective-copc-sql.md) records
the earlier research direction; its historical baseline and gap-oriented revisit
language do not make legacy tooling or a novelty claim prerequisites for this sequence.
Any consequential change to an accepted architectural decision needs its own scoped
ADR under the [decision rule](../.rules/documentation_decisions.mdc).

What exists and what does not:

- The reusable Rust package still contains Cargo's `add` scaffold; no project query
  engine, point-summary API, file provider, or spatial pruning has been implemented.
- The [ecosystem review](../docs/research/1-point-cloud-rust-ecosystem-review.md),
  [query landscape](../docs/research/point-cloud-query-landscape.md), and
  [retrospective](../docs/research/sprint-1-retrospective.md) preserve earlier work.
- Earlier PDAL/DuckDB results are recorded experiments. They do not establish
  DataFusion integration, independent reproduction, or human acceptance. They were
  not rerun for this planning rewrite.
- `benchmarks/` is noncanonical historical material. Its packages, environments,
  fixtures, runners, and setup steps are not requirements for new project work.
- The colocated Rust coursework has its own instructions. Do not edit, move, or
  promote exercises into the project as part of this sprint.

**This rewrite replaces the previous oversized active plan, not the historical
experiment.** The full previous sprint text, including its embedded original
specification, remains in Git at context revision
`c19bdea48d10789d1ae4006c00dfcad593d50590`:

```text
git show c19bdea48d10789d1ae4006c00dfcad593d50590:sprints/spatial_edge_platform_sprint_1_v0.0.1.md
```

That reference identifies the pre-rewrite document, not an implementation commit
for this revision. Nothing in the retrospective or benchmark evidence is rewritten.

## 2. One engine, three later operating modes

The user-provided screenshot, `Screenshot 2026-11-05 at 10.19.06.png`, was reviewed
on 2026-11-10. It illustrates one virtual laboratory on a laptop, with three modes:

| Mode | Role of the later query engine | Eventual evidence |
|---|---|---|
| Distributed — cooperation | Coordinated workers query assigned point-cloud partitions and combine results. | Compare the combined answer with one equivalent local query. |
| Edge — autonomy | A node can query its local data and produce a useful result without central availability. | Demonstrate local operation while coordination/connectivity is unavailable. |
| Hybrid — cooperation plus autonomy | Nodes retain local processing while a central component requests and combines selected results. | Show local operation continuing and coordinated results agreeing with a reference. |

Spark appears in the picture as an example coordinator. It is **not a selected
project dependency**. Runtime, transport, coordinator, resource simulation, and
failure contracts will be chosen when those experiments are scoped. Multiple
local processes can investigate behavior but do not prove real device or network
performance. The engine comes first; this sprint installs none of that infrastructure.

Keep the engine in this repository now. Reconsider a separate repository at a
stable engine handoff before downstream integration, rather than splitting it during
research. Python and Swift remain later consumers where a concrete task needs them.

## 3. Sprint 1: close the research pass and agree on the first query

**One reviewable outcome:** an accepted, small first-query assignment grounded in
understood evidence, with historical-tooling disposition visible. No engine code.

Work through **one checkpoint at a time**. Planning all checkpoints does not authorize
executing every one in a single session. If a checkpoint reveals a new investigation
or supporting component, defer it rather than expanding the assignment silently.

| Checkpoint | Human responsibility | Agent assistance | Completion evidence |
|---|---|---|---|
| 1A — understand the useful evidence | Explain one small fixture selection and the meaning/limits of one recorded comparison. | Point to existing sources, explain unfamiliar concepts, review the explanation. No benchmark rerun. | Human explanation or a concise agreed summary linked in the checkpoint log; gaps remain explicit. |
| 1B — decide historical-tooling disposition | Review an inventory and decide which retention/cleanup questions remain deferred. | Prepare a read-only inventory only when this checkpoint is agreed; distinguish tracked evidence, generated data, environments and caches. | Inventory/decision in this record. No deletion, movement, untracking, reinstallation or history rewrite. |
| 1C — agree on the first engine query | Review the small proposed contract below and approve or revise the bounded Sprint 2 assignment. | Explain DataFusion/Arrow responsibilities and identify the package/dependency questions to resolve at Sprint 2 kickoff. | Agreed input, result, verification, ownership and resource boundaries; unresolved items named. |
| 1D — review and close | Confirm understanding and acceptance, consulting documents and code as needed. | Review the actual artifacts and record remaining findings. | Explicit human acceptance or a bounded follow-up. Passing tests or generated prose is not acceptance. |

The walkthrough is open-book and proportionate. You do not need to learn or adopt
the entire legacy benchmark toolchain to close Sprint 1; identify what the evidence
supports and what remains outside the project.

### First-query proposal to review at 1C

The proposed first executable outcome is one local SQL aggregate over a handful of
synthetic points generated in test/example code:

```sql
SELECT COUNT(*) AS point_count, AVG(z) AS mean_z
FROM points;
```

- The initial table has numeric Cartesian `x`, `y`, and `z` coordinates. Use a
  declared synthetic frame with known axis units; add no geographic transformation.
- Preserve duplicates. Empty input produces count zero and null mean Z.
- Use DataFusion for SQL planning and aggregation and Arrow for table batches.
  Do not implement a SQL parser, custom aggregate engine, or a mandatory `Point3D`
  conversion layer simply to reach this query.
- Verify against hand-calculated answers, including empty input and duplicates;
  explain any floating-point tolerance. Spatial/class filters follow in Sprint 3.
- No file reader, database service, network source, CLI framework, Python binding,
  Swift client, or large dataset is needed for this first outcome.

This is a **proposal**, not an API/package decision or installation authorization.
At Sprint 2 kickoff, agree where the Rust component belongs, compatible dependency
versions, manifest changes, and expected build/cache costs before installing anything.
Use Cargo for Rust; do not revive the old conda environment as an engine prerequisite.

### Data and historical evidence boundaries

Autzen was an externally downloaded airborne survey of Autzen Stadium and the
surrounding University of Oregon campus in Eugene, Oregon. `boundaries` was a
14-point synthetic fixture authored locally, not a downloaded survey. The
[historical manifest](../benchmarks/pointcloud/datasets.json) records their origins.
Acknowledging that history does not authorize another download or ongoing dataset use.

Keep all current local artifacts for now, as previously requested. The inventory
checkpoint may identify these categories without removing anything:

- `.env/` and `.duckdb-env/`: related legacy runtime environments.
- `.tools/`: bootstrap tools, package caches, and the SQL extension.
- `data/`: downloaded source data and generated fixture binaries.
- `runs/` and `research-cache/`: recorded outputs and source snapshots.
- Tracked benchmark fixtures/results: a separate migration question, not incidental
  cleanup. The [backlog](backlog.md) preserves that unresolved policy issue.

Protect the retrospective and original evidence. Do not copy tracked legacy data
into new canonical locations as a workaround. New datasets and generated fixture
files belong outside Git under the [data rule](../.rules/pipeline_io.mdc), with
agreed provenance, locations, retention and costs. Code-based fixture generation
can be versioned. A specific dataset choice and acquisition authorization must
precede future downloads.

### Sprint 1 acceptance

- [ ] Human can distinguish the project goal, existing Rust scaffold, and legacy experiments.
- [ ] One recorded query/result and its limitations have been discussed; no novelty requirement remains.
- [ ] Data origins and future acquisition boundaries are understood.
- [ ] Historical-tooling inventory/disposition is reviewed, or explicitly deferred with a revisit trigger.
- [ ] A bounded first-query assignment is agreed without authorizing later sprints.
- [ ] Human review and acceptance are explicitly recorded; no remaining concern is silently closed.

No engine dependency installation, dataset acquisition, benchmark execution, cleanup,
repository extraction, release, staging or commit is part of Sprint 1 closeout.

## 4. Proposed sequential sprints after closeout

These are **candidate capability milestones**, not calendar promises or implementation
authorization. Scope only the next sprint after the current one is accepted. Create
its detailed record only then; use this table for orientation rather than creating
placeholder crates, directories, or ten simultaneous sprint documents.

| Sprint | One principal outcome | Relevant verification and stopping point |
|---|---|---|
| 2 — first local SQL result | Execute the aggregate above over a small generated in-memory Arrow table through DataFusion. | Hand-calculated aggregate, duplicates and empty result; explain the path from points to result. Stop before filtering or files. |
| 3 — exact spatial/attribute query | Add inclusive XYZ bounds and one classification predicate over generated in-memory data. | Inside/outside/face points, duplicates and empty selections; exact counts and documented mean tolerance. Stop before readers or indexes. |
| 4 — one point-cloud reader boundary | Use a suitable existing reader to decode one agreed small local source into bounded Arrow batches while retaining coordinate metadata. | Verify decoded coordinates, attributes, scale/offset, CRS/units, and one relevant failure case. Agree on format/fixture and reader costs first; COPC is the intended indexed target, not a reason to build a parser. No SQL-provider integration yet. |
| 5 — SQL over a local point-cloud source | Connect the accepted reader boundary to DataFusion for the same small query, initially with a full scan. | Compare with the fixture/reference answer; verify required columns and errors. Resolve reader/Send compatibility within a separately bounded assignment if needed. Stop before pruning. |
| 6 — selective COPC reads | Reuse an existing COPC hierarchy to skip irrelevant candidates while preserving exact query results. | Compare with the accepted full-scan result, especially boundaries. Keep residual filters unless exact filtering is guaranteed. Do not implement a new spatial index. |
| 7 — measured engine checkpoint | Record interpretable local execution measurements and a short reproducible engine demonstration. | Separate correctness, wall time, memory and available I/O counters. Report unavailable metrics and losing cases. No new benchmark framework; agree on workload/tool costs first. Review possible repository extraction here, without assuming it is necessary. |
| 8 — autonomous edge mode | Run the accepted query/reduction locally in one worker under one agreed resource or connectivity constraint. | Demonstrate useful local output without a coordinator. A process simulation does not establish hardware performance. Stop before retries, fleet management or multiple constraints. |
| 9 — distributed mode | Coordinate two local workers over distinct partitions and combine one query's results. | Compare with the same query over the union; combine counts/sums correctly rather than averaging averages. Handle a worker failure explicitly. No general distributed query planner or Spark adoption by default. |
| 10 — hybrid mode | Reuse autonomous and coordinated modes together for one query/reduction workload. | Demonstrate local operation during one agreed coordination interruption and a defined return to cooperation; specify duplicate/missing-result semantics before implementation. Stop before general orchestration or additional workloads. |

Before each kickoff, turn its row into one independently reviewable assignment with
human/agent ownership, concrete files, interfaces, exclusions, costs, tests and a
stopping point. If a row is too large after inspection, split it again. Resolve
one blocker before starting the next capability; do not carry hidden infrastructure
work into the same sprint.

Remote object storage, Python interoperability, Swift visualization, architectural
feature classification, weather streams, and richer failure/recovery experiments
are later workstreams. Their inclusion in the platform vision does not put them in
these initial engine assignments.

## 5. Checkpoint log

| Date | Checkpoint | Outcome / remaining work |
|---|---|---|
| 2026-10-30 | Historical agent-led research/baseline | See linked research and retrospective. Evidence exists; human understanding/acceptance was not certified. |
| 2026-11-02 | Scope clarification | Engine learning/portfolio value affirmed without an OSS-gap prerequisite. Research closeout selected; local artifacts retained pending an inventory-only task. |
| 2026-11-10 | Rules-aligned plan rewrite | Sprint 1 bounded to closeout; later capabilities separated into provisional sprints. Screenshot interpreted as operating modes, not tool selection. Document review and 1A agreement pending. |

**Rewrite verification:** current rules, backlog, ADR/research context, screenshot,
repository map freshness and current Rust scaffold inspected. Document links, scope
and diff checked at handoff. No engine, benchmark, network or package-installation
checks were run; the local Beacon recall only queried reviewed memory with uploads off.
No human checkpoint or future implementation is marked complete by this rewrite.

## 27. AI coding-agent contract for Sprint 1

Use the [co-authoring protocol](../.rules/coauthoring_protocol.mdc) for the actual
rules; this section records the assignment boundary rather than a parallel policy.

- This request delegates **the planning-document rewrite**, not engine implementation.
  The human remains the default implementer of later project assignments.
- Before a new assignment, agree on its one outcome, files, ownership, important
  contracts, verification, resource limits and stopping point.
- The agent provides investigation, explanations and sketches for human work.
  Review does not authorize fixes; edits need explicit delegation.
- Unexpected dependencies, environments, supporting components, experiments or
  material costs pause the affected assignment for a scope discussion.
- Keep implementation finished, checks passed, human review pending, and human
  acceptance distinct. Review is open-book and conversational, not memorization.
- Do not modify coursework, legacy benchmarks, datasets or retained evidence while
  implementing a planning task. Do not create infrastructure to represent the roadmap.
- Stop at the agreed checkpoint; proposing the next sprint does not authorize it.
