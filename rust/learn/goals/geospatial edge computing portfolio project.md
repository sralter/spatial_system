# Geospatial Edge Computing Portfolio Project

**Status:** Long-term learning / portfolio project  
**Time horizon:** Roughly one year, with useful milestones along the way  
**Primary goals:** Geospatial systems + Rust + distributed/edge computing + Swift/iOS

---

## 1. The idea

Build a small, end-to-end **geospatial edge-computing platform**.

The core idea is to simulate a fleet of geographically distributed edge nodes that receive spatial observations, process them locally, survive intermittent connectivity, and synchronize useful results with a central system.

A Swift/SwiftUI iPhone app sits on top as the user-facing interface. The iPhone should eventually be able to act as a **real edge node itself**, alongside the simulated Rust nodes.

The project deliberately combines three technologies that each have a natural role:

- **Python + SQL/PostGIS:** control plane, API, orchestration, analytics, central storage
- **Rust:** edge agent, local processing, storage, synchronization, systems-level work
- **Swift/SwiftUI:** iOS application, mapping, visualization, monitoring, and eventually a real mobile edge node

The goal is not to build a huge production system. The goal is to use a compelling geospatial problem to learn systems programming, distributed systems, data engineering, spatial computing, and Apple development.

---

## 2. Why this project matters

A recurring career goal is to combine strong geospatial expertise with software/systems engineering rather than treating geospatial as a siloed analyst specialty.

Modern geospatial work increasingly touches:

- software engineering
- distributed systems
- cloud-native data
- spatial databases
- data formats
- systems programming
- mobile computing
- edge computing

This project provides a way to explore all of those areas while retaining geospatial as the central domain.

The resulting portfolio story could eventually be:

> **I designed and built a distributed edge-computing platform for geospatial data, with Rust-based edge agents, a Python/PostGIS control plane, and a Swift/SwiftUI client for monitoring and visualization. Edge nodes process and aggregate spatial observations locally, continue operating during network outages, and synchronize results when connectivity returns.**

That is substantially more interesting than simply saying "I learned Rust" or "I built an iOS app."

---

## 3. High-level architecture

```text
                         ┌──────────────────────────┐
                         │       Swift / iOS        │
                         │                          │
                         │  Map UI                  │
                         │  Node monitoring         │
                         │  Data visualization      │
                         │  Job configuration       │
                         └────────────┬─────────────┘
                                      │
                                HTTPS / JSON
                                      │
                                      ▼
                         ┌──────────────────────────┐
                         │     Python control plane │
                         │                          │
                         │  FastAPI                 │
                         │  PostgreSQL/PostGIS      │
                         │  Job orchestration       │
                         │  Analytics               │
                         └────────────┬─────────────┘
                                      │
                                jobs / results
                                      │
                 ┌────────────────────┼────────────────────┐
                 ▼                    ▼                    ▼
          ┌─────────────┐      ┌─────────────┐      ┌─────────────┐
          │ Rust Node 1 │      │ Rust Node 2 │      │ Rust Node 3 │
          │             │      │             │      │             │
          │ ingest      │      │ ingest      │      │ ingest      │
          │ filter      │      │ filter      │      │ filter      │
          │ aggregate   │      │ aggregate   │      │ aggregate   │
          │ synchronize │      │ synchronize │      │ synchronize │
          └──────┬──────┘      └──────┬──────┘      └──────┬──────┘
                 │                    │                    │
             local data           local data           local data
```

The important architectural principle is:

> **Move computation toward the data instead of moving all raw data toward the central system.**

For example:

```text
1,000,000 raw observations
          │
          ▼
     Rust edge node
          │
   validation
   spatial filtering
   aggregation
   anomaly detection
          │
          ▼
    10,000 useful results
          │
          ▼
      central API
```

The project can measure whether this actually reduces network transfer, central processing, or latency.

---

## 4. Simulated edge nodes are legitimate

Physical hardware is **not required**.

A node is fundamentally a software abstraction:

```text
EdgeNode
├── identity
├── local storage
├── processing engine
├── network connection
├── job queue
└── synchronization
```

Multiple instances of the same Rust executable can run on one Mac:

```bash
./edge-agent --node-id node-001
./edge-agent --node-id node-002
./edge-agent --node-id node-003
./edge-agent --node-id node-004
```

Each instance can have independent:

- configuration
- local database/storage
- simulated location
- sensor stream
- network state
- processing workload

The simulator can deliberately introduce:

- network latency
- packet loss
- intermittent connectivity
- limited CPU
- limited disk
- different geographic locations
- different sensor streams
- clock drift

This creates a realistic distributed-systems test environment without purchasing a fleet of Raspberry Pis.

---

## 5. The iPhone as a real edge node

A particularly exciting extension is making the iPhone itself an actual participant in the system.

