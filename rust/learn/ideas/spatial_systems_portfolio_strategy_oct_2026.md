# Where to Build Next: A Point-Cloud Query Engine as the Anchor Project

**Spatial Systems Engineering — portfolio strategy**  
**Date:** October 22, 2026  
**Decision status:** Recommendation for validation, not an assertion of an uncontested market gap

## Executive recommendation

**Make a narrowly scoped, benchmark-driven point-cloud query engine the primary portfolio project now.** Keep the Rust/Python/Swift Spatial Edge Platform as the larger architectural destination, and make the engine its first genuinely differentiated subsystem. Do not try to build both as independent, full-sized products at once.

The best initial claim is not “I invented SQL for point clouds.” It is: **“I investigated how to query cloud-native 3D data efficiently, implemented and measured a specific missing capability, and exposed it through interfaces useful to analysts and eventually edge nodes.”**

This is a more defensible job-market signal than another model-training demonstration, but only if the project produces convincing correctness evidence, comparisons, and technical explanations. The novelty of the idea alone is not a moat.

**Start this week with an ecosystem and benchmark investigation, while implementing the tiny `spatial-core` Rust primitive already scoped for v0.0.1.** Within roughly two weeks, select one query pattern that existing tools handle poorly. Then build the smallest end-to-end engine that answers it.

## 1. What the conference changed—and what it did not

The conference's emphasis on AI agents is a meaningful signal about *interfaces and workflows*. Agents make it easier to assemble ordinary applications and to call analytical tools. That does not make reliable storage, spatial indexing, data semantics, query planning, or physical-world validation trivial.

Two conference examples illustrate complementary infrastructure directions:

- **RaQuet** places raster tiles and associated data in Apache Parquet so SQL-oriented analytics systems can work with raster data. Its design uses QUADBIN spatial organization and can store precomputed tile statistics. The lesson is not “all spatial data belongs in Parquet”; it is that a familiar, widely supported substrate plus a useful physical layout can unlock a new workflow.
- **Portolan** is **not a new spatial file format**. It is an open publishing specification and toolkit, based on STAC and existing cloud-native formats, to make datasets discoverable, documented, validated, and usable by people, software, and agents. The lesson is that interoperability, semantics, and trustworthy access can matter more than another parser.

Together they suggest a promising design rule: **reuse accepted standards where possible; innovate in the query behavior, spatial organization, interoperability, and validation where a gap is demonstrable.**

References: https://www.raquet.io/ ; https://carto.com/blog/introducing-portolan-and-carto-sdi/ ; https://portolan-sdi.org/

## 2. What is scarce when coding becomes cheaper?

The attached *What Will Be Scarce?* conversation makes an important distinction: producing code is not the same as producing a correct, trusted, economically useful capability. Its strongest recommendations emphasize hard-to-reproduce data, verification, infrastructure, domain knowledge, and real workflow adoption.

I agree with its central direction, with one qualification: **architectural prowess is not scarce merely because an architecture diagram is elaborate.** It becomes scarce when someone can explain and test the consequences of the design under real constraints. In this project, those constraints could be point count, data layout, selectivity, memory ceilings, network latency, CRS, precision, incomplete metadata, and failure recovery.

Soft skills also matter, but not as a substitute for technical depth. A strong engineer can discover the actual user problem, communicate alternatives, ask maintainers for feedback, document a decision, and explain a failed benchmark without defensiveness. Those abilities become more visible when agents make routine implementation faster.

**A portfolio moat is therefore accumulated evidence of judgment:** a well-chosen problem, faithful baselines, rigorous tests, reproducible measurements, useful integrations, and external feedback.

## 3. Why the query engine should lead

The proposed engine sits at an unusually good intersection of your existing geospatial and Python/SQL background and the systems skills you want to develop:

| Direction | Career signal | Risk if tackled first | Recommendation |
|---|---|---|---|
| Point-cloud query engine | Rust, data layouts, indexing, query execution, performance, spatial semantics | Building a general database before proving a need | **Primary focus** |
| Full Rust/Python/Swift edge platform | Cross-language design, distributed systems, native clients | Too many subsystems; weak first demonstration | **Long-term umbrella** |
| Door/window point-cloud classification | 3D ML, feature engineering, applied CV | Data/label difficulty; model-centric demo can look generic | **Downstream workload** |
| Weather-station edge stream | Reliability, buffering, retries, telemetry | Can feel disconnected from point clouds | **Later second workload** |
| New point-cloud file format | Deep storage design | Compatibility/adoption burden before a measured advantage | **Defer** |
| Agent-facing geospatial tool | AI integration, safety, traceability | Thin agent wrapper without novel backend | **Thin interface after engine works** |

