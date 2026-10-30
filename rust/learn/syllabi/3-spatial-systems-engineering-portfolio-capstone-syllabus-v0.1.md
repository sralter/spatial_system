# Spatial Systems Engineering Portfolio Capstone

**Syllabus Version:** 0.1  
**Course / Track:** 3 — Final Program Capstone  
**Filename:** `3-spatial-systems-engineering-portfolio-capstone-syllabus-v0.1.md`  
**Course Format:** Self-paced, ChatGPT-guided, project-based portfolio capstone  
**Expected Commitment:** Approximately 2–4 hours per unit, with additional time for bounded refactoring, reproducibility checks, demonstrations, and documentation  
**Prerequisites:** Completion of Courses 0–2C, or an equivalent working Spatial Edge Platform  
**Starting Artifact:** Spatial Edge Platform v4 — Multi-Device Apple Spatial System  
**Primary Goal:** Convert the working learning artifact into a coherent, reproducible, technically defensible, portfolio-grade engineering project  
**Course Vintage:** September 2026  

---

# 1. Course Purpose

Course 3 completes the Spatial Systems Engineering Learning Program.

The earlier courses were primarily about **building capability**:

```text
Course 0
Rust spatial computation
        ↓
Course 1
distributed spatial systems
        ↓
Course 2A
real iPhone spatial edge node
        ↓
Course 2B
3D sensing and point-cloud systems
        ↓
Course 2C
Watch + iPhone + Mac multi-device platform
```

Course 3 asks a different question:

> **How do I turn a complex system built incrementally for learning into a coherent, reproducible, technically credible engineering portfolio artifact?**

The course begins from a working but imperfect system.

It does **not** attempt to turn that system into a commercial product.

It does **not** require production-grade completeness.

It does **not** require the iPhone, Watch, or Mac applications to resemble finished consumer applications.

Instead, the target is **portfolio-grade engineering**:

> **The system should be architecturally coherent, technically defensible, reproducible, usable, and demonstrably working—but it does not need to pretend it is a commercial product.**

The student should finish with an artifact that demonstrates:

- systems thinking;
- spatial systems knowledge;
- software architecture;
- language boundaries;
- distributed-system reasoning;
- edge computing;
- real-device integration;
- 2D and 3D spatial computation;
- data modeling;
- testing;
- observability;
- performance reasoning;
- documentation;
- engineering judgment;
- the ability to explain and defend technical decisions.

The central course question is:

> **Can another engineer understand, reproduce, evaluate, and appreciate what I built—and can I explain why it works the way it does?**

---

# 2. The Final Program Arc

The full learning program is:

```text
0 — Rust for Geospatial Systems
        ↓
1 — Spatial Systems & Distributed Computing
        ↓
2A — Swift for Spatial & Edge Computing
        ↓
2B — Swift for 3D Spatial & Edge Computing
        ↓
2C — Apple Spatial Systems Capstone
        ↓
3 — Spatial Systems Engineering Portfolio Capstone
```

The conceptual progression is:

```text
learn the computation
        ↓
learn the system
        ↓
connect the nodes
        ↓
replace simulation with real hardware
        ↓
sense the physical world
        ↓
operate the heterogeneous platform
        ↓
prove and explain what was built
```

Course 3 closes the circle.

---

# 3. Starting Artifact

Course 2C ends with:

> **Spatial Edge Platform v4 — Multi-Device Apple Spatial System**

Conceptually:

```text
                     macOS Spatial Hub
                            │
                            ▼
                  Python Control Plane
                            │
             ┌──────────────┼──────────────┐
             │              │              │
          PostGIS       Rust systems     3D storage
             │              │              │
             └──────────────┼──────────────┘
                            │
           ┌────────────────┼────────────────┐
           │                │                │
     simulated Rust      Apple Watch       iPhone
         nodes              node             node
                                            │
                                      Core ML + LiDAR
```

The platform is already intended to demonstrate:

- high-performance Rust spatial computation;
- simulated distributed nodes;
- Python control-plane services;
- PostGIS;
- offline/retry behavior;
- real iPhone sensing;
- Core ML;
- LiDAR and point clouds;
- real Apple Watch sensing;
- multi-device field sessions;
- native macOS operation and diagnostics.

Course 3 does not rebuild this architecture.

It asks whether the accumulated architecture still makes sense.

---

# 4. What "Done" Means

Course 3 uses three completion gates.

## 4.1 Systems-Complete

Every major claimed system capability has a working prototype.

Examples:

```text
✓ Rust spatial compute
✓ simulated distributed nodes
✓ Python control plane
✓ PostGIS spatial persistence
✓ offline/retry behavior
✓ iPhone edge node
✓ Core ML inference
✓ LiDAR / 3D path
✓ Watch node
✓ multi-device field session
✓ Mac operator hub
✓ diagnostics / failure visibility
```

A prototype does not need exhaustive functionality.

It needs to work convincingly enough to demonstrate the concept.

## 4.2 Engineering-Complete

The artifact demonstrates that its author understands software architecture.

Examples:

```text
✓ sensible repository structure
✓ explicit component boundaries
✓ documented data contracts
✓ appropriate tests
✓ reproducible environment
✓ sensible configuration and secrets handling
✓ representative benchmarks
✓ important failure paths tested
✓ obvious dead/duplicate architecture removed
✓ important ADRs retained
✓ clear startup and run procedure
```

This is **not production certification**.

## 4.3 Portfolio-Complete

A technically competent stranger can understand what was built.

Examples:

```text
✓ excellent README
✓ architecture diagram
✓ system/data-flow diagrams
✓ concise technical case study
✓ screenshots
✓ short demo recording plan or recording
✓ reproducible demo scenario
✓ benchmark results
✓ design decisions
✓ lessons learned
✓ limitations / future work
✓ resume-ready project summary
✓ LinkedIn/project description
✓ interview walkthrough
✓ tagged release
```

