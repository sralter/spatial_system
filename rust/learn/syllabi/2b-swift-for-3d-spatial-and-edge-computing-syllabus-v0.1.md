# Swift for 3D Spatial & Edge Computing

**Syllabus Version:** 0.1  
**Course / Track:** 3B within the broader Spatial Systems Engineering program  
**Filename Sequence:** `2b-swift-for-3d-spatial-and-edge-computing-syllabus-v0.1.md`  
**Course Format:** Self-paced, ChatGPT-guided, project-based  
**Expected Commitment:** Up to 30 minutes per session; approximately 3–4 hours per unit, with additional time for checkpoints, real-world acquisition, benchmarks, and capstone hardening  
**Prerequisite Course:** *Swift for Spatial & Edge Computing v0.1*  
**Earlier Program Foundations:** *Rust for Geospatial Systems v0.2* and *Spatial Systems & Distributed Computing v0.1*  
**Primary Prior Knowledge:** Swift fundamentals, SwiftUI, MapKit, Core Location, Apple-native persistence, networking, offline synchronization, Core ML deployment, Python, SQL/PostGIS, Rust fundamentals, spatial analysis, distributed systems, and performance measurement  
**Prerequisite 3D Knowledge:** None required beyond ordinary geospatial coordinate/CRS familiarity  
**Strategic Context:** *Spatial Systems Engineering Learning Program — Working Strategy and North Star*  
**Portfolio Domain:** 3D extension of the existing Spatial Edge Platform using iPhone LiDAR/depth, point clouds, Rust spatial processing, Python analysis, and distributed 3D data movement  
**Course Vintage:** September 2026  

---

# 1. Course Purpose

This course extends the existing **Spatial Edge Platform v2** from primarily 2D mobile spatial sensing into **3D spatial systems engineering**.

Course 3A established a real iPhone edge node with:

- native SwiftUI application architecture;
- MapKit;
- Core Location;
- selected device sensors;
- durable local state;
- offline-first synchronization;
- local spatial computation;
- Core ML;
- real-device profiling;
- a stable distributed node contract.

Course 3B adds a new class of spatial data:

> **high-volume 3D observations of the physical world.**

The objective is not merely to learn how to display a 3D scene or call a LiDAR API.

The objective is to become sufficiently capable to:

- understand modern point-cloud data and its systems implications;
- understand 3D coordinate systems, frames, transforms, and registration at a practical engineering level;
- acquire depth and 3D spatial data from Apple hardware;
- understand ARKit's role in tracking, camera pose, depth, and spatial sensing;
- use RealityKit or another appropriate Apple-native 3D framework as an inspection/product layer;
- convert raw mobile 3D observations into explicit spatial data products;
- represent point clouds with useful metadata and provenance;
- filter, crop, downsample, voxelize, summarize, and index 3D data;
- understand KD-trees, octrees, voxel grids, and spatial hashing conceptually and implement selected structures where educationally valuable;
- work with modern point-cloud formats and tooling;
- reason about LAS/LAZ, COPC, PDAL, tiled/chunked representations, and cloud-native access patterns;
- connect the earlier Rust spatial systems layer to real 3D workloads;
- introduce direct Swift ↔ Rust interoperability only where a measured 3D workload justifies it;
- design chunked local storage for point-cloud data;
- stream or selectively synchronize 3D chunks instead of assuming whole-dataset transfer;
- preserve 3D coordinate, transform, timestamp, sensor, and provenance semantics across the distributed system;
- compare raw versus locally processed 3D transfer;
- perform useful 3D computation at the edge;
- explore selected 3D machine-learning or classification workflows when they serve the platform;
- ingest or process drone/photogrammetric point clouds as a second acquisition modality;
- compare mobile LiDAR and aerial/photogrammetric data within one spatial architecture;
- measure memory, CPU, storage, bandwidth, latency, and energy implications of 3D processing;
- build failure-aware, observable 3D data pipelines;
- explain where Swift, Rust, Python, PostGIS, object/file storage, and point-cloud tooling belong; and
- deliver a portfolio-grade distributed 3D spatial system rather than a disconnected LiDAR demo.

The course begins from a concrete transition:

```text
Course 3A
2D mobile observation
latitude + longitude + sensor value
        │
        ▼
Course 3B
3D spatial acquisition
many x/y/z observations + attributes + transforms
```

That transition changes the systems problem.

A single 2D observation may be tiny.

A 3D acquisition may contain:

- thousands;
- millions;
- or far more

individual spatial samples.

This makes familiar themes newly important:

- memory layout;
- indexing;
- chunking;
- streaming;
- compression;
- local processing;
- parallelism;
- storage;
- network transfer;
- selective access;
- synchronization;
- coordinate transforms;
- provenance;
- visualization.

The guiding course question is:

> **How should a spatial edge platform acquire, represent, process, index, store, transfer, and reason about 3D observations of the physical world under real device and distributed-system constraints?**

The recurring architectural question is:

> **Which 3D computations and data products belong on the device, which belong in Rust, which belong centrally, and which data should move across the network at all?**

---

# 2. Strategic Role in the Larger Program

This syllabus is **Course / Track 3B** of the broader **Spatial Systems Engineering** program.

The long-term professional target remains:

> **Spatial Systems Engineer**

The broader capability profile includes:

```text
2D spatial systems
       ↓
distributed edge computing
       ↓
real Apple edge device
       ↓
3D spatial sensing
       ↓
high-volume spatial data
       ↓
3D spatial algorithms
       ↓
distributed 3D processing
```

Course 3B occupies the intersection of the program's three technical cores:

```text
                      3D SPATIAL SYSTEM
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
     SPATIAL CORE        SYSTEMS CORE       PRODUCT CORE
          │                  │                  │
     point clouds           Rust              Swift
     3D geometry         memory/I/O           ARKit
     transforms          indexing             RealityKit
     registration        chunking             LiDAR/depth
     CRS/frames          streaming            native UI
     spatial index       performance          device sensing
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                        Python / ML
                             │
                        central data
```

The intentional responsibilities remain:

| Layer | Primary Technology | Purpose |
|---|---|---|
| Apple hardware acquisition | Swift + Apple APIs | camera pose, depth/LiDAR access, device integration |
| Apple-native 3D product | SwiftUI + ARKit/RealityKit as appropriate | acquisition control, 3D inspection, system state |
| Performance-sensitive 3D compute | Rust | point-cloud algorithms, indexing, chunk processing, memory-conscious computation |
| Scientific / experimental 3D work | Python | exploration, validation, ML, point-cloud analysis, benchmark analysis |
| Central metadata / spatial catalog | PostgreSQL / PostGIS | acquisition footprints, node metadata, derived spatial records, queryable catalog |
| Large 3D payload storage | appropriate file/object storage | point clouds, chunks, derived products |
| Point-cloud interoperability | LAS/LAZ/COPC and appropriate tooling | standard interchange and scalable access |
| Analytical workflows | Python / DuckDB / Arrow / Parquet where appropriate | analysis and derived tabular/spatial products |
| On-device ML | Core ML where justified | local model deployment |
| Distributed control | existing Python control plane | jobs, metadata, synchronization, platform integration |

A critical architectural principle is:

> **PostGIS does not need to become the byte store for every point in every scan merely because the platform already uses PostGIS.**

Likewise:

> **Swift does not need to become the high-performance point-cloud engine merely because the data originates on an iPhone.**

Course 3B should make storage and compute placement explicit.

---

# 3. Starting Point: Spatial Edge Platform v2

The course does not begin from a blank Xcode project.

It begins with the Course 3A platform:

```text
Rust Node A ──┐
Rust Node B ──┤
              │
iPhone Node ──┼──── Python Control Plane ──── PostGIS
              │
Rust Node D ──┤
Rust Node E ──┘
```

The iPhone already provides:

```text
SwiftUI
MapKit
Core Location
selected sensors
local persistence
offline synchronization
Core ML
observability
profiling
stable node identity
stable observation identity
```

Course 3B adds a 3D acquisition path:

```text
                       iPhone
                         │
             ┌───────────┼───────────┐
             │           │           │
           camera      depth       motion
             │         LiDAR         pose
             └───────────┼───────────┘
                         ▼
                    3D acquisition
                         │
                         ▼
                 local point cloud
                         │
             ┌───────────┼───────────┐
             │           │           │
           inspect     process     persist
             │           │           │
             └───────────┼───────────┘
                         ▼
                   chunk / summarize
                         │
                         ▼
                    synchronize
                         │
                         ▼
               Python control plane
                         │
             ┌───────────┼────────────┐
             ▼           ▼            ▼
          PostGIS    object/files   Rust/Python
          metadata    3D payloads    processing
```

The architecture should evolve only when 3D data creates a demonstrated need.

---

# 4. Governing Course Principles

## 4.1 3D Is a Systems Escalation, Not a New Demo

The governing progression is:

```text
existing spatial platform
        ↓
add 3D sensing
        ↓
data volume increases
        ↓
new indexing/storage/transfer problems appear
        ↓
reuse earlier systems concepts
        ↓
extend architecture deliberately
```

The course should never devolve into:

```text
open Xcode
   ↓
show cool LiDAR visualization
   ↓
course complete
```

The 3D data must participate in the same platform.

---

## 4.2 Point Clouds Are a Natural Systems Problem

A point cloud may contain:

```text
x
y
z
intensity
classification
color
timestamp
confidence
normal
source
```

and potentially millions of points.

This creates direct systems questions:

- How are points laid out in memory?
- Can the whole acquisition fit in memory?
- What is the access pattern?
- How is space partitioned?
- How are chunks selected?
- How much data must be transmitted?
- What should be compressed?
- Which computations can stream?
- Which computations require neighborhoods?
- How should indexes be persisted?
- What metadata is required to interpret the points later?

A governing statement is:

> **Point clouds are a geospatial problem and a systems problem at the same time.**

---

## 4.3 Coordinate Frames Are First-Class Data

In 2D geospatial work, the student already understands that coordinates without CRS context are dangerous.

3D mobile sensing introduces additional frame semantics:

```text
device frame
camera frame
AR/session frame
local world frame
geographic frame
projected CRS
```

A point such as:

```text
(1.2, -0.4, 2.8)
```

is meaningless without knowing:

- relative to what origin;
- in what axis convention;
- in what units;
- at what time;
- under which transform.

Therefore:

> **Transforms and frame metadata are part of the data contract, not incidental implementation details.**

---

## 4.4 Build from Small Physical Spaces

Early 3D work should use bounded scenes:

- a desk/object;
- a room;
- a wall;
- a building façade;
- a small outdoor feature.

