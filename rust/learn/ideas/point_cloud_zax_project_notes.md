# A Zax-Like Query Engine for Point Clouds

## Project idea

**Working concept:** build a Rust-based query and compute engine for cloud-native point clouds, analogous in spirit to Earthmover's **Zax** for multidimensional chunked arrays.

The central idea is **not** to create another point-cloud reader, file format, visualization library, or generic point-cloud database.

Instead:

> Build the missing compute/query layer above cloud-native point-cloud storage, initially using COPC as the storage and spatial-indexing substrate.

The motivating analogy is:

| Scientific arrays | Point clouds |
|---|---|
| Zarr | COPC |
| chunk | octree node / point chunk |
| chunk index | COPC hierarchy |
| multidimensional selection | 3D spatial predicate |
| chunk-aware reader | COPC reader |
| Xarray | ??? |
| Dask | ??? |
| Zax | **???** |

The hypothesis is that point clouds have mature pieces for storage, indexing, processing, and visualization, but there is not an obvious mature open-source project occupying the exact role of a **Zax-like, point-cloud-aware query/compute engine**.

This is worth validating with a more systematic ecosystem survey before implementation.

---

# 1. What makes Zax the useful analogy?

Earthmover's Zax is interesting because it is more than a file reader or storage format.

The important abstraction is:

```text
query
  ↓
understand physical data layout
  ↓
determine what actually needs to be read
  ↓
construct an execution plan
  ↓
stream / parallelize computation
```

For multidimensional chunked arrays, Zax can reason about chunks and selections rather than treating the underlying dataset as one giant logical object.

The analogous point-cloud problem is:

```text
SQL / API query
  ↓
understand point-cloud spatial layout
  ↓
determine which spatial chunks can possibly contain results
  ↓
determine which dimensions/attributes are required
  ↓
range-read only relevant data
  ↓
decode / filter / aggregate
  ↓
stream Arrow results
```

That distinction matters.

A conventional point-cloud library might answer:

> How do I read and process this LAS/COPC file?

A Zax-like engine should answer:

> Given this query and this physical organization, what is the cheapest way to execute it?

---

# 2. Why COPC is the natural starting point

COPC (Cloud Optimized Point Cloud) is particularly interesting because it already supplies much of the physical organization that a query engine needs.

Conceptually, a COPC dataset contains a spatial hierarchy based on an octree:

```text
                     root
                      │
            ┌─────────┼─────────┐
            │         │         │
          node       node      node
           │
       ┌───┼───┐
       │   │   │
     chunk chunk chunk
```

The hierarchy allows a reader to determine which portions of the point cloud overlap a spatial query.

A useful mental model is:

```text
query bounding box
       ↓
octree traversal
       ↓
relevant hierarchy nodes
       ↓
relevant compressed chunks
       ↓
HTTP/S3/local range reads
       ↓
LAZ decoding
       ↓
Arrow batches
```

This is already very close to the storage/chunk-selection layer needed by a Zax-like engine.

### Important project decision

**Do not begin by inventing a new point-cloud storage format.**

COPC already provides a strong cloud-native foundation:

- spatial hierarchy
- compressed point storage
- partial reads
- HTTP range access
- cloud/object-storage compatibility
- metadata
- point-cloud dimensions

A better first question is:

> What compute/query capabilities are missing above COPC?

If limitations in COPC eventually become apparent through real workloads, a new physical layout can be investigated later.

---

# 3. Existing ecosystem

There are many projects that solve important parts of the problem.

The interesting question is not whether point-cloud infrastructure exists. It clearly does.

The question is whether these pieces have been assembled into a **point-cloud-aware query optimizer and execution engine**.

## 3.1 PDAL

PDAL is the major general-purpose point-cloud processing ecosystem.

It provides readers, writers, filters, reprojection, classification, pipelines, etc.

PDAL is therefore an important comparison point, but its fundamental abstraction is a **point-cloud processing library/pipeline**, rather than a query optimizer specialized around cloud-native storage layout.

Useful question for this project:

> What does PDAL do that this engine should reuse rather than reinvent?

---

## 3.2 Entwine / EPT

Entwine is an important precedent for organizing enormous point clouds using hierarchical spatial structures.

It is much closer to the storage/indexing side of the proposed project.

Conceptually:

```text
large point cloud
       ↓
spatial hierarchy
       ↓
manageable chunks
       ↓
cloud access / visualization / processing
```

Entwine therefore demonstrates that scalable spatial organization works well.

The potential missing layer is the query planner that reasons about that physical organization.

---

## 3.3 COPC

COPC is likely the most important storage foundation for an initial implementation.

