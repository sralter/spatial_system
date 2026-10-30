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
  8. It should at least be a jumping off point for our purposes.

- Cloud-Optimized Point Cloud (COPC) for Rust: https://github.com/360-geo/copc
  - See its clone here: docs/research/open_source_repositories/copc
  1. Streams the opening of COPC files with async functionality
  2. This repo appears to be actively maintained, though its last activity was 3 months ago
  3. There's a streaming section and a temporal section of the repo. The temporal section seems to control for filtering point clouds by their capture date. Other abstractions, which I take to mean individual modules, include chunks and error handling.
  4. I'm not sure how to answer this. I think my knowledge of Rust is not at that point yet.
  5. I see some "&" in the repo, so that would suggest that it uses borrowing, at least for some things.
  6. LAZ, LAZ (and I assume COPC formats)
  7. I think this could definitely be used, especially for seeing how to structure streaming code and temporal filtering.
  8. We should study and reuse it.

- SpatialRust computing suite for point clouds, computer vision, and GPU compute without C++/FII layer: https://github.com/rsasaki0109/SpatialRust.git
  - See its clone here: docs/research/open_source_repositories/SpatialRust
  1. This looks like to be a one-stop shop for geospatial processing that relies on the heavy use of agent-assisted coding
  2. Very actively maintained. As of this writing (2026-10-16 17:19), the last commit was 33 minutes ago.
  3. Hard to characterize the core abstractions. The crates/ directory has a huge amount within it: Vision, search, vocelization, pipeline, math, metrics, pipeline, io, etc.
  4. I don't know how to answer this question right now.
  5. Hard to give one answer for this.
  6. The tags on the repo include `COPC`. IT seems to be focused mainly on raster (RGB+) and point cloud data.
  7. This repo is perhaps the closest to what we are trying to build here. The difference is that we have an emphasis on edge computing, and I'm not sure if that is what this repo is focusing on. Also, we have a goal of creating a SQL engine for point clouds, which doesn't appear to be the focus here.
  8. We should reuse and study it, with proper attribution, of course.

- Pure math Rust spatial positioning methods and common filters: https://github.com/joeysapp/spatial-core
  - See its clone here: docs/research/open_source_repositories/spatial-core
  1. Looks to be like a Rust-based implementation of the mathematics behind spatial positioning.
  2. This does not look to be actively maintained. In fact, it appears to have been a one-time upload so that the user could save and publish their work for the world to see.
  3. Quaternion is one abstraction, one struct, that is based in pure mathematics and I had never heard of it before today.
  4. As before, I don't think I know enough to answer this question correctly.
  5. It borrows data as far as I can tell.
  6. I'm not sure which formats it supports.
  7. I think it could fit into our architecture. If we need to do spatial positioning processing, we should look to this implementation.
  8. Perhaps it's more a repo that we should study rather than reuse, but that depends on a deeper review and the needs of the repo as it develops.

- Rust-based autonomous vehicle LiDAR point cloud spatial octree filter: https://github.com/ejajmahmud/lidar-pointcloud-octree-spatial-filter-rust-lidar-octree-filter-v2026-b70
  - See its clone here: docs/research/open_source_repositories/lidar-pointcloud-octree-spatial-filter-rust-lidar-octree-filter-v2026-b70
  1. This looks to be a thin project. I thought there was more to it.
   2. We should avoid this and find something that actually implements an autonomous vehicle octree filter.

- Lightweight type-1 Rust Hypervisor for edge devices: https://github.com/syswonder/hvisor
  - See its clone here: docs/research/open_source_repositories/hvisor
  1. A Rust-based virtual machine monitor to allow for edge computing. It creates virtual machines from a shared physical computer.
  2. Yes, it is actively maintained, with the most-recent pushes occurring 3 days ago (as of 2026-10-19)
  3. I don't know enough to answer this question
  4. I don't know enough to answer this question
  5. I'm not sure
  6. I'm not sure
  7. I think this could absolutely fit into our future architecture. In fact, we could use this exact project to handle the edge computing part of the project.
  8. We should reuse it.

- 3D simulator for training autonomous drones and ground vehicles: deterministic Rust physics, procedurally generated worlds, batched Gymnasium API, Bevy viewer: https://github.com/robertscholz22/autonomousim
  - See its clone here: docs/research/open_source_repositories/autonomousim
  1. This is more for fun, but it allows for a virtual testing environment for the software running drones and vehicles
  2. Yes, last update was two weeks ago (today is 2026-10-19)
  3. I'm not sure
  4. I'm not sure
  5. I'm not sure
  6. I'm not sure
  7. I'm sure there's something that we could find useful, but maybe only use this repo if we decide we need simulations
  8. Study it

