# Rust for Geospatial Systems

**Syllabus Version:** 0.2\
**Course Format:** Self-paced, ChatGPT-guided, project-based\
**Expected Commitment:** Up to 30 minutes per session; approximately
2--3 hours per unit\
**Prerequisite Rust Knowledge:** None\
**Primary Prior Knowledge:** Python, SQL, Spatial SQL, PostGIS,
GIS/geospatial analysis\
**Strategic Context:** *Spatial Systems Engineering Learning Program ---
Working Strategy and North Star*\
**Course Vintage:** September 2026

------------------------------------------------------------------------

## 1. Course Purpose

This course teaches Rust from the ground up as the **systems and
high-performance computational layer** of a larger Spatial Systems
Engineering learning program.

The objective is not to become a Rust language specialist or to replace
Python, SQL, PostGIS, DuckDB, or mature geospatial libraries. The
objective is to become sufficiently fluent in Rust to:

-   understand and write practical, idiomatic Rust;
-   understand why Rust differs from Python and where those differences
    matter;
-   strengthen selected computer-science and systems fundamentals
    relevant to geospatial engineering;
-   reason about memory, I/O, data structures, algorithms, spatial
    indexing, concurrency, and performance;
-   build correct and measurable geospatial computation;
-   understand binary and columnar spatial data representations;
-   build reusable Rust components that can participate in a larger
    multi-language spatial system;
-   integrate Rust with Python;
-   prepare Rust components for later use in edge and distributed
    computing;
-   intelligently decide when Rust is---and is not---the right
    primitive;
-   discuss Rust, performance, storage, algorithms, and geospatial
    systems confidently in technical interviews; and
-   contribute a substantial, portfolio-grade subsystem to the eventual
    Spatial Edge Platform.

Rust is therefore both a **language to learn** and a **vehicle for
learning how computation actually works**.

The guiding Rust question is:

> **How does computation actually work, and how can spatial computation
> be made fast, reliable, memory-conscious, and scalable?**

------------------------------------------------------------------------

## 2. Strategic Role in the Larger Program

This syllabus is Course / Track 1 of the broader **Spatial Systems
Engineering** program.

The long-term professional target is:

> **Spatial Systems Engineer**

The larger program intentionally combines spatial computation, data
infrastructure, systems programming, machine learning, edge/distributed
computing, and native application development.

Within that architecture, Rust has a deliberate responsibility:

``` text
Spatial problem
      │
      ▼
Python / SQL / PostGIS
experimentation, orchestration, durable data
      │
      ▼
Rust systems layer
      │
      ├── geometry
      ├── spatial indexing
      ├── binary I/O
      ├── chunk processing
      ├── serialization
      ├── compression
      ├── performance-sensitive algorithms
      ├── concurrency
      └── future edge-node processing
      │
      ▼
larger distributed spatial platform
```

The Rust course does **not** attempt to teach the full distributed
system. Networking, synchronization, resource-constrained nodes,
observability, orchestration, and edge-vs-central architecture will
receive dedicated treatment in the subsequent **Spatial Systems &
Distributed Computing** curriculum.

This course should, however, leave behind Rust components that can
naturally become part of that system.

------------------------------------------------------------------------

# 3. Governing Course Principles

## 3.1 Bridge from Known → Unknown

Rust concepts should whenever useful be connected to familiar Python,
SQL, Spatial SQL, PostGIS, and GIS concepts.

  -----------------------------------------------------------------------
  Rust                                Familiar Bridge
  ----------------------------------- -----------------------------------
  `Vec<T>`                            Python `list`

  `HashMap<K, V>`                     Python `dict`

  `struct`                            Python `dataclass`; structured
                                      database row

  `Option<T>`                         Python `None`; SQL `NULL`

  `Result<T, E>`                      Explicit alternative to
                                      exception-driven failure

  iterators                           Python generators/comprehensions;
                                      relational transformations

  ownership                           Contrast with Python references and
                                      garbage collection

  borrowing                           Temporary access without ownership
                                      transfer

  traits                              Interfaces/protocols and behavioral
                                      contracts

  enums + `match`                     Structured states plus exhaustive
                                      branching

  spatial predicates                  PostGIS/Shapely equivalents

  spatial indexes                     GiST/R-tree concepts

  Arrow                               Shared columnar bridge among
                                      analytical systems

  PyO3                                Rust functionality exposed inside
                                      Python
  -----------------------------------------------------------------------

These comparisons are bridges, not claims that the mechanisms are
identical.

------------------------------------------------------------------------

## 3.2 One Evolving Portfolio System

Small exercises are disposable learning material.

Major deliverables are not.

The Rust work should progressively build a subsystem that later plugs
into the larger Spatial Edge Platform:

``` text
Rust foundations
      ↓
typed spatial data tool
      ↓
binary spatial storage
      ↓
chunked + indexed spatial format
      ↓
geospatial algorithms
      ↓
performance-tested Rust library
      ↓
Python-accessible systems layer
      ↓
future edge-node component
```