The project can initially treat COPC as:

```text
point-cloud storage
+
spatial index
+
chunk layout
```

and focus on:

```text
query planning
+
chunk pruning
+
remote reads
+
execution
```

rather than rebuilding storage.

---

## 3.4 Rust COPC implementations

There are already Rust implementations that can provide building blocks.

Examples worth investigating include:

- `copc-rust`
- `copc-rs`
- Whitebox's `wblidar`

These demonstrate that a Rust-native COPC ecosystem is already possible.

That is important because the proposed project does **not** need to begin by implementing every low-level LAS/COPC detail.

A first engine could consume an existing Rust COPC implementation and focus on query planning and execution.

---

## 3.5 Apache Arrow

Arrow is an obvious interchange and execution representation.

The conceptual pipeline becomes:

```text
COPC
  ↓
decoded point records
  ↓
Arrow RecordBatch
  ↓
DataFusion execution
```

Arrow provides a columnar representation that maps naturally to point-cloud dimensions:

```text
x
y
z
intensity
classification
return_number
gps_time
...
```

This also creates a natural bridge to Python and other languages.

---

## 3.6 DataFusion

Apache DataFusion may be the most important existing system to study.

It provides:

- SQL parsing
- logical plans
- physical plans
- optimization
- vectorized execution
- Arrow RecordBatch
- parallel execution
- data-source abstractions
- custom execution nodes
- object-store support

This suggests that the project does **not** necessarily need to become an entire query engine from scratch.

Instead:

```text
DataFusion
     +
point-cloud-specific storage/provider
     +
point-cloud-specific optimizer logic
```

could be the core architecture.

That is both more realistic and more interesting.

---

## 3.7 SedonaDB

SedonaDB is particularly relevant because it demonstrates a modern Rust/Arrow/DataFusion approach to spatial query processing.

It provides a useful reference architecture for:

```text
Rust
+
Arrow
+
DataFusion
+
spatial operations
```

However, the core data model remains fundamentally geospatial/tabular rather than a massive 3D point-cloud hierarchy.

That distinction may be where the proposed project fits.

The project would not be trying to replace SedonaDB.

Instead, it could explore:

```text
SedonaDB / spatial SQL
        +
point-cloud-native physical storage
        +
COPC-aware execution
```

---

## 3.8 DuckDB

DuckDB is another important comparison point.

The DuckDB ecosystem can expose point-cloud processing through extensions such as PDAL.

DuckDB demonstrates the appeal of:

```sql
SELECT ...
FROM point_cloud
WHERE ...
```

but the proposed project would focus much more specifically on making the **physical execution of point-cloud queries spatially aware**.

The interesting question is not simply:

> Can point clouds be queried with SQL?

It is:

> Can the query planner exploit the point cloud's physical spatial hierarchy before reading and decoding data?

---

## 3.9 Potree and visualization systems

Potree and similar systems demonstrate efficient out-of-core visualization of enormous point clouds.

They are relevant because visualization engines also need:

```text
view/frustum
  ↓
spatial hierarchy
  ↓
select relevant nodes
  ↓
load only necessary data
```

That is conceptually similar to query-time spatial pruning.

The proposed engine would apply that idea to **analytical queries** rather than rendering.

---

# 4. The proposed engine

A useful working description is:

> **A query and execution engine for cloud-native point clouds.**

Or more specifically:

> **A Zax-like query engine for COPC point clouds, implemented in Rust and integrated with Arrow/DataFusion.**

The first implementation could look approximately like:

```text
                  SQL / DataFrame API
                         │
                         ▼
                  Query Planner
                         │
             ┌───────────┴───────────┐
             │                       │
       spatial reasoning       column reasoning
             │                       │
             └───────────┬───────────┘
                         ▼
                 execution planner
                         │
                         ▼
              COPC spatial hierarchy
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          chunk A     chunk B     chunk C
             │           │           │
             └───────────┼───────────┘
                         ▼
                 streaming Arrow
                         │
                         ▼
                  DataFusion ops
```

---

# 5. Example query

Imagine a COPC dataset containing billions of LiDAR points.

A user asks:

```sql
SELECT
    classification,
    AVG(z) AS mean_elevation,
    COUNT(*) AS n
FROM lidar
WHERE
    x BETWEEN 500000 AND 501000
    AND y BETWEEN 4400000 AND 4401000
    AND classification IN (2, 5)
GROUP BY classification;
```

A naive processing model might be:

```text
read point cloud
    ↓
decompress everything
    ↓
filter
    ↓
aggregate
```

A point-cloud-aware engine should instead aim for:

```text
1. Parse query

2. Identify spatial predicate

3. Traverse COPC hierarchy

4. Eliminate spatially irrelevant nodes

5. Identify relevant point chunks

6. Identify required dimensions:
       x
       y
       z
       classification

7. Range-read only relevant chunks

8. Decode the necessary data

9. Apply remaining predicates

10. Vectorized aggregation

11. Stream Arrow results
```

The important optimization is that **spatial pruning happens before expensive I/O and decoding**.

---

# 6. The genuinely interesting problem: point-cloud query planning

The project becomes substantially more interesting when it moves beyond simply wrapping COPC in SQL.

Consider:

```sql
SELECT x, y, z, intensity
FROM lidar
WHERE
    x BETWEEN 500000 AND 501000
    AND y BETWEEN 4400000 AND 4401000;
```

A normal relational optimizer might represent this as a filter.

A point-cloud-aware optimizer could represent it as:

```text
SpatialSelection
       ↓
OctreeTraversal
       ↓
ChunkPruning
       ↓
RangeRead
       ↓
Decode
       ↓
Filter
```

The physical storage structure becomes part of query planning.

This is the closest conceptual analogue to Zax.

---

# 7. Spatial + column pruning

Point clouds also have an interesting second dimension: attributes.

A query might only need:

```text
x
y
z
classification
```

rather than:

```text
x
y
z
intensity
return_number
number_of_returns
scan_angle
user_data
point_source_id
gps_time
...
```

A future engine could therefore combine:

```text
spatial pruning
+
attribute/dimension pruning
```

Conceptually:

```text
                     query
                       │
             ┌─────────┴─────────┐
             │                   │
       spatial filter       column filter
             │                   │
          octree               stats
             │                   │
             └─────────┬─────────┘
                       │
                  chunk pruning
                       │
                       ▼
                  remote reads
```

This is a promising area for experimentation.

---

# 8. Spatial joins

The project becomes even more interesting when it supports joins between point clouds and vector geospatial data.

For example:

```sql
SELECT
    b.building_id,
    COUNT(*) AS points
FROM lidar l
JOIN buildings b
  ON ST_3DIntersects(l.geometry, b.geometry)
GROUP BY b.building_id;
```

The naive interpretation could involve:

```text
billions of points
×
millions of buildings
```

A spatially aware engine can instead reason:

```text
building bounding box
        ↓
COPC hierarchy
        ↓
relevant nodes
        ↓
relevant point chunks
        ↓
exact geometry test
```

This is where the point-cloud engine starts to become a specialized spatial execution engine rather than merely a file reader.

---

# 9. Potential architecture

A more complete conceptual architecture:

```text
                 ┌──────────────────────┐
                 │     Python / SQL     │
                 └──────────┬───────────┘
                            │
                       Arrow Flight
                            │
                 ┌──────────▼───────────┐
                 │      DataFusion      │
                 │                      │
                 │ SQL / optimizer      │
                 └──────────┬───────────┘
                            │
                   point-cloud-aware
                        optimizer
                            │
              ┌─────────────┴─────────────┐
              │                           │
       spatial planner              column planner
              │                           │
              └─────────────┬─────────────┘
                            │
                   ┌────────▼────────┐
                   │  COPC Provider  │
                   └────────┬─────────┘
                            │
                   ┌────────▼────────┐
                   │ COPC hierarchy  │
                   └────────┬─────────┘
                            │
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
               HTTP        S3        local
              ranges     ranges       file
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                       LAZ decoding
                            │
                            ▼
                    Arrow RecordBatch
                            │
                            ▼
                       DataFusion
```

---

# 10. Why Rust makes sense

Rust is attractive here for more than generic "systems programming" reasons.

The problem naturally involves:

- low-copy data movement
- asynchronous I/O
- HTTP range requests
- object-storage access
- memory-bounded streaming
- parallel decompression
- SIMD/vectorized operations
- explicit ownership
- predictable memory usage
- concurrent query execution
- Arrow
- DataFusion

The closest analogue, Zax, is also implemented in Rust for precisely this sort of native execution-engine role.

Rust therefore provides both:

1. a good technical fit; and
2. an opportunity to learn systems programming through a meaningful geospatial workload.

---

# 11. Proposed development phases

## Phase 0 — Ecosystem research

Before writing significant code, systematically investigate:

- COPC
- EPT / Entwine
- PDAL
- LAZ
- Arrow
- DataFusion
- SedonaDB
- DuckDB
- Potree
- existing point-cloud databases
- spatial indexes
- academic work on point-cloud query processing
- Rust COPC implementations

The goal is to answer:

> What is genuinely missing?

and avoid rebuilding an existing project.

---