When these three gates are met:

> **Stop.**

---

# 5. The Stop Condition

The stop condition is **working prototypes for the important systems**, not perfection.

The project does not need to reach the standard:

> "This must immediately look like a shipping Apple product."

The Watch app may be small.

The iPhone app may be utilitarian.

The Mac hub may look like an engineering tool.

That is acceptable.

The required standard is:

> **Usable enough to demonstrate the system and technically coherent enough to defend it.**

Potential future ideas such as:

- visionOS;
- Metal optimization;
- elaborate UI design;
- cloud-scale deployment;
- additional sensors;
- advanced fitness analytics;
- sophisticated 3D visualization;
- more ML models;
- commercial authentication;
- App Store distribution;

belong in:

```text
FUTURE_WORK.md
```

unless they are required to repair a real weakness in the artifact.

---

# 6. Governing Course Principles

## 6.1 Portfolio-Grade, Not Production-Grade

The course should demonstrate engineering competence rather than imitate the operational obligations of a commercial product.

The artifact should be:

- coherent;
- usable;
- testable;
- measurable;
- reproducible;
- understandable;
- defensible.

It need not be:

- exhaustive;
- commercially supported;
- infinitely scalable;
- perfectly polished;
- compatible with every device;
- ready for an App Store launch.

---

## 6.2 Refactor for Evidence, Not Anxiety

Refactoring is expected throughout Courses 0–2C.

Course 3 is not "the refactoring course."

It performs a final architectural audit.

Refactor when there is a concrete reason:

- duplicated responsibility;
- unclear boundary;
- fragile contract;
- untestable component;
- measurable performance problem;
- confusing repository organization;
- unnecessary coupling;
- stale/dead architecture.

Do not refactor merely because a different abstraction might be prettier.

> **A good engineer must know when not to refactor.**

---

## 6.3 Preserve the Engineering History

The system evolved through several courses.

That evolution is useful evidence.

Do not erase every historical decision in pursuit of a falsely pristine repository.

Retain useful ADRs and documentation that explain:

- what changed;
- why it changed;
- what tradeoff was made;
- what was learned.

The final artifact should feel coherent without pretending it appeared fully formed.

---

## 6.4 Every Claim Must Be Demonstrable

If the README claims:

> "The system supports offline synchronization."

There should be a reproducible demonstration.

If it claims:

> "Rust accelerates point-cloud processing."

There should be a benchmark.

If it claims:

> "The Mac hub exposes distributed failures."

There should be a failure scenario.

Portfolio claims should map to evidence.

---

## 6.5 Documentation Is Part of the System

Documentation should explain the architecture rather than merely describe folders.

Important documentation includes:

- system purpose;
- architecture;
- component responsibilities;
- contracts;
- data flow;
- setup;
- demonstration;
- benchmarks;
- failures;
- limitations;
- design decisions.

---

## 6.6 Reproducibility Beats Deployment Theater

A portfolio project does not need Kubernetes merely to look serious.

A stronger demonstration is:

```text
clone
  ↓
configure
  ↓
start dependencies
  ↓
run backend
  ↓
start simulated nodes
  ↓
launch Apple clients
  ↓
run documented scenario
```

with predictable behavior.

---

## 6.7 Performance Claims Require Measurement

Do not write:

> "Rust makes it fast."

Measure it.

Do not write:

> "Edge processing saves bandwidth."

Measure representative payloads.

Do not write:

> "The system is resilient."

Break it and show recovery.

---

## 6.8 Limitations Increase Credibility

A strong engineering artifact explicitly says what it does **not** solve.

Examples:

- local-first development environment;
- prototype authentication;
- bounded number of nodes;
- intentionally simple Mac UI;
- limited hardware testing;
- simplified operational deployment;
- non-commercial persistence assumptions.

A limitations section is not an apology.

It demonstrates engineering judgment.

---

## 6.9 The Artifact Should Tell One Story

The repository should not feel like:

```text
Rust project
Python project
Swift project
GIS project
ML project
LiDAR project
```

It should feel like:

> **one spatial systems engineering project whose components require different technologies.**

---

## 6.10 Stop Adding Technologies

Course 3 has an unusually strict technology rule:

> **A new technology must repair a concrete portfolio-blocking problem.**

"Interesting" is not sufficient.

---

# 7. Coding Agents as Engineering Tools

Coding agents may be used extensively in Course 3.

Their use should reinforce, rather than replace, the student's understanding.

By Course 3, the student should be able to give an agent bounded instructions such as:

```text
Here is the node contract.

Here is the responsibility of this component.

Here is the failure model.

Here are the performance constraints.

Here is the ADR explaining the architecture.

Implement this bounded change.

Do not move responsibility across these boundaries.

Add these tests.

Show me the resulting diff and assumptions.
```

The important skill is not manually typing every line.

The important skill is:

> **understanding the system well enough to design, decompose, direct, review, test, measure, and defend implementation work.**

---

# 8. Agent-Assisted Engineering Standard

When coding agents contribute, the student should practice:

- defining the problem before prompting;
- specifying architectural boundaries;
- supplying relevant contracts;
- limiting scope;
- reviewing diffs;
- checking new dependencies;
- checking error behavior;
- requiring tests;
- running tests independently;
- benchmarking performance-sensitive changes;
- verifying security/configuration behavior;
- rejecting unnecessary abstractions;
- verifying documentation;
- understanding generated code before accepting it.

The student remains responsible for:

- architecture;
- acceptance criteria;
- correctness;
- integration;
- testing;
- performance;
- security;
- explanation.

A useful review question is:

> **Could I explain why this generated code belongs here and what would happen if it failed?**

If not, the work is not complete.

---

# 9. Portfolio Engineering Lens

Course 3 introduces a final recurring lens:

> **What evidence would convince another engineer that this architectural claim is true?**

Examples:

| Claim | Evidence |
|---|---|
| Rust improves a spatial workload | reproducible benchmark |
| nodes survive disconnects | failure demonstration |
| Watch is constrained | sampling/resource experiment |
| system is spatial | real map/query/3D operations |
| contracts are stable | documented schemas + tests |
| Mac is an operator hub | working diagnostic scenario |
| components are decoupled | clear interfaces + failure boundaries |
| project is reproducible | clean-machine/setup procedure |
| architecture is intentional | ADRs + diagrams |
| student understands it | technical case study + walkthrough |

---

# 10. Standard Learning Loop

Each unit should follow a bounded completion cycle:

```text
inspect
   ↓
identify evidence gap
   ↓
decide whether change is necessary
   ↓
make smallest defensible change
   ↓
test
   ↓
measure where relevant
   ↓
document
   ↓
freeze
```

This differs from earlier courses.

Earlier courses often asked:

> What should we build next?

Course 3 increasingly asks:

> **What can we stop changing because it is good enough and demonstrably correct?**

---

# 11. Course Architecture

Course 3 contains **8 units across three phases**.

```text
PHASE I — AUDIT THE SYSTEM

1. Architecture and Technical-Debt Review
2. Contracts, Boundaries, and Repository Structure
        │
        ▼
CHECKPOINT 1
ARCHITECTURE FREEZE


PHASE II — PROVE THE ENGINEERING

3. Testing and Failure Reproduction
4. Performance and Benchmark Reproduction
5. Reproducibility, Configuration, Security, and Setup
        │
        ▼
CHECKPOINT 2
ENGINEERING-COMPLETE ARTIFACT


PHASE III — EXPLAIN THE SYSTEM

6. Technical Documentation and Architecture Diagrams
7. Demo, Case Study, and Portfolio Presentation
8. Interview Walkthrough, Release, and Retrospective
        │
        ▼
CHECKPOINT 3
SPATIAL EDGE PLATFORM v1.0
PORTFOLIO-COMPLETE
```

---

# PHASE I — AUDIT THE SYSTEM

# Unit 1 — Architecture and Technical-Debt Review

## Core Question

> **Does the architecture we ended up with still make sense now that the whole system exists?**

## Core Topics

- architecture inventory;
- technical-debt inventory;
- feature-freeze review;
- component responsibilities;
- coupling;
- duplication;
- stale abstractions;
- dead code;
- accidental complexity;
- language boundaries;
- service boundaries;
- data ownership;
- operational boundaries;
- refactor prioritization;
- future-work triage.

## Starting Inputs

Review:

- Course 2C feature freeze;
- existing ADRs;
- architecture documentation;
- repository tree;
- tests;
- benchmark results;
- known bugs;
- technical-debt notes;
- failure models.

## Architecture Inventory

Create a concise inventory:

```text
Component
Responsibility
Inputs
Outputs
State owned
Dependencies
Failure mode
Why this technology?
```

Cover at least:

- Rust compute;
- simulated Rust nodes;
- Python control plane;
- PostGIS;
- 3D storage;
- iPhone;
- Watch;
- Mac hub.

## Audit Questions

Ask:

- Did two components acquire the same responsibility?
- Did Python absorb work that belongs in Rust?
- Did Swift acquire backend responsibilities?
- Is PostGIS being used appropriately?
- Are 3D payloads stored appropriately?
- Are data contracts duplicated?
- Can events be traced end-to-end?
- Are there modules that no longer serve a purpose?
- Are there abstractions that only add indirection?
- Are important responsibilities impossible to test?
- Are obvious performance problems measurable?
- Does the Mac hub depend on internals rather than contracts?
- Does the Watch remain appropriately constrained?

## Technical-Debt Classification

Classify findings:

```text
BLOCKER
Prevents convincing demonstration.

IMPORTANT
Meaningfully harms architecture, correctness, or reproducibility.

DEFER
Real issue, but not required for portfolio completion.

FUTURE
Interesting improvement or feature.
```

Only `BLOCKER` and selected `IMPORTANT` items belong in Course 3.

## Agent-Assisted Exercise

Give a coding agent the architecture and ask it to identify suspicious coupling or duplication.

Treat the response as a code-review hypothesis, not truth.

Verify findings manually.

## Deliverables

- architecture inventory;
- technical-debt register;
- bounded Course 3 refactor list;
- updated `FUTURE_WORK.md`.

---

# Unit 2 — Contracts, Boundaries, and Repository Structure

## Core Question

> **Can another engineer understand where one subsystem ends and another begins?**

## Core Topics

- API contracts;
- node contracts;
- capability model;
- observation schemas;
- field-session model;
- 3D acquisition model;
- error/operational event model;
- Rust ↔ Python boundary;
- Swift ↔ backend boundary;
- Swift ↔ Rust boundary;
- persistence ownership;
- repository structure;
- package/module naming;
- configuration boundaries;
- contract versioning conceptually.

## Contract Review

At minimum inspect:

```text
node identity
node capabilities
observation
field session
synchronization
3D acquisition
3D chunk
processing job
operational event
health/read model
```

Ask:

- Is there one authoritative definition?
- Are names consistent?
- Are units explicit?
- Are timestamps explicit?
- Are IDs stable?
- Are optional values intentional?
- Can malformed data fail clearly?
- Are language-specific representations drifting?

## Boundary Review

Create or update a responsibility matrix:

| Layer | Primary responsibility |
|---|---|
| Rust | high-performance spatial/system computation |
| Python | control plane, orchestration, scientific/ML workflows |
| PostGIS | authoritative relational/spatial state |
| 3D storage | heavy spatial payloads |
| watchOS | constrained wearable node |
| iOS | rich mobile spatial/ML/3D node |
| macOS | operator experience |

## Repository Review

The repository should make these responsibilities discoverable.

Do not reorganize solely for aesthetics.

Refactor structure when it reduces confusion.

## Contract Tests

Add targeted tests where a cross-language or cross-service contract is important.