Each checkpoint should improve the same repository or closely related
workspace rather than create disconnected tutorial projects.

The Git history should tell the story of the system evolving.

------------------------------------------------------------------------

## 3.3 Build Vertically

Prefer small end-to-end slices over months of isolated study.

A new concept should move as quickly as practical from:

``` text
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

The project should remain runnable throughout the course.

------------------------------------------------------------------------

## 3.4 Follow the Modern Geospatial Market

The supplied 2026 geospatial systems job materials serve as market
signals rather than exact specifications.

The Paces role emphasizes large-scale spatial search and analysis,
computational geometry, performance over tens of millions of parcels and
nationwide infrastructure data, DuckDB, Arrow/GeoArrow, file-based
spatial indexing, strong CS fundamentals, query plans, correctness, and
explicit performance measurement. It also lists systems languages,
GeoRust/`geo`, PostGIS, GDAL, GeoArrow, Zarr/GeoZarr, spatial pipelines,
spatial indexing, and distributed/ephemeral compute as valuable
capabilities.

The newer Radar Maps material reinforces a complementary signal: modern
location infrastructure can span Rust, Python, other backend languages,
large-scale data pipelines, reliable data foundations, high-throughput
serving, and engineers who are comfortable moving across stacks.

The course should therefore ask repeatedly:

> **What capability is a modern spatial systems engineer expected to
> possess, and how does this lesson help build it?**

------------------------------------------------------------------------

## 3.5 Use Industry Practitioners as a Compass

Contemporary practitioners who actively track and shape modern GIS
should influence **Industry Connection** sections.

Matt Forrest remains a particularly useful signal for modern Spatial
SQL, PostGIS, DuckDB, GeoParquet, cloud-native spatial workflows,
spatial data engineering, and changing expectations for GIS
professionals.

Practitioner guidance is a strong signal, not unquestionable doctrine.

------------------------------------------------------------------------

## 3.6 Benchmark Rather Than Assume

Performance claims must be measured.

Relevant dimensions include:

-   runtime;
-   memory;
-   CPU;
-   bytes read;
-   bytes written;
-   storage size;
-   number of I/O operations;
-   latency;
-   throughput;
-   compression ratio;
-   allocation behavior; and
-   data copied across language or system boundaries.

The expected conclusion is never automatically "Rust wins."

The objective is to explain **why** a design behaves as it does.

------------------------------------------------------------------------

## 3.7 Every Technology Must Solve a Real Problem

Do not add a crate, database, cloud service, orchestration framework, or
concurrency mechanism merely because it is marketable.

A governing rule for the entire program is:

> **Every new technology should solve a meaningful problem in the system
> rather than being added merely because it is fashionable or
> marketable.**

------------------------------------------------------------------------

# 4. The CS Lens

The student does not have a traditional computer-science education.

Selected CS concepts therefore appear as **CS Lens interludes** at the
point where they become useful to a GIS/spatial systems engineer.

The question guiding each CS Lens is:

> **What computer-science concept would make a geospatial engineer
> understand this problem more deeply?**

Likely topics include:

-   compilation and runtime models;
-   stack versus heap;
-   memory representation;
-   references and pointers;
-   static versus dynamic typing;
-   bytes, bits, integer representation, and endianness;
-   algorithmic complexity and Big-O;
-   arrays and dynamic arrays;
-   hash tables;
-   trees and spatial indexes;
-   offsets and random access;
-   serialization/deserialization;
-   chunking and locality;
-   caching;
-   row versus columnar storage;
-   cache locality;
-   zero-copy concepts;
-   concurrency versus parallelism;
-   I/O-bound versus CPU-bound work;
-   compression tradeoffs;
-   profiling and benchmarking;
-   system boundaries and data movement.

This is not an attempt to recreate a generic undergraduate CS
curriculum.

------------------------------------------------------------------------

# 5. Standard Learning Loop

Each unit should be divisible into approximately 30-minute sessions.

A typical unit may contain:

### Session A --- Rust Concept

Introduce the language or systems concept with small examples.

### Session B --- Known → Unknown

Compare it with Python, SQL, Spatial SQL, PostGIS, or familiar GIS
workflows.

### Session C --- Practice

The student attempts short exercises before receiving complete solutions
whenever practical.

### Session D --- CS Lens

Explain the underlying computer-science or systems concept.

### Session E --- Geospatial / Systems Application

Apply the concept to spatial data.

### Session F --- Industry Connection

Connect the lesson to contemporary geospatial systems engineering.

### Session G --- Portfolio Increment

Incorporate the concept into the evolving Rust subsystem where
justified.

Not every unit requires every session type.

------------------------------------------------------------------------

# 6. Teaching and Feedback Method

Instruction should favor rapid feedback and iteration.

``` text
teach
  ↓
small example
  ↓
student attempt
  ↓
review
  ↓
explain mistake or tradeoff
  ↓
student revises
  ↓
