# Spatial Edge Platform — Sprint 1: selective COPC query research

**Revision:** 2026-10-30  
**First overall goal:** Rust/DataFusion point-cloud SQL engine  
**Sprint deliverable:** research, reuse decisions, and a reproducible local baseline  
**Status:** implementation complete; user walkthrough and next-vertical review pending  
**Version:** no package version change or release tag in this research sprint

This revision supersedes the implementation-first scope of the original document,
which is preserved below as historical context. The umbrella remains Rust/Python/Swift
and edge/distributed computing. The first subsystem investigates selective COPC queries.
The original Point3D/summary implementation is paused, not a prerequisite for this sprint.

## 1. Objective and scope

Establish whether a bounded DataFusion COPC integration is useful alongside existing
SQL and GIS tooling. Deliver correct, reproducible evidence before engine code.
General GIS operations, SQL planning, parsing and point-file decoding should use
suitable existing implementations. RustGIS is an important reuse/reference candidate,
not an automatic whole-application dependency.

Execute local-file baselines only, with less than 1 GB of downloaded point-cloud
assets. Python is permitted for research scripts and independent references. No
production bindings, engine crate, custom format/parser, UI, networking service,
spatial index, Swift, ML, edge node or distributed system is added.

## 2. Required artifacts

- Preserve the original literature-review observations and append a dated assessment.
- Record a capability/evidence matrix and operation-level reuse decisions.
- Pin inspected RustGIS sources and distinguish documentation, source inspection,
  and actual executable results; preserve attribution on any future adaptation.
- Create ADR 0001 explaining the engine-first direction and reuse policy.
- Commit benchmark environment specification/lock, dataset manifest, concrete cases,
  fixture, hand-calculated expectations, configurations/generator, runner, reference
  checker, tests, and selected numeric evidence.
- Ignore downloaded assets, environments, caches and bulk run outputs.

References: [landscape](../docs/research/point-cloud-query-landscape.md),
[ADR](../docs/decisions/0001-prioritize-selective-copc-sql.md),
[benchmark reproduction](../benchmarks/pointcloud/README.md).

## 3. Workload contract

COUNT(*) and AVG(Z), over all points, inclusive XYZ boxes, and boxes plus classification
6. Use full resolution without sampling or a point-count cap. Return count zero and
mean null for an empty selection. Mean Z is not height above ground.

Preserve native coordinate arithmetic, scale/offset, CRS and per-axis units. The
independent reference decodes laspy/lazrs raw records with fused multiply/add to
match the declared PDAL f64 decoding contract; its predicates and summation are
independent of PDAL. The synthetic fixture uses binary-exact scale/offset so manual
boundary answers remain exact. A separate test records decimal-scale rounding.

## 4. Measurement contract

Compare streaming readers.las full scans with readers.copc bounds selection, followed
by identical exact expressions and Z statistics. Record first-observed behavior,
one warm-up and five measured repetitions per case/reader. Freeze query coordinates.
Record elapsed wall time, child-process peak RSS, selectivity, preparation cost,
versions, environment lock, machine, concurrency, and tolerance.

Counts match exactly; mean tolerance is absolute 1e-7 or relative 1e-9, accounting
for CLI metadata precision. Do not label the uncontrolled OS page cache cold. Do not
infer source bytes or chunks skipped from output counts or file sizes. Unavailable
counters are null. The final PDAL run must not overlap a separate SQL probe.

## 26. Acceptance evidence

- [x] Pinned RustGIS assessment and operation-level reuse matrix.
- [x] Existing SQL alternatives investigated: pgPointcloud and DuckDB–PDAL.
- [x] Licensed real COPC plus deterministic boundary/duplicate fixture prepared.
- [x] Native CRS, scale/offset, checksum, classification and axis units recorded.
- [x] Isolated PDAL environment with exact native-platform package lock.
- [x] Full-scan and selective-reader counts/means checked against an independent reference.
- [x] Signed DuckDB–PDAL 1.5.6 probe passes the equivalent 17 SQL cases.
- [x] Numerical-conformance tests pass; no Rust source or version edits.
- [x] Five-repeat timing/RSS evidence and limitations retained.
- [x] DataFusion feasibility questions and next-vertical recommendation documented.
- [ ] Samuel completes the walkthrough below.
- [ ] Review and choose the next bounded code/API proposal or upstream contribution.

Machine-readable evidence: [baseline results](../benchmarks/pointcloud/results/2026-10-30.json).
The checkboxes describe artifact/experiment completion, not independent product validation,
a performance advantage for a new engine, or an automatically approved next implementation.

## 27. AI coding-agent contract for the revised sprint

Use the agent as an implementation partner. Before a new scope of work:

1. Inspect the repository and applicable instructions.
2. Enumerate the concrete files to create/modify and explain each responsibility.
3. Stop at the proposal until the user reviews that scope. An explicit request to
   implement an already-reviewed plan authorizes that scope; do not request it again.