## Phase 1 — COPC spatial query prototype

Start without SQL.

Example CLI:

```bash
pcq query \
    s3://bucket/city.copc.laz \
    --bbox 500000,4400000,501000,4401000
```

Return an Arrow stream or equivalent.

The initial engine should learn to:

- open local COPC
- open remote COPC
- inspect hierarchy
- perform spatial traversal
- identify relevant chunks
- range-read chunks
- decode points
- stream results
- maintain bounded memory

This phase alone is a substantial Rust learning project.

---

## Phase 2 — Arrow integration

Represent query output as Arrow `RecordBatch`.

For example:

```text
RecordBatch
├── x
├── y
├── z
├── intensity
└── classification
```

This creates the bridge to:

- Python
- DataFusion
- DuckDB
- Polars
- Arrow Flight
- other Arrow-compatible systems

---

## Phase 3 — DataFusion integration

Expose COPC as a DataFusion table/data source.

Conceptually:

```sql
SELECT x, y, z, intensity
FROM read_copc('s3://bucket/file.copc.laz')
WHERE ...
```

At this point the project becomes an actual query engine rather than a specialized reader.

---

## Phase 4 — Point-cloud-aware physical planning

Teach the engine that a COPC source is not merely an arbitrary table.

Give the planner knowledge of:

```text
spatial hierarchy
chunk bounds
chunk sizes
point counts
available dimensions
```

Then make spatial predicates influence the physical plan.

---

## Phase 5 — Aggregations

Support common analytical workloads:

```sql
COUNT(*)
AVG(z)
MIN(z)
MAX(z)
STDDEV(z)
GROUP BY classification
```

Benchmark how much work can be eliminated before decoding.

---

## Phase 6 — Spatial joins

Investigate:

```text
point cloud ↔ polygons
point cloud ↔ buildings
point cloud ↔ roads
point cloud ↔ raster
point cloud ↔ another point cloud
```

This could become one of the most interesting differentiators.

---

## Phase 7 — Query optimizer research

Once real workloads exist, investigate:

- predicate pushdown
- projection pushdown
- spatial partition pruning
- statistics
- cost models
- parallel execution
- caching
- prefetching
- query scheduling
- adaptive execution

At this stage, the project starts approaching the deeper architectural territory occupied by Zax.

---

# 12. A compelling benchmark

A good demonstration would be a large public COPC dataset.

For example:

```text
Dataset:
    ~4.2 billion points
    ~47 GB

Query:
    1 km × 1 km spatial window
    selected dimensions
    classification filter
    aggregation
```

Report:

```text
Total points:       4.2 billion
Points examined:    18.7 million
COPC chunks read:   143
Bytes read:         81 MB
Dataset size:       47 GB
Execution time:     1.8 s
Peak memory:        XXX MB
```

The exact numbers are hypothetical; the important thing is the benchmark structure.

The demo should make the value of physical query planning obvious:

> The engine did not read a 47 GB point cloud to answer a query that only needed a tiny spatial subset.

---

# 13. What this project should NOT initially be

Avoid trying to build all of these simultaneously:

- a new point-cloud file format
- a full GIS
- a point-cloud viewer
- a replacement for PDAL
- a replacement for PostGIS
- a replacement for DuckDB
- a complete database server
- a distributed compute framework
- a new SQL implementation
- a new object-storage system

The strongest initial scope is:

> **A Rust execution engine that efficiently queries cloud-native COPC point clouds.**

---

# 14. The central research question

The most important question to investigate is:

> **What is the point-cloud equivalent of Zax's contribution beyond the underlying storage format?**

COPC appears to provide something analogous to the physical chunking/layout foundation.

DataFusion provides a general relational execution framework.

Arrow provides the columnar interchange representation.

Existing Rust COPC libraries provide low-level access.

The missing layer may therefore be:

```text
COPC
  +
point-cloud-aware query planning
  +
streaming execution
  +
Arrow/DataFusion
```

That is the hypothesis this project should test.

---

# 15. Why this is a particularly good Rust learning project

This project naturally forces exposure to several important systems concepts:

### Rust language

- ownership
- borrowing
- lifetimes
- traits
- generics
- iterators
- async Rust
- concurrency
- error handling
- memory management

### Systems

- network I/O
- HTTP range requests
- object storage
- compression
- memory budgeting
- streaming
- parallelism
- caching

### Data systems

- query planning
- logical vs physical plans
- predicate pushdown
- projection pushdown
- partition pruning
- cost models
- vectorized execution

### Geospatial systems

- octrees
- spatial bounding boxes
- 3D predicates
- spatial joins
- point-cloud attributes
- LiDAR data organization

