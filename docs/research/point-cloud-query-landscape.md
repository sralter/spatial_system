# Selective point-cloud queries: landscape and baseline

Reviewed: 2026-10-30. This is a capability investigation, not a claim to have invented
SQL for point clouds. The first subsystem of the Spatial Edge Platform is a proposed
Rust/DataFusion selective-COPC integration. Sprint 1 implements research tooling;
the production Rust library remains unchanged.

## Evidence and scope

Evidence labels below mean **documented** (upstream claim), **source-inspected**
(specific implementation reviewed), **executed** (this benchmark), or **unknown**.
Tests in another repository were inspected, not independently run. Recent commits,
stars, and feature counts are not reliability evidence. Exact revisions and file
hashes are in [sources.json](../../benchmarks/pointcloud/sources.json).

| System | Relevant capability and limits | Evidence / reuse decision |
|---|---|---|
| RustGIS | Layered GIS workspace, native data/analysis crates, optional external tools. Its LiDAR importer takes an evenly spaced visualization sample and does not use the COPC index for map views; remote files download whole. Its feature model is not an Arrow point batch. | Source-inspected at `8294f56a0f8d8dd982795d03eb8e46826e372631`; not executed. Study and consider as a future consumer; do not adopt wholesale. |
| PDAL | COPC bounds selection, streaming, LAS scale/offset decoding, exact expression filters and statistics. Remote sources are documented but not exercised here. | Executed locally, version 2.10.2. Primary baseline; no decision to link PDAL into the Rust engine. |
| DuckDB–PDAL | Existing SQL interface through `PDAL_Read` and `PDAL_Pipeline`. Its pinned README describes translating filters to a PDAL expression stage; that alone does not establish COPC hierarchy or projection pushdown. | Source-inspected at `29a535197d05fb69f42da40962fa6ed5948d99ba`; signed-extension compatibility tested separately. See results below. |
| pgPointcloud | PostgreSQL schemas describe typed dimensions and scale/offset; compressed patches support filtering and statistics, with optional PostGIS indexing/intersection functions. Requires ingestion into database storage for that path. | Documented; no server deployed. Capability comparison, not a local performance competitor this sprint. |
| pasture | `BorrowedBuffer`, `BorrowedMutBuffer`, `OwningBuffer`, interleaved and columnar layouts; arbitrary attributes. Borrowed access does not imply all conversions are zero-copy. | Published 0.5.0 buffer API documented; study representation, no dependency selected. Direct COPC pruning support not established. |
| las-rs | Public decoded points versus raw integer records; inspected local clone owns packed record storage and exposes borrowed column/record accessors and owned point materialization. LAZ is feature-gated. | Local source-inspected; candidate ingestion dependency. Match the released API and reader requirements before adoption. |
| 360-geo COPC | Hierarchy/chunk reads, partial-field decoding, borrowed column access, and owned point-vector materialization. Temporal indexing is an additional feature. | Local source-inspected, not integrated. Candidate reader; `ByteSource` documents non-Send futures, which requires a DataFusion compatibility investigation. |
| PCL | Established C++ point-cloud data structures, centroid/bounds algorithms and spatial processing. | Documented reference; do not add a C++ binding simply for this workload. |
| SpatialRust | Schema-aware column buffers and a broad processing suite. | Local source-inspected; study selective modules. Breadth is not a reason to add its full workspace. |