apply to spatial system
```

Code review should distinguish:

1.  **Correctness** --- Does it work?
2.  **Rust idiom** --- Is this how Rust is normally written?
3.  **Systems understanding** --- Does the student understand
    memory/data movement/I/O implications?
4.  **Software design** --- Is the abstraction appropriate?
5.  **Performance** --- Does performance matter here, and has it been
    measured?
6.  **Readability** --- Can another engineer understand it?
7.  **Geospatial correctness** --- Are spatial assumptions valid?
8.  **Interoperability** --- Does the component have a sensible boundary
    with Python/data systems?
9.  **Future system fit** --- Could this component participate cleanly
    in the later edge/distributed architecture?
10. **Production readiness** --- What would still need hardening?

------------------------------------------------------------------------

# 7. Course Architecture

The course contains **12 primary units across four phases**.

The pedagogical progression from v0.1 is preserved. The major v0.2
change is that exercises and deliverables increasingly converge on a
**Rust-native spatial systems layer**, with a small custom chunked
spatial raster format serving as a central learning vehicle.

------------------------------------------------------------------------

# PHASE I --- LEARN TO THINK IN RUST

## Unit 1 --- From Python to Rust

### Core Rust Topics

-   what Rust is;
-   compiled versus interpreted workflows;
-   `rustup`, `rustc`, Cargo;
-   crates and packages;
-   `cargo new`, `run`, `check`, `test`, `fmt`;
-   Clippy;
-   `fn main()`;
-   variables and mutability;
-   primitive scalar types;
-   functions;
-   expressions;
-   control flow.

### Known → Unknown

Compare Python's interpreter/runtime workflow with Rust's compile/run
workflow.

### CS Lens --- Compilation, Types, and Runtime Models

Questions:

-   What does a compiler do?
-   What does Python defer until runtime?
-   What can Rust establish before execution?
-   What is machine code?
-   Why can compile-time guarantees matter in a data system?

### Spatial Application

Represent coordinates, raster dimensions, measurements, and simple
observations with explicit types.

### Portfolio Increment

Initialize the Rust workspace with:

-   professional Cargo structure;
-   Git;
-   formatting and linting;
-   README skeleton;
-   tests;
-   a small CLI.

------------------------------------------------------------------------

## Unit 2 --- Data Has Shape

### Core Rust Topics

-   tuples;
-   arrays;
-   `Vec`;
-   `String` and `str`;
-   structs;
-   enums;
-   methods;
-   `Option<T>`;
-   `match`;
-   `if let`.

### Known → Unknown

Connect Rust structures to Python dataclasses, database records,
nullable fields, and explicit state models.

### CS Lens --- Representation and Invariants

Explore why data representation affects correctness and why types can
make invalid states harder to construct.

### Spatial Application

Model:

-   coordinates;
-   bounding boxes;
-   raster metadata;
-   data types;
-   CRS metadata;
-   sensor/spatial observations.

### Portfolio Increment

Define the first typed structures that will later form the `.spat` file
header and metadata model.

------------------------------------------------------------------------

## Unit 3 --- Ownership: The Big Rust Idea

### Core Rust Topics

-   ownership;
-   moves;
-   copies;
-   borrowing;
-   references;
-   mutable references;
-   slices;
-   lifetimes conceptually.

### Known → Unknown

Contrast Rust's ownership model with Python references and garbage
collection.

### CS Lens --- Memory

Explore:

-   stack;
-   heap;
-   allocation;
-   copying;
-   references;
-   object lifetime;
-   garbage collection;
-   memory safety.

### Spatial / Systems Application

Compare the cost of copying:

-   one coordinate;
-   one raster row;
-   one raster tile;
-   a large spatial buffer.

Ask when data can be borrowed rather than copied.

### Checkpoint 1 --- Rust Foundations

The evolving repository can:

-   model typed spatial/raster metadata;
-   manipulate small in-memory datasets;
-   validate inputs;
-   expose a CLI;
-   demonstrate ownership and borrowing correctly;
-   contain tests and documentation.

No custom binary format is required yet, but the types should prepare
for it.

------------------------------------------------------------------------

# PHASE II --- BUILD ROBUST SYSTEMS SOFTWARE

## Unit 4 --- Errors Are Data

### Core Rust Topics

-   `Option`;
-   `Result`;
-   `Ok` / `Err`;
-   `unwrap` and why to limit it;
-   `expect`;
-   `?`;
-   error propagation;
-   custom errors;
-   recoverable versus unrecoverable failures.

### Known → Unknown

Compare `Result` with Python exceptions and distinguish both from SQL
`NULL`.

### CS Lens --- Failure Models and Correctness

Distinguish:

-   missing value;
-   malformed value;
-   corrupt file;
-   unsupported version;
-   programmer error;
-   I/O failure;
-   system failure.

### Systems Application

Design errors for:

-   invalid magic bytes;
-   unsupported format version;
-   impossible dimensions;
-   invalid offsets;
-   truncated files;
-   invalid CRS metadata.

### Portfolio Increment

Introduce explicit error types and fail loudly on corrupt or invalid
spatial data.

------------------------------------------------------------------------

## Unit 5 --- Collections, Iterators, and Data Pipelines

### Core Rust Topics

-   `Vec`;
-   `HashMap`;
-   iteration;
-   iterator adapters;
-   closures;
-   `map`;
-   `filter`;
-   `fold`;
-   `collect`;
-   ownership during iteration.

### Known → Unknown

Compare Rust iterator pipelines with Python comprehensions/generators
and SQL relational transformations.

### CS Lens --- Core Data Structures and Complexity

Explore:

-   arrays;
-   dynamic arrays;
-   hash tables;
-   lookup and insertion costs;
-   contiguous storage;
-   introductory Big-O.

### Spatial Application

Process raster tiles or spatial records:

-   validate;
-   filter;
-   aggregate;
-   compute extents;
-   summarize values;
-   organize chunk metadata.

### Portfolio Increment

Build clean in-memory transformations that will later feed the writer
and reader.

------------------------------------------------------------------------

## Unit 6 --- Traits, Generics, Modules, and Reusable Software

### Core Rust Topics

-   traits;
-   generics;
-   `impl`;
-   trait bounds;
-   modules;
-   public/private APIs;
-   unit tests;
-   integration tests;
-   documentation;
-   project organization.

### CS Lens --- Abstraction and Contracts

Ask:

-   What behavior deserves an interface?
-   What should remain concrete?
-   When does generic code help?
-   When does abstraction hide the important part?

### Systems Application

Begin separating concepts such as:

``` text
format specification
reader
writer
storage
metadata
errors
```

without over-engineering.

### Checkpoint 2 --- First Binary Spatial Artifact

The repository now writes and reads a deliberately simple **uncompressed
raster `.spat` file**.

A minimal conceptual structure:

``` text
┌──────────────────────────┐
│ MAGIC: "SPAT"            │
├──────────────────────────┤
│ VERSION                  │
├──────────────────────────┤
│ WIDTH / HEIGHT / BANDS   │
├──────────────────────────┤
│ DTYPE                    │
├──────────────────────────┤
│ CRS / metadata           │
├──────────────────────────┤
│ DATA                     │
└──────────────────────────┘
```

The objective is not to invent a competitive geospatial standard.

The objective is to understand:

-   bytes;
-   serialization;
-   file I/O;
-   specification versus implementation;
-   reader/writer symmetry;
-   validation;
-   testable data contracts.

The project should now resemble a small systems-software product rather
than a Rust tutorial.

------------------------------------------------------------------------

# PHASE III --- SPATIAL STORAGE, INDEXING, AND COMPUTATION

## Unit 7 --- Bytes, Binary I/O, and Chunking

### Core Topics

-   byte buffers;
-   integer representation;
-   endianness;
-   fixed- versus variable-length fields;
-   offsets;
-   seek/read/write;
-   serialization/deserialization;
-   chunk tables;
-   random access.

### CS Lens --- Data on Disk

Explore:

-   what a file actually is;
-   byte offsets;
-   locality;
-   sequential versus random access;
-   metadata overhead;
-   I/O amplification.

### Spatial Application

Evolve `.spat` from:

``` text
header
data
```

to:

``` text
header
index
chunk
chunk
chunk
...
```

### Experiment

Compare chunk sizes and observe tradeoffs:

-   many small chunks;
-   fewer large chunks;
-   metadata overhead;
-   unnecessary bytes read.

### Portfolio Increment

Implement `.spat` v0.2 with chunked raster storage and indexed offsets.

------------------------------------------------------------------------

## Unit 8 --- Geometry, Spatial Relationships, and Spatial Querying

### Core Topics

Introduce appropriate GeoRust concepts and libraries.

Work with:

-   points;
-   bounding boxes;
-   geometry types where useful;
-   intersection;
-   containment;
-   distance;
-   coordinate systems conceptually;
-   spatial extents.

### Known → Unknown

Triangulate equivalent ideas across:

``` text
PostGIS
Shapely / GeoPandas
Rust / GeoRust
```

### CS Lens --- Computational Geometry and Algorithmic Complexity

Explore:

-   vertices and extents;
-   bounding-box rejection;
-   linear search;
-   candidate generation;
-   exact evaluation;
-   how dataset size changes engineering choices.

### Spatial Application

Associate each raster chunk with a spatial extent.

Implement the first conceptual:

``` rust
dataset.read_bbox(bbox)
```

using a simple scan of chunk extents.

### Portfolio Increment

The custom format becomes explicitly spatial rather than merely a
generic binary container.

------------------------------------------------------------------------

## Unit 9 --- Spatial Indexing and Search

### Core Topics

-   brute-force search;
-   bounding-box pruning;
-   R-trees;
-   spatial indexes;
-   nearest-neighbor concepts;
-   file-based indexes;
-   candidate generation versus exact evaluation.

### Known → Unknown

Connect in-memory/file-based Rust indexing with familiar PostGIS
spatial-index concepts.

### CS Lens --- Trees, Indexes, and Search

Explore:

-   tree structures;
-   index build cost versus query cost;
-   search-space reduction;
-   Big-O as an engineering tool;
-   why indexes change I/O as well as CPU work.

Introduce Morton/Z-order or Hilbert curves conceptually where useful,
without requiring implementation unless justified.

### Experiment

Benchmark simple spatial lookup at increasing scale.

Measure both:

-   computation;
-   amount of data read.

### Checkpoint 3 --- Chunked, Spatially Indexed Format

The Rust subsystem now contains:

-   a documented `.spat` specification;
-   reader and writer;
-   chunked raster storage;
-   chunk offset index;
-   chunk spatial extents;
-   bounding-box reads;
-   correctness tests;
-   benchmark fixtures;
-   documented tradeoffs.

Optional extension, only if it serves the learning goals:

-   independent chunk compression, such as Zstandard.

The important systems question is now:

> **How do I organize spatial data so that a spatial query retrieves the
> smallest useful amount of data with the fewest reasonable I/O
> operations?**

------------------------------------------------------------------------

## Unit 10 --- Modern Geospatial Data Systems and Interchange

### Core Topics

-   row versus columnar representation;
-   Arrow;
-   GeoArrow;
-   Parquet;
-   GeoParquet;
-   DuckDB;
-   Zarr as a chunked-array comparison point;
-   serialization;
-   memory movement;
-   zero-copy concepts;
-   data interchange.

### Known → Unknown

Follow data through:

``` text
GeoParquet / Zarr / .spat
          ↓
      Rust buffers
          ↓
 Arrow / Python / DuckDB
          ↓
 spatial computation
