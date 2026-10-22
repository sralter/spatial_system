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