4. Work in small explained steps. Preserve existing user edits and learning artifacts.
5. Reuse suitable public APIs. Record any copied/adapted source's revision and notices.
6. Run checks appropriate to changed artifacts and report actual results and limitations.
7. Do not add engine features or unrelated platform infrastructure to finish a research task.
8. Do not automatically merge, publish, tag, contact maintainers, or mark a human
   understanding gate complete.

The implementation request for this revision authorizes the research files and
benchmark tooling enumerated before editing. The Rust package, learning notes,
existing exercises and package version remain unchanged. Cargo checks are not a
completion gate for unchanged Rust code; benchmark conformance and reproduction are.

## 28. Understanding gate

Before choosing the next engine vertical, Samuel should:

- Explain the fixture's narrow-box count and mean without running the agent.
- Trace the full-scan and COPC-bound pipelines and explain residual filtering.
- Explain the fused-decoding boundary discrepancy and source-axis units.
- Distinguish sampling, decoding, projection, spatial pruning and result selectivity.
- Explain what the timing/RSS measurements include and which counters are missing.
- Describe what RustGIS/its underlying libraries could supply, and what remains unproven.
- Explain why existing SQL support changes the contribution claim.

## 29. Next decision

Review the measured baseline and DataFusion feasibility note. The recommended next
vertical is a bounded local COPC-to-DataFusion interoperability/measurement spike,
starting with released-reader and Send compatibility. Reuse DataFusion aggregates
and Arrow batches; add conservative pruning only after exact semantics pass. If an
existing maintained adapter covers the need, contribute conformance tests or
instrumentation instead. Present concrete files and API before implementation.

---

<details>
<summary>Historical original Sprint 1 specification — superseded by the revision above</summary>

# Spatial Edge Platform — Sprint 1 / v0.0.1

**Working title:** Spatial Edge Platform  
**Sprint:** 1  
**Version target:** `v0.0.1`  
**Primary language:** Rust  
**Primary component:** `rust/spatial-core`  
**Sprint theme:** Establish the smallest trustworthy 3D spatial systems primitive  
**Status:** Planning  
**Date:** October 2026

---

# 1. Purpose of This Sprint

Sprint 1 is the first implementation vertical of the larger **Spatial Edge Platform**.

The long-term project is intended to become a multi-language spatial computing system that combines:

- **Rust** for performance-sensitive, systems-level spatial processing;
- **Python** for orchestration, modeling, experimentation, analytics, and central coordination;
- **Swift** for native UI, visualization, and eventual device-facing or edge-facing interaction;
- **point-cloud processing and classification**, eventually including classification of architectural features such as doors versus windows;
- **distributed and edge computing**, including simulated constrained nodes;
- **weather observations** as a second data stream for learning continuous edge-data processing and delivery to a central hub;
- an architectural model inspired by **onboard satellite processing**, where useful computation occurs close to the sensor so that reduced or higher-value information is transmitted rather than all raw data;
- a possible **point-cloud SQL/query-engine track**, potentially using columnar storage, spatial partitioning, indexing, Arrow/Parquet concepts, and DataFusion-like query execution.

Sprint 1 should **not** attempt to implement this entire system.

Its purpose is to create the first small, production-quality Rust component that can credibly become part of that future architecture.

The central principle is:

> **Build the smallest real component that teaches the right systems concepts, is useful in the eventual platform, and is simple enough to understand completely.**

---

# 2. Why This Is the Correct First Vertical

The existing project strategy already emphasizes that major deliverables should evolve as one system rather than as disconnected exercises.

The desired progression is approximately:

```text
Rust foundations
      ↓
typed spatial data
      ↓
spatial operations
      ↓
performance-aware data processing
      ↓
Python interoperability
      ↓
edge-node processing
      ↓
distributed spatial platform
      ↓
native Swift client
```

Sprint 1 should therefore start at the level where the eventual project will genuinely need Rust: **typed 3D spatial data and computation over point collections**.

Before the project can reason about:

- point-cloud partitions;
- spatial queries;
- voxel grids;
- edge-node reduction;
- distributed query routing;
- 3D classification;
- Arrow buffers;
- COPC;
- SQL query planning;
- Swift visualization;

it needs trustworthy primitives for answering very basic questions about a collection of 3D points.

Those primitives begin with:

```text
How many points are present?
Where is their centroid?
What spatial volume do they occupy?
```

These operations are simple enough to understand thoroughly but foundational enough to survive into later versions.

---

# 3. Long-Term System Thesis

The individual project ideas should be organized around one systems-level thesis:

> **Large spatial datasets and sensor streams should not always be moved wholesale to a central system. Computation can occur close to the data source so that data can be validated, summarized, filtered, classified, partitioned, or otherwise reduced before transmission, while a central control plane coordinates the larger system.**

This thesis connects the major project tracks.

## 3.1 Point clouds

A local or edge node may receive or own a large 3D point collection.

Instead of transmitting every point, it may perform:

- validation;
- spatial filtering;
- bounding-box calculations;
- voxel downsampling;
- feature extraction;
- classification;
- spatial partitioning;
- aggregation;
- compression;
- indexing.

Later, the system may classify architectural features such as:

```text
door
window
other facade feature
```

and transmit the classified result or a reduced spatial representation.

