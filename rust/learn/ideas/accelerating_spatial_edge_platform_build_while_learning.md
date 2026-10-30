# Accelerating the Spatial Systems Portfolio Project While Learning Rust

## Recommendation

I think you should accelerate the actual project now.

I would **not** wait until you feel fluent in Rust, distributed systems, point-cloud tooling, Swift, or cross-language integration before beginning the portfolio system. Your existing program materials already point toward a better model: build one evolving system, develop it through vertical slices, and use the project itself as the vehicle for learning.

The important distinction is this:

> **Accelerate implementation, but do not outsource understanding.**

Using Codex or an equivalent coding agent to help construct the system is entirely reasonable. The danger is not that AI writes code you could not yet write from memory. The danger is allowing the codebase to get several conceptual layers ahead of your ability to explain, debug, modify, and defend its design.

So I would move from a **course-first model** to a **project-led, learning-in-the-loop model**.

Instead of:

```text
learn Rust
    ↓
learn distributed systems
    ↓
learn point clouds
    ↓
learn Swift
    ↓
eventually build portfolio project
```

I recommend:

```text
define one small architectural slice
            ↓
ask AI to help implement it
            ↓
read and interrogate the implementation
            ↓
learn the Rust / CS / spatial concepts it introduced
            ↓
modify part of it yourself
            ↓
test + benchmark + document it
            ↓
add the next vertical slice
```

That gets you to a compelling project sooner without turning the project into a black box.

---

# Why I Think This Is the Right Move

## 1. The project is more valuable to your job search than isolated exercises

You are trying to fill several identifiable gaps at once:

- systems-level programming;
- Rust;
- point-cloud processing;
- distributed computing;
- edge computing;
- cross-language systems;
- native/Swift development;
- performance engineering.

A set of exercises can demonstrate that you are learning those subjects.

A functioning system can demonstrate that you can **combine them into an engineering architecture**.

That distinction matters in an interview.

Compare:

> “I have been learning Rust ownership, iterators, and traits.”

with:

> “I built the Rust data plane for a small distributed spatial system. It performs point-cloud partitioning, spatial filtering, local aggregation, and serialization at the edge. Python operates the control plane, and a Swift client consumes the resulting spatial products. I benchmarked data movement and query behavior and documented why each responsibility belongs in each language.”

The second gives an interviewer many directions to explore:

- Why Rust?
- Why Python?
- Why Swift?
- What crosses the FFI boundary?
- Why not send the full point cloud?
- How are nodes partitioned?
- What happens when a node fails?
- How are spatial queries routed?
- What is serialized?
- Where are copies occurring?
- What did benchmarking show?
- What would change in production?

Those are exactly the conversations you want the project to create.

---

# 2. This actually matches the learning strategy we already designed

Your Rust syllabus explicitly treats Rust as the high-performance systems layer of a larger spatial system rather than as an isolated language exercise.

The intended progression is already roughly:

```text
Rust foundations
      ↓
typed spatial data
      ↓
binary / columnar representation
      ↓
spatial computation
      ↓
performance measurement
      ↓
Python interoperability
      ↓
edge-node component
      ↓
distributed spatial platform
```

It also explicitly favors **vertical development**:

```text
concept
   ↓
tiny exercise
   ↓
geospatial example
   ↓
real project increment
   ↓
measured behavior
```

I think your current instinct is therefore less a change in direction than an acceleration of the strategy that is already implicit in the curriculum.

The syllabus should remain useful, but it becomes a **just-in-time learning map** rather than a gate that must be completed before the project begins.

---

# 3. “Learning to fly while building the plane” can work if the plane stays small

The approach fails when the coding agent is told something like:

> Build me a distributed Rust/Python/Swift geospatial platform with point-cloud processing, edge computing, computer vision, networking, storage, and a native visualization application.

That is likely to produce a large amount of code that you technically possess but do not really own intellectually.

Instead, the agent should receive narrowly bounded engineering tasks.

For example:

> Add a Rust library function that accepts a slice or iterator of 3D points and computes count, centroid, and XYZ bounding box. First explain the files you will modify. Keep the API minimal. Add unit tests. Do not add networking, Python bindings, or file parsing.

That is almost exactly the kind of task you have already begun experimenting with.

Then:

> Expose that tested Rust function to Python through PyO3. Do not change the underlying geometry implementation. Explain every conversion or copy occurring at the Python/Rust boundary.

