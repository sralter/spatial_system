# 1 Literature Review

For each relevant project, record:
1. What problem does it solve?
2.  Is it actively maintained?
3.  What are its core abstractions?
4.  What data representation does it use?
5.  Does it copy or borrow data?
6.  What formats does it support?
7.  Could it fit our future architecture?
8.  Should we reuse it, study it, or avoid depending on it?

- LAS for Rust: https://github.com/gadomski/las-rs
  - See its clone here: docs/research/open_source_repositories/las-rs
  1. Purports to read and write ASPRS LAS files all within Rust
  2. This repo seems to hav ea long history, going back 11 years. Its most recent commit was 2 months ago.
  3. One thing I saw `src/error.rs`, which looks like bespoke error states. There's `src/point_data.rs`, which looks like a useful primitive for the repo.
  4. `src/raw/point.rs` looks like to be the ground truth definition of what a `Point` object is.
  5. Unsure - requires agent review
  6. It supports LAS file format.
  7. I think it could be useful when it comes time to write or read LAS files.
  8. 

Point3D representation
coordinate numeric type
slice vs iterator API
dependencies
error / empty-input behavior
likely real-data library
likely future Arrow strategy
likely future indexing direction
technologies deliberately deferred

## Process

### 1. Identify current Rust projects or crates relevant to:
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
- What problem does it solve?
- Is it actively maintained?
- What are its core abstractions?
- What data representation does it use?
- Does it copy or borrow data?
- What formats does it support?
- Could it fit our future architecture?
- Should we reuse it, study it, or avoid depending on it?

### 2. Key question
> What abstractions have already proven useful for representing and processing 3D point data?

### 3. Point-cloud data formats
- LAS
- LAZ
- COPC
- Parquet-based representations
- Arrow-based representations
- other relevant cloud-native approaches

Questions to ask:
- How are points physically stored?
- What attributes can points contain?
- How is spatial locality represented?
- How is random/spatial access achieved?
- How is compression handled?
- How does the format behave over object storage?
- What ideas matter for our future edge system?

### 4. Other data to collect:
- SQL over point data;
- spatial predicates over point collections;
- partition pruning;
- spatial indexing;
- columnar point-cloud storage;
- query planning;
- distributed point-cloud querying.

### 5. Edge and distributed spatial systems
Collect examples of systems where spatial or sensor data is processed near its source, such as:
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

Satellite onboard processing should be one research category, but other domains will use similar ideas, like:
- robotics;
- autonomous vehicles;
- drones;
- environmental sensor networks;
- mobile devices;
- IoT;
- industrial monitoring