```

### CS Lens --- Memory Layout and Analytical Systems

Explore:

-   contiguous memory;
-   row versus columnar layouts;
-   cache locality;
-   serialization overhead;
-   copies;
-   vectorized processing;
-   zero-copy interchange;
-   storage layout versus access pattern.

### Comparative Study

The custom format exists to expose design tradeoffs already solved by
mature technologies.

Compare `.spat` conceptually and experimentally where appropriate with:

-   GeoTIFF;
-   Zarr;
-   Parquet / GeoParquet.

Do not attempt to reproduce their full feature sets.

### Industry Connection

Revisit the modern geospatial stack and why current systems roles
emphasize Arrow/GeoArrow, DuckDB, file-based indexing, cloud-native
formats, and performance-aware data movement.

------------------------------------------------------------------------

# PHASE IV --- PERFORMANCE, INTEROPERABILITY, AND SYSTEM READINESS

## Unit 11 --- Performance Engineering

### Core Topics

-   debug versus release builds;
-   benchmarking;
-   profiling;
-   hot paths;
-   allocations;
-   unnecessary copying;
-   caching;
-   compression tradeoffs;
-   concurrency and parallelism where justified;
-   I/O-bound versus CPU-bound work.

### CS Lens --- Where Time and Memory Go

Learn to ask:

-   Is this CPU-bound?
-   memory-bound?
-   disk-I/O-bound?
-   network-I/O-bound?
-   algorithmically inefficient?
-   repeatedly allocating?
-   copying unnecessary data?
-   reading unnecessary chunks?

### Benchmark Suite

Potential measurements include:

-   file size;
-   write speed;
-   sequential read speed;
-   random chunk read speed;
-   bounding-box query speed;
-   chunks read;
-   bytes read;
-   compression ratio;
-   CPU utilization;
-   memory utilization.

Where useful, compare:

``` text
existing spatial format / tool
          vs