A working query engine also provides an objective basis for interviews. You can explain why a bounding-box predicate does or does not prune data, what gets loaded into memory, what the query plan does, and where the system loses against existing tools.

**Important caution:** difficulty finding an exact Rust/Apache-style project does *not* prove the space is empty. Existing point-cloud tooling, spatial databases, COPC readers, PDAL, DuckDB integrations, and Apache Arrow/DataFusion components may already cover much of the need. A serious literature review must distinguish a true missing capability from an unfamiliar product category.

## 4. The concrete problem to investigate

A useful starting question:

> **Can a Rust-based execution layer answer selective spatial and attribute queries over large point-cloud datasets without scanning or materializing irrelevant points, while exposing a familiar SQL/Python interface?**

Candidate query:

```sql
SELECT COUNT(*), AVG(z) AS mean_height
FROM points
WHERE x BETWEEN 100 AND 140
  AND y BETWEEN 250 AND 290
  AND classification = 6;
```

This is *illustrative local-coordinate SQL*, not yet a promise that the engine will implement a SQL parser or a particular classification code convention.

The critical questions are physical rather than syntactic:

1. Can the reader use chunk/hierarchy metadata to skip unrelated regions?
2. Can it avoid decoding unused attributes or chunks?
3. Can it stream filtered batches with bounded memory?
4. Can it preserve correct coordinate scale/offset, nulls, CRS assumptions, and numeric precision?
5. How does performance change with query selectivity, cold/warm cache, and remote range requests?
6. Does a mature existing tool already do this as well or better?

**Choose a query workload first, not a file format or a SQL grammar.**

## 5. A deliberately modest architecture

```text
Python notebook / CLI / future agent / future Swift UI
                       |
              typed query request
                       |
            Rust query interface
                       |
       predicate + projection planning
                       |
      chunk/hierarchy metadata pruning
                       |
      point reader -> filtered batches
                       |
            aggregate / stream
                       |
       results + provenance + metrics
```

**Rust:** reading integration, spatial predicates, bounded-memory execution, pruning, measurement, and eventually a DataFusion integration.  
**Python:** workload generation, reference results, benchmark harness, analysis, and later ML orchestration.  
**Swift:** later native visualization and query interaction, once useful outputs exist.  
**Distributed/edge:** later execute queries or reductions near a partition and transmit summaries or selected results rather than raw points.

This keeps one coherent platform story without making the first milestone dependent on Swift, networking, or ML.

### DataFusion: integration target, not a day-one requirement

Apache DataFusion is attractive for expression evaluation, SQL planning, and Arrow-native execution. But start by testing whether a narrow reader and typed query API can demonstrate useful pruning. Add DataFusion when there is a concrete reason to support its execution model. Otherwise you risk spending the first month on framework plumbing rather than spatial I/O behavior.

### Storage: prefer established formats first

Begin by evaluating **COPC/LAZ** for spatially indexed source data and **Arrow/Parquet** for analytical interchange or alternative physical layouts. A COPC hierarchy is not interchangeable with Parquet row-group statistics; the engine should measure each path's strengths rather than assume one is universally superior. Avoid designing a new `.spat` or point-cloud format (`.pcp` for point cloud parquet as an idea) until benchmarks show a missing storage capability.

## 6. The first four milestones

### Milestone 0 — Research and baseline (week 1)

Deliver `docs/research/point-cloud-query-landscape.md` and a benchmark design. Investigate PDAL, COPC readers and specification, LAS/LAZ crates, DuckDB spatial/point-cloud pathways, Apache Arrow, Parquet, DataFusion, and relevant point-cloud database products. Record exact supported queries, formats, spatial pruning, remote access, memory behavior, maintenance, and licensing. Collect two public datasets with clear licenses and one small deterministic synthetic fixture.