Then:

> Extend the Rust core with voxel-grid downsampling. Benchmark the original and reduced point sets.

Then:

> Wrap the Rust processing component in a simple edge-node service. The node receives a spatial request, processes only its local partition, and returns a compact summary.

Each step should be small enough that you can understand the architecture before proceeding.

---

# The Main Risk: Creating a Portfolio Project You Cannot Defend

The biggest downside is not really “I did not personally type every line.”

Professional software engineers routinely work with frameworks, code generation, libraries, documentation, coworkers, Stack Overflow, and increasingly AI coding agents.

The real problem would be reaching an interview and saying:

> “I know the project uses Arrow here, but Codex added that and I am not completely sure why.”

or:

> “There is an async runtime and some channels in the Rust service, but I haven't really looked at that part.”

That turns a portfolio advantage into a liability.

I would use a simple rule:

> **No major subsystem advances until you can explain the previous subsystem on a whiteboard.**

You do not need to remember every method call or piece of syntax.

You should be able to explain:

1. what the component does;
2. what data enters it;
3. what data leaves it;
4. why that language owns the responsibility;
5. the principal data structures;
6. the important algorithms;
7. what happens in memory;
8. what is serialized or copied;
9. its failure modes;
10. how it is tested;
11. what its performance characteristics are;
12. what you would improve next.

That is a much better definition of ownership than “I manually typed all the code.”

---

# A Better Division of Labor Between You and the Coding Agent

I would deliberately separate **architectural ownership** from **implementation acceleration**.

## You should own

You should make or explicitly approve decisions concerning:

- overall system architecture;
- boundaries among Rust, Python, and Swift;
- public APIs;
- data contracts;
- point-cloud representation;
- spatial partitioning strategy;
- distributed-system semantics;
- benchmark questions;
- what is considered an edge node;
- failure behavior;
- what gets transmitted over the network;
- what belongs locally versus centrally;
- project scope;
- acceptance criteria;
- architectural decision records.

These are the things you most need to be able to discuss in interviews.

## Let the coding agent accelerate

The coding agent can do substantial work on:

- boilerplate;
- Cargo/module wiring;
- test scaffolding;
- repetitive serialization code;
- PyO3 binding syntax;
- Swift networking boilerplate;
- benchmark harnesses;
- CLI plumbing;
- type conversions;
- documentation drafts;
- CI configuration;
- mechanical refactors;
- small well-specified algorithms.

The dividing line is not “AI versus you.”

The dividing line is:

> **Does this task contain an architectural idea that you need to understand professionally?**

If yes, slow down enough to learn it.

---

# I Would Also Change One Thing About the Current Project Direction

Your materials contain several excellent project ideas:

- the Rust-native spatial systems layer;
- the experimental `.spat` format;
- a distributed edge platform;
- Swift/native spatial applications;
- cloud-native point clouds;
- Arrow/Parquet/DataFusion;
- spatial indexing;
- a point-cloud query engine;
- computer vision;
- multi-device edge computing.

They are individually interesting.

Together, they can become too large.

I would **not** try to make the first demonstrable system contain the complete version of all of them.

Instead, I would define one project identity and let the other ideas become capabilities added over time.

---

# Proposed Project Identity

## Spatial Edge Platform

### One-sentence version

> **A multi-language spatial computing system in which Rust edge nodes process and reduce 3D geospatial data close to its source, Python coordinates distributed workloads and analytics, and a Swift client visualizes and interacts with the resulting spatial products.**

That is broad enough to grow but specific enough to explain.

The project can eventually touch:

- Rust;
- Python;
- Swift;
- point clouds;
- spatial indexing;
- Arrow/Parquet;
- edge processing;
- distributed computation;
- networking;
- performance;
- 3D visualization;
- computer vision.

But the first version does not need every one of those.

---

# What I Would Build First

I recommend a **point-cloud-first vertical slice**.

This is a particularly good choice because point clouds naturally expose the systems questions you want to learn:

- large data volumes;
- XYZ memory layout;
- bounding boxes;
- spatial partitioning;
- filtering;
- aggregation;
- indexing;
- compression;
- chunking;
- network transfer;
- spatial locality;
- parallel processing;
- 3D visualization.

