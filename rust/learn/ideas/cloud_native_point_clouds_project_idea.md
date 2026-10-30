# Cloud-Native Point Clouds: A Potential Rust/Python/Swift Project

## Motivation

A natural follow-on project from learning Rust and working with modern geospatial data systems is to explore what a **cloud-native, analytical data model for point clouds** could look like.

The motivating questions are:

- Is there a Zarr equivalent for point clouds: a chunked, sharded, cloud-native format?
- Is there a Parquet-style columnar format for efficiently storing and querying point clouds?
- Could these ideas be combined into something like a conceptual **"Zarrquet"**?
- What would a spatial SQL engine for point clouds look like?
- Could an existing Rust query engine such as Apache DataFusion provide the foundation?

The interesting question is broader than designing a better LAS file:

> **What is the native analytical data model for billions of spatially indexed, irregular observations in object storage?**

This document captures the current landscape and a possible experimental project direction.

---

# 1. The Existing Landscape

There are three particularly relevant ecosystems:

1. **COPC / LAZ** — mature cloud-oriented point-cloud storage.
2. **Zarr / Zarr Vectors** — chunked cloud-native storage, including emerging approaches for irregular spatial data.
3. **Arrow / Parquet / DataFusion** — columnar analytics and query execution.

They solve overlapping but different problems.

---

## 2. Is There a "Zarr for Point Clouds"?

### Zarr Vectors

A particularly relevant project is **Zarr Vectors**, an emerging specification for representing irregular spatial data using Zarr-style storage concepts.

Normal Zarr is designed primarily around dense N-dimensional arrays:

```text
value[y, x, time, band]
```

A point cloud is fundamentally different:

```text
(x0, y0, z0, attributes0)
(x1, y1, z1, attributes1)
(x2, y2, z2, attributes2)
...
```

It is irregular rather than a dense grid.

Zarr Vectors is intended to support data such as:

- point clouds
- meshes
- skeletons
- streamlines
- graphs
- other irregular spatial objects

The conceptual architecture includes ideas such as:

- spatial binning
- chunks
- fragments
- attributes
- object indexes
- multiple resolutions

So a useful mental model is:

> **Zarr Vectors ≈ Zarr for irregular spatial objects.**

This is very close to the first question.

---

# 3. COPC Is Already a Major Answer

Before inventing anything new, it is important to understand **COPC (Cloud Optimized Point Cloud)**.

COPC is essentially a spatially organized LAZ 1.4 point cloud designed for efficient access over cloud/object storage.

Its core idea is:

```text
point cloud
    ↓
spatial hierarchy
    ↓
spatially coherent compressed chunks
    ↓
retrieve only the relevant portions
```

This makes COPC particularly well suited to queries such as:

> Give me the points in this spatial region.

A simplified comparison:

| Format | Mental model | Primary strength |
|---|---|---|
| LAS | File of points | Interoperability |
| LAZ | Compressed LAS | Storage efficiency |
| COPC | LAZ + spatial hierarchy/index | Cloud point-cloud access |
| Zarr | Chunked N-D arrays | Cloud scientific arrays |
| Zarr Vectors | Chunked irregular spatial data | Cloud-native spatial objects |
| Parquet | Columnar table | Analytical queries |
| GeoParquet | Columnar geospatial table | Analytical vector data |

COPC is therefore an important benchmark for any future point-cloud storage experiment.

---

# 4. Could Point Clouds Use Parquet?

Absolutely.

A point cloud can naturally be represented as a columnar table:

```text
x
y
z
intensity
classification
return_number
number_of_returns
gps_time
...
```

This is attractive because Parquet provides:

- columnar storage
- compression
- row groups
- statistics
- predicate pushdown
- broad interoperability
- integration with Apache Arrow and modern analytical engines

The problem is that **columnar organization and spatial organization are not the same thing**.

Consider billions of LiDAR points.

A normal Parquet table is excellent at answering:

```sql
SELECT classification
FROM lidar;
```

or:

```sql
SELECT *
FROM lidar
WHERE classification = 2;
```

But a spatial query such as:

```sql
SELECT *
FROM lidar
WHERE
    x BETWEEN 500000 AND 501000
    AND y BETWEEN 4500000 AND 4501000
    AND z BETWEEN 100 AND 150;
```

requires spatial locality.

A Parquet row group is not inherently a spatial tile.

---

# 5. The "Zarrquet" Idea

This suggests a hybrid architecture.

Instead of inventing an entirely new point-record encoding, consider:

> **Parquet + spatial partitioning + spatial index + object-store layout**