Do not begin with:

- city-scale digital twins;
- enormous public LiDAR collections;
- nationwide point clouds;
- multi-drone production pipelines.

Small scenes make it possible to understand:

- acquisition;
- transforms;
- point density;
- noise;
- indexing;
- processing;
- transfer;
- reconstruction;
- failure.

Scale should increase only after the data model is understood.

---

## 4.5 Swift Owns Acquisition and Native Interaction

Swift should primarily own:

- Apple hardware access;
- AR session lifecycle;
- device pose;
- LiDAR/depth acquisition;
- camera/depth coordination;
- local mobile state;
- acquisition controls;
- native 3D inspection;
- offline behavior;
- synchronization orchestration;
- lightweight local processing when appropriate.

Swift should not automatically own:

- every point-cloud algorithm;
- every index implementation;
- every file-format parser;
- large central processing jobs.

The course should repeatedly ask:

> **Is this native-device logic or reusable spatial systems logic?**

---

## 4.6 Rust Earns a Larger Role in 3D

Course 3A could defer direct Swift ↔ Rust interoperability because the 2D mobile workloads did not necessarily justify it.

Course 3B should revisit that decision.

3D creates plausible reasons for a Rust core:

- memory-conscious point processing;
- voxelization;
- neighborhood queries;
- spatial indexes;
- chunk processing;
- binary serialization;
- compression;
- streaming transforms;
- reusable algorithms across edge and central environments.

However:

> **Do not add FFI merely because Course 3B contains Rust.**

First implement or measure a representative Swift/Python path.

Then identify a real bottleneck or reuse opportunity.

Then decide whether Rust improves the architecture.

---

## 4.7 Use Standard Formats Before Inventing New Ones

The earlier Rust course may contain a custom `.spat` file-format learning vehicle.

Course 3B should first understand established point-cloud ecosystems:

- LAS;
- LAZ;
- COPC;
- PDAL;
- tiled/chunked point-cloud approaches;
- relevant Arrow/Parquet representations where appropriate.

A custom representation may be extended only when doing so teaches a clear systems concept.

The governing rule is:

> **Understand the standards before designing around them or departing from them.**

---

## 4.8 Separate Metadata from Heavy Payloads

A 3D acquisition may naturally separate into:

```text
ACQUISITION METADATA
small, queryable, relational/spatial
        │
        ├── acquisition_id
        ├── node_id
        ├── timestamp
        ├── footprint
        ├── bounds
        ├── CRS/frame metadata
        ├── point count
        ├── processing state
        └── storage reference

3D PAYLOAD
large binary/chunked object
        │
        ├── points
        ├── attributes
        ├── chunks
        └── indexes
```

PostGIS may catalog the acquisition without storing every raw point as a row.

This distinction should be learned through implementation.

---

## 4.9 Process Before Transfer When Evidence Supports It

A central edge-computing question becomes more consequential with 3D data.

Compare:

```text
raw scan
   ↓
network
   ↓
central processing
```

with:

```text
raw scan
   ↓
local crop/filter/downsample
   ↓
chunk / compress
   ↓
network
   ↓
central processing
```

Measure:

- bytes;
- latency;
- local CPU;
- local memory;
- energy;
- information loss;
- downstream flexibility.

The expected answer is not predetermined.

---

## 4.10 Visualization Is for Understanding the System

3D visualization is required because the student needs to inspect:

- geometry;
- orientation;
- alignment;
- classification;
- processing states;
- chunks;
- bounds;
- registration;
- errors.

The course does not aim to become:

- a 3D graphics curriculum;
- a game-engine curriculum;
- a RealityKit effects curriculum;
- an AR experience-design curriculum.

The visualization should be good enough to understand the spatial data and demonstrate the platform.

---

## 4.11 Drone and Photogrammetry Data Are a Second Modality

The course should eventually introduce a second 3D source:

```text
iPhone LiDAR
```

and:

```text
drone / photogrammetric point cloud
```

This creates an important systems lesson:

> **A well-designed 3D platform should not assume that all 3D data originates from one Apple sensor.**

The second modality tests:

- file-format boundaries;
- coordinate systems;
- scale;
- metadata;
- processing portability;
- central ingestion;
- visualization.

Actual drone ownership is not required.

Existing imagery or point-cloud data may be used.

---

## 4.12 Failure and Measurement Remain Core Teaching Tools

Every major 3D capability should be tested under:

- malformed data;
- incomplete acquisition;
- transform error;
- unavailable sensor;
- memory pressure;
- storage pressure;
- interrupted processing;
- network loss;
- partial chunk transfer;
- duplicate synchronization;
- corrupt chunk;
- version mismatch.

Every major performance claim should be measured.

---

# 5. The 3D Systems Lens

Course 3A used the **Native Systems Lens**.

Course 3B extends this into the **3D Systems Lens**.

The guiding question is:

> **What mathematical, spatial, data-structure, or systems concept makes this 3D behavior understandable rather than magical?**

Likely interludes include:

- vectors;
- coordinate bases;
- homogeneous coordinates conceptually;
- rigid transforms;
- translation;
- rotation;
- matrices;
- quaternions conceptually;
- local versus global frames;
- pose;
- projection;
- depth;
- camera intrinsics conceptually;
- camera extrinsics conceptually;
- point density;
- sampling;
- quantization;
- measurement noise;
- nearest neighbors;
- spatial locality;
- bounding boxes;
- voxel grids;
- KD-trees;
- octrees;
- spatial hashing;
- registration;
- ICP conceptually;
- normals;
- surface representation;
- chunk boundaries;
- memory layout;
- structure-of-arrays versus array-of-structures conceptually;
- streaming algorithms;
- compression;
- range/selective reads;
- multiresolution representations;
- file metadata;
- distributed chunk identity;
- eventual synchronization of large payloads.

This is not a full computer graphics, robotics, photogrammetry, or computational geometry curriculum.

The concepts are introduced when they become useful to the evolving platform.

---

# 6. Standard Learning Loop

Each unit should remain divisible into approximately 30-minute sessions.

A typical unit may contain:

### Session A — 3D Concept

Introduce the spatial/math/data concept.

### Session B — Known → Unknown

Bridge from 2D GIS, Rust, Python, Course 3A Swift, or distributed systems.

### Session C — Small Exercise

Manipulate a small synthetic 3D dataset.

### Session D — 3D Systems Lens

Explain the deeper transform, data-structure, memory, or systems behavior.

### Session E — Apple / Real-Device Application

Apply the concept to iPhone sensing or native visualization.

### Session F — Rust / Python Comparison

Implement or inspect the same operation in another layer where educationally useful.

### Session G — Integration

Connect the capability to the existing Spatial Edge Platform.

### Session H — Failure Experiment

Break a transform, chunk, transfer, sensor path, or processing stage deliberately.

### Session I — Measurement

Measure memory, runtime, bytes, storage, latency, or energy.

### Session J — Industry Connection

Relate the lesson to modern point-cloud, Apple spatial, mapping, robotics-adjacent, or geospatial systems engineering.

### Session K — Portfolio Increment

Integrate the capability into the evolving 3D platform.

Not every unit requires every session type.

---

# 7. Teaching and Feedback Method

Instruction should continue the existing pattern:

```text
teach
  ↓
small synthetic example
  ↓
student prediction
  ↓
student implementation
  ↓
review
  ↓
inspect visually/numerically
  ↓
integrate real data
  ↓
inject failure
  ↓
measure
  ↓
revise architecture
  ↓
document
```

Code and architecture review should distinguish:

1. **3D correctness** — Are coordinates, frames, transforms, units, and bounds correct?
2. **Swift correctness** — Is the native acquisition/application code idiomatic and safe?
3. **Rust correctness** — Are memory and algorithm boundaries explicit where Rust is used?
4. **Data-structure reasoning** — Does the chosen index fit the access pattern?
5. **Storage reasoning** — Is the payload represented appropriately?
6. **Distributed correctness** — What happens under partial chunk transfer, retry, duplicate, or restart?
7. **Spatial correctness** — Are CRS, local frames, geographic references, and provenance preserved?
8. **Performance** — Are runtime and memory measured?
9. **Data movement** — Is the system transmitting unnecessary data?
10. **Resource behavior** — Can the mobile node remain bounded?
11. **Interoperability** — Can Swift, Rust, Python, and standard formats exchange data reliably?
12. **Visualization usefulness** — Can processing errors be seen and diagnosed?
13. **Failure behavior** — Can corrupted or incomplete 3D state be recovered?
14. **Observability** — Can an engineer trace an acquisition and its chunks?
15. **Architecture** — Are responsibilities placed deliberately?
16. **Scope discipline** — Is the project still one understandable platform?

---

# 8. Course Architecture

The course contains **12 primary units across four phases**.

```text
PHASE I
Learn the 3D Data Model

1. From 2D Geometry to 3D Spatial Data
2. Coordinate Frames, Pose, and Transforms
3. Point-Cloud Ecosystem, Formats, and Tooling
        │
        ▼
CHECKPOINT 1
3D Spatial Data Workbench


PHASE II
Acquire and Inspect the Physical World

4. ARKit, Depth, and LiDAR Acquisition
5. Point-Cloud Construction and 3D Visualization
6. Registration, Georeferencing, and Acquisition Quality
        │
        ▼
CHECKPOINT 2
Real iPhone 3D Sensor Node


PHASE III
Build the 3D Systems Layer

7. Point-Cloud Processing and Spatial Algorithms
8. 3D Spatial Indexing and Chunked Storage
9. Swift ↔ Rust 3D Compute Boundary
        │
        ▼
CHECKPOINT 3
High-Performance 3D Edge Pipeline


PHASE IV
Distribute, Compare, and Harden the 3D Platform

10. Distributed 3D Transfer and Edge Processing
11. Photogrammetry, Drone Data, and Multi-Source 3D
12. 3D ML, Benchmarking, Reliability, and Platform Hardening
        │
        ▼
CHECKPOINT 4
Spatial Edge Platform v3
Distributed 3D Spatial System
```

---

# PHASE I — LEARN THE 3D DATA MODEL

# Unit 1 — From 2D Geometry to 3D Spatial Data

## Core Topics

- 2D versus 3D coordinates;
- `x`, `y`, `z`;
- point clouds;
- point attributes;
- bounds;
- extents;
- point count;
- density;
- units;
- precision;
- numeric representation;
- RGB/color;
- intensity;
- classification;
- timestamp;
- confidence;
- provenance;
- organized versus unorganized point sets conceptually;
- raster/vector/point-cloud comparison.

## Known → Unknown

Begin with familiar GIS:

```text
2D point
(x, y)
```

then:

```text
3D point
(x, y, z)
```

then:

```text
3D sample
(x, y, z, color, intensity, classification, time, source...)
```

Compare data models:

```text
VECTOR
small number of meaningful geometries

RASTER
regular grid of cells

POINT CLOUD
large number of irregular 3D samples
```

## 3D Systems Lens — Volume Changes Architecture

Use synthetic datasets to compare:

```text
1 point
1,000 points
1,000,000 points
```

Estimate:

- bytes per point;
- total bytes;
- memory;
- transfer size.

The student should calculate rough size before loading data.

## Exercise

Create a synthetic point cloud in Python and a small typed representation in Rust or Swift.

Compute:

- bounding box;
- centroid;
- point count;
- attribute ranges.

## Spatial Application

Add a `PointCloudAcquisition` domain concept to the platform.

Potential metadata:

```text
acquisition_id
node_id
captured_at
point_count
bounds
coordinate_frame
units
source_type
processing_state
storage_reference
```

## Failure Experiment

Introduce:

- NaN;
- impossible bounds;
- wrong units;
- missing frame metadata;
- inconsistent point attributes.

Discuss what should be rejected versus retained with warning.

## Portfolio Increment

Add a `3d/` or equivalent domain area without restructuring the entire repository unnecessarily.

---

# Unit 2 — Coordinate Frames, Pose, and Transforms

## Core Topics

- coordinate frame;
- origin;
- axes;
- handedness conceptually;
- translation;
- rotation;
- scale;
- rigid transformation;
- transformation matrices;
- homogeneous coordinates conceptually;
- pose;
- local/world/device/camera frames;
- quaternion conceptually;
- geographic versus local coordinates;
- projected CRS versus local metric frame;
- transform composition;
- transform inversion.

## Known → Unknown

Bridge from familiar GIS transformations:

```text
EPSG:4326
   ↓
ST_Transform
   ↓
projected CRS
```

to local 3D sensing:

```text
camera coordinates
      ↓ transform
AR world coordinates
      ↓ transform / anchor
local acquisition coordinates
      ↓ optional georeference
geographic/projected system
```

The mechanisms differ, but the core lesson is familiar:

> Coordinates are meaningful only relative to a defined reference system.

## 3D Systems Lens — Transform Chains

Represent:

```text
P_camera
   ↓ T_camera_to_world
P_world
   ↓ T_world_to_project
P_project
```

Work through small numeric examples.

The student should be able to predict what translation and rotation do before running code.

## Exercise

Transform a small cube or set of points.

Verify:

- transformed bounds;
- distances preserved under rigid transform;
- inverse transform returns the original points within tolerance.

## Failure Experiment

Intentionally:

- swap axes;
- use degrees as radians;
- invert the wrong matrix;
- apply transforms in the wrong order;
- mix meters and centimeters.

Visualize the consequences.

## Portfolio Increment

Define explicit transform/frame metadata rather than passing anonymous matrices throughout the application.

---

# Unit 3 — Point-Cloud Ecosystem, Formats, and Tooling

## Core Topics

Understand the modern ecosystem before designing custom storage.

Required concepts:

- LAS;
- LAZ;
- COPC;
- PDAL;
- tiled/chunked point-cloud representations;
- Entwine conceptually/historically where relevant;
- Potree or contemporary web visualization concepts where relevant;
- metadata;
- point attributes;
- scale/offset;
- bounding boxes;
- CRS metadata;
- compression;
- random/selective access;
- cloud/object-storage access;
- range reads conceptually.

Python point-cloud tooling may be used for inspection.

## Governing Rule

> **Use standards to learn the problem before extending the custom format.**

## Known → Unknown

Connect to earlier experience:

```text
GeoTIFF
Zarr
Parquet / GeoParquet
```

Ask the same questions:

- Is the data monolithic or chunked?
- Can a spatial subset be read?
- Is metadata self-describing?
- Can the file live remotely?
- Does compression preserve useful access patterns?

## 3D Systems Lens — File Layout Is Query Architecture

Compare:

```text
single compressed blob
```

with:

```text
spatially organized chunks
```

Ask what happens when the user needs only:

```text
one small region
```

## Practical Lab

Using a small public/sample point cloud:

- inspect metadata;
- inspect attributes;
- crop a region;
- convert format where useful;
- compare file sizes;
- inspect bounds and CRS;
- measure read time.

## Architecture Decision

Write:

> **ADR — Standard point-cloud format and internal representation strategy**

The ADR should distinguish:

- interchange;
- local working representation;
- network representation;
- central archival representation.

## Checkpoint 1 — 3D Spatial Data Workbench

The platform now includes:

- typed 3D acquisition metadata;
- explicit coordinate-frame concepts;
- transform utilities/tests;
- small point-cloud inspection tools;
- standard point-cloud format literacy;
- Python-based validation/reference workflows;
- initial storage ADR;
- a reproducible sample dataset.

The student should now be able to explain what a point cloud is as a data system, not only as a picture.

---

# PHASE II — ACQUIRE AND INSPECT THE PHYSICAL WORLD

# Unit 4 — ARKit, Depth, and LiDAR Acquisition

## Core Topics

- ARKit role;
- session lifecycle;
- device tracking;
- camera pose;
- depth;
- scene depth where supported;
- confidence where available;
- LiDAR capability;
- camera frames;
- depth frames;
- timestamps;
- intrinsics conceptually;
- device capability checks;
- permissions;
- acquisition state;
- interruption;
- thermal/resource implications conceptually.

The exact Apple APIs should be refreshed against current documentation when this unit begins.

## Governing Distinction

ARKit is not taught primarily as an augmented-reality effects framework.

It is taught as:

> **an Apple-native spatial sensing and tracking system.**

## Known → Unknown

Course 3A collected:

```text
latitude
longitude
accuracy
timestamp
```

Course 3B collects a spatial field:

```text
camera pose
depth observations
confidence
timestamp
frame metadata
```

## 3D Systems Lens — Depth Is Not Yet a Point Cloud

A depth image or depth sample needs geometric context before becoming 3D world points.

Conceptually:

```text
pixel
  +
depth
  +
camera model
  +
camera pose
  ↓
3D point
```

Do not treat the conversion as magic.

## Real-Device Exercise

Capture a very small scene.

Record:

- acquisition ID;
- start/end time;
- device capability;
- pose/frame metadata;
- depth availability;
- basic quality information.

Do not optimize or build a polished scanner yet.

## Failure Experiments

Test or reason through:

- unsupported device;
- sensor unavailable;
- AR session interruption;
- low-quality depth;
- rapid movement;
- insufficient scene structure;
- application backgrounding;
- incomplete capture.

## Portfolio Increment

The iPhone becomes a real 3D sensing node.

---

# Unit 5 — Point-Cloud Construction and 3D Visualization

## Core Topics

- depth-to-point conversion;
- camera intrinsics at a practical level;
- sampling pixels;
- world transform;
- point color association where useful;
- point accumulation;
- point density;
- filtering invalid depth;
- confidence filtering;
- bounding box;
- local point-cloud buffer;
- 3D visualization;
- RealityKit or appropriate native 3D rendering;
- camera controls/inspection;
- processing-state visualization.

## Governing Visualization Rule

The goal is to inspect:

- shape;
- orientation;
- density;
- noise;
- missing regions;
- transform errors;
- processing results.

Do not over-invest in rendering effects.

## 3D Systems Lens — Sampling and Data Volume

Compare constructing a point from:

```text
every depth sample
```

versus:

```text
every nth sample
```

Measure:

- point count;
- memory;
- visual usefulness;
- processing time.

## Exercise

Construct a point cloud from a bounded acquisition.

Compute:

- bounds;
- centroid;
- point count;
- density proxy;
- invalid-point count.

Render the result.

## Failure Experiment

Visualize the effects of:

- wrong intrinsics;
- wrong transform;
- axis swap;
- invalid depth;
- duplicate accumulation;
- excessive sampling.

## Portfolio Increment

Add a 3D acquisition/inspection view to the existing Swift application.

The application should still expose:

- node state;
- synchronization state;
- acquisition metadata;
- diagnostics.

---

# Unit 6 — Registration, Georeferencing, and Acquisition Quality

## Core Topics

- relative/local registration;
- pose accumulation;
- drift conceptually;
- overlapping scans;
- point-cloud alignment;
- ICP conceptually;
- correspondences;
- registration error;
- georeferencing;
- Core Location as coarse geographic anchor;
- local metric frame;
- geographic/projected coordinate output;
- accuracy;
- uncertainty;
- provenance;
- acquisition quality metrics.

## Scope Rule

The student does not need to become a SLAM researcher.

The objective is to understand enough to reason about:

- why scans may not align perfectly;
- what tracking contributes;
- what registration attempts to solve;
- what georeferencing can and cannot guarantee.

## Known → Unknown

Connect:

```text
GIS layer alignment
```

with:

```text
3D scan alignment
```

and:

```text
GPS coordinate uncertainty
```

with:

```text
georeferenced 3D acquisition uncertainty
```

## 3D Systems Lens — Local Precision Versus Global Accuracy

A mobile scan can be internally useful in a local frame while its absolute global placement is much less precise.

This distinction should be explicit.

## Practical Exercise

Capture two overlapping small scans or use prepared data.

Compare:

- unaligned;
- pose-aligned;
- optionally refined alignment.

Measure a simple error statistic.

## Geospatial Integration

Create a central acquisition record with:

- approximate geographic location;
- footprint/bounds where meaningful;
- local frame metadata;
- transform metadata;
- quality fields;
- storage reference.

Use PostGIS for the catalog/footprint rather than forcing the full cloud into relational rows.

## Checkpoint 2 — Real iPhone 3D Sensor Node

The iPhone can now:

- start and stop a bounded 3D acquisition;
- collect real depth/LiDAR-derived data;
- preserve pose/frame metadata;
- construct a local point cloud;
- visualize the point cloud natively;
- compute basic acquisition statistics;
- persist acquisition metadata;
- reason about local versus geographic coordinates;
- associate the acquisition with approximate geographic context;
- expose quality and failure state;
- survive an interrupted workflow appropriately.

Architecture:

```text
              iPhone 3D Node
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      ARKit       LiDAR       Location
        │           │           │
        └───────────┼───────────┘
                    ▼
              local point cloud
                    │
             inspect / persist
                    │
                    ▼
           acquisition metadata
                    │
                    ▼
             central catalog
```

---

# PHASE III — BUILD THE 3D SYSTEMS LAYER

# Unit 7 — Point-Cloud Processing and Spatial Algorithms

