# Geospatial Edge Computing — Year 2: 3D, Point Clouds, Drones, and the SEAL Vision
**Status:** Long-term extension of the Geospatial Edge Computing portfolio project  
**Likely timing:** Year 2  
**Theme:** Understanding the physical world through spatial data, computation, and systems engineering

---

## 1. The larger vision

The first year of the project focuses on building a distributed geospatial edge-computing system using:

- **Python + SQL/PostGIS** for the control plane and central spatial data system
- **Rust** for edge processing, local storage, synchronization, and systems programming
- **Swift/SwiftUI** for the iOS application and eventually a real mobile edge node

The second year can expand the project from primarily 2D spatial observations into **3D spatial computing**:

- point clouds
- photogrammetry
- structure-from-motion
- LiDAR
- drone imagery
- 3D reconstruction
- 3D spatial processing

This is not simply adding another technology. It extends the underlying question:

> **How can we use computation and spatial data to understand the physical world?**

---

## 2. The personal north star

The broader motivation is not to learn a random collection of programming languages. It comes from a long-standing interest in understanding the world through science and technology:

- geology
- geography
- geospatial science
- data science
- spatial analysis
- Earth observation
- physical landscapes
- computation

Python provides an excellent scientific and analytical environment.
SQL/PostGIS provides a powerful spatial database foundation.
Rust provides an opportunity to understand lower-level systems and performance.
Swift provides an opportunity to build polished software on Apple platforms.

The ultimate goal is to become a deeply capable **spatial technologist**: someone who understands the physical world, spatial data, algorithms, systems, and software deeply enough to move between disciplines.

---

## 3. The "SEAL" idea

A useful personal shorthand for this ambition is:

> **SEAL — Space, Air, and Land**

Not necessarily as a formal job title or discipline, but as a personal north star for becoming a holistic spatial expert.

```text
                         SEAL
               Space • Air • Land
                         │
         ┌───────────────┼───────────────┐
         │               │               │
       SPACE            AIR             LAND
         │               │               │
   satellites       drones/UAS       terrestrial
   remote sensing   photogrammetry   mobile
   Earth data       LiDAR           sensors
         │               │               │
         └───────────────┼───────────────┘
                         │
                 SPATIAL COMPUTING
                         │
          ┌──────────────┼──────────────┐
          │              │              │
     Geospatial       Systems        Software
     processing      engineering     engineering
          │              │              │
          └──────────────┼──────────────┘
                         │
                    Understanding
                     our physical
                         world
```

The goal is breadth **with a strong technical core**, not shallow familiarity with every possible geospatial technology.

---

## 4. Why 3D belongs in the project

The first version of the edge project primarily deals with observations such as:

```text
timestamp
latitude
longitude
measurement
```

Point clouds change the character of the problem.

Instead of:

```text
POINT
(x, y)
```

we start working with:

```text
POINT
(x, y, z)
```

and potentially:

```text
x
y
z
intensity
classification
color
return number
timestamp
```

A single acquisition can contain millions or billions of points.

That creates exactly the kind of problem where the project's existing themes become important:

- spatial indexing
- chunking
- streaming
- compression
- local processing
- memory management
- parallelism
- file formats
- network transfer
- edge computing

In other words, **point clouds are a natural systems problem disguised as a geospatial problem.**

---

## 5. The historical starting point

There is already some personal experience with photogrammetry and structure-from-motion from roughly a decade ago, particularly using Agisoft/Metashape.

That provides useful conceptual grounding:

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
mesh / DEM / orthomosaic
```

The second-year goal is not to relearn photogrammetry from scratch. It is to revisit the field with modern tools, data formats, hardware, and computational approaches.

---

## 6. Drones become a natural data source

Drone/UAS data provides an excellent bridge between **Air** and **Land**.

```text
                 DRONE
                   │
          ┌────────┴────────┐
          │                 │
        RGB              LiDAR
       imagery           (if available)
          │                 │
          ▼                 ▼
   photogrammetry       point cloud
          │                 │
          └────────┬────────┘
                   ▼
              3D products
                   │
                   ▼
             edge processing
                   │
                   ▼
             central system