You also already have some relevant point-cloud experience from structure-from-motion work, so the new project extends your geospatial background rather than appearing disconnected from it.

---

# Milestone 0 — Architecture Skeleton

Keep your existing monorepo concept:

```text
spatial_system/
├── rust/
├── python/
├── swift/
├── docs/
├── data/
└── README.md
```

Create a very small architecture document answering:

```text
Rust:
performance-sensitive spatial data plane

Python:
control plane, orchestration, experiments, analytics

Swift:
native client / edge-device interface / visualization
```

Do not worry yet about sophisticated networking or deployment.

The first accomplishment is simply making the language responsibilities explicit.

---

# Milestone 1 — Rust Point-Cloud Core

Start from the small task you have already been experimenting with.

Input:

```text
Point3D { x, y, z }
```

Operations:

```text
count
centroid
XYZ bounding box
```

Then add, progressively:

```text
spatial filtering
voxel-grid aggregation/downsampling
simple partitioning
```

Possible API:

```text
PointCloud
    ├── count()
    ├── centroid()
    ├── bounds()
    ├── filter_bbox()
    └── voxel_downsample()
```

This milestone is small enough that you should understand essentially all of the Rust involved.

It gives you practice with:

- structs;
- vectors/slices;
- iterators;
- ownership;
- borrowing;
- `Option`;
- `Result`;
- methods;
- modules;
- tests;
- numerical operations;
- algorithmic complexity.

This is where the Rust curriculum and the production project are almost perfectly aligned.

---

# Milestone 2 — Real Point-Cloud Data

Introduce an actual point-cloud dataset.

Initially, avoid writing your own LAS/LAZ/COPC parser.

Use an existing Rust ecosystem library where practical.

The engineering question is not:

> Can I reimplement LAS?

It is:

> Can I design an efficient spatial processing system around point-cloud data?

At this stage the Rust program should be able to do something demonstrable such as:

```text
load point subset
      ↓
calculate spatial extent
      ↓
filter region
      ↓
voxel-downsample
      ↓
output compact result
```

Now you have a genuine geospatial systems component rather than a language exercise.

---

# Milestone 3 — Rust ↔ Python

This should arrive relatively early.

Expose a deliberately small Rust API to Python.

For example:

```python
from spatial_core import PointCloud

cloud = PointCloud.from_numpy(points)

print(cloud.bounds())

reduced = cloud.voxel_downsample(0.5)
```

Now the architecture becomes tangible:

```text
Python
workflow / orchestration / experimentation
        │
        ▼
Rust
point-cloud processing / hot path
```

This is an important portfolio milestone by itself.

It demonstrates that Rust is not being learned in isolation—you are embedding it into the ecosystem where you are already productive.

At this boundary, explicitly learn and document:

- PyO3;
- maturin;
- FFI;
- Python ↔ Rust type conversion;
- ownership;
- buffer layout;
- copies;
- NumPy memory representation;
- potential zero-copy approaches.

That is excellent interview material.

---

# Milestone 4 — Simulated Edge Nodes

This is where the project begins filling the distributed-computing gap.

Do not start with Kubernetes.

Do not start with AWS.

Do not start with a complicated message broker.

Run several local processes or containers.

For example:

```text
               Python control plane
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Rust node A  Rust node B  Rust node C
          │           │           │
      points A     points B     points C
```

Each node “owns” a spatial partition.

A query such as:

```text
bbox = [xmin, ymin, xmax, ymax]
```

can be routed only to intersecting nodes.

Each node might:

1. identify relevant local data;
2. filter points;
3. aggregate or downsample;
4. return a smaller result.

Now you can measure an actual systems question:

> **How much data can be discarded at the edge before transmission to the central process?**

That connects point clouds, spatial processing, distributed computing, edge computing, networking, and performance in one coherent problem.

---

# Milestone 5 — Failure and Distributed-System Behavior

Once several nodes exist, deliberately make the system imperfect.

Introduce:

- node timeout;
- unavailable node;
- retry;
- idempotent request ID;
- partial response;
- health endpoint;
- structured logging;
- request timing.

Now you can discuss distributed systems in concrete terms rather than only academically.

For example:

```text
Query sent to nodes A, B, C

A → success
B → timeout
C → success
```

The Python control plane must decide:

```text
retry B?
return partial result?
fail entire request?
record degraded result?
```

That is real distributed-systems reasoning.