## 3.2 Weather observations

Weather data provides a complementary distributed-systems workload.

A simulated weather station may continuously produce:

```text
timestamp
station/location
temperature
humidity
pressure
wind
precipitation
quality flags
```

A Rust edge process could eventually perform:

```text
validation
      ↓
local buffering
      ↓
aggregation
      ↓
quality checks
      ↓
compression / serialization
      ↓
delivery to central control plane
```

The Python layer could then coordinate:

- node registration;
- ingestion;
- retries;
- monitoring;
- aggregation;
- persistence;
- analytics;
- modeling.

This provides a much more natural environment for learning continuous distributed data processing than point clouds alone.

## 3.3 Satellite/onboard-computing analogy

The project should use satellite onboard processing as an architectural inspiration:

```text
sensor acquires large/raw observation
              ↓
local compute determines what is useful
              ↓
raw data is filtered/reduced/interpreted
              ↓
smaller or higher-value result is transmitted
              ↓
central system performs broader analysis
```

The project does **not** need to simulate satellite hardware literally.

The useful systems question is:

> **What processing should happen where the data originates, and what information is valuable enough to transmit across a constrained connection?**

That question should eventually become measurable through metrics such as:

```text
raw bytes
processed bytes
bytes transmitted
processing time
end-to-end latency
compression/reduction ratio
CPU use
memory use
accuracy / information retained
```

## 3.4 Point-cloud SQL/query engine

The point-cloud query engine should remain connected to the main platform while being capable of standing alone as a portfolio project.

A possible long-term architecture remains:

```text
COPC / LAZ
    ↓
Arrow representation
    ↓
Parquet / columnar storage
    ↓
spatial partitioning
    ↓
spatial index
    ↓
query planner
    ↓
DataFusion-style execution
    ↓
spatial SQL
```

This track addresses a related question:

> **How should a very large 3D spatial dataset be physically organized and queried so that irrelevant data does not need to be scanned?**

That is closely related to the edge-platform concern:

> **How do we avoid moving or processing spatial data that a request does not need?**

The SQL engine therefore belongs in the broader ecosystem, but it should not enter Sprint 1.

---

# 4. Architectural Principle: One Platform, Multiple Vertical Workloads

The project should avoid becoming a collection of unrelated demos.

A better mental model is:

```text
                        SPATIAL EDGE PLATFORM

                              Python
                         control / analysis
                               plane
                                 │
             ┌───────────────────┼───────────────────┐
             │                   │                   │
             ▼                   ▼                   ▼
       Point-cloud          Weather-stream      Query-engine
       edge workload        edge workload       / storage lab
             │                   │                   │
             └──────────────┬────┴───────────────────┘
                            ▼
                      Rust spatial /
                      systems layer
                            │
                            ▼
                    common contracts,
                 measurement, reliability
                            │
                            ▼
                          Swift
                  client / visualization
```

Not every subsystem must use every technology.

The important goal is for the pieces to reinforce the same engineering story.

---

# 5. Sprint 1 Objective

Build the first production-quality Rust spatial component:

```text
rust/spatial-core
```

The component should represent 3D points and calculate a summary over a collection of those points.

The initial public concepts are:

```rust
Point3D
BoundingBox3D
PointCloudSummary
summarize_points(...)
```

The resulting summary should contain:

```text
point count
centroid
minimum X
minimum Y
minimum Z
maximum X
maximum Y
maximum Z
```

The implementation should be small enough that every line can be reviewed and understood.

---

# 6. Sprint 1 Research Gate — Literature / Library Review

Before or alongside implementation, conduct a **time-boxed literature and open-source ecosystem review**.

This should become a standard practice at the beginning of major future verticals.

The purpose is not to delay implementation.

The purpose is to avoid:

- recreating mature libraries accidentally;
- choosing poor abstractions because existing designs were never examined;
- missing accepted terminology or data models;
- building around abandoned or incompatible technologies;
- making architectural decisions without understanding the current ecosystem.

The research process should answer:

> **What already exists, what problems do those projects solve, what design choices can we learn from, and what should we reuse rather than recreate?**

---

# 7. Sprint 1 Action Item — Conduct the Initial Ecosystem Review

## Owner

**Samuel**

## Deliverable

Create:

```text
docs/research/
└── 001-point-cloud-rust-ecosystem-review.md
```

or an equivalent research note.

The review does **not** need to be academic-publication length.

A useful first version might examine approximately **8–15 high-value projects, libraries, standards, papers, or technical references**.

Quality matters more than quantity.

---

# 8. Research Questions for the Review

The first review should investigate several layers.

## 8.1 Rust point-cloud ecosystem

Identify current Rust projects or crates relevant to:

- LAS;
- LAZ;
- COPC;
- point-cloud data structures;
- point-cloud iteration;
- spatial filtering;
- voxelization;
- geometry;
- spatial indexes;
- Arrow;
- Parquet;
- GeoArrow;
- DataFusion;
- numerical arrays;
- serialization.

For each relevant project, record:

```text
1. What problem does it solve?
2. Is it actively maintained?
3. What are its core abstractions?
4. What data representation does it use?
5. Does it copy or borrow data?
6. What formats does it support?
7. Could it fit our future architecture?
8. Should we reuse it, study it, or avoid depending on it?
```

## 8.2 Established point-cloud tools outside Rust

Rust should not be researched in isolation.

Review mature systems from adjacent ecosystems to understand established point-cloud architecture.

Potential categories include:

- point-cloud processing libraries;
- LAS/LAZ tooling;
- COPC tooling;
- spatial indexing systems;
- point-cloud visualization systems;
- point-cloud databases or query engines;
- Python point-cloud libraries;
- C/C++ point-cloud libraries.

The purpose is not to port them to Rust.

The purpose is to ask:

> **What abstractions have already proven useful for representing and processing 3D point data?**

## 8.3 Point-cloud data formats

Review the role and design concepts of formats such as:

```text
LAS
LAZ
COPC
Parquet-based representations
Arrow-based representations
other relevant cloud-native approaches
```

Questions should include:

```text
How are points physically stored?
What attributes can points contain?
How is spatial locality represented?
How is random/spatial access achieved?
How is compression handled?
How does the format behave over object storage?
What ideas matter for our future edge system?
```

Sprint 1 itself will **not** implement these formats.

This research exists so that the core API does not accidentally make future integration unnecessarily difficult.

## 8.4 Existing point-cloud query approaches

Because a point-cloud SQL engine is a potential side project, begin collecting references now for systems that support:

- SQL over point data;
- spatial predicates over point collections;
- partition pruning;
- spatial indexing;
- columnar point-cloud storage;
- query planning;
- distributed point-cloud querying.

Do not design the query engine in Sprint 1.

Simply begin an evidence base.

## 8.5 Edge and distributed spatial systems

Collect examples of systems where spatial or sensor data is processed near its source.

Look for concepts such as:

- edge filtering;
- local aggregation;
- constrained bandwidth;
- delayed connectivity;
- store-and-forward;
- local inference;
- event detection;
- distributed spatial partitioning;
- telemetry;
- retry semantics;
- central coordination.

Satellite onboard processing should be one research category, but similar ideas from:

- robotics;
- autonomous vehicles;
- drones;
- environmental sensor networks;
- mobile devices;
- IoT;
- industrial monitoring

may also provide useful architectural precedent.

## 8.6 Point-cloud machine learning

Begin a separate bibliography for eventual door-versus-window classification.

Relevant topics may include:

- PointNet-style architectures;
- PointNet++;
- sparse convolution;
- voxel-based networks;
- point transformers;
- point-cloud semantic segmentation;
- indoor/outdoor architectural feature classification;
- facade understanding;
- RGB + point-cloud fusion;
- geometric feature engineering;
- normals;
- local neighborhoods.

Sprint 1 should **not implement any ML**.

The purpose is to understand what eventual downstream consumers may require from the point representation.

For example, future points may require more than:

```text
x
y
z
```

They may eventually contain:

```text
RGB
intensity
normal
classification
timestamp
sensor/source ID
learned features
```

Sprint 1 should remain minimal while avoiding assumptions that make later extension awkward.

---

# 9. Recommended Research Record Format

Use the same structure for each project/library/reference.

For example:

```markdown
## Project / Library Name

### Category
Rust crate / C++ library / format / paper / system / standard

### Purpose
What problem does it solve?

### Core abstraction
What is the important data or processing model?

### Relevant technologies
Rust, Arrow, COPC, octree, etc.

### What is useful for our project?
Specific architectural lessons.

### What should we reuse?
Library, format, concept, algorithm, nothing yet.

### What should we not copy?
Anything overly complex or inappropriate for our POC.

### Maintenance / maturity
Active? Stable? Experimental?

### Source
Repository / documentation / paper.

### Follow-up
Questions to investigate later.
```

---

# 10. Research Output Should End With Decisions

The review should not end as a collection of links.

Finish it with a short decision table:

| Question | Decision | Confidence | Revisit When |
|---|---|---:|---|
| Use our own `Point3D` in v0.0.1? | TBD | — | After review |
| Add a point-cloud crate immediately? | TBD | — | After review |
| Support LAS now? | No | High | Real-data vertical |
| Support COPC now? | No | High | Cloud-native data vertical |
| Add Arrow now? | No | High | Interop/query-engine vertical |
| Add spatial index now? | No | High | Filtering/indexing vertical |
| Add Python now? | No | High | Rust/Python vertical |
| Add ML now? | No | High | Classification vertical |

This keeps research tied to engineering decisions.

---

# 11. The Literature Review Should Be Repeated for Future Verticals

The review process should become part of the project methodology.

Before a substantial vertical:

```text
define problem
      ↓
research current ecosystem
      ↓
identify reusable components
      ↓
record design options
      ↓
choose smallest architecture
      ↓
implement
      ↓
benchmark / evaluate
      ↓
record decision
```

Examples:

```text
Vertical: LAS/COPC ingestion
Review: point-cloud format/tooling ecosystem

Vertical: voxel downsampling
Review: established algorithms + Rust/C++/Python implementations

Vertical: spatial index
Review: octree / kd-tree / R-tree / Morton / Hilbert approaches

Vertical: Rust ↔ Python
Review: PyO3 / NumPy / Arrow interchange patterns

Vertical: edge networking
Review: HTTP / gRPC / QUIC / message systems / async Rust

Vertical: distributed orchestration
Review: worker patterns / retries / idempotency / scheduling

Vertical: Swift visualization
Review: Metal / SceneKit / RealityKit / point rendering

Vertical: point-cloud ML
Review: semantic segmentation / point transformers / sparse conv

Vertical: SQL engine
Review: DataFusion / Arrow / spatial query engines / pruning

Vertical: satellite-like onboard processing
Review: onboard inference / bandwidth-aware remote sensing systems
```

This is worth preserving as part of the eventual portfolio story because it demonstrates engineering judgment rather than technology collection.

---

# 12. Sprint 1 Functional Requirements

The initial Rust component should support a collection of 3D Cartesian points.

## 12.1 `Point3D`

Conceptually:

```rust
pub struct Point3D {
    pub x: f64,
    pub y: f64,
    pub z: f64,
}
```

The exact API should be decided during implementation.

Important design questions:

- `f32` or `f64`?
- public fields or constructor/accessors?
- `Copy`?
- `Clone`?
- `Debug`?
- `PartialEq`?
- whether a generic numeric coordinate type adds value now.

### Sprint recommendation

Prefer the simplest concrete representation that satisfies the current problem.

Avoid generic coordinate types in `v0.0.1` unless the literature review identifies a compelling near-term reason.

The goal is not to create a universal geometry library.

---

# 13. `BoundingBox3D`

Conceptually:

```text
min_x
min_y
min_z
max_x
max_y
max_z
```

Potential representation:

```rust
pub struct BoundingBox3D {
    pub min: Point3D,
    pub max: Point3D,
}
```

or explicit scalar fields.

This choice should be discussed rather than automatically generated.

Questions:

```text
Is min/max as Point3D conceptually clean?
What invariants should hold?
Can an invalid box exist?
Should construction be public?
Do we need methods such as contains() yet?
```

### Sprint recommendation

Only implement functionality required by the summary operation.

Do not add:

```text
intersection
union
contains
distance
volume
transform
CRS
```

unless needed by acceptance criteria.

Those can enter later verticals.

---

# 14. `PointCloudSummary`

The result should conceptually contain:

```text
count
centroid
bounds
```

For example:

```rust
pub struct PointCloudSummary {
    pub count: usize,
    pub centroid: Point3D,
    pub bounds: BoundingBox3D,
}
```

The exact representation depends on the empty-input policy.

---

# 15. Empty Input Is a Real API Decision

The function must explicitly define behavior for:

```rust
let points: Vec<Point3D> = vec![];
```

Possible approaches include:

```text
Option<PointCloudSummary>
Result<PointCloudSummary, Error>
summary with optional centroid/bounds
panic
```

Sprint 1 should treat this as a design discussion rather than an incidental coding detail.

### Recommendation

Do **not** panic for an ordinary absence-of-data case.

Prefer an API that makes empty input explicit.

The exact `Option` versus `Result` choice should be decided after discussing whether “no points” is:

```text
an expected absence
```

or:

```text
an invalid operation / domain error
```

That discussion is itself a useful Rust learning exercise.

---

# 16. `summarize_points(...)`

The function should compute:

```text
count
centroid
bounding box
```

in a single traversal if practical.

Conceptually:

```text
for each point:
    increment count

    accumulate x
    accumulate y
    accumulate z

    update min values
    update max values
```

Then:

```text
centroid_x = sum_x / count
centroid_y = sum_y / count
centroid_z = sum_z / count
```

Target complexity:

```text
Time:  O(N)
Space: O(1) auxiliary memory
```

excluding storage of the input itself.

The implementation should not create unnecessary intermediate collections.

---

# 17. Slice Versus Iterator Question

This sprint should deliberately examine whether the public function should accept:

```rust
&[Point3D]
```

or an iterator-oriented abstraction.

Both are educationally useful.

## Slice

Advantages:

- straightforward;
- easy to understand;
- contiguous collection semantics;
- simple borrowing;
- easy testing.

## Iterator

Advantages:

- more flexible;
- can support streaming-style computation;
- can summarize points without requiring a new collection;
- conceptually useful for future edge processing.

### Sprint recommendation

Do not build a complicated generic API simply to demonstrate advanced Rust.

A good progression may be:

```text
simple slice API
      ↓
understand it completely
      ↓
evaluate whether iterator generalization is useful
```

If an iterator version remains readable and idiomatic, it may be worth implementing.

The decision should be documented.

---

# 18. Numerical Questions to Discuss

Even this small operation exposes real numerical issues.

Questions include:

- Why use `f32` versus `f64`?
- Can summing many coordinates accumulate floating-point error?
- Does naïve summation matter at Sprint 1 scale?
- What happens if points contain `NaN`?
- What happens with `Infinity`?
- Should invalid numeric values be rejected?
- Should geospatial coordinates be normalized?
- Are these Cartesian coordinates or geographic longitude/latitude?