**Exit gate:** one specific query gap or integration pain point is documented, with a credible existing baseline. If no gap emerges, favor contributing a measured improvement to an existing project rather than inventing a redundant engine.

### Milestone 1 — Rust foundation (`v0.0.1`, week 1–2)

Finish the already-scoped `Point3D`, `BoundingBox3D`, `PointCloudSummary`, and `summarize_points(...)` with tests, empty-input semantics, documentation, `cargo fmt`, `cargo clippy`, and a code walkthrough. Follow with bounding-box filtering. This is **learning infrastructure**, not the differentiating deliverable by itself.

**Exit gate:** explain borrowing, iteration, allocation, numeric behavior, and `O(N)` complexity without relying on the coding agent.

### Milestone 2 — End-to-end selective query (weeks 2–4)

Implement a small local-data path using a mature reader, with a typed query request: bounding box + one attribute predicate + `COUNT` or `AVG(z)`. Return a deterministic result and basic execution metrics. Verify against a trusted reference implementation. Avoid general SQL parsing initially.

**Exit gate:** one reproducible real-data query, reference-matched results, bounded memory, and documented behavior for empty results, boundaries, and invalid inputs.

### Milestone 3 — Evidence and demonstration (weeks 4–6)

Add chunk/hierarchy pruning where the chosen source format supports it; measure query selectivity and bytes read. Build a Python-facing demonstration (CLI or notebook is enough). Compare with established tools using equivalent predicates and warm/cold cache conditions. Publish a short architecture note and benchmark report.

**Exit gate:** a stranger can reproduce the demo and understand exactly when the prototype wins, loses, or lacks features.

The dates are targets, not promises. **A narrow, demonstrable vertical beats a sprawling unfinished architecture.**

## 7. What to measure—and what not to claim

Record:

- Query correctness versus a trusted reference, including boundary and numeric cases.
- Wall-clock latency and throughput across small and large datasets.
- Peak resident memory and output size.
- Source bytes read and, where possible, network bytes transferred.
- Fraction of chunks pruned versus decoded.
- Selectivity, attribute projection, and local versus remote storage.
- Cold and warm cache results, repeated trials, machine specs, and tool versions.

Do not claim “faster than DuckDB/PDAL/COPC” based on mismatched tasks or one favorable example. A fair benchmark specifies equivalent semantics and acknowledges features that the prototype does not support.

A strong outcome could be **“we found no speed advantage, but identified an interoperability gap and implemented a reliable adapter”**. That is still evidence of engineering judgment.

## 8. Where the agentic angle belongs

An agent should be a **consumer of a trustworthy spatial engine**, not the main achievement.

A later read-only tool interface might expose:

```text
inspect_dataset(uri)
explain_query(query)
query_points(query, limits)
query_summary(query, limits)
```

The agent can discover schema, propose a query, inspect an explain plan, and present results. The deterministic engine must enforce query limits, read-only access, timeouts, and spatial/CRS validation; record dataset version, query parameters, and execution metrics; and reject unsupported requests. The agent should never be allowed to invent results when execution fails.

This is a meaningful bridge to the Portolan idea: **AI-ready data requires machine-readable semantics and verifiable access, not just a chat interface.** A future catalog integration could expose point-cloud assets and tested query patterns without creating a new publication standard.

## 9. How this grows into the Spatial Edge Platform

The original multi-language vision should remain intact, but sequencing matters:

```text
Rust point primitives
        -> spatial filtering
        -> indexed point-cloud reads
        -> selective query + metrics
        -> Python interface
        -> constrained edge worker
        -> remote coordinator / multiple workers
        -> point-cloud ML feature extraction
        -> Swift spatial client
        -> weather stream as second edge workload
```

A natural edge demo eventually asks two workers to process different point-cloud partitions, transmit only summaries or candidate facade features, and compare bytes transferred with centralized raw-data processing. That makes the satellite-onboard-processing analogy concrete and measurable.

Door-versus-window classification can then become a **demanding downstream use case**: query facade regions, extract candidate geometric features, classify them, and return a small set of spatially located predictions. Its value comes from the complete acquisition-to-inference-to-result system, not merely the neural network architecture.

Weather streams should later test different distributed-systems properties—ordering, retries, disconnection, backpressure, and local aggregation—using the same observability and edge-control concepts. Do not force point clouds and weather into a single artificial data model.