---

# Milestone 6 — Swift Client

Only after the system has something useful to consume should Swift enter the main path.

The first Swift application should be intentionally simple.

For example:

```text
Swift app
   │
   ├── choose/query region
   │
   ▼
Python API / control plane
   │
   ▼
distributed Rust nodes
   │
   ▼
reduced point data
   │
   ▼
Swift 3D visualization
```

A macOS or iOS client could:

- submit a bounding-box query;
- display node status;
- request a point-cloud subset;
- visualize the returned points;
- show counts/bounds/latency;
- adjust downsampling resolution.

Now all three languages have an authentic responsibility.

Rust is not present merely because you wanted Rust.

Python is not present merely because you already know Python.

Swift is not present merely because you wanted a third language.

Each occupies a defensible system layer.

---

# Milestone 7 — Computer Vision

I would add computer vision **after** the spatial edge pipeline works.

Otherwise computer vision risks turning the project into several projects at once.

A later version might associate:

```text
camera frame
     +
point-cloud / depth data
```

and perform some lightweight perception task.

Possible directions include:

- object/scene classification;
- point/image association;
- feature extraction;
- segmentation;
- change detection;
- image-derived metadata attached to spatial observations.

The key architectural question should remain:

> **What computation should happen near the data source, and what information should be transmitted centrally?**

That keeps computer vision connected to the edge-computing thesis rather than simply bolting an ML model onto the project.

---

# Milestone 8 — Cloud-Native Point-Cloud Experiment

The cloud-native point-cloud idea from your existing notes is worth preserving, but I would treat it as an advanced branch of the platform.

Your notes outline a particularly interesting stack:

```text
COPC / LAZ
    ↓
Arrow RecordBatch
    ↓
Parquet
    ↓
spatial partitioning
    ↓
spatial index
    ↓
DataFusion
    ↓
Spatial SQL
```

That could eventually become the **storage/query subsystem** behind the distributed edge platform.

The research question you already identified is strong:

> Can a spatially partitioned columnar point-cloud representation improve analytical spatial-query behavior while retaining Arrow/Parquet interoperability?

But this is sufficiently deep that I would not make it a prerequisite for the first working distributed demo.

Build the system first.

Then make the storage engine more sophisticated.

---

# A Useful Definition of “POC Complete”

Do not define completion as:

> Rust + Python + Swift + distributed computing + CV + point clouds + edge computing + cloud infrastructure + custom format + spatial SQL are all finished.

That finish line will continually retreat.

Instead, define **POC v0.1** as something like:

```text
1. A real point cloud is partitioned across 2–3 simulated Rust edge nodes.

2. Each Rust node can:
   - load its local partition;
   - compute bounds/count/centroid;
   - spatially filter points;
   - voxel-downsample results.

3. A Python control plane:
   - knows which nodes exist;
   - routes a spatial query;
   - collects responses;
   - handles a node failure;
   - reports latency and bytes transferred.

4. Rust processing is also accessible from Python through a tested
   interoperability boundary.

5. A small Swift client:
   - sends a spatial query;
   - receives the reduced point data;
   - displays basic 3D/spatial output and metrics.

6. The repository contains:
   - tests;
   - benchmark results;
   - an architecture diagram;
   - a short design document;
   - at least a few architectural decision records;
   - a reproducible demo.
```

That alone would be a substantial portfolio project.

Everything else can become v0.2, v0.3, and beyond.

---

# How I Would Use Codex / Coding Agents

I would absolutely use one.

But change the way you prompt it.

Do not primarily ask:

> Build feature X.

Use a structure closer to:

```text
Context:
Here is the current architecture and the responsibility of this component.

Task:
Implement one narrowly defined vertical increment.

Constraints:
Do not add unrelated abstractions or dependencies.

Before coding:
1. Inspect the relevant repository files.
2. Explain the proposed change.
3. List files that will be modified.
4. Identify any new dependencies.
5. Explain the important Rust / systems concepts involved.

Implementation:
Add the feature with tests.

After implementation:
1. Explain the resulting data flow.
2. Explain ownership / memory behavior.
3. Identify copies and allocations.
4. Explain complexity.
5. Show how to run the tests.
6. Give me three questions I should be able to answer before merging.
```

That turns the coding agent into both an implementation accelerator and a tutor.

---