```

Potential products include:

- point clouds
- digital surface models
- digital elevation models
- orthomosaics
- meshes
- 3D building/terrain representations
- classified point clouds

The edge-computing system could process or summarize some of this data before transferring it to a central system.

---

## 7. The iPhone becomes much more interesting

The iPhone is not merely the UI.
Pro-class iPhones with LiDAR provide a compelling real-world edge device.

```text
                     ┌─────────────────────┐
                     │       iPhone        │
                     │                     │
                     │  Swift / SwiftUI    │
                     │  Camera             │
                     │  LiDAR              │
                     │  GPS / location     │
                     │  IMU / motion       │
                     │  Local storage      │
                     └──────────┬──────────┘
                                │
                         local processing
                                │
                                ▼
                         central system

```

The phone can therefore participate in the same conceptual architecture as the simulated Rust edge nodes.

```text
                 CENTRAL SYSTEM
                       ▲
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   Rust node       Rust node       iPhone
   simulated      simulated       real node
        │              │              │
     sensor         sensor        LiDAR/GPS
      data           data           data
```

This makes the iPhone a genuine experimental platform for edge geospatial computing.

---

## 8. A potential second-year demonstration

A compelling demonstration could eventually look like this:

### Step 1 — Capture

Use an iPhone LiDAR sensor or drone imagery to capture a small real-world environment.

```text
building / terrain / objects
            ↓
        acquisition
```

### Step 2 — Process locally

```text
raw scan
   ↓
filter
   ↓
downsample
   ↓
spatial index
   ↓
derive useful features
```

### Step 3 — Synchronize

```text
large raw dataset
        ↓
locally processed
        ↓
smaller useful dataset
        ↓
central API / storage
```

### Step 4 — Visualize

Use the Swift application to explore:

- node locations
- point clouds
- 3D scenes
- derived spatial products
- processing status
- synchronization state
The result is a complete physical-world-to-software pipeline.

---

## 9. Point clouds and the existing spatial file-format project

Point-cloud processing introduces questions about:

- binary layouts
- spatial partitioning
- chunking
- compression
- metadata
- coordinate reference systems
- spatial indexes
- random access
- streaming
- cloud/object storage

These connect directly to the earlier exploration of:

- GeoTIFF
- Zarr
- Parquet / GeoParquet
- point-cloud formats
- cloud-native spatial storage

A future system could use a spatially chunked point-cloud representation:

```text
pointcloud/
├── metadata
├── spatial_index
└── chunks/
    ├── tile_001
    ├── tile_002
    ├── tile_003
    └── ...
```

The Rust edge agent could operate on chunks rather than requiring the entire point cloud in memory.

This connects:

**file-format design → spatial indexing → Rust → edge computing → 3D processing.**

---

## 10. Why this should probably be Year 2

The project already has a substantial first-year curriculum.

Trying to add point clouds, drones, LiDAR, 3D processing, and iOS simultaneously would risk turning it into an unfinishable monster.

The first year should establish:

```text
Python
SQL/PostGIS
Rust
distributed systems
edge computing
Swift
SwiftUI
iOS
2D geospatial processing
```

Then Year 2 adds:

```text
3D
point clouds
LiDAR
photogrammetry
drone data
3D visualization
large spatial datasets
```

The second year therefore becomes an **extension of an existing platform**, rather than a separate giant project.

---

## 11. Possible Year 2 roadmap

### Phase 1 — Modern point-cloud ecosystem

Understand:

- LAS/LAZ
- COPC
- PDAL
- Entwine
- Potree
- modern cloud-native point-cloud approaches
- Python point-cloud tooling
- spatial indexing
- tiled/chunked representations

The goal is understanding the ecosystem before building anything.

### Phase 2 — Point-cloud processing

```text
point cloud
    ↓
filter
    ↓
crop
    ↓