### Sprint 1 scope

The component should be explicit that it operates on generic **3D numeric Cartesian coordinates** unless otherwise specified.

Do not introduce CRS transformation.

Do not silently treat longitude/latitude as Euclidean XYZ.

Document assumptions.

---

# 19. Proposed Repository Shape

The exact layout should stay small.

One possible structure:

```text
spatial_system/
└── rust/
    └── spatial-core/
        ├── Cargo.toml
        ├── README.md
        ├── src/
        │   ├── lib.rs
        │   └── point.rs
        └── tests/
```

Do not create a large directory hierarchy unless the code actually requires it.

Repository structure should emerge from actual responsibilities, not from assumptions about what a “serious” Rust project looks like.

---

# 20. Dependencies

Sprint 1 should strongly prefer:

```text
Rust standard library only
```

unless research identifies a genuinely necessary dependency.

This is important because the sprint is primarily about:

- Rust data representation;
- borrowing;
- iteration;
- correctness;
- API design;
- testing.

A dependency that solves the entire problem would reduce the educational value.

The literature review still matters even if we intentionally choose not to use external crates.

That decision can be documented as:

> Existing libraries were reviewed; v0.0.1 intentionally implements this tiny primitive directly because the implementation is small, educationally useful, and avoids premature coupling.

---

# 21. Tests

Testing is part of the deliverable, not an afterthought.

Minimum scenarios should include:

## One point

```text
count = 1
centroid = point
bounds min = point
bounds max = point
```

## Two points

Validate:

```text
count
centroid
min
max
```

## Multiple mixed coordinates

Include:

```text
positive
negative
zero
different Z values
```

## Empty input

Validate the chosen empty-input contract.

## Repeated points

Ensure repeated coordinates behave correctly.

## Floating-point comparisons

Determine an appropriate strategy for comparing floating-point results.

Avoid fragile exact equality when the expected result requires non-exact floating-point arithmetic.

---

# 22. Tooling Requirements

Before Sprint 1 is complete:

```bash
cargo fmt --check
cargo clippy -- -D warnings
cargo test
```

should pass.

If the repository already has different conventions, use the existing conventions rather than inventing parallel ones.

---

# 23. Documentation Requirements

At minimum, Sprint 1 should produce:

```text
README / component documentation
public API documentation
tests
research note
brief architecture note or ADR
```

Useful documentation topics include:

```text
What does spatial-core do?
Why does it exist?
What does it intentionally not do?
What coordinate assumptions does it make?
How is empty input handled?
Why were external dependencies avoided/selected?
How do I run the tests?
What future components are expected to build on it?
```

---

# 24. Architecture Decision Record

Create a first ADR if the project does not already have one.

Suggested file:

```text
docs/decisions/
└── 0001-start-with-minimal-rust-point-core.md
```

Potential decision:

> Begin the Spatial Edge Platform with a dependency-light Rust library implementing minimal 3D point summary primitives before introducing file formats, networking, Python bindings, Swift, or machine learning.

The ADR should capture:

```text
Context
Decision
Alternatives
Consequences
When to revisit
```

This begins a useful architecture history.

---

# 25. Explicit Sprint 1 Non-Goals

The following are out of scope for `v0.0.1`:

- Python bindings;
- Swift;
- networking;
- HTTP;
- gRPC;
- async Rust;
- Tokio;
- distributed execution;
- multiple edge nodes;
- weather streams;
- LAS parsing;
- LAZ parsing;
- COPC;
- Arrow;
- Parquet;
- DataFusion;
- SQL;
- spatial indexes;
- octrees;
- kd-trees;
- voxel downsampling;
- point-cloud visualization;
- GPU processing;
- Metal;
- computer vision;
- point-cloud classification;
- door/window classification;
- model inference;
- cloud deployment;
- AWS;
- Docker unless the repository requires it;
- custom binary point-cloud formats;
- `.spat` integration;
- premature generic geometry frameworks.

These are not rejected ideas.

They are deliberately sequenced future work.

---

# 26. Sprint 1 Acceptance Criteria

Sprint 1 is complete when all of the following are true.

## Research

- [ ] Initial point-cloud / spatial systems ecosystem review exists.
- [ ] At least several serious existing systems or libraries have been examined.
- [ ] Relevant point-cloud formats have been noted.
- [ ] Candidate Rust libraries have been identified.
- [ ] Initial future query-engine references have been collected.
- [ ] Research concludes with concrete current decisions.

## Rust implementation

- [ ] `Point3D` exists.
- [ ] `BoundingBox3D` exists.
- [ ] `PointCloudSummary` or equivalent exists.
- [ ] `summarize_points(...)` exists.
- [ ] Count is correct.
- [ ] Centroid is correct.
- [ ] XYZ bounds are correct.
- [ ] Empty input behavior is explicit.
- [ ] Implementation avoids unnecessary allocations.
- [ ] Implementation is `O(N)`.

## Quality