The simulated Rust nodes represent hypothetical embedded/edge devices, while the iPhone provides a real mobile edge environment:

```text
                    ┌────────────────┐
                    │     iPhone     │
                    │                │
                    │ GPS            │
                    │ motion sensors │
                    │ local storage  │
                    │ Swift app      │
                    └───────┬────────┘
                            │
                     local processing
                            │
                            ▼
                     central system
```

This makes the project more than an iOS dashboard. The phone becomes an actual data-producing and processing node.

The Swift app can also visualize the simulated fleet:

```text
                 EDGE NETWORK

       ● node-002              ● node-003
              \                  /
               \                /
                ● node-001
                     |
                     |
                ● node-004

             [iPhone / local node]
```

Tapping a node could expose:

```text
EDGE NODE 003

Status          Online
Location        40.72, -74.01

Observations    1,284,923
Pending         1,204
Last sync       12 seconds ago

CPU             31%
Memory          184 MB
Storage         2.1 GB

Processing
──────────────
Spatial filter       ✓
Aggregation          ✓
Anomaly detection    ✓
Synchronization      ✓
```

A development control could simulate network failure:

```text
node-003

Status       OFFLINE
Pending      17,392

LOCAL PROCESSING
● Continuing
● Continuing
● Continuing
```

Restoring connectivity:

```text
node-003

Synchronizing...

17,392 → 12,000 → 4,200 → 0

✓ Synchronized
```

This makes the distributed architecture visible and understandable.

---

## 6. Natural responsibilities of each language

### Python

Python should remain the flexible, high-level environment.

Potential responsibilities:

- FastAPI service
- job creation
- orchestration
- simulation
- experimentation
- analytics
- test data generation
- central database integration

### SQL / PostGIS

PostgreSQL/PostGIS provides the central spatial data system.

Potential responsibilities:

- observations
- devices/nodes
- geometries
- jobs
- results
- spatial queries
- spatial indexing
- central analytics

### Rust

Rust is the most important learning component.

The edge agent can own:

- ingestion
- validation
- local storage
- spatial filtering
- aggregation
- job execution
- asynchronous networking
- retry logic
- batching
- synchronization
- resource management
- offline operation

The point is not to rewrite Python in Rust. Rust should solve the part of the system where a systems language is interesting.

### Swift / SwiftUI

Swift provides:

- iOS application
- MapKit integration
- map-based visualization
- node monitoring
- system status
- job configuration
- local mobile data collection
- eventually, mobile edge processing

---

## 7. Communication boundaries

Keep the components loosely coupled.

A healthy initial architecture is:

```text
Swift  ←──── HTTPS / JSON ────→  Python
                                  │
                                  │ jobs / results
                                  ▼
                                Rust
```

There is no need for complicated language bindings initially.

The network/API boundary gives each language a clear responsibility and makes the architecture resemble a real distributed system.

---

## 8. Example workload

The system could model environmental, transportation, sensor, drone, or other spatial observations.

A raw observation might contain:

```text
timestamp
sensor_id
latitude
longitude
measurement
```

An edge node could:

1. Receive observations.
2. Validate them.
3. Transform coordinates if necessary.
4. Determine spatial membership/grid cell.
5. Filter against an area of interest.
6. Aggregate observations.
7. Detect anomalies.
8. Store data locally.
9. Synchronize selected results upstream.

The precise domain can evolve. The important part is that the workload is genuinely spatial and benefits from local computation.

---

# 9. Geospatial component

Geospatial should not merely be a theme. It should be part of the computational problem.

Possible operations include:

- point-in-polygon filtering
- bounding-box filtering
- spatial grids
- spatial indexing
- coordinate transformation
- proximity calculations
- spatial aggregation
- area-of-interest processing
- raster/vector workloads

This builds on existing interest in PostGIS, GeoPandas, raster processing, spatial indexes, and geospatial data architecture.

---

# 10. Connection to the spatial file-format project

Another major thread of the broader learning plan is exploring how spatial file formats work and potentially designing a Rust-native cloud-oriented format.

That project should remain conceptually related but not necessarily become part of the first version of this system.

The file-format work explores questions such as:

- binary file specifications
- headers and metadata
- chunking
- spatial indexes
- byte offsets
- compression
- random access
- HTTP Range requests
- object storage
- raster/vector organization

A possible future connection is for Rust edge nodes to produce spatial data shards:

```text
dataset/
├── metadata.json
├── spatial_index/
└── shards/
    ├── z10/
    │   ├── x123_y456.bin
    │   └── x124_y456.bin
    └── z11/
        └── ...
```

The edge system could eventually consume or produce these shards.

However, this should be treated as an **advanced extension**, not a prerequisite for the edge-computing MVP.

The existing file-format learning plan is intentionally incremental:

- v0.1 — uncompressed raster
- v0.2 — chunks/random access
- v0.3 — Zstandard compression
- v0.4 — bounding-box querying
- v0.5 — S3/object-storage access
- benchmark against GeoTIFF/Zarr/GeoParquet

The same principle applies here: avoid accidentally trying to reimplement the entire geospatial data ecosystem.

---

# 11. Development roadmap

This is intentionally a year-scale project. Each phase should produce something independently useful.

## Phase 1 — Learn Rust through the edge agent

Build:

```text
sensor simulator
       ↓
     Rust
       ↓
 local storage
```

Learn:

- ownership
- borrowing
- structs/enums
- traits
- error handling
- modules/crates
- testing
- serialization
- filesystem APIs

Do not worry about distributed systems yet.

---

## Phase 2 — Local geospatial processing

Add:

```text
ingest
  ↓
validate
  ↓
spatial filter
  ↓
aggregate
  ↓
local storage
```

Begin introducing:

- spatial data structures
- spatial indexing
- geospatial algorithms
- performance measurement

---

## Phase 3 — Python control plane

Build:

```text
Python/FastAPI
       │
       ▼
   Rust agent
```

Add:

- node registration
- job creation
- result submission
- node status
- configuration

Use PostgreSQL/PostGIS centrally.

---

## Phase 4 — Offline operation

This is a major milestone.

Disconnect the node from the network.

It must continue:

- receiving data
- processing data
- storing data
- accepting work that can be performed locally

When connectivity returns:

- synchronize automatically
- retry failed work
- avoid duplicate results
- recover cleanly

This phase introduces real distributed-systems concepts.

---

## Phase 5 — Multiple simulated nodes

Run several Rust processes locally.

```text
node-001
node-002
node-003
node-004
...
```

Give them different:

- locations
- workloads
- configurations
- connectivity conditions

The Python control plane should treat them as independent edge devices.

---

## Phase 6 — Swift/SwiftUI application

Build the iOS interface.

Initial functionality:

- map of nodes
- node details
- status
- recent observations
- processing statistics
- job submission
- connectivity state

Use MapKit for spatial visualization.

---

## Phase 7 — iPhone as an edge node

Move beyond visualization.

Use the phone's actual capabilities as an edge data source, such as:

- location
- motion
- locally generated observations

Process some data locally before sending it upstream.

Now the project contains both:

```text
simulated Rust edge nodes
             +
real iPhone edge node
```

---

## Phase 8 — Failure simulation and observability

Build deliberate failure modes:

- network outage
- delayed network
- dropped requests
- node restart
- full local queue
- corrupted/invalid observation
- central service unavailable

Add observability:

- logs
- metrics
- processing latency
- queue depth
- bytes sent
- synchronization status
- CPU/memory usage where practical

---

## Phase 9 — Benchmark the architecture

Compare:

### Centralized

```text
raw observations
        ↓
     network
        ↓
     PostGIS
        ↓
    processing
```

### Edge

```text
raw observations
        ↓
    edge nodes
        ↓
local filtering
aggregation
        ↓
 summarized results
        ↓
    PostGIS
```

Measure:

| Metric | Centralized | Edge |
|---|---:|---:|
| Network bytes | TBD | TBD |
| Processing latency | TBD | TBD |
| Central CPU | TBD | TBD |
| Edge CPU | TBD | TBD |
| Storage | TBD | TBD |
| Offline resilience | No | Yes |

The benchmark should become evidence for the architectural decisions rather than merely a claim that edge computing is "faster."

---

# 12. Suggested repository

```text
geo-edge/
│
├── edge-agent/          # Rust
├── control-plane/       # Python
├── ios-app/              # Swift / SwiftUI
├── simulator/            # Python
├── infrastructure/
├── benchmarks/
├── docs/
│
└── README.md
```

Potential documentation:

```text
docs/
├── architecture.md
├── protocol.md
├── edge-processing.md
├── offline-sync.md
├── spatial-model.md
├── benchmarks.md
└── decisions/
```

An architecture decision record (ADR) folder would be especially useful for documenting *why* the system works the way it does.

---

# 13. Portfolio presentation

The finished project should not just be a GitHub repository.

The strongest presentation would include:

1. **A polished README**
2. **Architecture diagram**
3. **Short demo video/GIF**
4. **Interactive Swift app**
5. **Benchmark results**
6. **Technical writeups**
7. **Failure/recovery demonstrations**
8. **Clear explanation of the geospatial problem**

A compelling demo might show:

```text
1. Launch simulated edge fleet
2. Open iPhone app
3. See nodes appear on map
4. Start streaming observations
5. Watch local processing occur
6. Disable network for one node
7. Observe local processing continue
8. Restore connectivity
9. Watch queued results synchronize
10. Compare network traffic with centralized processing
```