## Core Topics

- filtering;
- crop;
- bounding-box query;
- radius query;
- nearest neighbor;
- downsampling;
- voxelization;
- duplicate/near-duplicate reduction;
- outlier removal conceptually;
- normals conceptually;
- clustering conceptually;
- segmentation conceptually;
- classification metadata;
- derived products;
- streaming versus whole-cloud algorithms.

## Governing Rule

Implement a small number of algorithms deeply enough to understand their systems behavior.

Do not build a point-cloud library from scratch.

## Known → Unknown

Bridge from 2D:

```text
ST_DWithin
spatial index
bounding box
nearest neighbor
```

to 3D:

```text
3D radius search
3D bounds
nearest point
voxel neighborhood
```

## 3D Systems Lens — Neighborhood Operations

Some algorithms operate independently per point:

```text
transform
simple filter
```

Others need nearby points:

```text
normal estimation
outlier detection
clustering
registration
```

Neighborhood requirements affect:

- indexing;
- chunk boundaries;
- memory;
- parallelism.

## Exercise Sequence

Implement or use:

1. bounding-box crop;
2. voxel downsampling;
3. nearest-neighbor or radius search;
4. one derived summary.

Use Python as a reference implementation where helpful.

## Benchmark

Measure before and after downsampling:

- point count;
- memory;
- processing time;
- file size;
- transfer size;
- visual difference.

## Portfolio Increment

Create a repeatable 3D processing pipeline:

```text
raw
 ↓
validate
 ↓
filter
 ↓
crop
 ↓
downsample
 ↓
derive
 ↓
persist
```

---

# Unit 8 — 3D Spatial Indexing and Chunked Storage

## Core Topics

- spatial locality;
- bounding-volume hierarchy conceptually;
- KD-tree;
- octree;
- voxel grid;
- spatial hashing;
- chunking;
- fixed versus adaptive partitioning;
- chunk bounds;
- chunk identity;
- multiresolution concepts;
- index persistence;
- chunk metadata;
- random access;
- range/selective reads;
- cache behavior;
- chunk overlap/halo conceptually;
- object/file storage layout.

## Known → Unknown

Course 1 introduced spatial indexes and chunk-aware reads.

Course 3B now applies them to a dataset where:

```text
load everything
```

can become an architectural failure.

## 3D Systems Lens — Index Choice Follows Query Pattern

Ask:

- nearest neighbor?
- radius query?
- viewport/region query?
- streaming spatial chunks?
- multiresolution visualization?
- fixed local processing cells?

No index is universally best.

## Exercise

Compare at least two representations on a bounded cloud:

```text
flat point array
```

versus one indexed/chunked representation.

Measure:

- build time;
- query time;
- memory;
- serialized size;
- subset-read behavior.

## Chunk Contract

A chunk should have explicit identity and metadata such as:

```text
acquisition_id
chunk_id
bounds
point_count
level / resolution
encoding
checksum
processing_state
byte_size
storage_reference
```

## Failure Experiments

- missing chunk;
- duplicate chunk;
- corrupt chunk;
- bad bounds;
- wrong acquisition ID;
- index references nonexistent chunk;
- partial index write.

## Architecture Decision

Write:

> **ADR — 3D indexing and chunking strategy**

The decision should be workload-driven.

---

# Unit 9 — Swift ↔ Rust 3D Compute Boundary

## Core Topics

- identifying a justified native compute boundary;
- Swift calling Rust conceptually;
- C-compatible FFI boundary;
- stable data contract;
- ownership across language boundaries;
- buffers;
- copies;
- serialization versus shared/native memory;
- error propagation;
- build integration;
- testing across FFI;
- benchmark design;
- crash boundary;
- versioning.

The exact interop mechanism should be selected based on the contemporary Swift/Rust ecosystem when the unit begins.

## Governing Rule

First establish:

```text
working Swift path
```

or:

```text
working Python reference
```

Then benchmark.

Only then move a targeted operation to Rust.

## Candidate Rust Operations

Potential candidates:

- voxel downsampling;
- bounds calculation;
- point transform;
- spatial-index construction;
- radius query;
- chunk encoding;
- compression.

Choose one or two.

## 3D Systems Lens — Copies Can Erase Compute Wins

A Rust algorithm may be faster while the overall call is slower if:

```text
Swift buffer
   ↓ expensive conversion/copy
Rust
   ↓ expensive conversion/copy
Swift
```

Measure end-to-end behavior.

## Required Experiment

Compare:

### A — Swift implementation

```text
Swift point buffer
      ↓
Swift processing
```

### B — Rust implementation

```text
Swift point buffer
      ↓
interop boundary
      ↓
Rust processing
      ↓
interop boundary
      ↓
Swift result
```

Measure:

- total latency;
- processing latency;
- conversion/copy overhead;
- memory;
- correctness.

## Safety / Failure Experiments

Test:

- empty buffer;
- malformed length;
- unsupported version;
- Rust error;
- allocation failure conceptually;
- unexpected result size.

The Swift app should not treat native-library failure as impossible.

## Checkpoint 3 — High-Performance 3D Edge Pipeline

The platform now contains:

- reusable 3D processing operations;
- measured point-cloud reduction;
- a documented spatial-index strategy;
- chunk-aware local storage;
- stable chunk metadata;
- at least one justified Swift ↔ Rust 3D computation boundary;
- correctness tests against a Python/reference path;
- end-to-end performance benchmarks;
- explicit ownership/error behavior across the language boundary.

Architecture:

```text
             Swift / iPhone
                  │
          acquisition + UI
                  │
                  ▼
            point buffers
                  │
        ┌─────────┴─────────┐
        │                   │
        ▼                   ▼
 Swift lightweight       Rust core
 processing             3D processing
        │                   │
        └─────────┬─────────┘
                  ▼
           chunked local data
```

Rust is now present because 3D created a real systems responsibility.

---

# PHASE IV — DISTRIBUTE, COMPARE, AND HARDEN THE 3D PLATFORM

# Unit 10 — Distributed 3D Transfer and Edge Processing

## Core Topics

- large-payload synchronization;
- manifest;
- acquisition identity;
- chunk identity;
- checksums;
- partial transfer;
- resumable transfer conceptually;
- retry;
- idempotency;
- upload state;
- chunk ordering;
- concurrent transfers;
- bounded concurrency;
- backpressure;
- bandwidth limits;
- compression;
- selective synchronization;
- raw versus derived data;
- local retention policy;
- central archival policy;
- object/file storage;
- metadata registration;
- eventual consistency across metadata and payloads.

## Governing Transition

Course 3A synchronized records.

Course 3B may synchronize datasets.

Compare:

```text
observation message
~small
```

with:

```text
point-cloud acquisition
~many chunks
```

The synchronization contract must evolve.

## Acquisition Manifest

A conceptual manifest may include:

```text
acquisition_id
node_id
captured_at
coordinate_metadata
chunk_count
total_points
total_bytes
processing_level
chunks[]
checksum/version
```

## 3D Systems Lens — Dataset Consistency

Ask:

- When is an acquisition considered synchronized?
- If 9 of 10 chunks arrive, what is central state?
- Can processing begin before every chunk arrives?
- What happens if metadata arrives before payload?
- What happens if payload arrives before metadata?
- How is a retry distinguished from a new chunk?

## Core Experiment — Raw Versus Edge-Processed Transfer

### Architecture A — Raw

```text
raw acquisition
      ↓
chunk
      ↓
network
      ↓
central storage
      ↓
central processing
```

### Architecture B — Edge Processed

```text
raw acquisition
      ↓
filter
      ↓
downsample
      ↓
spatially chunk
      ↓
compress
      ↓
network
      ↓
central storage
```

### Architecture C — Selective / Hybrid

```text
raw acquisition retained locally
      │
      ├── derived low-resolution cloud → central
      │
      └── selected raw chunks → on demand
```

Measure:

- raw bytes;
- transmitted bytes;
- upload duration;
- local processing duration;
- local memory;
- local storage;
- energy behavior;
- information retained;
- central reprocessing flexibility.

## Failure Experiments

- network loss mid-chunk;
- network loss between chunks;
- duplicate chunk;
- corrupt checksum;
- central service restart;
- app termination during upload;
- storage reference failure;
- manifest/chunk mismatch.

## Portfolio Increment

The platform gains a durable large-3D-payload synchronization protocol.

---

# Unit 11 — Photogrammetry, Drone Data, and Multi-Source 3D

## Core Topics

- photogrammetry review;
- structure-from-motion conceptually;
- dense reconstruction conceptually;
- drone imagery as input;
- aerial point clouds;
- LiDAR versus photogrammetric point clouds;
- orthomosaic;
- DSM;
- DEM;
- mesh;
- coordinate systems;
- scale;
- georeferencing;
- standard point-cloud ingestion;
- acquisition provenance;
- multi-source catalog.

## Scope Rule

The course does not reteach photogrammetry from first principles.

The student should understand the pipeline:

```text
photographs
    ↓
feature matching
    ↓
camera estimation
    ↓
structure from motion
    ↓
dense reconstruction
    ↓
point cloud
    ↓
surface / terrain products
```

The focus is how the resulting 3D data enters the same platform.

## Second-Modality Experiment

Import a small drone/photogrammetric or public aerial point cloud.

Run the same platform operations where appropriate:

- metadata inspection;
- bounds;
- crop;
- downsample;
- chunk;
- index;
- visualize;
- catalog;
- process.

## 3D Systems Lens — Sensor Independence

Compare:

| Concern | iPhone LiDAR | Drone / Photogrammetry |
|---|---|---|
| acquisition environment | mobile terrestrial | aerial / reconstructed |
| coordinate context | local + device/geographic anchor | often georeferenced |
| density | scene/device dependent | reconstruction dependent |
| data volume | bounded mobile capture | potentially much larger |
| source metadata | Apple sensor/session | imagery/camera/reconstruction |
| platform need | 3D payload + metadata | 3D payload + metadata |

The shared system should operate on explicit contracts rather than sensor-specific assumptions.

## Optional Extension

If drone access is available and safe/legal, capture a small dataset.

Actual flight is not required for course completion.

## Portfolio Increment

The platform becomes a **multi-source 3D spatial system** rather than an iPhone-only scanner.

---

# Unit 12 — 3D ML, Benchmarking, Reliability, and Platform Hardening

## Core Topics

- selected 3D ML use cases;
- point classification conceptually;
- segmentation conceptually;
- learned versus geometric processing;
- feature derivation;
- Core ML suitability for selected tasks;
- central Python/PyTorch 3D inference;
- hybrid inference;
- model/version metadata;
- benchmark synthesis;
- end-to-end profiling;
- fault injection;
- data integrity;
- checksums;
- observability;
- test strategy;
- acquisition reproducibility;
- platform documentation;
- portfolio demonstration.