Examples:

- serialize/deserialize representative observation;
- validate node capabilities;
- round-trip acquisition metadata;
- reject invalid schema/version;
- preserve IDs/timestamps.

## Checkpoint 1 — Architecture Freeze

At this checkpoint:

- major component responsibilities are explicit;
- portfolio-blocking technical debt is identified;
- required refactors are complete or bounded;
- important contracts are stable;
- repository organization is understandable;
- unnecessary duplication is removed where justified;
- future features are deferred;
- no major architectural redesign remains planned.

The governing statement is:

> **We have corrected the architectural problems worth correcting. Now stop redesigning it.**

---

# PHASE II — PROVE THE ENGINEERING

# Unit 3 — Testing and Failure Reproduction

## Core Question

> **Can the important claims about correctness and resilience be reproduced?**

## Core Topics

- test inventory;
- unit tests;
- integration tests;
- contract tests;
- end-to-end smoke tests;
- real-device tests;
- deterministic fixtures;
- failure injection;
- regression tests;
- test scope;
- test value;
- flaky tests;
- failure documentation.

## Test Pyramid Without Dogma

The project does not need exhaustive coverage.

It needs useful coverage.

Prioritize:

```text
high-value pure logic
cross-language contracts
database behavior
sync/idempotency
spatial correctness
failure recovery
critical end-to-end paths
```

## Required Demonstrations

At minimum preserve reproducible evidence for:

- node registration;
- spatial observation ingestion;
- offline queue recovery;
- duplicate-safe synchronization;
- Rust spatial operation correctness;
- PostGIS spatial persistence/query;
- iPhone observation path;
- Watch observation path;
- 3D acquisition metadata path;
- at least one Rust/3D processing failure;
- Mac health/diagnostic display.

## Failure Matrix

Build a concise matrix:

| Failure | Expected behavior | Evidence |
|---|---|---|
| Watch disconnect | queue + stale state + recovery | test/demo |
| iPhone disconnect | local preservation + recovery | test/demo |
| control plane unavailable | clients degrade safely | demo |
| PostGIS unavailable | persistence failure explicit | integration test |
| Rust processing fails | correlated error visible | test/demo |
| malformed contract | rejected clearly | contract test |
| duplicate observation | idempotent handling | test |

## Agent-Assisted Testing

Agents may generate test scaffolding, fixtures, and candidate edge cases.

The student must verify:

- what the test actually proves;
- whether it could pass incorrectly;
- whether mocks hide the real boundary;
- whether assertions reflect the architecture.

## Deliverable

A documented command or small set of commands that runs the portfolio-relevant automated test suite.

---

# Unit 4 — Performance and Benchmark Reproduction

## Core Question

> **Can every important performance claim be supported with a repeatable measurement?**

## Core Topics

- benchmark inventory;
- benchmark harnesses;
- warmup;
- repeated measurements;
- representative inputs;
- latency;
- throughput;
- memory;
- payload size;
- network transfer;
- edge versus central processing;
- Swift versus Rust;
- indexed versus unindexed spatial queries;
- benchmark interpretation;
- avoiding misleading claims.

## Required Benchmark Families

Select representative benchmarks from earlier courses.

### Rust Spatial Compute

For example:

```text
baseline implementation
vs
Rust implementation
```

or:

```text
flat scan
vs
spatial index
```

### 3D Processing

For example:

```text
raw point cloud
vs
downsampled point cloud
```

and:

```text
Swift implementation
vs
Rust implementation
```

including interop overhead.

### Edge Data Movement

For example:

```text
raw transfer
vs
edge-processed transfer
```

### Distributed Recovery

Measure representative queue-drain/recovery time.

### Operator Experience

Measure one meaningful Mac read/load path if performance is relevant.

## Benchmark Report

For each benchmark document:

```text
question
hardware
software/version context
input
method
iterations
metric
result
interpretation
limitation
```

Avoid résumé-scale claims such as "10x faster" without context.

## Benchmark Freeze

Once the representative suite is reproducible and useful:

> stop benchmarking.

The project is not a benchmark competition.

---

# Unit 5 — Reproducibility, Configuration, Security, and Setup

## Core Question

> **Can the project be started, understood, and demonstrated without reconstructing months of hidden local-machine state?**

## Core Topics

- environment setup;
- dependency versions;
- Rust toolchain;
- Python environment;
- database setup;
- Xcode/Apple requirements;
- Docker/Compose where appropriate;
- environment variables;
- secrets;
- sample configuration;
- migrations;
- fixtures/demo data;
- startup ordering;
- teardown;
- seed scripts;
- one-command or few-command local startup;
- reproducibility;
- security review;
- privacy review.

## Reproducibility Target

A strong local flow might resemble:

```text
clone
  ↓
install documented prerequisites
  ↓
copy example configuration
  ↓
start PostGIS / storage
  ↓
run migrations
  ↓
load demo data
  ↓
start Python control plane
  ↓
start simulated Rust nodes
  ↓
launch Mac hub
  ↓
optionally connect Watch/iPhone
  ↓
run demo
```

It does not need to be literally one command.

It should be understandable and repeatable.

## Configuration Review

Verify:

- secrets are excluded from Git;
- `.env.example` or equivalent is useful;
- defaults are sensible;
- paths are not hard-coded unnecessarily;
- development configuration is documented;
- credentials do not appear in logs;
- platform-specific configuration is explicit.

## Security/Privacy Review

Focus on portfolio-relevant fundamentals:

- least-privilege permissions;
- secure token/credential storage;
- TLS assumptions;
- safe demo data;
- no real private location history committed;
- no secrets in fixtures;
- no unnecessary raw personal sensor data;
- bounded operator actions.

## Clean-Setup Exercise

Perform a clean-environment rehearsal as far as practical.

Record every undocumented assumption encountered.

Fix the important ones.

## Checkpoint 2 — Engineering-Complete Artifact