For example:

```text
pointcloud/
    metadata.json

    index/
        ...

    cells/
        12/
            3841.parquet
            3842.parquet
            3843.parquet

        13/
            ...
```

Each Parquet file might contain:

```text
x
y
z
intensity
classification
return_number
...
```

while a separate spatial index records things such as:

```text
cell_id
bbox
z_min
z_max
point_count
object_location
```

A spatial query could then execute as:

```text
query bounding box
       ↓
spatial index
       ↓
identify relevant partitions
       ↓
read only those Parquet files
       ↓
Parquet predicate pushdown
       ↓
exact point filtering
       ↓
return results
```

This is the basic idea behind a conceptual **"Zarrquet"**: cloud-native spatial partitioning combined with columnar analytical storage.

It does not necessarily need to be a single monolithic file.

A more Zarr-like interpretation would be a dataset consisting of objects in object storage:

```text
s3://bucket/pointcloud/
    metadata.json
    spatial-index/
    partitions/
        ...
```

This fits the modern cloud-native data-lake model better than a single giant file.

---

# 6. Three Possible Physical Architectures

There are at least three interesting approaches.

## A. COPC-like

```text
spatial hierarchy
       ↓
compressed point chunks
       ↓
binary point records
```

Strength:

- excellent spatial retrieval
- mature point-cloud ecosystem
- efficient visualization/access

Primary optimization:

> "Give me the points in this spatial region."

---

## B. Parquet-like

```text
spatial partitions
       ↓
Parquet row groups
       ↓
columnar compression
```

Strength:

- analytical workloads
- SQL
- aggregations
- column projection
- predicate pushdown

Primary optimization:

> "Run analytical queries over billions of point records."

---

## C. Zarr-like

```text
spatial bins
       ↓
Zarr arrays
       ↓
x[]
y[]
z[]
intensity[]
classification[]
```

Strength:

- cloud-native scientific workflows
- object storage
- chunked access
- compatibility with the broader Zarr/Xarray ecosystem
- potentially multiscale data

Zarr Vectors is already exploring this general direction.

---

# 7. A Hybrid May Be the Most Interesting Direction

A potentially compelling architecture is:

```text
                 Point Cloud Dataset
                         │
             ┌───────────┴───────────┐
             │                       │
       spatial index             metadata
             │
       ┌─────┴─────┐
       │           │
    partition   partition
       │           │
    ┌──┴──┐     ┌──┴──┐
    │     │     │     │
    x y z ...   x y z ...
    │     │     │     │
   Arrow/Parquet chunks
```

The key concept would be:

> **Cloud-native spatial columnar storage**

rather than necessarily creating another monolithic file format.

---

# 8. Is There Spatial SQL for Point Clouds?

Yes, at least conceptually, and there are important precedents.

A point cloud can be treated as a table:

```text
lidar
----------------
x
y
z
intensity
classification
return_number
...
```

Then ordinary SQL can already express many useful queries:

```sql
SELECT *
FROM lidar
WHERE
    x BETWEEN 500000 AND 501000
    AND y BETWEEN 4500000 AND 4501000;
```

A spatial SQL dialect could add functions such as:

```text
ST_Within()
ST_Intersects()
ST_DWithin()
ST_3DDWithin()
ST_ClusterDBSCAN()
ST_ConvexHull()
ST_Envelope()
```

alongside point-cloud-specific operations such as:

```text
voxelize()
decimate()
sample()
density()
height_above_ground()
nearest_neighbor()
radius_query()
```

For example:

```sql
SELECT
    classification,
    COUNT(*),
    AVG(z),
    MIN(z),
    MAX(z)
FROM lidar
WHERE ...
GROUP BY classification;
```

This begins to resemble **PostGIS for point clouds**.

---

# 9. Earthmover's Zax as a Conceptual Analogy

Earthmover's recent work around **Zax** is a useful analogy.

The broader Earthmover architecture can be understood conceptually as:

```text
Zarr
  ↓
Icechunk
  ↓
Arraylake
  ↓
Zax
```

with the final layer exposing SQL/query-engine capabilities over cloud-native scientific array data.

The interesting question for point clouds is therefore:

> **What would "Zax for point clouds" look like?**

A corresponding architecture might be:

```text
point-cloud storage
        ↓
spatial index
        ↓
query engine
        ↓
spatial SQL
        ↓
Arrow / Flight SQL / client APIs
```

The important insight is that the file format and query engine do not have to be designed simultaneously.

---

# 10. DataFusion Is an Especially Interesting Foundation