custom .spat implementation
```

The goal is explanation, not victory.

### Future Edge Connection

Introduce the idea that the same constraints---memory, CPU, storage,
bandwidth, latency---will become explicit in the next course when Rust
code runs as simulated constrained edge nodes.

The distributed-systems curriculum owns that deeper treatment.

------------------------------------------------------------------------

## Unit 12 --- Rust ↔ Python and the Systems Boundary

### Core Topics

-   PyO3;
-   maturin;
-   Python bindings;
-   input/output conversion;
-   exception mapping;
-   packaging;
-   API boundaries;
-   integration testing;
-   copying across language boundaries.

### Known → Unknown

Use a layered model:

``` text
Python
scientific workflows / orchestration / API
        │
        ▼
Rust
binary spatial I/O / indexed reads / hot-path compute
        │
        ▼
spatial storage
```

### CS Lens --- System Boundaries and Interoperability

Explore:

-   FFI;
-   ownership across boundaries;
-   buffer transfer;
-   copying;
-   serialization;
-   API stability;
-   separation of concerns.

### Spatial Application

Expose useful Rust functionality to Python, for example:

``` python
from spat import SpatialRaster

ds = SpatialRaster.open("weather.spat")
window = ds.read_bbox(minx, miny, maxx, maxy)
```

The exact public API should emerge from the implementation.

### Checkpoint 4 --- Rust Systems Layer v1

The course concludes with a portfolio-grade Rust subsystem that can:

-   read and write the custom spatial format;
-   perform chunk-aware spatial reads;
-   expose a clean Rust API;
-   expose useful functionality to Python;
-   benchmark its behavior;
-   document its format and architecture;
-   explain its limitations;
-   serve as a credible foundation for later edge-node work.

------------------------------------------------------------------------

# 8. Capstone Definition

## Working Capstone

**A Rust-native, chunked, spatially indexed binary raster format and
processing library designed as the high-performance systems layer of the
eventual Spatial Edge Platform.**

A concise project description:

> **A small, Rust-native, chunked, spatially indexed binary raster
> format designed to explore efficient local spatial data access, data
> movement, and systems-level geospatial computation, with Python
> interoperability and a path toward later edge/cloud use.**

The format may use the working extension:

``` text
.spat
```

The name is provisional.

------------------------------------------------------------------------

## 8.1 What the Capstone Is For

The capstone is a learning vehicle for:

-   Rust;
-   memory;
-   binary representation;
-   serialization;
-   offsets;
-   chunking;
-   indexing;
-   spatial extents;
-   compression;
-   I/O locality;
-   caching;
-   benchmarking;
-   Python interoperability;
-   data contracts;
-   systems design.

It is **not** initially intended to replace GeoTIFF, Zarr, GeoParquet,
or other mature formats.

Recreating a small subset of their design problems is valuable precisely
because it exposes the engineering problems those systems solve.

------------------------------------------------------------------------

## 8.2 Deliberate Scope

Initial support should remain narrow:

-   raster only;
-   one simple numeric dtype initially;
-   local files first;
-   explicit metadata;
-   chunked storage;
-   spatial bounding-box reads;
-   one reader;
-   one writer;
-   tests;
-   benchmarks.

Potential later extensions:

-   compression;
-   cloud/object-storage range reads;
-   additional dtypes;
-   richer CRS metadata;
-   alternative indexes;
-   vector sibling format;
-   point-cloud chunks.

These are not required for course completion.

------------------------------------------------------------------------

## 8.3 Relationship to the Future Edge Platform

The capstone should be designed so it can later become useful in the
distributed weather-station system.

A future architecture may resemble:

``` text
simulated sensor observations
          │
          ▼
     Rust edge node
          │
     local processing
          │
          ├── validation
          ├── aggregation
          ├── spatial chunking
          ├── compression
          └── local persistence
          │
          ▼
     Rust systems layer
      (.spat / buffers)
          │
          ▼
        network
          │
          ▼