# Add a Mandatory “Understanding Gate” Before Every Merge

Before merging an AI-generated feature, require yourself to answer something like:

```text
[ ] I can explain what changed.

[ ] I can identify the main Rust types.

[ ] I understand who owns the important data.

[ ] I can explain the algorithm.

[ ] I know its time complexity at a useful level.

[ ] I know what gets allocated/copied.

[ ] I understand the public API.

[ ] I understand the error cases.

[ ] I can run and interpret the tests.

[ ] I can modify at least one behavior myself.

[ ] I can explain why this belongs in Rust/Python/Swift.

[ ] I can explain how this component fits the larger system.
```

If several of those answers are “no,” the project has moved too far ahead.

That is when you pause feature development and use the code itself as the next lesson.

---

# Keep the Formal Rust Course, but Change Its Role

I would **not abandon the Rust syllabus**.

It is solving a different problem.

The portfolio system answers:

> What can I build?

The syllabus answers:

> Do I understand the concepts underneath what I am building?

Those should proceed together.

A good pattern would be:

```text
PROJECT NEED
    ↓
"I need a Vec<Point3D> and bbox calculation."
    ↓
RUST LESSON
Vec, structs, borrowing, iterators
    ↓
PROJECT IMPLEMENTATION
point-cloud statistics
```

Later:

```text
PROJECT NEED
    ↓
"I need Python to call Rust without unnecessary copies."
    ↓
RUST / SYSTEMS LESSON
FFI, buffers, memory layout, ownership
    ↓
PROJECT IMPLEMENTATION
PyO3 / NumPy boundary
```

Later:

```text
PROJECT NEED
    ↓
"I need several edge workers."
    ↓
SYSTEMS LESSON
processes, networking, async I/O, failure
    ↓
PROJECT IMPLEMENTATION
distributed Rust nodes
```

That is probably a more powerful way for you to learn than treating every curriculum unit as independent material.

---

# Preserve the `.spat` Work, but Do Not Let It Block the Main Demo

Your Rust curriculum uses the experimental `.spat` format as a learning vehicle for:

- bytes;
- offsets;
- chunking;
- indexing;
- compression;
- random access;
- I/O locality;
- benchmarking.

Those remain valuable systems lessons.

But if the immediate career goal is to demonstrate:

- Rust;
- point clouds;
- distributed systems;
- edge computing;
- Python interoperability;
- Swift;

then I would not require the full `.spat` raster project to be finished before touching the edge platform.

Instead, treat it as a **Rust systems laboratory** whose ideas transfer into the larger project.

For example:

```text
.spat lesson                   point-cloud platform
-----------------------------------------------------
chunking                →      spatial partitions
offsets                 →      indexed data access
locality                →      local node processing
compression             →      network/storage tradeoffs
bbox index              →      query routing
benchmarking            →      edge-vs-central measurement
Python bindings         →      control-plane integration
```

The learning remains valuable even if `.spat` itself never becomes the centerpiece of the final portfolio demo.

---

# The Git History Becomes Part of the Portfolio

One advantage of starting now is that the repository history can show genuine progression.

For example:

```text
v0.0
Rust Point3D + centroid + bbox

v0.1
PointCloud abstraction + filtering

v0.2
Voxel downsampling + benchmarks

v0.3
Python bindings

v0.4
Real LAS/COPC ingestion

v0.5
Single Rust edge service

v0.6
Multi-node Python orchestration

v0.7
Failure handling + observability

v0.8
Swift query client

v0.9
3D visualization

v1.0
documented, benchmarked portfolio demonstration
```

That progression tells a much stronger story than one large commit produced after months of preparation.

---

# What Not to Do

I would specifically avoid five traps.

## 1. Do not let the coding agent design the whole architecture in one pass

You should retain architectural authorship.

## 2. Do not chase every interesting technology immediately

Arrow, DataFusion, COPC, GeoArrow, Swift, Metal, gRPC, Tokio, Kubernetes, object storage, computer vision, and custom formats are all interesting.

They do not all belong in week one.

## 3. Do not confuse infrastructure complexity with distributed-systems knowledge

Three well-understood local nodes with retries, routing, partial failure, and instrumentation can teach and demonstrate more than a Kubernetes deployment you barely understand.

## 4. Do not optimize merely because the project uses Rust

Benchmark first.

