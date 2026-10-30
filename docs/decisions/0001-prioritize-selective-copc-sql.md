# ADR 0001: Prioritize selective COPC queries and explicit reuse

Date: 2026-10-30  
Status: Accepted direction; production dependency selection remains experimental

## Context

The Spatial Edge Platform remains the umbrella for Rust data processing, Python
analysis, a future Swift client, and eventual edge/distributed execution. The first
portfolio subsystem will be a Rust/DataFusion point-cloud query path. The October
strategy and scarcity notes motivate evidence of correctness, interoperability,
and measured trade-offs; they do not prove an underserved market.

SQL for point clouds already exists in pgPointcloud and DuckDB–PDAL. RustGIS also
provides substantial GIS functionality. A new parser, GIS suite, file format, or
unmeasured performance claim would not establish useful differentiation.

## Decision

Sprint 1 is a research and local-baseline sprint. Pause the originally planned
`spatial-core` implementation and retain its current source and package version.
Use less than 1 GB of point-cloud downloads, a hand-calculated synthetic fixture,
and an independently decoded real COPC dataset. Compare PDAL full scans with COPC
bounds selection using identical exact predicates and full-resolution aggregates.

Investigate a DataFusion COPC source emitting Arrow batches. Reuse DataFusion's SQL,
expression evaluation, and aggregation, and evaluate mature readers rather than
implementing LAS/LAZ decoding. Prefer library APIs over copying code; inspect
RustGIS's underlying dependencies before adopting its application-oriented model.
Use the RustGIS application and GeoLibre runner as reference or optional consumers,
not mandatory engine dependencies.

Do not assume its visualization sample is a full-resolution analytical table.
Preserve native XYZ, coordinate metadata, scale/offset, and axis units. Do not
normalize everything to longitude/latitude or treat a 2D envelope as a 3D predicate.

For a future DataFusion provider, hierarchy overlap is conservative candidate
selection. Report filter pushdown as `Inexact` unless every emitted point has been
tested against the predicate; retain residual filters and their required columns.
Never prune using an unsupported expression in a way that can remove true matches.

## Alternatives

- **Build the point-summary primitive first:** still a useful learning exercise,
  but no longer a prerequisite for validating the engine workload.
- **Adopt RustGIS wholesale:** provides many operations but introduces dataset,
  application, and coordinate conventions that are not automatically suitable for
  native-CRS point batches.
- **Convert everything to Parquet:** worth a later layout comparison, but adds
  preparation/storage costs and does not answer the direct-COPC question.
- **Extend an existing project:** preferred if the missing capability belongs in
  a reader, an existing SQL integration, or an upstream DataFusion source.

## Consequences

Python is permitted for benchmark tooling, fixture generation, and verification;
no production Python binding or platform service is introduced. PDAL's native
dependencies are baseline tooling, not a decision to link them into a Rust engine.
No engine crate, SQL parser, spatial index, UI, networking service, release tag,
automatic publication, or automatic merge is part of this sprint.

Pinned sources, dataset attribution, measured results, and limitations live in the
[query landscape](../research/point-cloud-query-landscape.md) and
[benchmark README](../../benchmarks/pointcloud/README.md). Source borrowing must
record the upstream revision, changes, and applicable notices. Independent expected
results must state which decoder and arithmetic generated them.

## Revisit gate

After the baseline, choose a bounded DataFusion interoperability prototype, an
upstream contribution, or a specifically bounded investigation. A speed advantage
is not required, and PDAL's pruning performance is not evidence that new Rust code
will outperform it. Revisit storage layout and remote range I/O only after exact
local semantics and the integration need are established.