Python control plane
          │
          ▼
PostGIS / analytics / ML
```

The Rust course should prepare components for this architecture without
prematurely teaching the entire distributed system.

------------------------------------------------------------------------

# 9. Portfolio Repository Standard

A likely structure may evolve toward:

``` text
spat/
├── Cargo.toml
├── pyproject.toml
├── README.md
├── LICENSE
├── docs/
│   ├── format-spec.md
│   ├── architecture.md
│   └── decisions/
├── src/
│   ├── lib.rs
│   ├── header.rs
│   ├── metadata.rs
│   ├── chunk.rs
│   ├── index.rs
│   ├── reader.rs
│   ├── writer.rs
│   ├── errors.rs
│   └── python.rs
├── tests/
├── benches/
├── examples/
├── python/
└── .github/
    └── workflows/
```

The exact structure should emerge naturally rather than being imposed
prematurely.

The repository should eventually include:

-   tests;
-   formatting;
-   linting;
-   documentation;
-   explicit errors;
-   benchmarks;
-   reproducible examples;
-   CI;
-   a professional README;
-   a file-format specification;
-   architecture diagrams;
-   design/architecture decisions;
-   performance investigations.

------------------------------------------------------------------------

# 10. Capstone Narrative

A reviewer should be able to follow this story:

### The Problem

Spatial data can be large, and users often need only a small spatial
subset.

### The Naïve Design

Store the raster contiguously and read more data than necessary.

### The Systems Question

How should bytes be organized so useful spatial queries require less
I/O?

### The Design

Chunk the raster, index chunk offsets and spatial extents, and retrieve
only relevant chunks.

### The CS

Explain offsets, locality, indexing, complexity, caching, and memory
behavior.

### The GIS

Explain raster extents, bounding boxes, CRS assumptions, and spatial
query semantics.

### The Rust

Explain ownership, borrowing, typed errors, reader/writer APIs, memory
safety, and efficient buffers.

### The Measurement

Benchmark file size, reads, writes, spatial subset access, memory, and
CPU.

### The Comparison

Explain how the experiment relates to ideas in GeoTIFF, Zarr,
Parquet/GeoParquet, Arrow/GeoArrow, and object-storage-oriented designs.

### The System Boundary

Expose the useful Rust functionality to Python rather than rewriting the
scientific ecosystem.

### The Future

Show how the same Rust layer can later participate in constrained edge
nodes and distributed spatial processing.

------------------------------------------------------------------------

# 11. Checkpoint Progression

``` text
CHECKPOINT 1
Rust foundations + typed spatial models
        │
        ▼