At this checkpoint:

- portfolio-relevant tests pass;
- important failure scenarios are reproducible;
- representative benchmarks run;
- performance claims are evidence-based;
- environment/configuration is documented;
- secrets are handled sensibly;
- demo data is safe;
- setup is reproducible;
- the system can be started without relying on forgotten local state.

The project is now **engineering-complete**.

---

# PHASE III — EXPLAIN THE SYSTEM

# Unit 6 — Technical Documentation and Architecture Diagrams

## Core Question

> **Can another engineer build an accurate mental model of the system before reading thousands of lines of code?**

## Core Topics

- README architecture;
- system overview;
- component responsibilities;
- architecture diagrams;
- data-flow diagrams;
- sequence diagrams;
- deployment/runtime diagrams;
- repository map;
- ADR curation;
- data contracts;
- runbook;
- benchmark documentation;
- failure documentation;
- limitations;
- future work;
- documentation hierarchy.

## Documentation Layers

A useful hierarchy may be:

```text
README
   ↓
architecture overview
   ↓
component / contract docs
   ↓
ADRs
   ↓
runbooks / benchmark details
```

The README should not contain every detail.

It should help the reader decide where to go next.

## Required Architecture Diagram

Show:

```text
Watch
iPhone
simulated Rust nodes
macOS hub
Python control plane
Rust compute
PostGIS
3D storage
```

with major communication paths.

## Required Data-Flow Diagram

Choose at least one representative flow:

### Observation

```text
Watch/iPhone
  ↓
local persistence
  ↓
sync
  ↓
control plane
  ↓
PostGIS
  ↓
Mac hub
```

### 3D Acquisition

```text
iPhone LiDAR
  ↓
point cloud
  ↓
Rust processing
  ↓
chunk/storage
  ↓
metadata sync
  ↓
central system
  ↓
Mac inspection
```

## Required Failure Diagram or Sequence

Show one failure/recovery path.

## ADR Curation

Retain decisions that explain important architecture.

Archive or remove trivial/stale ADRs only when they actively confuse the project.

## Documentation Test

Give the documentation to an imagined technically competent reader and ask:

- What is this?
- Why does it exist?
- How do I run it?
- What are the components?
- Why these languages?
- Where is authoritative state?
- What happens offline?
- Where is 3D data stored?
- How do I see it work?
- What are the limitations?

The documentation should answer those questions.

---

# Unit 7 — Demo, Case Study, and Portfolio Presentation

## Core Question

> **How do I show the system without forcing a reviewer to discover its value by reading the repository?**

## Core Topics

- demonstration design;
- deterministic demo scenario;
- sample data;
- screenshots;
- short video;
- technical case study;
- project narrative;
- benchmark presentation;
- failure demonstration;
- scope explanation;
- limitations;
- GitHub presentation;
- portfolio page;
- concise project description.

## Demo Philosophy

The demo should show architecture, not UI decoration.

A strong sequence might be:

```text
1. Start Mac hub.
2. Simulated Rust nodes appear.
3. Watch and iPhone appear.
4. Show map/state.
5. Run or replay a field session.
6. Show Watch/iPhone observations.
7. Show an iPhone 3D acquisition.
8. Show Rust processing result.
9. Disconnect/fail a component.
10. Show diagnostic state.
11. Recover.
12. Show representative benchmark.
```

The demo can use controlled/replayed data where live hardware would make presentation fragile, provided the distinction is explicit.

## Demo Data

Create a small, safe, deterministic dataset that exercises the system.

Avoid requiring a reviewer to use the student's personal location history.

## Technical Case Study

The case study should answer:

1. What problem did I set out to explore?
2. Why spatial systems engineering?
3. What architecture emerged?
4. Why Rust?
5. Why Python?
6. Why PostGIS?
7. Why Swift?
8. What does the Watch contribute?
9. What does the iPhone contribute?
10. What does the Mac contribute?
11. How does 3D fit?
12. What distributed-system problems appeared?
13. What performance tradeoffs did I measure?
14. What failed?
15. What did I change?
16. What did I deliberately not build?
17. What did I learn?

## Portfolio Claim Standard

Prefer:

> "Built a multi-device spatial edge platform combining Rust spatial compute, a Python/PostGIS control plane, Apple Watch and iPhone sensor nodes, iPhone LiDAR/3D processing, and a native macOS operator hub."

over vague language such as:

> "Created an innovative next-generation geospatial AI platform."

Technical specificity is stronger.

---

# Unit 8 — Interview Walkthrough, Release, and Retrospective

## Core Question

> **Can I explain this project at multiple levels of technical depth and then declare it finished?**

## Core Topics

- interview storytelling;
- architecture walkthrough;
- deep dives;
- tradeoffs;
- failure stories;
- benchmark stories;
- agent-assisted development explanation;
- limitations;
- future work;
- résumé translation;
- LinkedIn/project description;
- release checklist;
- version/tag;
- retrospective;
- final stop condition.

## Three-Level Explanation

Prepare:

### 30 Seconds

What is it and why does it matter?

### 3 Minutes

What are the major components and engineering problems?

### 15–30 Minutes

Architecture, contracts, distributed behavior, spatial computation, 3D, edge constraints, benchmarks, failures, and tradeoffs.

## Technical Deep Dives

Be prepared to choose several:

- Rust ownership/performance;
- spatial indexing;
- Rust ↔ Python;
- distributed synchronization;
- idempotency;
- PostGIS modeling;
- Watch constraints;
- Core Motion sensing;
- iPhone offline architecture;
- Core ML deployment;
- LiDAR/point clouds;
- Swift ↔ Rust;
- 3D chunking;
- Mac observability;
- failure recovery.

## Agent-Assisted Development Story

The student should be able to explain coding-agent use confidently:

> I used coding agents as implementation and review tools, but the architecture, contracts, acceptance criteria, testing strategy, benchmarks, and integration decisions came from the concepts I learned while building the system.