## Scope Rule

3D ML is included only when it creates a meaningful systems experiment.

Do not attempt to become a specialist in every 3D neural architecture.

A valid capstone can emphasize geometric 3D processing more heavily than ML.

## Possible ML Questions

- Can a lightweight local model classify a bounded set of 3D features?
- Should local geometry derive features before central inference?
- Does downsampling materially change model performance?
- Can uncertain cases be sent centrally?
- Is the model too large or expensive for the iPhone?

## Hybrid Pattern

```text
raw 3D acquisition
       ↓
local geometric processing
       ↓
lightweight local inference
       ↓
      ┌┴───────────────┐
      │                │
confident          uncertain
      │                │
local result       central model
      │                │
      └───────┬────────┘
              ▼
         central catalog
```

## End-to-End Failure Model

Test a representative set of:

### Acquisition Failures

- unsupported hardware;
- interrupted AR session;
- incomplete scan;
- invalid depth;
- bad pose.

### Transform Failures

- wrong frame;
- wrong transform order;
- unit mismatch;
- invalid georeference.

### Processing Failures

- empty cloud;
- excessive memory use;
- invalid point;
- failed Rust operation;
- index build failure.

### Storage Failures

- local disk pressure;
- corrupt chunk;
- missing manifest;
- unsupported encoding.

### Transfer Failures

- network loss;
- partial chunk;
- duplicate upload;
- checksum mismatch;
- central storage unavailable.

### ML Failures

- model mismatch;
- unsupported input;
- inference failure;
- low confidence.

For each:

```text
detection
   ↓
bounded local behavior
   ↓
retry / reject / quarantine / degrade
   ↓
operator visibility
   ↓
recovery
```

## Final Benchmark Suite

At minimum, benchmark:

1. raw versus downsampled point cloud;
2. flat versus indexed query;
3. Swift versus Rust for the selected operation;
4. raw versus edge-processed network transfer;
5. one local versus central/hybrid 3D computation or inference question.

## Checkpoint 4 — Spatial Edge Platform v3: Distributed 3D Spatial System

The course concludes with a platform that can:

- use an iPhone as a real 3D sensing edge node;
- acquire bounded LiDAR/depth-derived spatial data;
- preserve acquisition/frame/transform metadata;
- construct and inspect point clouds;
- geolocate/catalog acquisitions appropriately;
- process point clouds locally;
- filter, crop, and downsample;
- perform selected neighborhood/spatial operations;
- use an explicit 3D spatial index;
- store data in chunk-aware form;
- use standard point-cloud formats where appropriate;
- invoke Rust for at least one justified 3D systems operation;
- benchmark the Swift ↔ Rust boundary;
- synchronize multi-chunk 3D datasets;
- resume after partial transfer;
- validate chunks with identity/integrity metadata;
- compare raw and edge-processed transfer;
- catalog metadata in PostGIS without forcing every point into relational storage;
- store heavy 3D payloads appropriately;
- ingest a second 3D modality such as photogrammetric/drone/public aerial data;
- visualize multiple 3D processing states;
- optionally perform meaningful 3D ML;
- expose acquisition, processing, storage, and synchronization observability;
- reproduce important failure scenarios;
- measure runtime, memory, storage, bandwidth, latency, and real-device resource behavior;
- document architecture and decisions; and
- tell one coherent portfolio story from physical-world sensing to distributed spatial computation.

---

# 9. Capstone Definition

## Working Capstone

**Spatial Edge Platform v3 — Distributed 3D Spatial System**

A concise project description:

> **A distributed 3D spatial edge-computing platform that extends a Swift/Rust/Python/PostGIS system with real iPhone LiDAR/depth acquisition, point-cloud construction and visualization, Rust-accelerated 3D processing and indexing, chunk-aware local storage, resilient selective synchronization, central metadata/catalog services, and multi-source 3D ingestion, with measured tradeoffs between raw transfer, edge processing, and centralized computation.**

The capstone should demonstrate a complete physical-world-to-software path:

```text
PHYSICAL WORLD
      │
      ▼
iPhone LiDAR / depth
      │
      ▼
3D acquisition
      │
      ▼
point cloud
      │
      ▼
local processing
      │
      ├── filter
      ├── crop
      ├── downsample
      ├── index
      ├── derive
      └── optional infer
      │
      ▼
chunked local persistence
      │
      ▼
resilient synchronization
      │
      ▼
central metadata + payload storage
      │
      ▼
Rust / Python / PostGIS analysis
      │
      ▼
native / analytical inspection
```

---

# 9.1 What the Capstone Is For

The capstone is a learning vehicle for:

- 3D spatial data;
- point clouds;
- LiDAR/depth;
- ARKit;
- native Apple sensing;
- coordinate frames;
- transforms;
- camera pose;
- georeferencing;
- point-cloud formats;
- LAS/LAZ/COPC literacy;
- PDAL/tooling literacy;
- 3D visualization;
- point-cloud filtering;
- downsampling;
- voxelization;
- nearest-neighbor reasoning;
- spatial indexing;
- KD-trees/octrees/spatial hashing concepts;
- chunking;
- binary data;
- memory-conscious processing;
- Swift ↔ Rust interoperability;
- large-payload synchronization;
- partial/resumable transfer;
- checksums and integrity;
- edge processing;
- central versus local computation;
- object/file storage architecture;
- PostGIS metadata/catalog architecture;
- photogrammetric/drone data;
- multi-source 3D systems;
- optional 3D ML;
- observability;
- benchmarking;
- failure recovery;
- systems architecture;
- portfolio communication.

It is not intended to become a production digital-twin company, commercial scanner, drone platform, or full point-cloud database.

---

# 9.2 Deliberate Scope

## Required

- existing Course 3A Swift application;
- real-device 3D acquisition on supported Apple hardware, or a clearly documented fallback dataset path if hardware access is temporarily unavailable;
- ARKit/depth/LiDAR concepts;
- explicit coordinate-frame and transform handling;
- point-cloud construction;
- native 3D inspection;
- acquisition metadata;
- point-cloud filtering;
- cropping;
- downsampling/voxelization;
- at least one neighborhood/spatial query;
- standard point-cloud format/tooling exposure;
- 3D indexing;
- chunked storage;
- stable chunk identity;
- data-integrity/checksum concept;
- one justified Rust 3D compute path;
- Swift ↔ Rust benchmark;
- multi-chunk synchronization;
- partial-transfer recovery;
- raw-versus-edge-processed transfer benchmark;
- central acquisition catalog;
- appropriate large-payload storage;
- second-source 3D data such as photogrammetric/drone/public point cloud;
- failure injection;
- observability;
- tests;
- ADRs;
- capstone demonstration.

## Optional

- direct drone acquisition;
- mesh generation;
- advanced surface reconstruction;
- normals;
- advanced registration;
- Core ML 3D inference;
- multiresolution visualization;
- cloud object storage;
- remote range reads;
- `.spat` 3D extension;
- GPU/Metal experimentation;
- advanced compression;
- TestFlight distribution;
- macOS companion tooling.

## Not Required

- city-scale digital twin;
- autonomous robotics;
- full SLAM implementation;
- custom photogrammetry engine;
- bundle adjustment implementation;
- custom ICP from first principles;
- production drone operations;
- production point-cloud database;
- production distributed object store;
- production AR experience;
- advanced computer graphics;
- game development;
- custom rendering engine;
- Metal specialization;
- every 3D index;
- every point-cloud format;
- billion-point production benchmark;
- Kubernetes;
- Kafka;
- service mesh;
- multi-cloud architecture.

Depth follows the capstone's architectural needs.

---

# 9.3 Core Capstone Demonstration

The final demonstration should be reproducible and evidence-driven.

## Scenario A — Real 3D Capture

Capture a bounded physical scene.

Show:

- acquisition metadata;
- device/session state;
- raw point count;
- bounds;
- coordinate-frame metadata;
- native visualization.

## Scenario B — Local 3D Processing

Run:

```text
raw
 ↓
validate
 ↓
filter
 ↓
crop
 ↓
voxel/downsample
 ↓
index
 ↓
chunk
```

Show before/after:

- point count;
- memory;
- size;
- processing time;
- visual result.

## Scenario C — Rust Acceleration

Run the selected operation through:

- Swift;
- Rust via interop.

Show:

- correctness;
- compute time;
- boundary overhead;
- total latency;
- memory.

Explain whether Rust was justified.

## Scenario D — Offline / Partial Transfer

Begin synchronization.

Interrupt connectivity.

Demonstrate:

- completed chunks remain acknowledged;
- incomplete chunk state is explicit;
- application restart does not lose transfer state;
- reconnect resumes safely;
- duplicate logical chunks are not created.

## Scenario E — Edge Versus Central 3D Processing

Compare raw transfer with locally reduced/selective transfer.

Show:

- bytes;
- upload duration;
- device processing cost;
- information loss;
- central flexibility.

## Scenario F — Multi-Source 3D

Ingest a non-iPhone point cloud.

Demonstrate that the central system can catalog and process:

```text
iPhone acquisition
        +
drone/photogrammetric/public acquisition
```

through shared platform concepts.

## Scenario G — Spatial Query / Inspection

Use metadata and/or the 3D index to select a spatial subset rather than reading the entire acquisition.

Explain the access path.

The final conclusion should answer:

> **How did 3D data change the architecture of the Spatial Edge Platform, and which design decisions were driven specifically by data volume, spatial locality, device constraints, and network transfer cost?**

---

# 10. Relationship to Course 3A

Course 3A produced:

```text
real iPhone node
      │
      ├── SwiftUI
      ├── MapKit
      ├── Core Location
      ├── sensors
      ├── persistence
      ├── offline sync
      ├── Core ML
      ├── profiling
      └── distributed contract
```

Course 3B does not reteach these foundations.

It extends them:

```text
Course 3A observation
      ↓
Course 3B acquisition

small record
      ↓
large spatial dataset

single-message sync
      ↓
multi-chunk dataset sync

2D coordinate
      ↓
3D frame + transform

local compute
      ↓
memory-intensive 3D compute

optional Rust interop
      ↓
measured Rust 3D systems layer
```

The Course 3A application remains the product shell and node runtime.

---

# 11. Relationship to the Rust Course

Course 1 established:

- ownership/borrowing;
- typed models;
- binary I/O;
- chunking;
- spatial algorithms;
- spatial indexing;
- performance engineering;
- Python interoperability.