- [ ] Unit tests pass.
- [ ] Empty-input test exists.
- [ ] Floating-point behavior is tested appropriately.
- [ ] `cargo fmt --check` passes.
- [ ] `cargo clippy -- -D warnings` passes.
- [ ] `cargo test` passes.
- [ ] Public API has documentation.
- [ ] Component README explains purpose and limits.
- [ ] Architecture decision is recorded.

## Learning

- [ ] You can explain every public type.
- [ ] You can explain ownership and borrowing in the implementation.
- [ ] You can explain whether input is copied.
- [ ] You can explain how iteration works.
- [ ] You can explain the centroid calculation.
- [ ] You can explain the bounding-box calculation.
- [ ] You can explain why complexity is `O(N)`.
- [ ] You can explain auxiliary memory behavior.
- [ ] You can explain empty-input semantics.
- [ ] You can explain the chosen floating-point type.
- [ ] You can modify the implementation yourself.

---

# 27. AI Coding-Agent Contract for Sprint 1

The coding agent should be used as an implementation partner, not as an autonomous system architect.

A suitable prompt structure is:

```text
You are working in the existing Spatial Edge Platform repository.

Goal:
Implement the first Rust point-cloud core primitive.

Before editing:
1. Inspect the repository.
2. Identify the existing Rust workspace/package layout.
3. Tell me exactly which files you plan to create or modify.
4. Explain why each file is needed.
5. Do not modify anything yet.

Implementation scope:
- Point3D
- BoundingBox3D
- PointCloudSummary
- summarize_points(...)

Requirements:
- idiomatic Rust;
- minimal API;
- no unnecessary dependencies;
- explicit empty-input behavior;
- O(N) processing;
- avoid unnecessary allocations;
- unit tests;
- public documentation.

Do not add:
- Python;
- Swift;
- LAS/LAZ/COPC;
- networking;
- async;
- Arrow;
- SQL;
- ML;
- unrelated abstractions.

After implementation:
1. Run cargo fmt.
2. Run cargo clippy.
3. Run cargo test.
4. Explain ownership and borrowing.
5. Explain allocations/copies.
6. Explain time and space complexity.
7. Explain empty-input behavior.
8. Identify anything I should understand before merging.
```

The first agent turn should stop after inspecting and proposing changes.

This prevents the agent from racing ahead before the architecture is reviewed.

---

# 28. Understanding Gate Before Merge

Before merging `v0.0.1`:

```text
[ ] I know why every source file exists.

[ ] I can describe every public struct.

[ ] I can write a Point3D myself.

[ ] I understand why the function borrows or owns its input.

[ ] I know whether any point data is copied.

[ ] I can explain the loop/iterator.

[ ] I can calculate the centroid manually.

[ ] I can explain how min/max values evolve.

[ ] I know why the algorithm is O(N).

[ ] I understand the empty-input API.

[ ] I understand the tests.

[ ] I can add a test without AI assistance.

[ ] I can make a small implementation change myself.

[ ] I know what the next vertical will build on.
```

If several items are not true, feature development should pause while the existing code becomes the next learning exercise.

---

# 29. Suggested Work Sequence

A practical Sprint 1 sequence is:

```text
Step 1
Create / refine this sprint specification.

Step 2
Conduct the ecosystem / literature review.

Step 3
Record initial technology decisions.

Step 4
Inspect current repository structure.

Step 5
Ask coding agent for implementation plan only.

Step 6
Review the proposed types and API.

Step 7
Implement minimal Rust core.

Step 8
Run fmt / clippy / tests.

Step 9
Perform code walkthrough.

Step 10
Make at least one manual change.

Step 11
Complete understanding gate.

Step 12
Write/update ADR and README.

Step 13
Tag or otherwise mark v0.0.1.

Step 14
Plan next vertical using another targeted ecosystem review.
```

---

# 30. What Should Sprint 2 Be?

The preferred next step remains **bounding-box filtering**.

Conceptually:

```rust
filter_bbox(points, bounds)
```

or an API appropriate to the implementation.

Why filtering should likely precede Python:

```text
summary
   ↓
spatial predicate
   ↓
spatial subset
   ↓
future partitioning / indexing
```

Bounding-box filtering introduces a genuinely spatial operation while remaining easy enough to understand.

It also creates the first primitive that resembles future edge behavior:

> Receive many points, retain only the subset relevant to a spatial request.

The likely progression is therefore:

```text
v0.0.1
point summary
    ↓
v0.0.2
bounding-box filtering
    ↓
v0.0.3
voxel/downsampling experiment or point collection abstraction
    ↓
v0.0.x
real point-cloud ingestion
    ↓
Rust ↔ Python
```

The precise order should be revisited after the Sprint 1 ecosystem review.

---

# 31. Longer-Term Vertical Sequence

A provisional sequence could be:

## Phase A — Spatial core

```text
v0.0.1  Point summary
v0.0.2  Bounding-box filtering
v0.0.3  Downsampling / aggregation
v0.0.4  Simple spatial partitioning
```

## Phase B — Real point-cloud data

```text
LAS / LAZ / COPC ingestion
      ↓
real datasets
      ↓
benchmarking
```