Be prepared to show how generated changes were:

- scoped;
- reviewed;
- tested;
- measured;
- rejected or revised when necessary.

## Release Checklist

Before v1.0:

- tests pass;
- demo works;
- setup instructions work;
- diagrams match architecture;
- benchmark results reproduce;
- screenshots are current;
- no secrets;
- no private demo data;
- links work;
- limitations are documented;
- future work is separated;
- license decision is explicit;
- repository default branch is clean;
- release notes summarize the artifact.

## Final Release

Create a meaningful release/tag such as:

```text
v1.0.0
```

or an intentionally chosen equivalent.

The point is psychological and technical:

> **The learning artifact now has a defined completed version.**

Further work can occur later without preventing completion.

---

# 12. Architecture Freeze Standard

Architecture Freeze does not mean the code can never change.

It means:

- no planned major component replacement;
- no new major language;
- no new infrastructure category;
- no major data-model redesign;
- no major application rewrite;
- no new feature track.

Allowed after freeze:

- bug fixes;
- testability improvements;
- small refactors;
- documentation corrections;
- benchmark fixes;
- demo reliability;
- security/configuration fixes.

Anything larger requires a clear portfolio-blocking justification.

---

# 13. Testing Standard

Course 3 does not pursue arbitrary coverage percentages.

The test suite should prioritize:

- correctness of core spatial logic;
- serialization/contracts;
- synchronization/idempotency;
- database behavior;
- failure recovery;
- cross-language boundaries;
- critical end-to-end flows.

A 100% coverage badge is not a course goal.

A smaller suite that proves important behavior is preferable.

---

# 14. Benchmark Standard

Benchmarks should be:

- representative;
- repeatable;
- documented;
- bounded;
- interpreted honestly.

Every benchmark should state:

- hardware;
- workload;
- input size;
- method;
- metric;
- result;
- limitation.

Avoid unsupported generalization.

A result on one M-series Mac is evidence about that experiment, not proof of universal superiority.

---

# 15. Documentation Standard

Minimum final documentation should include:

```text
README.md
docs/
├── architecture.md
├── setup.md
├── demo.md
├── data-contracts.md
├── failure-model.md
├── benchmarks.md
├── security-and-privacy.md
├── limitations.md
├── FUTURE_WORK.md
└── decisions/
```

Exact filenames may differ.

Documentation structure should reflect the actual project rather than satisfy a template mechanically.

---

# 16. README Standard

The README should make the project understandable quickly.

A strong structure may include:

1. project title;
2. one-paragraph description;
3. architecture diagram;
4. what the project demonstrates;
5. major components;
6. technology responsibilities;
7. quick-start/demo path;
8. screenshots;
9. representative benchmarks;
10. key engineering decisions;
11. limitations;
12. documentation links.

Avoid an enormous technology badge wall.

The story matters more than the inventory.

---

# 17. Diagram Standard

Diagrams should answer real questions.

Useful diagrams include:

## System Architecture

> What components exist?

## Runtime / Deployment

> Where do they run?

## Observation Data Flow

> How does sensor data move?

## 3D Data Flow

> How does LiDAR become a processed spatial artifact?

## Failure / Recovery Sequence

> What happens when connectivity disappears?

## Language Responsibility Diagram

> Why Rust, Python, Swift, and SQL/PostGIS?

Avoid diagrams whose only purpose is decoration.

---

# 18. Demonstration Standard

The final demo should be:

- short enough to watch;
- technically dense;
- reproducible;
- robust;
- honest about simulated versus real behavior.

A 5–10 minute demonstration is likely more useful than a long narrated tour.

The student should maintain a written demo script even if no video is published.

---

# 19. Portfolio Presentation Standard

The project should be expressible through several surfaces:

## GitHub

Technical source of truth.

## Portfolio Site

Concise narrative and visuals.

## LinkedIn

Short project description focused on capability.

## Résumé

One compact project entry or selected bullets.

## Interview

Flexible technical walkthrough.

These surfaces should tell the same underlying story at different levels of compression.

---

# 20. Resume Translation

Potential themes—not final résumé wording—include:

- architected a multi-language spatial edge platform;
- built Rust spatial/3D processing components;
- designed Python/PostGIS control and persistence layers;
- implemented distributed/offline synchronization;
- integrated Apple Watch and iPhone sensor nodes;
- deployed Core ML on-device;
- processed iPhone LiDAR/point-cloud data;
- built a native macOS operations client;
- benchmarked edge versus central computation;
- designed failure handling and observability.

Final bullets should use real measured outcomes where available.

Never invent scale.

---

# 21. Interview Readiness

The student should be able to answer:

- What problem were you trying to solve?
- Why one evolving system instead of separate projects?
- Why Rust?
- Why Python?
- Why PostGIS?
- Why Swift?
- Why use a Watch?
- What does the iPhone do that the Watch does not?
- Why is the Mac only the operator layer?
- How do nodes identify themselves?
- How do capabilities work?
- What happens offline?
- How do you prevent duplicate observations?
- How is spatial state represented?
- How do coordinate systems/frames matter?
- How is 3D data represented and stored?
- Why not put every point in PostGIS?
- What does Rust accelerate?
- How did you measure it?
- Where is the system bottleneck?
- What happens when PostGIS fails?
- What happens when Rust processing fails?
- What happens when the Watch disappears?
- How does the Mac learn that a node is stale?
- What is your most important ADR?
- What did you refactor?
- What did you deliberately not refactor?
- What would you change for production?
- What would you build next?
- How did coding agents contribute?
- How did you verify agent-generated code?
- What part taught you the most?
- What are the system's current limitations?

---

# 22. Course Non-Goals

Course 3 does **not** require:

- production certification;
- commercial deployment;
- App Store launch;
- TestFlight distribution;
- enterprise authentication;
- multi-region infrastructure;
- Kubernetes;
- Kafka;
- massive node counts;
- billions of points;
- perfect UI/UX;
- design-award visual polish;
- every possible test;
- arbitrary coverage percentages;
- exhaustive benchmarking;
- full observability infrastructure;
- every known technical-debt item;
- rewriting working components in a preferred language;
- eliminating all TODOs;
- eliminating all future work;
- new ML models;
- new 3D algorithms;
- new sensor families;
- visionOS;
- Metal specialization;
- cloud infrastructure merely for résumé value.

---

# 23. Technology Selection Rule

Course 3's rule is:

> **Do not add a new technology unless it fixes a concrete problem that prevents the artifact from meeting the Systems-Complete, Engineering-Complete, or Portfolio-Complete gates.**

Before adding anything, answer:

1. What completion gate is blocked?
2. Why can the current stack not solve it?
3. What complexity does the technology add?
4. How will it be tested?
5. How will it be documented?
6. Will a reviewer care about the solved problem?
7. Could the work instead be listed as future work?

If #7 is yes, defer it.

---

# 24. Security and Privacy Review

The final artifact may involve:

- location;
- movement;
- sensor observations;
- device identifiers;
- 3D scans;
- credentials;
- network services.

Before release verify:

- no credentials are committed;
- sample environment files contain placeholders;
- private endpoints are removed;
- logs contain no secrets;
- personal location histories are not published unintentionally;
- screenshots do not expose sensitive information;
- demo data is safe;
- device identifiers are anonymized where appropriate;
- 3D scans do not reveal private spaces unintentionally;
- permissions are explained;
- limitations are documented.

---

# 25. Reproducibility Review

A technically competent reader should be able to determine:

- prerequisites;
- supported development environment;
- how to configure the project;
- how to initialize PostGIS;
- how to run migrations;
- how to load demo data;
- how to start Python;
- how to start Rust nodes;
- how to launch the Mac app;
- what requires real Apple hardware;
- what can be simulated;
- how to run tests;
- how to run benchmarks;
- how to run the demo;
- how to clean up.

Not every reader must own the required Apple hardware to understand the system.

Provide fallback screenshots, recorded/replayed demo paths, or sample data where appropriate.

---

# 26. Portfolio Evidence Matrix

Before final release, build a table like:

| Capability | Implementation | Evidence | Documentation |
|---|---|---|---|
| Rust spatial compute | Rust module | benchmark/test | architecture + benchmarks |
| distributed nodes | Rust/Python | demo/test | architecture |
| PostGIS | database layer | integration test/query | data model |
| iPhone sensing | Swift | screenshot/demo | component docs |
| offline sync | Swift/backend | failure demo | failure model |
| Core ML | Swift/Core ML | inference demo | ML section |
| LiDAR/3D | Swift/Rust | acquisition demo | 3D docs |
| Watch node | watchOS | field session | device docs |
| Mac hub | macOS | operator demo | hub docs |
| diagnostics | multi-component | failure drill | observability docs |

This matrix prevents portfolio language from outrunning the artifact.

---

# 27. Course Completion Record

At the end of each unit, ChatGPT should produce a concise completion record containing:

- work audited;
- evidence gap identified;
- changes made;
- refactors made;
- refactors deliberately rejected;
- tests added/changed;
- benchmarks added/changed;
- documentation updated;
- agent-assisted work performed;
- agent-generated code review notes;
- remaining blockers;
- items deferred to future work;
- completion-gate status;
- recommended next unit.

---

# 28. Definition of Course Completion

Course 3 is complete when the student can:

1. inventory the major platform components and responsibilities;
2. explain why each major technology exists;
3. identify and prioritize technical debt;
4. distinguish blockers from optional improvements;
5. refactor only where justified;
6. establish an architecture freeze;
7. explain all important cross-component contracts;
8. identify authoritative state;
9. demonstrate contract validation;
10. run portfolio-relevant automated tests;
11. reproduce important failure scenarios;
12. demonstrate offline recovery;
13. demonstrate duplicate-safe synchronization;
14. demonstrate a Rust spatial workload;
15. demonstrate PostGIS spatial persistence/query;
16. demonstrate Watch ingestion;
17. demonstrate iPhone ingestion;
18. demonstrate a 3D acquisition path;
19. demonstrate Mac diagnostics;
20. reproduce representative benchmarks;
21. state benchmark hardware and workload;
22. interpret benchmarks without overclaiming;
23. demonstrate at least one edge-versus-central tradeoff;
24. reproduce the local development environment;
25. initialize the database from documented steps;
26. run migrations and demo data;
27. start the control plane;
28. start simulated nodes;
29. launch the Mac hub;
30. explain what requires physical Apple hardware;
31. demonstrate sensible secrets/configuration handling;
32. perform a security/privacy review;
33. provide safe demo data;
34. maintain an architecture overview;
35. provide useful architecture diagrams;
36. document observation data flow;
37. document 3D data flow;
38. document at least one failure/recovery flow;
39. curate important ADRs;
40. document limitations;
41. maintain future work separately;
42. provide a strong README;
43. run a bounded, reproducible demonstration;
44. explain simulated versus real components honestly;
45. provide representative screenshots;
46. prepare a technical case study;
47. explain the project in 30 seconds;
48. explain it in approximately 3 minutes;
49. conduct a deep technical walkthrough;
50. discuss major tradeoffs;
51. discuss a failure and recovery story;
52. discuss a performance story;
53. explain coding-agent use and verification;
54. translate the work into portfolio/resume language without invented scale;
55. complete a release checklist;
56. create a stable v1.0-style release/tag;
57. classify remaining ideas as future work;
58. satisfy Systems-Complete;
59. satisfy Engineering-Complete;
60. satisfy Portfolio-Complete; and
61. stop.

The ultimate test is:

> **Can another engineer understand, reproduce, evaluate, and appreciate the system—and can I explain and defend the architecture, evidence, tradeoffs, failures, and limitations without pretending the prototype is a commercial product?**