**Apache DataFusion** is a query engine written in Rust and built around Apache Arrow.

That makes it unusually relevant to this project.

The ecosystem can be visualized as:

```text
                         SQL
                          │
                          ▼
                  ┌───────────────┐
                  │   DataFusion  │
                  │ query engine  │
                  └───────┬───────┘
                          │
                     Apache Arrow
                          │
             ┌────────────┴────────────┐
             │                         │
         Parquet                   spatial
                                   functions
             │                         │
             └────────────┬────────────┘
                          │
                    object storage
                          │
                         S3
```

There is also **GeoDataFusion**, which adds geospatial functionality to DataFusion and provides a useful precedent for building spatial SQL on top of a Rust query engine.

This means a point-cloud query engine would not necessarily require building an entire SQL engine from scratch.

---

# 11. Why Rust Is a Strong Candidate

Rust is particularly well suited to this kind of systems project because the relevant ecosystem already aligns with it.

Potential building blocks include:

### Apache Arrow

Columnar in-memory representation.

### Apache Parquet

Columnar persistent storage.

### DataFusion

SQL planning and execution.

### GeoDataFusion

Existing spatial-query foundations.

### object_store

Cloud object-storage abstraction.

### Tokio

Asynchronous I/O.

### SIMD / native numerical computation

Potentially useful for point-cloud processing and spatial predicates.

### Rust's ownership model

Important when streaming and manipulating very large datasets without garbage collection.

A possible architecture:

```text
                     SQL
                      │
                      ▼
              ┌─────────────┐
              │  DataFusion │
              └──────┬──────┘
                     │
             query optimizer
                     │
        ┌────────────┴────────────┐
        │                         │
 spatial predicates        attribute predicates
        │                         │
        └────────────┬────────────┘
                     │
               spatial index
                     │
             object-store scan
                     │
             ┌───────┴───────┐
             │               │
          Parquet          COPC
             │               │
             └───────┬───────┘
                     │
                   Arrow
                     │
                     ▼
                  results
```

Most of these components already exist independently.

The experimental opportunity is **connecting them intelligently for point-cloud workloads**.

---

# 12. A Possible Rust Learning Project

Rather than immediately inventing a new file format, the project could be developed incrementally.

## Stage 1 — Point Cloud → Arrow

Represent a point cloud as Arrow columns.

Conceptually:

```rust
struct Point {
    x: f64,
    y: f64,
    z: f32,
    intensity: u16,
    classification: u8,
}
```

Then investigate how the data should actually be represented as Arrow `RecordBatch` objects.

---

## Stage 2 — Arrow → Parquet

Write:

```text
points.parquet
```

with columns such as:

```text
x
y
z
intensity
classification
```

Benchmark:

```sql
WHERE classification = 2
```

against spatial predicates:

```sql
WHERE
    x BETWEEN ...
    AND y BETWEEN ...
```

This demonstrates the distinction between:

- columnar filtering
- spatial filtering

---

## Stage 3 — Spatial Partitioning

Introduce spatial partitions.

For example:

```text
tile_123.parquet
tile_124.parquet
tile_125.parquet
```

or some more sophisticated spatial key.

Then benchmark spatial queries against the unpartitioned dataset.

Potential spatial organizations to investigate:

- regular grids
- Morton/Z-order curves
- Hilbert curves
- H3
- S2
- octrees
- kd-trees
- R-trees / related spatial indexes

---

## Stage 4 — DataFusion

Use DataFusion rather than writing a SQL engine.

Then queries such as:

```sql
SELECT
    classification,
    COUNT(*)
FROM lidar
GROUP BY classification;
```

can execute through a real query planner.

---

## Stage 5 — Spatial Query Planning

Teach the query engine that:

```sql
WHERE ST_Within(...)
```

can be optimized approximately as:

```text
1. Determine query bounding box
2. Consult spatial index
3. Eliminate irrelevant partitions
4. Scan relevant Parquet row groups
5. Apply exact spatial predicate
6. Return results
```

This is where the project becomes a genuine query-engine experiment.

---

# 13. Potential Monorepo Structure

Given the Rust/Python/Swift spatial project, an experimental implementation could eventually look something like:

```text
rust/
└── spatial_query/
    ├── pointcloud-core/
    ├── pointcloud-parquet/
    ├── pointcloud-index/
    └── pointcloud-sql/

python/
└── spatial_query/
```

Swift could eventually consume the Rust core through a C-compatible or Swift-friendly interface if there is a compelling application for it.

The initial project should remain Rust-heavy rather than prematurely building all three language layers.