classify
    ↓
downsample
    ↓
derive products
```

Explore Python and Rust implementations where useful.

### Phase 3 — 3D spatial algorithms

Explore:

- nearest neighbors
- voxelization
- octrees
- KD-trees
- spatial hashing
- clustering
- surface reconstruction
- normal estimation
- segmentation
- point-cloud registration

### Phase 4 — LiDAR iPhone integration

Build a Swift application capable of collecting or importing 3D spatial data.

Start small: a room, object, building facade, or outdoor feature is enough.

### Phase 5 — Drone data

Introduce aerial data and a workflow such as:

```text
drone imagery
     ↓
photogrammetry
     ↓
point cloud
     ↓
terrain/surface products
     ↓
edge/cloud pipeline
```

### Phase 6 — 3D visualization

Extend the Swift application to visualize 3D spatial data:

- rotate
- zoom
- pan
- inspect points
- toggle layers
- display classifications
- show metadata
- compare processing states

### Phase 7 — Edge 3D processing

Move meaningful computation toward the edge:

```text
raw point cloud
       │
       ▼
┌───────────────────┐
│ Edge processing   │
│                   │
│ crop              │
│ filter            │
│ voxelize          │
│ classify          │
│ summarize         │
└─────────┬─────────┘
          │
          ▼
 central system
```

The key question becomes:

> **Which 3D computations should happen locally, and which should happen centrally?**

---

## 12. The technology stack at full maturity

```text
                         ┌───────────────────────┐
                         │      Swift / iOS      │
                         │                       │
                         │  SwiftUI              │
                         │  MapKit               │
                         │  3D visualization     │
                         │  LiDAR                │
                         │  GPS / sensors        │
                         └───────────┬───────────┘
                                     │
                              API / synchronization
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │   Python control plane │
                         │                       │
                         │   FastAPI             │
                         │   PostgreSQL/PostGIS  │
                         │   Analytics            │
                         └───────────┬───────────┘
                                     │
                         jobs / data / metadata
                                     │
              ┌──────────────────────┼──────────────────────┐
              │                      │                      │
              ▼                      ▼                      ▼
        ┌───────────┐          ┌───────────┐          ┌───────────┐
        │ Rust edge │          │ Rust edge │          │ Rust edge │
        │ node      │          │ node      │          │ node      │
        └─────┬─────┘          └─────┬─────┘          └─────┬─────┘
              │                      │                      │
          2D/3D data             2D/3D data             2D/3D data
              │                      │                      │
              └──────────────────────┼──────────────────────┘
                                     │
                              spatial storage
                                     │
                                     ▼
                         ┌───────────────────────┐
                         │ Spatial data formats  │
                         │                       │
                         │ raster                │
                         │ vector                │
                         │ point cloud           │
                         │ spatial chunks        │
                         └───────────────────────┘
```

---

## 13. The deeper learning arc

### Year 1

```text
2D spatial data
      ↓
spatial databases
      ↓
edge computing
      ↓
Rust
      ↓
distributed systems
      ↓
Swift / iOS
      ↓
real mobile edge node
```

### Year 2

```text
3D spatial data
      ↓
point clouds
      ↓
LiDAR
      ↓
photogrammetry
      ↓
drones
      ↓
3D algorithms
      ↓
3D edge processing
```

Underneath both years:

```text
              UNDERSTAND THE WORLD
                       │
                       ▼
                 spatial data
                       │
                       ▼
                  computation
                       │
                       ▼
                 software
                       │
                       ▼
                   systems