---

# 29. Final Capstone Artifact

The final artifact is:

> **Spatial Edge Platform v1.0 — Portfolio Release**

The exact version number may differ if repository history makes another version more sensible.

The release should represent:

```text
working prototypes
        +
coherent architecture
        +
tests
        +
failure evidence
        +
benchmarks
        +
reproducibility
        +
documentation
        +
demonstration
        +
technical narrative
```

It should not represent:

```text
perfect software
```

---

# 30. Final Portfolio Narrative

The full program should support a narrative like:

> I built one spatial platform from the computational core outward. I began by learning systems programming through Rust spatial computation and indexing, then connected independent nodes into a distributed Python/PostGIS platform. I replaced simulated assumptions with a real iPhone edge node, added on-device Core ML, and extended the system into LiDAR and point-cloud processing with a measured Swift/Rust compute boundary. I then added an Apple Watch as a constrained wearable sensing node and a native macOS hub for operating and diagnosing the heterogeneous platform. Finally, I audited the architecture, reproduced its tests and benchmarks, documented its failure behavior and tradeoffs, and packaged the working prototypes into a reproducible portfolio artifact.

A shorter version:

> **Built and documented a multi-device spatial edge-computing platform spanning Rust, Python, PostGIS, Swift, Apple Watch, iPhone, macOS, Core ML, and LiDAR/3D processing, with explicit system boundaries, offline synchronization, observability, failure testing, and reproducible performance benchmarks.**

The project should demonstrate the professional identity:

> **Spatial Systems Engineer**

---

# 31. Final Retrospective

The final retrospective should answer:

## Technical

- Which architecture decisions held up best?
- Which decisions changed?
- Which component became more complicated than expected?
- Where did performance matter?
- Where did it not?
- What failure was most instructive?
- What did real hardware teach that simulation did not?
- What did 3D add to the systems problem?
- What did the Watch teach about constraints?

## Engineering

- What did you refactor?
- What did you deliberately leave alone?
- Which tests created the most confidence?
- Which benchmark changed a decision?
- Which documentation exposed an architectural problem?
- Which abstraction proved unnecessary?

## Agent-Assisted Development

- Where did coding agents save time?
- Where did they propose poor abstractions?
- Which generated changes required the most review?
- How did your prompts change as your architectural understanding improved?
- What work would you now delegate confidently?
- What work would you still insist on reasoning through yourself?

## Career

- Which parts best represent Spatial Systems Engineering?
- Which parts are strongest for geospatial systems roles?
- Which are strongest for Apple Maps/spatial intelligence roles?
- Which overlap with on-device, movement, fitness, or sensor-system roles?
- Which technical deep dives are strongest in interviews?
- What would you build next if a real product requirement justified it?

---

# 32. Course Progression

```text
      SPATIAL SYSTEMS ENGINEERING
          PORTFOLIO CAPSTONE
               COURSE 3

PHASE I
AUDIT THE SYSTEM

1. Architecture + Technical Debt
2. Contracts + Boundaries + Repository
              │
              ▼
         CHECKPOINT 1
       ARCHITECTURE FREEZE
              │
              ▼
PHASE II
PROVE THE ENGINEERING

3. Testing + Failure Reproduction
4. Performance + Benchmarks
5. Reproducibility + Config + Security
              │
              ▼
         CHECKPOINT 2
     ENGINEERING-COMPLETE
              │
              ▼
PHASE III
EXPLAIN THE SYSTEM

6. Documentation + Diagrams
7. Demo + Case Study + Portfolio
8. Interview + Release + Retrospective
              │
              ▼
         CHECKPOINT 3

      SPATIAL EDGE PLATFORM
             v1.0

       PORTFOLIO-COMPLETE
```

---

# 33. The Program's Final Stop Condition

The final stop condition is deliberately modest and demanding at the same time.

It is modest because the project does not need to be a commercial product.

It is demanding because every important engineering claim should be real.

Stop when:

```text
the Rust prototype works
the distributed prototype works
the PostGIS layer works
the iPhone prototype works
the Core ML path works
the 3D/LiDAR prototype works
the Watch prototype works
the Mac hub works
the failure paths are demonstrable
the benchmarks are reproducible
the setup is understandable
the architecture is defensible
the documentation explains it
the demo shows it
you can discuss it confidently
```

Then:

```text
tag v1.0
      ↓
publish the portfolio artifact
      ↓
move future ideas to the backlog
      ↓
use what you learned
```

The standard is not:

> **"John Ternus, Craig Federighi, and Joz have got to see how cool this is right now."**

The standard is:

> **"I built working prototypes of the systems I set out to understand, I can demonstrate that they work, I can explain why I designed them this way, and another engineer can understand what I accomplished."**

That is enough.

---

# 34. Status

**Syllabus v0.1**

This course completes the initial Spatial Systems Engineering Learning Program.

The program began with a question about learning Rust for geospatial work and evolved into one integrated curriculum spanning:

- Rust;
- systems programming;
- distributed computing;
- Python;
- PostGIS;
- spatial data systems;
- Swift;
- iOS;
- watchOS;
- macOS;
- edge computing;
- Core ML;
- LiDAR;
- point clouds;
- real-device sensing;
- observability;
- performance;
- architecture;
- portfolio engineering.

Its final purpose is not to claim mastery of every one of these areas.

Its purpose is to demonstrate a durable engineering method:

```text
learn the concept
      ↓
build a small working component
      ↓
measure it
      ↓
connect it to a larger system
      ↓
experience its failures
      ↓
refine the architecture
      ↓
explain the tradeoffs
      ↓
preserve the evidence
```

The program's final portfolio artifact should show that the student can work across the spatial, systems, data, machine-learning, distributed, and native-device layers while maintaining a coherent architectural model.

The final professional direction remains:

> **Spatial Systems Engineer**