Your own Rust syllabus correctly emphasizes distinguishing algorithmic, memory, I/O, and language-level performance.

## 5. Do not hide behind AI-generated code

If a subsystem becomes important, rewrite or extend a meaningful portion yourself.

That is where passive familiarity becomes engineering fluency.

---

# What I Think the Project Could Eventually Demonstrate

If we execute this carefully, your portfolio story could become unusually coherent.

You already have strong evidence around:

```text
Python
geospatial analytics
spatial databases
raster/vector processing
remote sensing
ML / computer vision
data engineering
production pipelines
```

This project would extend that story downward and outward:

```text
                 Swift
          native spatial client
                   │
                   ▼
Python ───── distributed control plane
                   │
                   ▼
                Rust
      high-performance spatial core
                   │
                   ▼
       point clouds / Arrow / COPC
                   │
                   ▼
        constrained edge nodes
```

That is not a random collection of technologies.

It says:

> **I understand spatial systems across application, orchestration, data, compute, and performance boundaries.**

That is much closer to the “Spatial Systems Engineer” identity that your broader learning strategy is targeting.

---

# Career Value

Your current experience already gives you substantial material around Python geospatial engineering, remote sensing, ML/CV, PostGIS, cloud-native data, orchestration, and performance work.

The important value of this project is therefore not proving that you can build another Python geospatial workflow.

It is adding credible evidence for the missing layers:

```text
systems programming        → Rust
3D spatial data            → point clouds
interoperability           → Rust/Python
distributed computing      → multiple nodes + control plane
edge computing             → local reduction / constrained processing
native applications        → Swift
performance engineering    → benchmarks + profiling
systems design             → architecture + ADRs + failure semantics
```

That is a strategically strong use of portfolio time.

---

# My Recommended Strategy

I would adopt a roughly **70/30 project-to-course relationship** for the next phase.

Not necessarily 70% of clock time exactly, but conceptually:

### 70% — Build the real system

Use Codex or another capable coding agent aggressively for implementation acceleration.

### 30% — Stop and learn whatever the project exposes

Use the formal Rust syllabus, distributed-systems curriculum, documentation, experiments, and manual coding to deepen understanding.

The project creates the questions.

The curriculum answers them.

That is the model I would use.

---

# The First Concrete Sprint

I would begin immediately with a very small **Spatial Edge Platform Sprint 0**.

## Objective

Create the first production-quality Rust component that will eventually become the point-cloud edge-processing core.

## Deliverable

```text
rust/spatial-core
```

with:

```rust
Point3D
BoundingBox3D
PointCloudSummary
summarize_points(...)
```

where the result contains:

```text
count
centroid
min_x / min_y / min_z
max_x / max_y / max_z
```

Requirements:

- idiomatic Rust;
- slices/iterators where appropriate;
- explicit empty-input behavior;
- unit tests;
- documentation;
- `cargo fmt`;
- `cargo clippy`;
- `cargo test`;
- no Python;
- no Swift;
- no networking;
- no LAS;
- no async;
- no premature abstraction.

Then you review the implementation until you can explain:

- every public type;
- ownership/borrowing;
- iterator behavior;
- why the centroid requires an accumulation;
- numeric types;
- complexity;
- allocations;
- empty-input semantics;
- test cases.

After that, the next sprint adds either:

1. bounding-box filtering; or
2. Python interoperability.

My preference would be **bounding-box filtering first**, then Python interoperability.

---

# Final Position

Yes: **start building the real project now.**

Waiting until you “know enough” Rust, distributed systems, point clouds, Swift, and cross-language integration creates a very distant finish line. Those subjects are large enough that you could study them indefinitely without ever feeling completely ready.

But I would not hand the entire project to Codex and simply accept the resulting repository.

The better approach is:

> **You are the system architect and engineering owner. AI is an extremely fast implementation partner. The project is the curriculum.**

Build one narrow vertical slice at a time.

Let each new project requirement expose the next thing you need to learn.

Use the coding agent to eliminate the cost of boilerplate and unfamiliar syntax, but require yourself to understand the data structures, algorithms, boundaries, performance behavior, and architectural decisions.

If we do that, you get both outcomes you want:

```text
faster portfolio progress
          +
real systems understanding
```

rather than having to choose between them.

And importantly, you can start creating interview-worthy evidence **well before the entire long-term Spatial Edge Platform is finished**.