```

---

## 14. The Apple connection

Working at Apple has been a lifelong dream, and that gives the otherwise broad personal project a useful direction.

Swift is therefore not an arbitrary addition.

It creates an opportunity to develop experience relevant to an eventual Apple interview or application:

- Swift
- SwiftUI
- MapKit
- iOS architecture
- mobile sensors
- spatial computing
- local/on-device processing
- polished user interfaces

More importantly, the Apple component connects naturally to the scientific goal.

Apple hardware increasingly provides sophisticated sensors and significant local computational capability. An iPhone with LiDAR is an especially interesting platform for someone interested in:

**geospatial + 3D + sensors + edge computing + software.**

The objective is not to build something merely because Apple uses Swift. It is to use Swift and Apple hardware as another instrument for investigating the physical world.

---

## 15. What the portfolio eventually demonstrates

### Domain

- geography
- geology
- spatial analysis
- Earth observation
- 3D spatial data
- photogrammetry
- LiDAR

### Data

- PostgreSQL/PostGIS
- raster
- vector
- point clouds
- spatial indexes
- chunked/cloud-native formats

### Software

- Python
- Rust
- Swift
- SQL

### Systems

- distributed processing
- edge computing
- asynchronous systems
- synchronization
- failure recovery
- resource constraints
- benchmarking

### Product

- iOS application
- interactive maps
- 3D visualization
- real sensor data
- polished user experience

That combination is unusual.

---

## 16. The north-star portfolio story

The eventual story is bigger than any one technology:

> **I am interested in understanding the physical world through data and computation. My interests span geology, geography, geospatial science, and data science. I built a geospatial edge-computing platform to explore what happens when spatial computation moves closer to the sensors generating the data. The system combines Python and PostGIS for central analysis, Rust for high-performance edge processing, and Swift/SwiftUI for a mobile spatial interface. I then extended the system into 3D using point clouds, LiDAR, photogrammetry, and drone data, including an iPhone as a real edge device.**

That is a coherent personal technical identity.

It says:

**I understand spatial problems.**
**I understand data.**
**I can build software.**
**I understand systems.**
**I can work close to the hardware.**
**I can build polished user-facing applications.**

And most importantly:

**I am curious about the physical world and use technology to understand it.**

---

## 17. Scope discipline

The SEAL idea is a north star, not a requirement to learn everything.

A useful rule:

> **Every new technology must answer a meaningful question about the world, the data, or the system.**

Do not add drones because drones are cool. Add them because they create an interesting aerial spatial-data problem.

Do not add LiDAR merely because the iPhone has LiDAR. Add it because direct 3D sensing creates a useful edge-computing experiment.

Do not add Rust because it looks impressive. Use it because the edge agent creates meaningful systems-programming problems.

Do not add Swift merely to have Swift on a résumé. Use it to build a genuinely useful interface and eventually to interact with real Apple sensors and hardware.

This keeps the project intellectually coherent.

---

## 18. Final vision

The long-term project can be thought of as a personal laboratory for **computational understanding of the Earth and physical world**.

```text
                         THE WORLD
                            │
             ┌──────────────┼──────────────┐
             │              │              │
           SPACE           AIR            LAND
             │              │              │
        satellites       drones          iPhone
        imagery          cameras         LiDAR
        sensors          LiDAR           GPS
             │              │              │
             └──────────────┼──────────────┘
                            │
                       spatial data
                            │
              ┌─────────────┼─────────────┐
              │             │             │
            2D            3D          temporal
              │             │             │
              └─────────────┼─────────────┘
                            │
                     EDGE COMPUTING
                            │
                     ┌──────┴──────┐
                     │             │
                   Rust         Swift
                     │             │
                     └──────┬──────┘
                            │
                         Python
                            │
                       PostGIS / SQL
                            │
                            ▼
                    UNDERSTANDING
                    OUR PHYSICAL
                        WORLD
```

The project does not need to become a company, a startup, or a production-scale platform.

It can remain a lifelong technical laboratory.

**Year 1:** build the spatial edge-computing foundation.

**Year 2:** add 3D, point clouds, LiDAR, photogrammetry, and drones.

**Beyond that:** follow the questions that become interesting.

The enduring theme is simple:

> **Understand our world with science, data, and technology.**

The "SEAL" concept—**Space, Air, and Land**—is a useful way to describe the breadth of that ambition, while geospatial processing, systems engineering, and software engineering provide the technical foundation underneath it.