CHECKPOINT 2
first binary .spat reader/writer
        │
        ▼
CHECKPOINT 3
chunked + spatially indexed .spat
        │
        ▼
CHECKPOINT 4
benchmarked + Python-accessible Rust systems layer
        │
        ▼
NEXT COURSE
Spatial Systems & Distributed Computing
        │
        ▼
Rust layer becomes part of simulated edge nodes
```

Each checkpoint survives into the next.

------------------------------------------------------------------------

# 12. Interview Readiness

By the end of the course, the student should be able to discuss:

-   Why Rust?
-   What problem does ownership solve?
-   What is borrowing?
-   Stack versus heap?
-   What are `Option` and `Result`?
-   Why prefer a loud failure to plausible corrupt output?
-   What is serialization?
-   What is endianness?
-   What is a byte offset?
-   Why chunk a large spatial dataset?
-   How does chunk size affect I/O?
-   What is spatial indexing?
-   How does an R-tree differ conceptually from scanning every extent?
-   Why does memory layout matter?
-   What is columnar storage?
-   What are Arrow and GeoArrow trying to accomplish?
-   What is zero-copy interchange?
-   When would PostGIS or DuckDB be preferable to custom Rust?
-   What did profiling reveal?
-   Which optimization mattered most?
-   Which optimization did not matter?
-   Where does the Python/Rust boundary sit?
-   Where are copies occurring?
-   How would object-storage range reads change the design?
-   How might this component operate on a constrained edge node?
-   What would need to change for much larger rasters or many concurrent
    users?

Answers should come from building and measuring the system rather than
memorization.

------------------------------------------------------------------------

# 13. IDE and Tooling Milestones

The course remains primarily ChatGPT-guided, but the repository is a
real software artifact from the beginning.

## Early Course

Use ChatGPT for:

-   instruction;
-   examples;
-   exercises;
-   conceptual debugging;
-   quizzes;
-   code review.

Use the IDE for:

-   Rust installation;
-   Cargo;
-   compilation;
-   project files;
-   Git;
-   tests.

## Middle Course

The IDE becomes essential for:

-   binary files;
-   hexdumps/debugging;
-   multi-module code;
-   fixtures;
-   integration tests;
-   benchmarks;
-   real raster data.

## Late Course

The repository becomes the primary artifact.

ChatGPT serves as:

-   instructor;
-   reviewer;
-   debugging partner;
-   systems-design critic;
-   benchmark reviewer;
-   interviewer;
-   documentation reviewer.

The student remains the author and should understand all portfolio code.

------------------------------------------------------------------------

# 14. Assessment Model

There are no conventional exams.

Progress is assessed through:

### Exercise Mastery

Can the student solve small Rust problems without immediately receiving
the answer?

### Explanation

Can the student explain why the code works and what happens in memory or
on disk?

### Transfer

Can the student apply a concept to a new spatial/systems problem?

### Debugging

Can the student interpret compiler errors, test failures, and
corrupt-data cases?

### Systems Reasoning

Can the student reason about bytes, I/O, memory, indexing, and data
movement?

### Design Judgment

Can the student choose appropriately among Rust, Python, SQL, DuckDB,
PostGIS, and existing spatial formats/libraries?

### Measurement

Can the student design a benchmark and avoid unsupported performance
claims?

### Checkpoint Quality

Does each checkpoint improve correctness, clarity, architecture,
testing, geospatial sophistication, and system usefulness?

------------------------------------------------------------------------

# 15. Course Non-Goals

This course does **not** attempt to:

-   cover every Rust feature;
-   make the student an expert systems programmer;
-   teach advanced lifetime syntax without practical need;
-   recreate a computer-science degree;
-   replace Python with Rust;
-   replace PostGIS or DuckDB with Rust;
-   replace GeoTIFF, Zarr, GeoParquet, or Arrow;
-   build a production geospatial file standard;
-   support raster and vector equally in the first format;
-   implement every spatial algorithm from scratch;
-   teach the entire distributed-systems curriculum early;
-   add networking, cloud infrastructure, or orchestration before the
    project requires them;
-   optimize code before measuring it;
-   create numerous disconnected portfolio repositories.

Depth follows professional usefulness.

------------------------------------------------------------------------

# 16. Technology Selection Rule

Distinguish:

``` text
FOUNDATIONAL
durable concepts
```

from:

``` text
CURRENT INDUSTRY SIGNAL
important in the present ecosystem
```

from:

``` text
EXPERIMENTAL / FRONTIER
worth understanding, not automatically adopting
```

Examples of foundational concepts:

-   ownership and memory;
-   data structures;
-   algorithmic complexity;
-   binary representation;
-   spatial indexing;
-   I/O;
-   serialization;
-   chunking;
-   concurrency;
-   benchmarking.

Examples of current industry signals:

-   Rust;
-   DuckDB;
-   Arrow / GeoArrow;
-   GeoParquet;
-   Zarr / GeoZarr;
-   file-based spatial indexing;
-   high-performance multi-language spatial infrastructure.

Specific crates and platforms may change. The underlying engineering
concepts should remain useful.

------------------------------------------------------------------------

# 17. Industry Connection Protocol

Relevant lessons may consult current signals from:

-   the supplied Paces Geospatial Systems role;
-   the supplied Radar Maps/backend role;
-   other contemporary spatial systems positions;
-   Matt Forrest's writing, books, teaching, and community guidance;
-   GeoRust;
-   PostGIS;
-   DuckDB;
-   Arrow / GeoArrow;
-   cloud-native geospatial projects and standards;
-   organizations operating large spatial systems.

The purpose is not endless technology research.

The recurring question is:

> **Are we still learning toward where modern spatial systems
> engineering is going?**

Major curriculum changes should require more than one fashionable
announcement.

------------------------------------------------------------------------

# 18. Course Freshness

This syllabus reflects the program strategy and geospatial engineering
environment of **September 2026**.

The foundational Rust and CS material should remain relatively stable.

Industry Connections, crate choices, storage libraries, and
interoperability tooling may evolve.

When returning after a long pause, conduct a short **Industry Refresh**
only when current tooling materially affects the next lesson.

------------------------------------------------------------------------

# 19. Unit Completion Records

At the end of each unit, ChatGPT should produce a concise **Unit
Completion Record** containing:

-   Rust concepts learned;
-   CS Lens covered;
-   exercises completed;
-   portfolio changes;
-   tests/benchmarks added;
-   Industry Connection covered;
-   unresolved questions;
-   recommended next unit.

This makes the course resilient to pauses.

------------------------------------------------------------------------

# 20. Definition of Course Completion

The course is complete when the student can:

1.  read and write practical Rust without treating the syntax as
    foreign;
2.  explain ownership, borrowing, `Option`, `Result`, traits, iterators,
    and core Rust idioms;
3.  reason about stack/heap behavior, buffers, allocations, and copying
    at a useful level;
4.  explain binary representation, serialization, offsets, and random
    access;
5.  use Big-O reasoning on practical spatial problems;
6.  explain chunking and I/O locality;
7.  explain how spatial indexing changes search and data access;
8.  work with relevant Rust geospatial libraries;
9.  understand the role of Arrow/GeoArrow, GeoParquet, DuckDB, and
    Zarr-like systems;
10. benchmark and profile Rust spatial code;
11. distinguish algorithmic, memory, and I/O improvements from
    language-level performance claims;
12. expose Rust functionality to Python;
13. maintain a tested, documented Rust systems project;
14. explain why responsibilities were left to Python, SQL, DuckDB,
    PostGIS, or mature formats;
15. describe how the Rust subsystem could become part of a constrained
    edge node; and
16. confidently demonstrate and discuss the project with another
    engineer.

The ultimate test is not:

> **"Do I know Rust?"**

It is:

> **"Can I use Rust, computer-science fundamentals, and geospatial
> systems thinking to build and measure a real spatial systems
> component---and explain why I designed it the way I did?"**

------------------------------------------------------------------------

# 21. Course Progression

``` text
                 RUST FOR GEOSPATIAL SYSTEMS v0.2