## Phase C — Python interoperability

```text
Rust core
   ↓
PyO3 / Arrow / NumPy boundary
   ↓
Python analysis and orchestration
```

## Phase D — Edge node

```text
local point-cloud partition
        ↓
Rust processing
        ↓
request / response
        ↓
metrics
```

## Phase E — Distributed control plane

```text
                 Python
              coordinator
             /     |      \
            /      |       \
        Rust A   Rust B   Rust C
```

Add:

```text
routing
timeouts
retries
partial failure
observability
idempotency
```

## Phase F — Weather-stream workload

Use the same architectural principles with a continuous sensor stream.

## Phase G — Swift

Build a client only once the system has meaningful functionality to consume.

## Phase H — Point-cloud classification

Add a real ML task such as architectural-feature classification.

## Phase I — Query-engine track

Develop the storage/query subsystem sufficiently that it can become a standalone portfolio project.

---

# 32. Direction for the Project as a Whole

The strongest form of this project is **not**:

> “I used Rust, Python, Swift, point clouds, ML, distributed computing, and edge computing in one repo.”

That sounds technology-driven.

The stronger story is:

> **I built a spatial system around the problem of deciding what computation should happen near the data source, what information should move across a constrained boundary, and how a central system should coordinate and analyze the resulting spatial information.**

The technologies then become justified:

```text
Rust
because local spatial processing needs strong systems primitives,
predictable performance, and explicit data movement.

Python
because orchestration, experimentation, analytics, ML, and the
scientific ecosystem belong there.

Swift
because a native spatial client provides an authentic application
surface for interacting with edge-derived spatial products.

Point clouds
because they are spatially rich, large, irregular 3D datasets with
meaningful opportunities for filtering, partitioning, indexing,
classification, and reduction.

Weather streams
because they introduce continuous time-series ingestion, buffering,
aggregation, connectivity, and failure semantics.

Satellite/onboard processing
because it provides the architectural analogy for computing before
transmission.

The query engine
because it explores the complementary problem of minimizing how much
spatial data must be read and processed for analytical requests.
```

That is a coherent systems portfolio.

---

# 33. A Crucial Scope Principle

The project should repeatedly distinguish three things:

```text
PLATFORM CAPABILITY
something the full system eventually needs

LEARNING EXPERIMENT
something worth implementing to understand the systems problem

PRODUCTION DEPENDENCY
something mature that should probably be reused rather than recreated
```

For example:

```text
LAS parser
likely production dependency

centroid / bbox
reasonable learning + platform primitive

DataFusion query planner
production dependency / integration target

custom spatial pruning experiment
reasonable learning experiment

PointNet implementation
possibly learning/modeling experiment

distributed consensus system
almost certainly not something this POC needs to invent
```

This distinction will prevent the project from becoming an attempt to reimplement the geospatial software ecosystem.

---

# 34. Definition of Success for v0.0.1

The version is successful if it looks unimpressive from a feature-count perspective but impressive from an engineering-discipline perspective.

A reviewer should see:

```text
small API
clear types
correct behavior
tests
documented assumptions
clean Rust
measured complexity
research-informed decisions
deliberate scope
clear future path
```

The first version does not need to prove that the platform is ambitious.

The roadmap already does that.

The first version needs to prove that the platform will be built carefully.

---

# 35. Sprint 1 Exit Narrative

At the end of the sprint, you should be able to explain the work approximately like this:

> **I am building a multi-language spatial edge-computing platform around point clouds and sensor data. Rather than starting with networking or ML, I began with the smallest reusable Rust data-plane primitive: representing and summarizing 3D points. I first reviewed existing point-cloud libraries, formats, and systems so I could distinguish what should be reused from what was valuable to implement for learning. The initial Rust component computes count, centroid, and 3D bounds in a single O(N) pass with explicit empty-input semantics and no unnecessary allocations. The next vertical introduces spatial filtering, which becomes the basis for later partitioning, edge reduction, and distributed spatial queries.**

That is already a defensible engineering story.

It makes clear that `v0.0.1` is small by design rather than because the larger project lacks ambition.

---

# 36. Immediate Next Action

The next action should be:

> **Conduct the Sprint 1 point-cloud / spatial-systems literature and open-source ecosystem review before allowing the implementation to become more complex.**

The output should be:

```text
docs/research/001-point-cloud-rust-ecosystem-review.md
```

The review should end with explicit recommendations for:

```text
Point3D representation
coordinate numeric type
slice vs iterator API
dependencies
error / empty-input behavior
likely real-data library
likely future Arrow strategy
likely future indexing direction
technologies deliberately deferred
```

Once that research note exists, it can be used together with this sprint specification to give the coding agent a tightly constrained first implementation task.

---

# 37. Final Sprint Principle

The governing rule for Sprint 1 and every vertical after it should be:

> **Research enough to understand the ecosystem, build only the smallest useful slice, measure what matters, and do not allow implementation speed to exceed understanding.**

That keeps the project moving quickly while preserving the main reason for building it: becoming able to design, explain, implement, and defend modern spatial systems.


</details>