That is a story someone can understand in a few minutes.

---

# 14. What this project is really teaching

Although the visible project is "geospatial edge computing," the deeper curriculum is much broader.

### Computer science

- memory and ownership
- concurrency
- synchronization
- networking
- serialization
- storage
- algorithms
- data structures

### Systems engineering

- processes
- resource constraints
- failure modes
- retries
- backpressure
- queues
- observability
- distributed state

### Geospatial engineering

- coordinate systems
- spatial indexes
- geometry operations
- spatial databases
- spatial partitioning
- raster/vector concepts

### Data engineering

- ingestion
- batching
- local persistence
- synchronization
- data formats
- compression
- benchmarking

### Mobile development

- Swift
- SwiftUI
- MapKit
- device sensors
- local processing
- mobile connectivity

### Architecture

Most importantly, the project forces decisions about **where computation should happen and why**.

---

# 15. Scope discipline

This idea can easily become enormous.

That is both its strength and its danger.

The rule should be:

> **Build the smallest system that demonstrates the next concept.**

Do not begin with:

- Kubernetes
- Kafka
- cloud IoT platforms
- multiple message brokers
- five physical devices
- microservices everywhere
- custom file formats
- production-scale authentication
- elaborate infrastructure

Start with:

```text
Python
   │
   ▼
one Rust edge process
   │
   ▼
local data
```

Then make it work.

Then make it spatial.

Then make it offline.

Then make it distributed.

Then add Swift.

Then make the iPhone a node.

Complexity should be earned by the problem.

---

# 16. A possible one-year progression

This is not a rigid schedule, but a useful mental model.

| Period | Focus | Result |
|---|---|---|
| Months 1–2 | Rust fundamentals | Working local edge agent |
| Months 2–4 | Spatial processing | Rust geospatial workload |
| Months 4–5 | Python/PostGIS control plane | End-to-end single-node system |
| Months 5–7 | Offline + synchronization | Resilient edge system |
| Months 7–8 | Multi-node simulation | Distributed system |
| Months 8–10 | Swift/SwiftUI | Polished iOS client |
| Months 10–11 | iPhone edge node | Real mobile edge device |
| Months 11–12 | Benchmarks + polish | Portfolio-quality project |

These phases can overlap. The important thing is that every stage leaves behind a working artifact.

---

# 17. The north-star version

The eventual system could look like this:

```text
                              ┌───────────────────┐
                              │   iPhone / Swift   │
                              │                   │
                              │  MapKit           │
                              │  Sensor data      │
                              │  Local processing │
                              └─────────┬─────────┘
                                        │
                                        │
                              ┌─────────▼─────────┐
                              │   Python API      │
                              │                   │
                              │   FastAPI         │
                              │   PostGIS         │
                              │   Control plane   │
                              └─────────┬─────────┘
                                        │
                         ┌──────────────┼──────────────┐
                         │              │              │
                         ▼              ▼              ▼
                    ┌─────────┐   ┌─────────┐   ┌─────────┐
                    │ Rust    │   │ Rust    │   │ Rust    │
                    │ Edge 01 │   │ Edge 02 │   │ Edge 03 │
                    └────┬────┘   └────┬────┘   └────┬────┘
                         │              │              │
                         ▼              ▼              ▼
                    local data     local data     local data
                         │              │              │
                         └──────────────┴──────────────┘
                                        │
                              selective synchronization
                                        │
                                        ▼
                                  ┌───────────┐
                                  │  PostGIS  │
                                  │           │
                                  │ canonical │
                                  │   data    │
                                  └───────────┘
```

And potentially, much later:

```text
                    spatial data shards
                           ▲
                           │
                    ┌──────┴──────┐
                    │ Rust format │
                    │ / storage   │
                    └─────────────┘
```

That last piece connects the edge system to the separate exploration of spatial file formats and cloud-native storage.

---

# 18. The guiding philosophy

This project should be treated as a **learning laboratory**, not as a startup that needs to be finished.

The most valuable outcome is not necessarily the final application.

It is the accumulation of understanding:

> What happens when spatial data has to be processed outside the central database?

> What should happen when the network disappears?

> What belongs in a systems language?

> How should spatial data be partitioned and stored?

> How do independent nodes synchronize?

> How do you benchmark edge versus centralized computation?

> What can a mobile device contribute as an edge computer?

> How do geospatial systems intersect with modern software engineering?

Those questions are the real project.

The polished iOS application is the visible surface.

The Rust edge agent is the systems core.

Python/PostGIS is the familiar analytical/control environment.

Geospatial computation is the domain that ties everything together.

And the entire thing becomes a practical path toward becoming a software engineer who happens to have unusually deep geospatial expertise—not a geospatial analyst who happens to write some code.