---

# 14. A Useful Research/Benchmark Question

A concrete first research question could be:

> **Can a spatially partitioned columnar point-cloud format provide better analytical query performance than conventional Parquet while retaining Parquet/Arrow interoperability, and how does it compare with COPC?**

For example:

```text
                    Dataset
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      COPC        Parquet       spatial Parquet
                       │              │
                       │              │
                  benchmark queries
                       │
        ┌──────────────┼──────────────┐
        │              │              │
      spatial       attribute      aggregation
       query          query           query
```

Metrics could include:

- storage size
- compression ratio
- bytes read
- number of objects/chunks touched
- query latency
- CPU time
- memory usage
- scalability with point count
- performance over local disk vs S3/object storage

This would make the project empirical rather than purely speculative.

---

# 15. The Bigger Ecosystem Symmetry

There is a useful conceptual symmetry across modern geospatial data:

## Raster

```text
COG
  ↓
Zarr
  ↓
Xarray
  ↓
Zax / array query engines
```

## Vector

```text
GeoParquet
  ↓
Arrow
  ↓
DuckDB / DataFusion
  ↓
Spatial SQL
```

## Point Cloud

```text
COPC
   ?
Zarr Vectors
   ?
Spatial columnar format
   ?
Point-cloud SQL engine
```

The point-cloud ecosystem is not as settled around one analytical architecture.

That makes it an interesting area to explore.

---

# 16. The Central Project Idea

The project does **not** necessarily need to invent a new file format.

The more interesting goal may be:

> **Explore a cloud-native spatial columnar representation for point clouds and build a query engine capable of exploiting its spatial organization.**

The conceptual stack would be:

```text
        Cloud-native point-cloud dataset
                     │
              spatial metadata
                     │
               spatial index
                     │
             spatial partitions
                     │
              Arrow / Parquet
                     │
                 DataFusion
                     │
               spatial SQL
                     │
             Python / CLI / APIs
```

This approach also preserves interoperability with existing technologies rather than replacing them.

---

# 17. Existing Technologies to Study Before Building

A sensible investigation order would be:

1. **LAS / LAZ**
2. **COPC**
3. **Zarr**
4. **Zarr Vectors**
5. **Apache Arrow**
6. **Apache Parquet**
7. **GeoParquet**
8. **Apache DataFusion**
9. **GeoDataFusion**
10. **DuckDB spatial / spatial Parquet workflows**
11. **Icechunk / Arraylake / Zax**
12. Spatial indexing approaches:
    - Morton/Z-order
    - Hilbert ordering
    - H3
    - S2
    - octrees
    - R-trees
    - kd-trees

The goal would be to understand what each existing technology already solves before introducing anything new.

---

# 18. The Deeper Systems Question

The most interesting version of the project is not:

> "Can I make a better LAS file?"

It is:

> **"What should the native analytical data model be for billions of spatially indexed, irregular observations stored in object storage?"**

That question connects:

- geospatial data engineering
- distributed systems
- columnar storage
- spatial indexing
- query optimization
- cloud object storage
- Rust
- Arrow
- Parquet
- Zarr
- SQL
- PostGIS-style spatial computation

It is therefore a particularly good candidate for a longer-term Rust project because it can start extremely small while having a path toward genuinely sophisticated systems work.

---

# 19. Possible Project Evolution

A realistic progression could be:

```text
                 Point Cloud
                     │
                     ▼
              Read COPC / LAZ
                     │
                     ▼
              Arrow RecordBatch
                     │
                     ▼
                  Parquet
                     │
                     ▼
             Spatial partitioning
                     │
                     ▼
              Spatial index
                     │
                     ▼
                DataFusion
                     │
                     ▼
                Spatial SQL
                     │
                     ▼
             S3 / object storage
                     │
                     ▼
              Python bindings
                     │
                     ▼
            Optional Swift client
```

At each stage there is a useful, independently testable project.

The eventual system could be benchmarked against:

- COPC
- conventional Parquet
- Zarr Vectors
- existing spatial databases
- DuckDB
- PostGIS
- other point-cloud query systems

The end result does not need to "win" against those systems. The learning value is in understanding **why their physical and logical designs make the tradeoffs they do**.

---

## One-Sentence Project Pitch

> **Explore a cloud-native spatial columnar data model for point clouds, combining Parquet/Arrow-style analytical storage with COPC/Zarr-style spatial chunking and a Rust/DataFusion-based spatial SQL query engine.**

That is the core idea worth carrying forward into the Rust/Python/Swift project.