### Modern data infrastructure

- Arrow
- DataFusion
- COPC
- cloud object storage
- Arrow Flight
- Python/Rust interoperability

This makes it a particularly good intersection of the user's existing geospatial/data-science experience and the goal of becoming more capable with Rust and systems programming.

---

# 16. Possible project names / positioning

Working names could be deliberately simple:

- `pointq`
- `pcq`
- `cloudpoint`
- `pointfusion`
- `copc-query`
- `lidar-query`
- `point-engine`

The name is less important than the architectural positioning.

A concise project description could eventually be:

> **A Rust query and execution engine for cloud-native point clouds, built around COPC, Arrow, and DataFusion.**

Or, more aspirationally:

> **Zax for point clouds.**

The latter is an excellent internal shorthand while developing, even if the eventual public description uses more precise language.

---

# 17. Open questions to investigate

Before implementation, research these carefully.

### Storage

- Is COPC's octree hierarchy sufficient for analytical workloads?
- How expensive is LAZ decompression relative to network I/O?
- Can dimensions be decoded selectively?
- Are point chunks the right physical unit?
- Would a columnar point-cloud layout improve analytical workloads?

### Indexing

- How much pruning can COPC provide?
- Can attribute statistics provide additional pruning?
- Could chunk-level statistics be stored separately?
- Would secondary indexes be useful?

### Query planning

- How should spatial predicates enter DataFusion's logical/physical plans?
- Can spatial pruning be represented as partition pruning?
- Does DataFusion need a custom execution node?
- Where should COPC-specific optimization occur?

### Execution

- How should remote range requests be scheduled?
- How aggressively should chunks be prefetched?
- How should memory usage be bounded?
- How much parallelism is useful?
- When should chunks be decompressed concurrently?

### Spatial analytics

- How should 3D spatial joins work?
- What should the geometry representation be?
- Can 2D vector geometries be pushed into a 3D point-cloud traversal?
- Could the engine query raster + vector + point cloud together?

### API

- SQL?
- Python API?
- Rust API?
- Arrow Flight?
- DataFusion SQL?
- DataFrame interface?

These questions should be answered incrementally rather than upfront.

---

# 18. Initial recommended direction

The most promising first target is:

```text
Rust
  +
COPC
  +
Arrow
  +
DataFusion
```

with the first milestone being:

```text
SELECT x, y, z, ...
FROM COPC
WHERE spatial_predicate
```

implemented such that:

```text
SQL predicate
    ↓
spatial pruning
    ↓
COPC chunk selection
    ↓
remote range reads
    ↓
streaming Arrow batches
```

Once that works, add:

```text
attribute filters
    ↓
aggregations
    ↓
spatial joins
    ↓
statistics
    ↓
cost-based planning
```

That gives the project a very clear progression from a manageable Rust prototype toward a serious query engine.

---

# 19. Current hypothesis

The strongest current hypothesis is:

> **The point-cloud ecosystem has mature storage, spatial indexing, processing, visualization, and general-purpose query components, but there is an opportunity for a specialized execution engine that treats the physical spatial organization of cloud-native point clouds as a first-class query-planning concern.**

COPC may be the point-cloud equivalent of the storage layer.

DataFusion may be the general-purpose query engine substrate.

Arrow may be the execution/interchange layer.

The project opportunity is the missing connective tissue:

```text
                 COPC
                  │
          physical spatial layout
                  │
                  ▼
       point-cloud query planner
                  │
        ┌─────────┴─────────┐
        │                   │
 spatial pruning       attribute pruning
        │                   │
        └─────────┬─────────┘
                  ▼
            execution plan
                  │
                  ▼
          streaming Arrow
                  │
                  ▼
             DataFusion
```

**That is the project worth investigating further.**

---

# 20. Next research step

Before writing the first Rust crate, perform a systematic landscape survey.

Specifically compare:

1. COPC
2. EPT / Entwine
3. PDAL
4. existing COPC Rust crates
5. DataFusion
6. SedonaDB
7. DuckDB point-cloud integrations
8. Potree
9. point-cloud databases
10. academic point-cloud query engines and spatial indexes

For each, document:

```text
What problem does it solve?
What is its physical data model?
Does it support remote/object storage?
Does it support query planning?
Does it perform spatial pruning?
Does it perform attribute pruning?
Does it expose Arrow?
Is it Rust?
Can it be embedded?
What does it NOT do?
```

The output of that survey should be a project specification and a deliberately small MVP.

Only then should the first implementation begin.

---

## One-sentence project thesis

> **Build the query engine that point clouds have storage formats for, but not yet an obvious Zax-like compute layer for.**