Primary references: [RustGIS architecture](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/docs/architecture.md),
[RustGIS LiDAR source](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/data/src/lidar.rs),
[PDAL COPC reader](https://pdal.io/en/2.10.2/stages/readers.copc.html),
[DuckDB–PDAL source](https://github.com/ahuarte47/duckdb-pdal/tree/29a535197d05fb69f42da40962fa6ed5948d99ba),
[pgPointcloud schemas](https://pgpointcloud.github.io/pointcloud/concepts/schemas.html),
[patch functions](https://pgpointcloud.github.io/pointcloud/functions/patchs.html),
[PostGIS functions](https://pgpointcloud.github.io/pointcloud/functions/postgis.html),
[pasture buffers](https://docs.rs/pasture-core/0.5.0/pasture_core/containers/index.html),
[PCL](https://github.com/PointCloudLibrary/pcl).

## Operation-level reuse decisions

| Needed operation | Existing implementation / boundary | Cost, semantics and evidence | Decision / revisit |
|---|---|---|---|
| LAS/LAZ decoding | las-rs; laz; existing COPC reader | Decode scaled integer XYZ into f64; record/chunk buffers are owned. Partial-field masks and materialization have real costs. Local source inspected; MIT reader licenses must be retained if code is adapted. | Evaluate public reader APIs; do not write a parser. Check released-version compatibility and conformance first. |
| COPC hierarchy selection | Existing COPC readers and PDAL | Candidate octree overlap can include out-of-box points. No measured chunk or byte counters are available in this harness. | Reuse reader hierarchy traversal; new adapter code only for a demonstrated integration gap. |
| Exact XYZ/class predicates | DataFusion expressions; PDAL filters for baseline | Three native coordinate axes, inclusive bounds, no CRS conversion. Filters need columns even if those columns are not projected in results. | Use existing expression evaluators. A 2D geometry envelope cannot replace an exact XYZ predicate. |
| COUNT and mean Z | DataFusion aggregate operators; PDAL stats baseline | Exact row count; mean subject to rounding and CLI metadata precision. Empty count is zero; empty AVG is null. | No custom production aggregator or mandatory PointCloudSummary intermediary. |
| Coordinate transformation | RustGIS uses proj4rs/crs-definitions; other projection libraries exist | RustGIS's geometry core is 2D and uses longitude/latitude and Web Mercator conventions. Its data crate has substantial format/database dependencies. No transform is needed for native-CRS queries. | Preserve metadata and units now; evaluate the underlying projection library only when a transformation workload exists. |
| Vector geoprocessing | `rustgis-analysis` delegates operations to `geo` | Dataset/tool integration and owned feature representations; not automatically columnar or 3D. Reference tests exist but were not executed here. RustGIS Apache-2.0; inspect underlying crate licenses when selected. | Prefer direct public library APIs when a specific operation is needed. Out of Sprint 1 execution scope. |
| GeoLibre/Whitebox algorithms | Optional native subprocess / WASI runner | File-oriented inputs/outputs and process overhead; runner implementation and notices are separate from RustGIS. | Optional later processing stage, not a query-engine dependency. |
| UI and presentation | RustGIS CLI/app/command interfaces | Useful future consumer, but display sampling is analytically different from exact aggregation. | Defer integration and Swift alternatives until the engine emits useful results. |

RustGIS's [analysis manifest](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/analysis/Cargo.toml),
[geometry source](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/geom/src/lib.rs),
[data dependencies](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/data/Cargo.toml),
[GeoLibre boundary](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/crates/geolibre/src/lib.rs), and
[attribution/reference corpus](https://github.com/opengeos/RustGIS/blob/8294f56a0f8d8dd982795d03eb8e46826e372631/ATTRIBUTION.md)
support these decisions. No upstream implementation was copied into this repository.

## Query semantics and independent verification

The SQL-shaped workloads are `COUNT(*)` and `AVG(Z)` over all points, over inclusive
XYZ bounds, and over bounds plus `Classification = 6`. Class 6 means buildings in
the chosen classified Autzen asset, not a universal assumption about every dataset.
`AVG(Z)` is mean source Z, not height above ground. There is no reprojection.

The synthetic fixture has 14 points, duplicates, exact box faces, points just
outside every axis, an empty selection and an exact-point box. Scale 0.125 and
nonzero offsets are exactly representable, so hand-calculated answers are meaningful
at boundaries. Its CRS is deliberately synthetic; the small coordinates are not a
claim about a real UTM location.

An early decimal-scale pilot exposed a decoding discrepancy: PDAL uses fused
multiply/add, whereas laspy's scaled NumPy view uses separate operations. For raw
500, scale 0.01, offset -5, these produce about `1.0408340855860843e-16` and zero,
respectively. An exact zero-width Z predicate therefore differs. We retained this
as a regression test and made the independent reference explicitly decode raw
laspy/lazrs integers with the C `fma` operation. This is a declared decoded-f64
contract, not a claim of exact decimal arithmetic. Quantization, decoding arithmetic
and predicate boundaries must be tested again in the eventual Rust adapter.

Real-data reference: separate laspy/lazrs full scan, independent NumPy masks and
`math.fsum` chunk sums; no reference results are taken from PDAL statistics. The
reference retains chunk partial sums, not the entire point cloud. Counts match
exactly; means use absolute tolerance `1e-7` or relative tolerance `1e-9`, accounting
for PDAL CLI metadata's approximately ten significant digits. This does not establish
bit-identical aggregate evaluation. The reference is not a timed competitor.

Autzen contains 10,653,336 points in an 81,123,042-byte COPC file, below the 1 GB
download budget. Its compound CRS is NAD83 / Oregon GIC Lambert horizontal feet
(EPSG:2992) and NAVD88 vertical US survey feet (EPSG:6360). Preserve the distinction:
horizontal feet are not the same unit as US survey feet. Attribution and checksum
are in the [dataset manifest](../../benchmarks/pointcloud/datasets.json); the
[publisher](https://pointcloud.org/datasets/autzen/) identifies CC-BY-4.0 and the
[original dataset notes](https://github.com/PDAL/data/blob/main/autzen/README.md)
describe the acquisition and classification. A second dataset is cataloged only;
we do not infer scaling behavior from two downloaded dataset sizes.

## Execution and result evidence

See the [benchmark README](../../benchmarks/pointcloud/README.md#recorded-results--october-30-2026) for the full results table,
and [selected machine-readable evidence](../../benchmarks/pointcloud/results/2026-10-30.json).
On Apple M2/macOS, all 238 PDAL executions passed. The 23,550-point narrow box
had median full-scan/COPC times of 4.094/0.254 seconds; whole-file scans were
3.794/4.100 seconds. These are comparisons of existing PDAL reader paths, not
evidence that a new engine wins. DuckDB 1.5.6's signed extension `482655f` passed
all 17 equivalent SQL cases, including null AVG on empty input. Its binary hash,
EXPLAIN plans and separately pinned source revision are retained. Newer inspected
upstream source must not be conflated with that tested binary. The 2.0.0 extension
endpoint was unavailable for this platform; no unsigned extension was loaded.

See the [benchmark README](../../benchmarks/pointcloud/README.md) for reproduction,
environment locks, concrete query cases, preparation commands, and measured results.
The report records process wall time, macOS peak RSS, source metadata, selectivity,
machine and versions, and first-observed/warm-up/five measured runs. It includes
CLI startup, decoding, predicates, statistics and the null writer; it excludes
downloads, reference generation, and fixture conversion.

The full-scan path uses `readers.las`; the selective path uses `readers.copc` with
bounds, then the identical exact expression. Both are explicitly streaming, without
a resolution or point-count limit. LAS reader threads, COPC requests/keep-alive,
and OpenMP concurrency are set to one where exposed. OS file cache is uncontrolled,
reference preparation has already read the data, and full scans run before the
selective path. First-observed is not cold-cache evidence. No CPU isolation or
cross-machine performance claim is made.

Source bytes read and chunks decoded/pruned are unavailable. These are null, not
inferred from result selectivity or input file size. Peak RSS at one real-data size
does not prove an asymptotic memory bound. No DataFusion implementation was timed.

## DataFusion feasibility and next vertical

The public extension boundary is a table provider and a physical plan emitting
Arrow record batches. Use the released DataFusion API selected for the prototype;
pin compatible Arrow/DataFusion versions together. A generic file source may be
appropriate later; begin with one local COPC table rather than a catalog or service.

- Preserve native XYZ as f64 and classification as its validated integer type;
  retain CRS/axis units as dataset metadata. Missing fields must not become silent
  zero values. Define missing-attribute handling explicitly in the next API proposal.
- Translate a narrow, supported conjunction of coordinate comparisons into a
  conservative COPC candidate box. Keep residual predicates for `Inexact` pushdown;
  unsupported predicates remain DataFusion's responsibility. Do not claim `Exact`
  based on hierarchy overlap alone.
- Read projected columns plus all residual-filter columns. Distinguish fewer
  materialized attributes from fewer decoded LAZ layers and fewer source bytes.
- Emit bounded-size batches and bound concurrent live chunks. Honor cancellation
  and error propagation; expose counters at the reader boundary rather than guessing.
- Verify `Send` compatibility: the inspected COPC `ByteSource` deliberately returns
  non-Send futures. Establish a supported bridge or choose a compatible reader;
  do not assume it can be awaited inside DataFusion's Send execution tasks.
- Test aggregate/null behavior, exact boundaries, fma decoding, partial masks,
  unsupported filters, and projection dependencies before optimizing anything.

Reference: [DataFusion provider and filter contracts](https://datafusion.apache.org/library-user-guide/custom-table-providers.html).
Those documented interfaces are a feasibility reference, not an installed dependency.

**Recommendation:** pursue a bounded DataFusion interoperability/measurement spike
after reviewing this evidence. First prove a released reader can feed a local table
correctly; only then implement conservative pruning and counters. Existing PDAL and
DuckDB functionality means this is not yet a demonstrated missing algorithm or
performance advantage. If a maintained adapter already solves this exact path,
contribute conformance tests or instrumentation upstream instead. The next concrete
code/files/API proposal remains a user-reviewed gate under Sprint 1 §27.