Course 3B is where several of those topics encounter a high-volume real-world workload.

Rust may own:

```text
Rust 3D Core
│
├── point transforms
├── bounds
├── voxelization
├── spatial indexing
├── neighborhood queries
├── chunk processing
├── binary encoding
├── compression
└── selected 3D algorithms
```

The course should reuse earlier Rust knowledge rather than restarting syntax instruction.

A key question is:

> **Which 3D operations become sufficiently expensive, reusable, or memory-sensitive that they deserve a Rust implementation?**

---

# 12. Relationship to Python and the Point-Cloud Ecosystem

Python remains the scientific/reference environment.

Possible responsibilities:

```text
Python
│
├── exploratory point-cloud analysis
├── reference implementations
├── PDAL orchestration
├── validation
├── photogrammetry workflow integration
├── ML training
├── central processing
├── benchmark analysis
└── visualization/debugging where useful
```

Python should often provide a trustworthy comparison path before optimizing in Rust.

The course should make the student comfortable moving among:

```text
Swift
  ↕
Rust
  ↕
Python
  ↕
standard point-cloud formats
```

without treating any one layer as the universal solution.

---

# 13. Relationship to PostGIS and Large 3D Storage

PostGIS remains valuable, but its role changes.

A likely central model is:

```text
PostGIS
│
├── acquisition ID
├── node/device
├── capture time
├── approximate geographic location
├── footprint / bounds
├── processing state
├── provenance
├── quality
├── storage references
└── derived queryable spatial products
```

Large payload storage may contain:

```text
3D storage
│
├── raw point cloud
├── processed point cloud
├── chunks
├── indexes
├── meshes
└── derived products
```

The exact storage technology should be selected when the system reaches this unit.

The durable lesson is:

> **Choose storage according to access pattern and payload characteristics rather than forcing every spatial object into the same database abstraction.**

---

# 14. Relationship to `.spat` and the Spatial File-Format Work

The custom Rust-based spatial format remains a learning vehicle, not an obligation.

Course 3B should first understand:

- LAS;
- LAZ;
- COPC;
- standard metadata;
- chunked access;
- point attributes;
- compression;
- spatial organization.

Only then ask whether `.spat` should gain an experimental 3D representation.

A possible educational extension might explore:

```text
spat3d/
├── header
├── acquisition_metadata
├── spatial_index
└── chunks/
    ├── chunk_0001
    ├── chunk_0002
    └── ...
```

If implemented, the purpose should be to study:

- binary layout;
- offsets;
- chunk identity;
- spatial indexing;
- range reads;
- compression;
- cross-language access.

It should not be presented as a replacement for mature point-cloud standards.

---

# 15. Relationship to Photogrammetry and Drones

The broader 3D vision includes:

```text
LAND
iPhone LiDAR
```

and:

```text
AIR
drone imagery / LiDAR
```

Photogrammetry provides a natural bridge:

```text
drone imagery
      ↓
structure from motion
      ↓
dense reconstruction
      ↓
point cloud
      ↓
surface products
      ↓
Spatial Edge Platform
```

The course should leverage existing conceptual familiarity with photogrammetry rather than spending excessive time reproducing old workflows.

The important new question is:

> **Can the same platform process and catalog 3D data regardless of whether it originated from an iPhone, drone, or another sensor?**

---

# 16. Portfolio Repository Standard

The repository may evolve toward:

```text
spatial-edge-platform/
├── README.md
├── Cargo.toml
├── pyproject.toml
│
├── edge/
│   ├── rust/
│   │   ├── src/
│   │   │   ├── pointcloud/
│   │   │   ├── indexing/
│   │   │   ├── chunking/
│   │   │   ├── ffi/
│   │   │   └── ...
│   │   └── tests/
│   │
│   └── apple/
│       ├── SpatialEdge/
│       │   ├── App/
│       │   ├── Domain/
│       │   ├── Networking/
│       │   ├── Persistence/
│       │   ├── Location/
│       │   ├── Sensors/
│       │   ├── Spatial3D/
│       │   │   ├── Acquisition/
│       │   │   ├── Frames/
│       │   │   ├── PointCloud/
│       │   │   ├── Processing/
│       │   │   └── Visualization/
│       │   ├── Sync/
│       │   ├── ML/
│       │   └── Observability/
│       └── SpatialEdgeTests/
│
├── control_plane/
│   ├── app/
│   └── tests/
│
├── db/
│   ├── migrations/
│   └── schema/
│
├── pointcloud/
│   ├── samples/
│   ├── tooling/
│   ├── schemas/
│   └── conversions/
│
├── storage/
│   ├── manifests/
│   └── local_dev/
│
├── models/
│   ├── training/
│   └── exported/
│
├── benchmarks/
│   ├── pointcloud/
│   ├── ffi/
│   ├── transfer/
│   ├── device/
│   └── results/
│
├── docs/
│   ├── architecture.md
│   ├── 3d-data-contract.md
│   ├── coordinate-frames.md
│   ├── pointcloud-storage.md
│   ├── chunk-protocol.md
│   ├── swift-rust-boundary.md
│   ├── synchronization.md
│   ├── failure-model.md
│   ├── observability.md
│   ├── benchmarking.md
│   ├── acquisition-runbook.md
│   └── decisions/
│       ├── 3d-0001-pointcloud-format.md
│       ├── 3d-0002-coordinate-frames.md
│       ├── 3d-0003-index.md
│       ├── 3d-0004-chunking.md
│       ├── 3d-0005-rust-boundary.md
│       ├── 3d-0006-transfer.md
│       └── ...
│
└── scripts/
```

Do not create this entire tree at the start.

Allow implementation to reveal the appropriate structure.

---

# 17. Architecture Decision Records

Likely Course 3B ADRs include:

## ADR 1 — 3D Coordinate and Frame Contract

Which frames exist?

How are transforms represented?

What units and conventions are used?

## ADR 2 — Point-Cloud Interchange Format

Which standard formats are supported and why?

## ADR 3 — Internal Point Representation

How are points represented in Swift, Rust, and Python?

## ADR 4 — Central 3D Storage

What belongs in PostGIS?

What belongs in file/object storage?

## ADR 5 — Spatial Index

KD-tree, octree, voxel grid, spatial hash, or another approach?

Which query drove the decision?

## ADR 6 — Chunking Strategy

How are chunks bounded and identified?

Are they fixed or adaptive?

## ADR 7 — Swift ↔ Rust Boundary

Which operation crosses the language boundary?

What benchmark justified it?

## ADR 8 — 3D Transfer Protocol

How are manifests, chunks, retries, integrity, and partial completion handled?

## ADR 9 — Edge Processing

Which processing occurs before transfer?

What information is lost?

## ADR 10 — Raw Data Retention

What raw data remains on-device?

For how long?

What is uploaded centrally?

## ADR 11 — Multi-Source Acquisition Contract

How do iPhone and photogrammetric/drone data share platform concepts?

## ADR 12 — 3D ML Placement

If ML is used, which inference belongs locally versus centrally?

Every ADR should be concise and evidence-driven.

---

# 18. 3D Data Contract Standard

A 3D acquisition should have an explicit contract.

Potential acquisition metadata:

```text
acquisition_id
node_id
source_type
captured_at_start
captured_at_end
coordinate_frame
units
transform_metadata
geographic_anchor
horizontal_accuracy
vertical_accuracy_if_known
bounds
point_count
attribute_schema
processing_level
format
chunk_count
total_bytes
storage_reference
version
status
```

Potential chunk metadata:

```text
acquisition_id
chunk_id
bounds
point_count
resolution
encoding
byte_size
checksum
processing_level
storage_reference
sync_status
```

Potential point attributes may include:

```text
x
y
z
r
g
b
intensity
confidence
classification
timestamp
```

Only fields genuinely supported by the acquisition source should be populated.

Do not fabricate semantics to make different sensors appear identical.

---

# 19. Failure Model

## Acquisition Failures

- unsupported device;
- unavailable depth;
- interrupted AR session;
- incomplete acquisition;
- invalid sensor state;
- low-confidence depth;
- excessive motion;
- thermal/resource degradation conceptually.

## Coordinate / Transform Failures

- missing frame;
- wrong frame;
- wrong transform order;
- invalid matrix;
- unit mismatch;
- axis mismatch;
- bad geographic anchor;
- stale pose.

## Point-Cloud Failures

- empty cloud;
- NaN/Inf coordinate;
- impossible bounds;
- malformed attribute buffer;
- inconsistent point counts;
- unsupported schema.

## Processing Failures

- out-of-memory condition conceptually;
- Rust operation failure;
- invalid index;
- failed chunk generation;
- processing interruption.

## Storage Failures

- disk unavailable/full;
- corrupt file;
- corrupt chunk;
- manifest missing;
- checksum mismatch;
- unsupported version.

## Transfer Failures

- connection failure;
- timeout;
- partial upload;
- duplicate upload;
- lost acknowledgement;
- server restart;
- storage service unavailable;
- metadata/payload inconsistency.

## Multi-Source Failures

- unsupported CRS;
- missing provenance;
- incompatible attributes;
- extreme scale/density mismatch;
- malformed external file.

## ML Failures

- model unavailable;
- unsupported feature shape;
- inference failure;
- incompatible model version;
- low-confidence result.

For each failure:

```text
detect
  ↓
contain
  ↓
preserve valid state
  ↓
retry / reject / quarantine / degrade
  ↓
expose diagnostics
  ↓
recover
```

---

# 20. Observability Standard

3D workflows need observability at both acquisition and chunk level.

Potential acquisition events:

```text
timestamp
node_id
acquisition_id
event
source_type
point_count
bounds
processing_stage
processing_ms
memory_bytes
local_bytes
chunk_count
sync_status
error
```

Potential chunk events:

```text
timestamp
acquisition_id
chunk_id
event
point_count
byte_size
checksum_status
attempt
upload_ms
bytes_sent
status
error
```

Potential Rust/FFI events:

```text
operation
input_points
output_points
copy_in_ms
rust_compute_ms
copy_out_ms
total_ms
memory_bytes
status
error
```

The system should answer:

- Is acquisition active?
- How many points were captured?
- What coordinate frame is used?
- Which processing stage is running?
- Is memory growing unexpectedly?
- Which chunks exist?
- Which chunks are synchronized?
- Which chunk failed?
- Was integrity verified?
- How much data was reduced locally?
- Where is transfer time being spent?
- Did Rust improve total performance?
- Which acquisition generated this central artifact?
- Which processing version produced it?

---

# 21. Benchmark Standard

Every major 3D benchmark should state:

## Question

What are we trying to learn?

## Hypothesis

What do we expect?

## Dataset

Document:

- source;
- point count;
- attributes;
- bounds;
- format;
- coordinate system/frame;
- raw size.

## Environment

Document:

- iPhone/device where relevant;
- Mac/CPU architecture where relevant;
- OS;
- build configuration;
- network condition;
- Rust build mode;
- processing version.

## Workload

Examples:

- crop;
- voxel downsample;
- radius query;
- index build;
- chunk generation;
- transfer;
- inference.

## Variables

What changes?

## Controls

What remains fixed?

## Measurements

Potential measurements:

- wall-clock runtime;
- compute runtime;
- FFI overhead;
- memory;
- peak memory;
- point throughput;
- points retained;
- index build time;
- query time;
- local storage;
- compressed size;
- bytes transmitted;
- transfer duration;
- retry count;
- energy impact;
- information loss;
- model accuracy.

## Result

What happened?

## Explanation

Why?

## Decision

Does the architecture change?

---

# 22. Industry Connection Protocol

Relevant lessons may consult current signals from:

- Apple developer documentation;
- ARKit and RealityKit documentation;
- Apple Maps / spatial-intelligence engineering;
- Apple on-device systems and ML;
- modern LiDAR workflows;
- PDAL;
- LAS/LAZ/COPC ecosystem;
- modern cloud-native point-cloud tooling;
- GeoRust;
- point-cloud Rust crates;
- 3D geospatial infrastructure;
- photogrammetry;
- drone/UAS geospatial workflows;
- mapping/localization systems;
- modern geospatial systems roles;
- 3D computer vision roles;
- edge-computing systems roles.

Industry refresh should remain bounded.

The recurring question is:

> **Are we learning durable 3D spatial-systems concepts rather than chasing one framework?**

Durable concepts include:

- frames;
- transforms;
- spatial locality;
- indexing;
- chunking;
- streaming;
- memory;
- storage;
- transfer;
- acquisition provenance;
- edge processing;
- distributed integrity.

---

# 23. Interview Readiness

By the end of the course, the student should be able to discuss:

- What is a point cloud?
- How does a point cloud differ from vector and raster data?
- What attributes can a point contain?
- Why do point clouds become systems problems?
- Why does point count matter for memory?
- What is a coordinate frame?
- Why is `(x, y, z)` meaningless without frame context?
- What is a rigid transform?
- Why does transform order matter?
- What is pose?
- What is the distinction between local coordinates and geographic coordinates?
- What does ARKit contribute to 3D sensing?
- What is depth?
- How does depth become a 3D point conceptually?
- What role do camera intrinsics play?
- What does LiDAR provide?
- What causes noisy or incomplete scans?
- What is point-cloud registration?
- What is ICP conceptually?
- What is drift?
- What is the difference between local precision and global geospatial accuracy?
- What are LAS and LAZ?
- What is COPC trying to enable?
- What does PDAL do?
- Why does file layout affect query behavior?
- Why chunk a point cloud?
- What is voxel downsampling?
- What information does downsampling lose?
- What is a KD-tree?
- What is an octree?
- What is spatial hashing?
- How do you choose an index?
- What operations need neighborhood information?
- Why can chunk boundaries complicate neighborhood operations?
- Why use Rust for selected 3D computation?
- What is the Swift ↔ Rust FFI cost?
- Why can data copying erase a faster Rust compute time?
- What belongs in PostGIS versus large-payload storage?
- What is an acquisition manifest?
- How do you synchronize a dataset containing many chunks?
- How do you resume after partial transfer?
- How do checksums help?
- What does idempotency mean for chunk upload?
- What did raw versus edge-processed transfer show?
- What should remain raw on the device?
- What should be transmitted centrally?
- How does a drone/photogrammetric cloud differ from iPhone LiDAR?
- How can both fit the same platform?
- When is 3D ML useful?
- When is geometric processing sufficient?
- Which 3D computation belongs on-device?
- Which belongs in Rust?
- Which belongs centrally?
- What are the major failure modes?
- How do you trace one acquisition from capture to central storage?
- What did your benchmarks change about the architecture?
- What would need to change for 100× larger point clouds?
- What would need to change for many simultaneous 3D nodes?

Answers should come from the student's own system.

---

# 24. Assessment Model

There are no conventional exams.

Progress is assessed through:

## 3D Spatial Understanding

Can the student reason about:

- points;
- frames;
- transforms;
- bounds;
- density;
- uncertainty?

## Data-Structure Understanding

Can the student explain why an index or chunking strategy fits a workload?

## Systems Understanding

Can the student reason about:

- memory;
- I/O;
- storage;
- transfer;
- concurrency;
- backpressure;
- failure?

## Apple-Native Acquisition

Can the student collect and inspect real 3D data without treating ARKit/LiDAR as a black box?

## Rust Integration

Can the student identify a justified Rust boundary and measure it honestly?

## Interoperability

Can the student preserve semantics across:

- Swift;
- Rust;
- Python;
- standard point-cloud files;
- central storage?

## Distributed Correctness

Can the student reason about:

- chunk identity;
- partial transfer;
- retry;
- duplicates;
- checksums;
- eventual completion?

## Spatial Correctness

Are frames, transforms, CRS/geographic anchors, units, and provenance explicit?

## Measurement

Can the student design fair 3D benchmarks?

## Failure Reasoning

Can the student diagnose whether a problem belongs to:

- acquisition;
- transform;
- processing;
- index;
- storage;
- FFI;
- network;
- central service;
- external dataset?

## Architecture

Can the student explain why responsibilities live where they do?

## Scope Discipline

Can the student avoid turning the project into a robotics, graphics, drone, or digital-twin megaproject?

## Portfolio Quality

Does the final system visibly extend the same portfolio architecture?

---

# 25. Course Non-Goals

This course does **not** attempt to:

- make the student a robotics researcher;
- make the student a SLAM researcher;
- teach all of computer graphics;
- teach game development;
- build a custom rendering engine;
- specialize in Metal;
- implement a photogrammetry engine;
- implement structure-from-motion from scratch;
- implement bundle adjustment from scratch;
- implement every registration algorithm;
- implement every point-cloud index;
- implement a production point-cloud database;
- implement a production object store;
- create a city-scale digital twin;
- process billions of points merely for résumé scale;
- require drone ownership;
- require commercial drone operations;
- require expensive external sensors;
- replace standard point-cloud formats;
- replace PDAL;
- replace Python;
- replace Rust;
- replace PostGIS;
- put every point into PostGIS;
- force every operation onto the iPhone;
- force every operation into Rust;
- require 3D ML when geometric methods answer the question;
- require Kubernetes;
- require Kafka;
- require cloud infrastructure before needed;
- create a disconnected 3D demo app.

---

# 26. Technology Selection Rule

Distinguish:

```text
FOUNDATIONAL 3D CONCEPT
```

from:

```text
CORE PROGRAM TECHNOLOGY
```

from:

```text
STANDARD 3D ECOSYSTEM TOOL
```

from:

```text
OPTIONAL ACCELERATION / INFRASTRUCTURE
```

from:

```text
CURRENT INDUSTRY SIGNAL
```

## Foundational 3D Concepts

- point clouds;
- coordinate frames;
- transforms;
- pose;
- depth;
- spatial locality;
- nearest neighbors;
- voxelization;
- spatial indexes;
- chunking;
- streaming;
- memory layout;
- compression;
- storage;
- distributed transfer;
- provenance;
- integrity.

## Core Program Technology

- Swift;
- Rust;
- Python;
- SQL / Spatial SQL;
- PostgreSQL / PostGIS.

## Apple-Native 3D Tooling

- ARKit;
- device depth/LiDAR APIs;
- RealityKit or appropriate native 3D framework;
- Core Location;
- SwiftUI;
- Instruments;
- Core ML where justified.

## Standard 3D Ecosystem

Potentially:

- LAS;
- LAZ;
- COPC;
- PDAL;
- appropriate Python point-cloud libraries;
- established visualization/conversion tools.

## Optional Infrastructure

Potential examples:

- object storage;
- cloud range-read workflows;
- specialized compression;
- Metal;
- advanced Rust point-cloud libraries;
- web point-cloud visualization;
- workflow orchestration.

Every addition should answer:

1. What problem exists?
2. What workload demonstrates it?
3. Why is the current approach insufficient?
4. What capability does this technology add?
5. What complexity does it add?
6. Can the benefit be measured?
7. Does it preserve interoperability?
8. Is the opportunity cost justified?

---

# 27. Scope Discipline

The course should broaden the system along one coherent axis:

```text
2D
 ↓
3D
```

not:

```text
2D
 ↓
3D
 ↓
robotics
 ↓
game engine
 ↓
drone fleet
 ↓
digital twin startup
 ↓
everything
```

The intended depth profile is:

```text
                     3D SPATIAL SYSTEM
                            │
            ┌───────────────┼───────────────┐
            │               │               │
          DATA           SYSTEMS         DEVICE
            │               │               │
      point clouds         Rust            Swift
      formats/indexes    memory/I/O       ARKit
      chunk/storage      algorithms       LiDAR
      CRS/transforms     networking       Core ML
            │               │               │
            └───────────────┼───────────────┘
                            │
                         PRODUCT
                            │
                    inspect + operate
```

The breadth comes from understanding the whole 3D path.

---

# 28. Hardware and Tooling Milestones

## Phase I

Hardware is optional.

Use:

- synthetic point clouds;
- sample LAS/LAZ/COPC data;
- Python;
- Rust;
- Xcode;
- small visualization tools.

The goal is to understand the data model before touching LiDAR.

## Phase II

A LiDAR/depth-capable Apple device becomes strongly preferred and eventually required for the intended real-device capstone.

Use Xcode and the real device for:

- ARKit;
- depth;
- pose;
- point-cloud capture;
- native visualization.

If hardware is temporarily unavailable, prepared/sample acquisitions may keep the curriculum moving, but the course is not fully complete until the real-device acquisition requirement is satisfied.

## Phase III

Use:

- Rust release builds;
- Swift/Rust integration;
- benchmark tooling;
- representative point clouds;
- local chunk storage;
- profiling.

## Phase IV

Use:

- real iPhone;
- central control plane;
- PostGIS;
- large-payload storage;
- controlled network-failure scenarios;
- external/drone/photogrammetric point cloud;
- end-to-end observability.

ChatGPT remains:

- instructor;
- 3D systems explainer;
- code reviewer;
- transform debugger;
- Rust/Swift interoperability reviewer;
- architecture critic;
- benchmark reviewer;
- interview partner;
- documentation reviewer.