PHASE I                     PHASE II
Think in Rust               Build Robust Software

1. Rust Foundations         4. Errors & Correctness
2. Data Has Shape           5. Collections & Pipelines
3. Ownership                6. Traits & Architecture
       │                           │
       ▼                           ▼
 CHECKPOINT 1                 CHECKPOINT 2
 typed spatial models         basic binary .spat
              \                 /
               \               /
                ▼             ▼
                    PHASE III
          Spatial Storage + Computation

          7. Binary I/O + Chunking
          8. Geometry + Spatial Queries
          9. Spatial Indexing
         10. Modern Spatial Data Systems
                    │
                    ▼
               CHECKPOINT 3
          chunked + indexed .spat
                    │
                    ▼
                    PHASE IV
         Performance + Interoperability

             11. Performance
             12. Rust ↔ Python
                    │
                    ▼
               CHECKPOINT 4
         Rust Systems Layer v1
                    │
                    ▼
              NEXT CURRICULUM
      Spatial Systems & Distributed Computing
                    │
                    ▼
       simulated constrained edge nodes
                    │
                    ▼
       eventual Spatial Edge Platform
```

------------------------------------------------------------------------

## Status

**Syllabus v0.2**

This revision preserves the pedagogical foundation of v0.1 while
changing the destination: Rust is no longer an isolated portfolio
exercise. It becomes the first high-performance systems layer of the
broader Spatial Systems Engineering program.

The custom `.spat` format is intentionally a learning vehicle, not a
commitment to invent a new production geospatial standard. Its purpose
is to make memory, bytes, I/O, chunking, indexing, data movement,
performance, and interoperability concrete.

The next curriculum should be **Spatial Systems & Distributed
Computing**, using the simulated distributed weather-station / edge-node
architecture as the initial domain. Swift should be designed only after
those earlier system responsibilities are clearer.