- Apache Arrow: https://github.com/apache/arrow-rs
  - I am not going to git clone this locally
  1. Highly-regarded library, I list it here because we will most certainly use it at some point.

- Apache DataFusion: https://github.com/apache/datafusion
  - I am not going to git clone this locally
  1. Highly-regarded library, I list it here because we will use it when creating our point cloud query tool

- Machine Learning infrastructure in Rust, particularly numr (https://github.com/ml-rust/numr), a Rust-based NumPy equivalent (in progress): https://github.com/ml-rust
  - I am not going to git clone this locally, it's probably too large
  1. This seems like a promising library for our purposes, since we are relying on Rust for lower-level processing. However, Python's NumPy may be better when we need linear algebra and vectorized processing for heavy numerical loads.

- Serialization framework for Rust: https://github.com/serde-rs/serde
  - I am not going to git clone this locally
  1. Allows for serialization in Rust
  2. Yes, it's widely used
  3. I'm not sure
  4. I'm not sure
  5. I'm not sure
  6. I'm not sure
  7. Yes, I'm guessing we'll need to use it when we need data to be serialized
  8. Reuse it

- Kubernetes Native Edge Computing Framework: https://github.com/kubeedge/kubeedge
  - I am not going to git clone this locally
  1. This seems like a well-known edge computing framework, though it's written in Go and seems to be a lot more complicated than what we'll need at the beginning. Maybe it will be useful in the future.

- Rust library for point cloud processing: https://github.com/igd-geo/pasture
  - I am not going to git clone this locally
  1. This is an older repo but maybe worth studying for our work.

- Point Cloud Library: https://github.com/PointCloudLibrary/pcl
  - I am not going to git clone this locally
  1. This should be used as a reference and possibly reuse.

- Extension for PostgreSQL to allow it to store point clouds: https://github.com/pgpointcloud/pointcloud
  - I am not going to git clone this locally
  1. This is extremely close to what I was thinking, and may indicate that a "SQL engine for point clouds" already exists.
   
- Rust-based GIS App: https://github.com/opengeos/RustGIS
  - I am not going to git clone this locally
  1. Probably the closest example of a large component of what we want to do. 
     1. We could adapt individual operations for an edge computing demonstration?
     2. Build on the work?

---

## Second pass — 2026-10-30: query-engine focus and RustGIS reuse

The observations above are preserved as the original research journal. This
addendum records the implementation review, rather than silently rewriting those
observations. The first overall deliverable is now selective COPC querying through
Rust/DataFusion; Sprint 1 is research and a reproducible local baseline. The Rust
point-summary implementation is paused.

### RustGIS: reuse the right layer

Reviewed revision: `8294f56a0f8d8dd982795d03eb8e46826e372631` (2026-10-30).
[Source revision and file hashes](../../benchmarks/pointcloud/sources.json).

1. **Problem:** a layered desktop/web GIS and scriptable command system, including
   data access, analysis and external tools. It is not evidence that every advertised
   operation is implemented directly in one reusable RustGIS library.
2. **Maintenance:** the inspected revision is dated October 30; this is activity
   evidence, not an independent stability or correctness assessment.
3. **Abstractions:** geometry/extents, owned feature datasets and typed attributes,
   data providers, analysis tools, commands, sessions, and separate frontends.
4. **Representation:** the geometry core has 2D coordinates and geographic/Web
   Mercator conventions. LiDAR Z is an attribute in its feature-oriented import
   path; this differs from native-CRS XYZ Arrow batches.
5. **Data movement:** the LiDAR reader allocates a sampled point collection. The
   data crate has substantial format/database dependencies; lower layers are
   UI-independent, but that alone does not make them minimal engine dependencies.
6. **Formats:** LAS/LAZ/COPC import is documented, with sampling/caps. The reviewed
   importer does not use the COPC hierarchy for map views; remote files download
   whole. Reading a COPC container is different from exact indexed SQL execution.
7. **Fit:** useful architecture, source and test references; possible future engine
   consumer. The GeoLibre/Whitebox suite is a separate optional runner, so assess
   that implementation and process boundary separately.
8. **Decision:** prefer the public APIs of underlying libraries for needed
   operations. Evaluate individual RustGIS crates only when their semantics and
   dependency cost fit. No code was copied and no RustGIS dependency was added.

Sources at the pinned revision:
[architecture](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/docs/architecture.md),
[LiDAR implementation](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/data/src/lidar.rs),
[analysis dependencies](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/analysis/Cargo.toml),
[geometry](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/geom/src/lib.rs),
[GeoLibre runner](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/geolibre/src/lib.rs),
[attribution and independently generated reference tests](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/ATTRIBUTION.md).
RustGIS is Apache-2.0; underlying crates, runners, assets and test data have their
own notices. Follow the applicable notices if reuse is selected.

### Corrections and additions across the ecosystem

- **las-rs:** public decoded `Point` uses f64; raw records use integer coordinates
  with scale/offset. The inspected clone also has owned packed point storage with
  borrowed accessors and owned point materialization. LAZ support is feature-gated.
- **COPC:** owned fetched/decompressed buffers coexist with borrowed column views.
  Seeing `&` does not establish zero-copy ingestion. Its temporal index is an
  additional capability, not a property every COPC file supplies. The inspected
  byte-source futures are non-Send: a concrete DataFusion integration question.
- **pasture:** ownership traits and interleaved/columnar layouts directly address
  earlier uncertainty about data representation. Study the public buffer API;
  direct COPC pruning support has not been established here.
- **PCL:** an established reference for point algorithms and semantics. It does not
  justify bringing C++ bindings into this small Rust path.
- **pgPointcloud:** SQL over point clouds already exists. Its schema/patch storage,
  dimensional filters and PostGIS integration are a capability baseline, with
  ingestion/setup costs distinct from direct-file access. Its documented
  `PC_FilterBetween` endpoints are exclusive: normalize semantics in comparisons.
- **DuckDB–PDAL:** an additional mandatory competitor. The reviewed source describes
  SQL filter translation into PDAL expression filters. That does not by itself
  prove COPC hierarchy pushdown. Signed-extension availability varies by release
  and platform; the benchmark records the executable probe separately.
- **SpatialRust:** useful schema/column-buffer ideas; breadth alone does not prove
  an appropriate dependency. **joeysapp/spatial-core** is positioning mathematics,
  not a point-cloud format/query library. **hvisor** is hardware virtualization,
  not a prerequisite for simulated edge workers. The advertised octree repository's
  inspected entry point prints status rather than implementing an octree filter.
- **autonomousim:** retain as a future sensor-data reference. Infinite ranges can
  represent missing returns, so a later ingestion layer must establish valid XYZ.
- **Arrow/DataFusion:** reuse columnar execution and SQL planning when implementing
  the next vertical. **Serde**, **numr**, **KubeEdge**, ML and Swift remain deferred
  until a concrete boundary or workload requires them.

Published references: [pasture buffers](https://docs.rs/pasture-core/0.5.0/pasture_core/containers/index.html),
[PCL](https://github.com/PointCloudLibrary/pcl),
[pgPointcloud patches](https://pgpointcloud.github.io/pointcloud/functions/patchs.html),
[DuckDB–PDAL](https://github.com/ahuarte47/duckdb-pdal/tree/29a535197d05fb69f42da40962fa6ed5948d99ba).
The [query landscape](point-cloud-query-landscape.md) contains the operation-level
reuse matrix, source evidence, numerical conformance findings, and baseline report.

### Decisions

| Question | Decision | Confidence | Revisit when |
|---|---|---|---|
| First overall subsystem | Rust/DataFusion selective COPC queries | High on direction; utility unproven | Baseline and existing adapters reviewed |
| Sprint 1 implementation | Research tooling and local baseline only | High | Next bounded vertical approved |
| Adopt RustGIS wholesale | No; assess lower layers and underlying libraries | High | A needed operation fits a specific public API |
| Write GIS algorithms/parsers now | No | High | A documented gap remains after reuse evaluation |
| Point3D slice API | Park the prior learning proposal | High | A learning exercise or actual consumer needs it |
| Real-data reader | Evaluate mature COPC/LAS readers; no production choice yet | Medium | Version, Send and conformance spike |
| Claims of novelty or speed | None for a new engine | High | Equivalent-workload measurements exist |
| Next work | Bounded DataFusion interoperability/measurement spike or upstream contribution | Medium | Review the benchmark and feasibility gate |