## 10. Reducing the risk of being scooped

You cannot reliably protect a broad idea such as “SQL for point clouds.” Someone may already be building it, and mature products may solve most of it today. Optimize for **speed to credible evidence**, not secrecy or first-mover claims.

A practical defense is to:

1. Publish an early problem statement and benchmark harness.
2. Narrow to one hard, measurable query path.
3. Ship a usable vertical before adding infrastructure layers.
4. Record design decisions and benchmark failures publicly.
5. Seek feedback from point-cloud, COPC, DataFusion, and cloud-native geospatial maintainers.
6. Contribute upstream where the missing capability fits an existing project.
7. Keep building domain-specific test data, compatibility tests, and documentation that become useful regardless of who writes the code.

A contribution merged into a widely used project may carry more hiring credibility than an isolated, ambitious repository with no users.

## 11. Differentiating yourself in interviews

Aim to demonstrate **four distinct abilities**:

**Problem selection:** “I compared existing tools and found a concrete bottleneck in selective 3D spatial querying.”

**Systems judgment:** “I chose an established storage format, explained the indexing and memory trade-offs, and avoided inventing a new format before it was justified.”

**Verification:** “I matched reference results, tested coordinate semantics, and published reproducible benchmarks—including cases where my implementation was worse.”

**Communication and collaboration:** “I documented the architecture, incorporated maintainer feedback, and can explain the implementation from storage bytes to Python result.”

These are stronger signals than a large AI-generated commit history or a long technology list. Coding agents can accelerate scaffolding, documentation, test generation, and bounded implementation tasks; **you should own the problem definition, contracts, benchmarks, and architecture decisions**.

## 12. Decision gates and fallback paths

After the first research sprint, make one of three decisions:

- **Clear missing capability:** build the focused Rust engine and benchmark it.
- **Existing tool solves the core problem but integration is poor:** build a high-quality adapter, DataFusion extension, or Python/Arrow interface; consider upstream contribution.
- **Existing tools already solve both efficiently:** pivot to a related neglected problem—correctness/conformance testing, query explainability, remote I/O cost measurement, or agent-safe spatial querying.

This is not abandoning the original project. It is ensuring the portfolio demonstrates discovery and judgment rather than attachment to an initial idea.

## 13. Immediate next actions

**Today:** create the repository issue and research note titled **“Selective point-cloud queries: existing solutions and benchmark gap.”** Write down three candidate queries and the baseline tool for each.

**Next session:** finish the minimal Rust point summary from the existing Sprint 1 specification; do not wait for the full literature review to finish.

**Within one week:** choose a licensed point-cloud dataset, run one baseline query, and capture elapsed time, peak memory, and bytes read where available.

**Within two weeks:** commit to the first narrowly defined engine vertical—or explicitly choose an upstream integration if research reveals that to be the more valuable contribution.

## Final position

**Prioritize the point-cloud query engine as the first serious systems portfolio artifact.** Use it as the nucleus of the larger Rust/Python/Swift spatial edge platform, not a competing project. Preserve the door/window classification, weather-stream, and Swift ideas as later consumers that make the engine useful in a realistic distributed setting.

The durable differentiation is not “I wrote a new format” or “I used agents.” It is **“I can identify a consequential spatial-data bottleneck, design an appropriate system, prove what it does, measure its trade-offs, and make it useful to other engineers.”**

---

## Reference starting points

- User-provided conversation: *What Will Be Scarce in an AI-Coding-Led World?* (attached RTF), especially its recommendation to benchmark a point-cloud query engine against established alternatives.
- Existing project planning: *Spatial Edge Platform — Sprint 1 / v0.0.1* and the project's point-cloud/cloud-native spatial system notes.
- RaQuet overview: https://www.raquet.io/
- Portolan and CARTO SDI explanation: https://carto.com/blog/introducing-portolan-and-carto-sdi/
- Portolan project: https://portolan-sdi.org/
- Apache DataFusion: https://datafusion.apache.org/
- COPC specification: https://copc.io/
- PDAL: https://pdal.io/
- Apache Arrow: https://arrow.apache.org/

*The project/tool list is a research starting point, not a completed competitive landscape review. Current support and performance must be verified in the proposed research sprint.*