The student remains the author.

---

# 29. Course Freshness

This syllabus reflects the Spatial Systems Engineering strategy of **September 2026**.

Durable concepts should remain stable:

- frames;
- transforms;
- point clouds;
- spatial indexes;
- chunking;
- streaming;
- memory;
- data movement;
- edge processing;
- distributed integrity.

Specific Apple APIs, point-cloud libraries, Rust crates, and recommended storage tools may evolve.

Before units involving:

- ARKit/LiDAR APIs;
- Swift ↔ Rust tooling;
- current point-cloud ecosystem choices;
- Core ML 3D deployment;

perform a bounded **Platform / Industry Refresh**.

Do not rewrite the course around every library release.

---

# 30. Unit Completion Records

At the end of each unit, ChatGPT should produce a concise **Unit Completion Record** containing:

- 3D concepts learned;
- 3D Systems Lens covered;
- Known → Unknown bridges used;
- exercises completed;
- real/synthetic datasets used;
- Apple hardware work completed;
- Rust/Python work completed;
- portfolio changes;
- failure experiments completed;
- tests added;
- metrics/benchmarks added;
- architecture decisions made;
- Industry Connection covered;
- unresolved questions;
- recommended next unit.

This keeps a long-running 3D curriculum resilient to pauses.

---

# 31. Definition of Course Completion

The course is complete when the student can:

1. explain how point clouds differ from vector and raster data;
2. estimate the memory/storage implications of a point-cloud representation;
3. represent 3D acquisition metadata explicitly;
4. explain coordinate frames, origins, axes, units, and pose;
5. apply and invert practical rigid transforms;
6. explain why transform order matters;
7. distinguish local 3D coordinates from geographic/projected coordinates;
8. explain ARKit's role in spatial tracking and sensing;
9. explain conceptually how depth becomes a 3D point;
10. acquire a bounded real 3D scene on supported Apple hardware;
11. preserve acquisition, pose/frame, time, and quality metadata;
12. construct a point cloud from mobile sensing data;
13. inspect that cloud in a native 3D interface;
14. identify obvious acquisition and transform failures visually and numerically;
15. explain local precision versus global geospatial accuracy;
16. understand the purpose of registration and ICP conceptually;
17. read and inspect standard point-cloud metadata;
18. explain LAS, LAZ, COPC, and PDAL at a practical systems level;
19. filter and crop a point cloud;
20. downsample/voxelize a point cloud;
21. perform at least one 3D neighborhood/spatial query;
22. explain why neighborhood operations affect indexing and chunking;
23. explain KD-tree, octree, voxel-grid, and spatial-hash tradeoffs at a practical level;
24. select and benchmark an appropriate 3D index for a representative query;
25. design a chunk-aware point-cloud representation;
26. preserve chunk identity, bounds, integrity, and processing metadata;
27. identify a justified 3D operation for Rust;
28. call that Rust operation from the Swift application or native layer;
29. measure compute time and language-boundary overhead separately;
30. explain whether Rust improved end-to-end behavior;
31. distinguish PostGIS metadata/catalog responsibilities from heavy 3D payload storage;
32. synchronize a multi-chunk acquisition;
33. recover from interrupted/partial transfer;
34. prevent duplicate logical chunk creation under retries;
35. verify chunk integrity;
36. compare raw transfer with edge-processed/selective transfer;
37. quantify bandwidth savings and local processing cost;
38. explain what information is lost through downsampling or local derivation;
39. ingest a second 3D source such as photogrammetric/drone/public point-cloud data;
40. preserve source-specific provenance rather than pretending all sensors are identical;
41. explain the photogrammetry-to-point-cloud pipeline conceptually;
42. optionally deploy/evaluate a meaningful 3D ML path when justified;
43. profile real-device 3D processing;
44. reproduce important acquisition, transform, processing, storage, and transfer failures;
45. trace one acquisition from iPhone capture through chunks to central storage/catalog;
46. document the 3D data contract;
47. document coordinate-frame conventions;
48. document the chunk/synchronization protocol;
49. produce evidence-driven ADRs;
50. run a reproducible final benchmark suite;
51. explain why Swift, Rust, Python, PostGIS, and large-payload storage have distinct responsibilities;
52. explain how 3D data changed the architecture compared with Course 3A; and
53. confidently demonstrate and discuss the distributed 3D system with another engineer.

The ultimate test is not:

> **"Do I know LiDAR?"**

Nor:

> **"Can I render a point cloud?"**

It is:

> **"Can I acquire, represent, transform, process, index, store, transfer, observe, benchmark, and explain 3D spatial data across a real edge device and distributed spatial system—and make defensible decisions about where computation and data should live?"**

---

# 32. Course Progression

```text
          SWIFT FOR 3D SPATIAL & EDGE COMPUTING v0.1
                         COURSE 3B

PHASE I                                  PHASE II
Learn the 3D Data Model                  Acquire the Physical World

1. 2D → 3D Spatial Data                 4. ARKit + LiDAR / Depth
2. Frames + Pose + Transforms           5. Point Cloud + Visualization
3. Formats + Ecosystem                  6. Registration + Georeference
          │                                       │
          ▼                                       ▼
   CHECKPOINT 1                             CHECKPOINT 2
3D Spatial Data Workbench               Real iPhone 3D Sensor Node
            \                                  /
             \                                /
              ▼                              ▼
                         PHASE III
                  Build the 3D Systems Layer

                  7. Point-Cloud Algorithms
                  8. Indexing + Chunked Storage
                  9. Swift ↔ Rust 3D Compute
                         │
                         ▼
                    CHECKPOINT 3
             High-Performance 3D Edge Pipeline
                         │
                         ▼
                         PHASE IV
             Distribute + Compare + Harden

                  10. Distributed 3D Transfer
                  11. Drone / Photogrammetry
                  12. 3D ML + Reliability
                         │
                         ▼
                    CHECKPOINT 4
              SPATIAL EDGE PLATFORM v3
             DISTRIBUTED 3D SPATIAL SYSTEM
```

Each checkpoint survives into the next.

---

# 33. Capstone Narrative

A reviewer should be able to follow one continuous story.

## The Starting Point

The portfolio already contains:

- Rust spatial systems code;
- a Python control plane;
- PostGIS;
- simulated distributed edge nodes;
- a real Swift/iPhone edge node;
- offline synchronization;
- local processing;
- Core ML;
- observability;
- real-device profiling.

## The New Problem

2D observations are small.

3D acquisitions are not.

Point clouds create:

- memory;
- indexing;
- chunking;
- storage;
- compression;
- transfer;
- processing

problems.

## The Physical-World Layer

The iPhone uses Apple spatial hardware to observe a real environment.

## The Geometry Layer

Depth and pose become explicit 3D points with known frame semantics.

## The Data Layer

The system represents acquisitions, point attributes, bounds, transforms, chunks, and provenance.

## The Systems Layer

Point-cloud volume makes:

- memory layout;
- spatial indexing;
- streaming;
- Rust processing;
- chunk-aware I/O

material architectural concerns.

## The Edge Layer

The device can reduce or derive useful 3D data before transmission.

## The Distributed Layer

Large acquisitions synchronize as durable multi-chunk datasets rather than single messages.

## The Central Layer

PostGIS catalogs the acquisition while appropriate storage retains the heavy payload.

## The Multi-Source Layer

A drone/photogrammetric or other point cloud enters the same architecture, proving that the platform is not merely an iPhone scanner.

## The Measurement

Benchmarks compare:

- raw versus reduced clouds;
- flat versus indexed queries;
- Swift versus Rust;
- raw versus edge-processed transfer;
- local versus central/hybrid computation.

## The Result

The project becomes a distributed system for computationally understanding real 3D environments.

---

# 34. Broader SEAL Connection

The broader portfolio vision can be described as:

> **SEAL — Space, Air, and Land**

Course 3B primarily deepens **Land** and introduces **Air**.

```text
                         PHYSICAL WORLD
                              │
              ┌───────────────┼───────────────┐
              │               │               │
            SPACE             AIR            LAND
              │               │               │
         satellites         drones         iPhone
         imagery            imagery        LiDAR
         sensors            LiDAR          camera
              │               │            sensors
              └───────────────┼───────────────┘
                              │
                         spatial data
                              │
                   ┌──────────┴──────────┐
                   │                     │
                  2D                    3D
                   │                     │
                   └──────────┬──────────┘
                              │
                       edge computation
                              │
                    ┌─────────┴─────────┐
                    │                   │
                  Swift               Rust
                    │                   │
                    └─────────┬─────────┘
                              │
                            Python
                              │
                      PostGIS + storage
                              │
                              ▼
                     UNDERSTANDING THE
                       PHYSICAL WORLD
```

The SEAL idea is a north star, not a requirement to learn every sensing modality.

The governing rule remains:

> **Every new technology must answer a meaningful question about the world, the data, or the system.**

---

# 35. Status

**Syllabus v0.1**

This syllabus is the 3D continuation of **Swift for Spatial & Edge Computing v0.1**.

Its destination is:

> **Extend the existing real mobile edge node into a distributed 3D spatial system capable of acquiring, processing, indexing, storing, and synchronizing high-volume observations of the physical world.**

It preserves the broader program's governing philosophy:

- one evolving portfolio system;
- technologies with explicit responsibilities;
- Known → Unknown teaching;
- systems concepts introduced through meaningful spatial problems;
- real hardware when it adds learning value;
- standard formats before custom invention;
- failure as a learning tool;
- benchmark rather than assume;
- explicit coordinate and provenance semantics;
- architectural simplicity;
- scope discipline;
- real portfolio artifacts at every checkpoint.

The intended progression across the first four curriculum artifacts is now:

```text
COURSE 1
Rust for Geospatial Systems
        │
        ▼
high-performance spatial systems layer
        │
        ▼
COURSE 2
Spatial Systems & Distributed Computing
        │
        ▼
distributed edge platform
        │
        ▼
COURSE 3A
Swift for Spatial & Edge Computing
        │
        ▼
real 2D iPhone edge node
        │
        ▼
COURSE 3B
Swift for 3D Spatial & Edge Computing
        │
        ▼
distributed 3D spatial system
```

The final portfolio story is not:

> **"I learned Rust, distributed systems, Swift, and LiDAR."**

It is:

> **"I built one spatial platform from the computational core outward: first high-performance spatial processing, then distributed edge nodes, then a real Apple-native mobile node, and finally a 3D sensing and point-cloud system that forced me to solve real problems in transforms, indexing, memory, storage, data movement, interoperability, and edge-versus-central computation."**
