# Spatial Systems & Distributed Computing

**Syllabus Version:** 0.1  
**Course Format:** Self-paced, ChatGPT-guided, project-based  
**Expected Commitment:** Up to 30 minutes per session; approximately 2–3 hours per unit  
**Prerequisite Course:** *Rust for Geospatial Systems v0.2* or equivalent familiarity with the resulting Rust systems layer  
**Primary Prior Knowledge:** Python, SQL, Spatial SQL, PostGIS, general geospatial analysis, basic Rust from Course 1  
**Strategic Context:** *Spatial Systems Engineering Learning Program — Working Strategy and North Star*  
**Portfolio Domain:** Simulated distributed weather-station / spatial edge-node network  
**Course Vintage:** September 2026  

---

# 1. Course Purpose

This course teaches **spatial systems and distributed computing** by connecting previously independent computational components into a working, measurable distributed spatial platform.

The objective is not to become a specialist in every distributed-systems technology or to assemble a résumé checklist of infrastructure tools. The objective is to become sufficiently capable to:

- understand how independent processes become a system;
- reason about services, networks, messages, state, time, and failure;
- understand what changes when computation spans multiple machines or processes;
- design reliable communication between constrained edge nodes and a central platform;
- reason about synchronization, retries, duplicates, ordering, and idempotency;
- understand the implications of intermittent connectivity;
- reason about CPU, memory, storage, bandwidth, latency, and power constraints;
- decide what computation belongs at the edge and what belongs centrally;
- integrate Rust edge components with Python services and PostGIS;
- design observable systems that can be inspected when something goes wrong;
- benchmark end-to-end system behavior rather than isolated functions;
- introduce orchestration, queues, brokers, containers, or other infrastructure only when a concrete system problem justifies them;
- build a portfolio-grade distributed geospatial system incrementally;
- explain distributed-systems tradeoffs confidently in technical interviews; and
- prepare the platform for a later Swift/iPhone edge-node implementation.

The course begins from a simple observation:

> A fast program is not yet a system.

The Rust course established a high-performance computational layer. This course asks what happens when that layer must operate as one component among many.

The guiding question is:

> **How do independent spatial computing nodes communicate, coordinate, survive failure, and decide what computation and data should remain local versus move through a distributed system?**

---

# 2. Strategic Role in the Larger Program

This syllabus is Course / Track 2 of the broader **Spatial Systems Engineering** program.

The long-term professional target remains:

> **Spatial Systems Engineer**

The larger learning program combines:

- spatial computation;
- spatial data systems;
- systems programming;
- machine learning;
- edge computing;
- distributed systems;
- native Apple application development;
- performance engineering; and
- user-facing spatial software.

Course 1 gave Rust a deliberate responsibility:

```text
Python / SQL / PostGIS
experimentation, orchestration, durable spatial data
        │
        ▼
Rust systems layer
geometry / indexing / binary I/O / chunk processing
        │
        ▼
future edge-node computation
```

Course 2 turns that future edge-node idea into a working system:

```text
             SIMULATED SPATIAL EDGE NETWORK

  Rust Node A ──┐
  Rust Node B ──┤
  Rust Node C ──┤
  Rust Node D ──┼──── network ──── Python Control Plane
  Rust Node E ──┤                         │
  Rust Node F ──┤                         ▼
  Rust Node G ──┤                     PostGIS
  Rust Node H ──┘                         │
                                          ▼
                                      analytics
```

The system begins entirely on one Mac using independent processes.

That is deliberate.

A distributed-systems concept does not require multiple physical computers to become meaningful. Separate processes with independent state, communication boundaries, failures, clocks, and resource constraints are sufficient to learn the important engineering ideas.

Later courses can replace one simulated node with a real iPhone or another device without replacing the architecture.

---

# 3. Governing Course Principles

## 3.1 Depth Over Tool Accumulation

The program intentionally develops depth in a **small number of strategically important technologies**.

The core language responsibilities remain:

| Layer | Primary Technology | Purpose |
|---|---|---|
| Systems / edge | Rust | performance, memory control, reliability, concurrency |
| Scientific / ML / control plane | Python | scientific ecosystem, services, orchestration, APIs |
| Durable spatial data | PostgreSQL / PostGIS | central spatial storage and querying |
| Analytical spatial workflows | DuckDB / Arrow / Parquet where useful | analytical processing and interchange |
| Apple-native layer | Swift | future mobile edge node and native application |
| Spatial queries | SQL / Spatial SQL | durable declarative spatial computation |

The program does **not** seek breadth through additional general-purpose languages merely for exposure.

There is no curricular requirement to learn:

- Go;
- Ruby;
- C++;
- Java;
- Scala;
- Elixir;
- another backend language;

unless a future project requirement creates a compelling, specific reason.

Rust and Swift are exceptions because they have deliberate, durable architectural roles in the larger program:

```text
Python / SQL
     │
     ├── scientific + data + control plane
     │
Rust
     │
     ├── systems + performance + constrained edge
     │
Swift
     │
     └── Apple-native product + real mobile edge node
```

The governing rule is:

> **Learn technologies deeply when they own a meaningful responsibility in the system. Do not accumulate technologies for résumé breadth.**

---

## 3.2 Infrastructure Must Earn Its Place

The same principle applies to tools and platforms.

Docker, Kubernetes, MQTT, Kafka, Redis, RabbitMQ, NATS, gRPC, Dagster, Airflow, cloud services, and similar technologies are not course objectives by themselves.

The course should first expose the underlying problem.

For example:

```text
PROBLEM
many nodes repeatedly open expensive direct connections
        │
        ▼
QUESTION
does a message broker solve something real here?
        │
        ▼
EVALUATE
MQTT / NATS / other appropriate option
        │
        ▼
ADOPT OR REJECT
based on measured system needs
```

Likewise:

```text
PROBLEM
multiple services are difficult to reproduce and operate
        │
        ▼
QUESTION
would containerization materially improve the system?
        │
        ▼
evaluate Docker
```

And later:

```text
PROBLEM
many replicated services require scheduling,
health management, rollout, and discovery
        │
        ▼
QUESTION
is Kubernetes justified?
```

The answer may be **no**.

That is a valid engineering result.

The course is about learning systems judgment, not infrastructure maximalism.

---

## 3.3 Bridge from Known → Unknown

New concepts should be connected to familiar Python, SQL, PostGIS, Rust, and geospatial workflows.

| New Concept | Familiar Bridge |
|---|---|
| process | running Python script / CLI |
| service | long-running API or application component |
| socket | communication endpoint |
| HTTP request | familiar web/API call |
| message | structured record moving between components |
| serialization | converting typed state into transferable bytes |
| node | independent process/device with local state |
| local state | file, memory, local database |
| central state | PostGIS-backed authoritative store |
| retry | rerunning failed ETL work |
| idempotency | safe repeatable database upsert |
| acknowledgement | confirmation that work/data was received |
| queue | ordered work awaiting processing |
| backpressure | downstream system cannot consume work fast enough |
| heartbeat | liveness observation |
| distributed log/event | time-stamped record of system activity |
| eventual consistency | replicas become consistent after delay |
| partition | loss of communication between components |
| orchestration | scheduling/coordinating existing workflow steps |
| observability | structured logs + metrics + traces/state inspection |
| edge processing | moving computation nearer the data source |

These comparisons are conceptual bridges rather than claims that the mechanisms are identical.

---

## 3.4 One Evolving Portfolio System

Small exercises are disposable.

Major deliverables are not.

The course builds one evolving **Spatial Edge Platform**:

```text
single simulated station
        ↓
multiple independent stations
        ↓
network communication
        ↓
central ingestion service
        ↓
PostGIS persistence
        ↓
local buffering
        ↓
offline synchronization
        ↓
fault recovery
        ↓
resource constraints
        ↓
edge computation
        ↓
observability
        ↓
system benchmarking
        ↓
operational tooling
        ↓
Spatial Edge Platform v1
```

Each checkpoint should improve the same repository or coordinated workspace.

The Git history should tell the story of a system evolving from one process into a distributed platform.

---

## 3.5 Build Vertically

Prefer a tiny working end-to-end system over a large collection of disconnected concepts.

A recurring pattern should be:

```text
concept
   ↓
tiny experiment
   ↓
single-node implementation
   ↓
multi-node behavior
   ↓
failure case
   ↓
measurement
   ↓
portfolio increment
```

The system should remain runnable throughout the course.

---

## 3.6 Failure Is a First-Class Learning Tool

Distributed systems are defined as much by failure as by successful execution.

The course should deliberately simulate:

- dropped requests;
- timeouts;
- node crashes;
- duplicated messages;
- reordered messages;
- stale data;
- corrupt payloads;
- central-service outages;
- slow consumers;
- storage exhaustion;
- process restarts;
- intermittent connectivity;
- bandwidth limits;
- clock skew where practical;
- partial synchronization.

Fault injection is therefore not merely a testing technique.

It is a teaching method.

---

## 3.7 Benchmark Rather Than Assume

Claims about edge computing or distributed architecture must be measured.

Relevant dimensions include:

- end-to-end latency;
- per-message latency;
- throughput;
- CPU;
- memory;
- local storage;
- central storage;
- bytes transmitted;
- requests transmitted;
- retries;
- synchronization delay;
- duplicate rate;
- failure recovery time;
- queue depth;
- backlog age;
- dropped-data rate;
- compression ratio;
- information loss from aggregation;
- database write rate;
- system availability;
- resource utilization.

The expected conclusion is never automatically:

> "Edge is better."

Nor is it:

> "Centralized processing is simpler, therefore it is better."

The objective is to explain the tradeoff.

---

## 3.8 Spatial Meaning Must Survive the System

The system is distributed, but it remains geospatial.

Every observation should preserve spatial semantics such as:

- station identity;
- coordinate;
- CRS assumptions;
- timestamp;
- measurement type;
- observation quality;
- spatial provenance;
- processing stage;
- local-versus-central derivation.

Geospatial correctness should not disappear underneath systems engineering.

---

# 4. The Distributed Systems Lens

The student does not have a traditional computer-science degree.

Selected distributed-systems and systems concepts therefore appear as **Systems Lens** interludes when they become useful.

The guiding question is:

> **What systems concept would make a spatial engineer understand this behavior more deeply?**

Likely topics include:

- process isolation;
- operating-system scheduling;
- ports and sockets;
- TCP versus UDP conceptually;
- request/response;
- serialization;
- protocols;
- client/server architecture;
- service boundaries;
- state;
- stateless versus stateful services;
- local versus remote calls;
- latency;
- throughput;
- concurrency;
- asynchronous execution;
- timeouts;
- retries;
- exponential backoff;
- jitter;
- idempotency;
- duplicate delivery;
- ordering;
- acknowledgements;
- at-most-once / at-least-once / effectively-once behavior;
- distributed time;
- clocks and timestamps;
- eventual consistency;
- synchronization;
- partitions;
- fault tolerance;
- availability;
- backpressure;
- queues;
- flow control;
- heartbeats;
- liveness versus readiness;
- observability;
- metrics;
- structured logs;
- tracing conceptually;
- scheduling;
- orchestration;
- resource constraints;
- graceful degradation;
- edge versus central architectures.

This is not an attempt to recreate a full distributed-systems university sequence.

Topics are introduced in proportion to their usefulness for building and explaining the Spatial Edge Platform.

---

# 5. Standard Learning Loop

Each unit should be divisible into approximately 30-minute sessions.

A typical unit may contain:

### Session A — Systems Concept

Introduce the systems or distributed-computing concept.

### Session B — Known → Unknown

Connect it to Python, Rust, SQL, PostGIS, ETL, APIs, or familiar production workflows.

### Session C — Small Experiment

Observe the concept directly with the smallest practical experiment.

### Session D — Systems Lens

Explain the deeper computer-science or distributed-systems idea.

### Session E — Failure Experiment

Break the system deliberately.

### Session F — Spatial Application

Apply the idea to spatial observations or node behavior.

### Session G — Measurement

Collect metrics that reveal system behavior.

### Session H — Industry Connection

Relate the lesson to contemporary spatial systems, edge computing, or modern backend practice.

### Session I — Portfolio Increment

Integrate the lesson into the evolving Spatial Edge Platform.

Not every unit requires every session type.

---

# 6. Teaching and Feedback Method

Instruction should favor implementation, failure, inspection, and revision.

```text
teach
  ↓
small experiment
  ↓
student prediction
  ↓
run system
  ↓
observe behavior
  ↓
explain mismatch
  ↓
modify design
  ↓
inject failure
  ↓
measure
  ↓
integrate
```

Code and architecture review should distinguish:

1. **Correctness** — Does the system produce correct results?
2. **Distributed correctness** — What happens under delay, duplication, retries, restart, or partial failure?
3. **Spatial correctness** — Are coordinates, timestamps, CRS assumptions, and provenance valid?
4. **System boundaries** — Are responsibilities placed sensibly?
5. **State ownership** — Which component owns authoritative state?
6. **Failure handling** — Does failure become visible and recoverable?
7. **Idempotency** — Can operations safely be repeated?
8. **Resource behavior** — What happens under constrained CPU, memory, disk, or bandwidth?
9. **Observability** — Can another engineer understand what the system is doing?
10. **Performance** — Has latency/throughput/resource behavior been measured?
11. **Complexity discipline** — Is every infrastructure component justified?
12. **Interoperability** — Do Rust, Python, PostGIS, and future Swift boundaries remain clear?
13. **Maintainability** — Can the architecture evolve without collapsing into tightly coupled code?
14. **Production readiness** — What would still need hardening?

---

# 7. Initial Portfolio Architecture

The initial domain is a network of simulated weather stations.

Each station emits observations such as:

```text
station_id
timestamp
latitude
longitude
temperature
humidity
pressure
wind_speed
precipitation
quality_flag
```

The first architecture is intentionally simple:

```text
┌─────────────────────┐
│ Rust Weather Node A │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│                     │
│     HTTP / TCP      │
│                     │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ Python Ingestion    │
│ Service             │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│ PostgreSQL/PostGIS  │
└─────────────────────┘
```

The architecture then evolves:

```text
 Node A ──┐
 Node B ──┤
 Node C ──┤
 Node D ──┼── network ── ingestion ── persistence
 Node E ──┤                   │              │
 Node F ──┤                   │              ▼
 Node G ──┤                   │           PostGIS
 Node H ──┘                   ▼
                         control plane
```

Later:

```text
RAW SENSOR STREAM
       │
       ▼
   Rust edge node
       │
       ├── validation
       ├── quality control
       ├── aggregation
       ├── rolling statistics
       ├── anomaly screening
       ├── local spatial logic
       ├── compression
       └── local persistence
               │
               ▼
        DERIVED / GOLD DATA
               │
               ▼
             network
               │
               ▼
       Python control plane
               │
          ┌────┼────┐
          ▼    ▼    ▼
       PostGIS ML analytics
```

The initial environment remains local.

Cloud infrastructure is optional and late.

---

# 8. Course Architecture

The course contains **12 primary units across four phases**.

The progression is:

```text
PHASE I
From Programs to Systems

1. Processes, Services, and Boundaries
2. Networking, Protocols, and APIs
3. Multiple Nodes and Message Passing
        │
        ▼
CHECKPOINT 1
Connected Spatial System


PHASE II
Distributed State and Failure

4. Identity, Time, State, and Ordering
5. Delivery, Idempotency, and Synchronization
6. Failure, Retry, Offline Operation, Recovery
        │
        ▼
CHECKPOINT 2
Resilient Synchronization


PHASE III
Edge Computing and Resource Constraints

7. Constrained Nodes
8. Edge vs Central Computation
9. Spatial Persistence and Data Movement
        │
        ▼
CHECKPOINT 3
Measured Edge Architecture


PHASE IV
Operating the System

10. Concurrency, Queues, and Backpressure
11. Observability, Fault Injection, Benchmarking
12. Orchestration, Deployment, and Architecture
        │
        ▼
CHECKPOINT 4
Spatial Edge Platform v1
```

---

# PHASE I — FROM PROGRAMS TO SYSTEMS

# Unit 1 — Processes, Services, and System Boundaries

## Core Topics

- programs versus processes;
- process isolation;
- command-line programs versus long-running services;
- process lifecycle;
- environment and configuration;
- ports conceptually;
- client and server roles;
- service boundaries;
- local calls versus remote calls;
- stateful versus stateless components;
- process exit and restart.

## Known → Unknown

Compare:

```text
Python function call
        vs
request to another process
```

and:

```text
CLI script
        vs
long-running service
```

A local function call shares a process and memory space.

A remote call crosses a system boundary.

That boundary introduces:

- serialization;
- latency;
- failure;
- timeouts;
- versioning;
- independent lifecycle.

## Systems Lens — Processes and Isolation

Questions:

- What is a process?
- What resources belong to a process?
- Why can one process crash without necessarily crashing another?
- What does the operating system schedule?
- Why is an independent process already a useful approximation of an edge device?
- What changes once two components cannot share memory directly?

## Spatial Application

Create one simulated weather station process.

It generates typed observations with:

- station ID;
- timestamp;
- coordinate;
- measurement;
- quality metadata.

## Experiment

Run:

```text
station process
     │
     ▼
stdout / local file
```

Then terminate and restart it.

Observe what state disappears and what survives.

## Portfolio Increment

Create the first edge-node executable around the Rust systems work from Course 1 where practical.

The node should have:

- configuration;
- identity;
- deterministic startup;
- structured observation generation;
- clean shutdown;
- tests for core observation logic.

---

# Unit 2 — Networking, Protocols, and APIs

## Core Topics

- network interfaces conceptually;
- localhost;
- IP addresses;
- ports;
- sockets conceptually;
- TCP;
- UDP conceptually;
- HTTP;
- request/response;
- client/server;
- DNS conceptually;
- connection lifecycle;
- serialization;
- JSON;
- binary payloads conceptually;
- API contracts;
- status codes;
- timeouts.

## Known → Unknown

Connect web scraping and API experience to the underlying network model.

A familiar HTTP request:

```python
response = client.post(url, json=payload)
```

becomes:

```text
application data
      ↓
serialization
      ↓
HTTP
      ↓
TCP
      ↓
network
      ↓
server
```

## Systems Lens — Protocol Layers

Explore conceptually:

```text
application semantics
        ↓
HTTP
        ↓
transport
        ↓
network
```

The goal is understanding boundaries, not memorizing the full networking stack.

## Spatial Application

Build a minimal Python ingestion service.

A Rust node sends:

```json
{
  "station_id": "station-a",
  "timestamp": "...",
  "latitude": 40.67,
  "longitude": -73.98,
  "temperature_c": 24.3
}
```

The service validates and acknowledges the observation.

## Failure Experiment

Try:

- wrong port;
- server unavailable;
- malformed JSON;
- delayed server response;
- invalid observation schema.

Observe failure at the node.

## Portfolio Increment

The first end-to-end flow now exists:

```text
Rust station
     │
     ▼
network request
     │
     ▼
Python ingestion service
     │
     ▼
validated observation
```

No database is required yet.

---

# Unit 3 — Multiple Nodes and Message Passing

## Core Topics

- node identity;
- independent processes;
- message passing;
- request correlation;
- connection reuse conceptually;
- throughput;
- fan-in;
- multiple producers;
- central ingestion;
- service load;
- basic concurrency.

## Known → Unknown

Move from:

```text
one producer
    ↓
one consumer
```

to:

```text
many producers
      ↓
 one consumer
```

Relate to:

- many ETL inputs writing into one warehouse;
- multiple clients calling one API;
- concurrent web-scraping workers.

## Systems Lens — Shared Memory versus Message Passing

Compare:

```text
threads / shared memory
```

with:

```text
processes / explicit messages
```

Ask why distributed systems must encode state explicitly rather than passing arbitrary in-memory objects.

## Spatial Application

Launch several stations with distinct coordinates.

Example:

```text
Station A — Brooklyn
Station B — Queens
Station C — Manhattan
Station D — Bronx
Station E — Staten Island
```

Synthetic observations need not represent real weather.

Spatial placement creates a meaningful geographic network.

## Experiment

Vary:

- number of stations;
- message frequency;
- payload size.

Measure:

- total requests;
- ingest throughput;
- average latency;
- maximum latency.

## Checkpoint 1 — Connected Spatial System

The portfolio now contains:

- multiple independent Rust station processes;
- stable station identity;
- typed spatial observations;
- serialization;
- network transport;
- Python ingestion service;
- schema validation;
- basic structured logging;
- a repeatable local launcher;
- first system-level benchmark.

Architecture:

```text
Station A ──┐
Station B ──┤
Station C ──┼── HTTP ── Python Ingestion
Station D ──┤
Station E ──┘
```

The student should now understand why several correct programs do not automatically form a reliable distributed system.

---

# PHASE II — DISTRIBUTED STATE AND FAILURE

# Unit 4 — Identity, Time, State, and Ordering

## Core Topics

- identity;
- event IDs;
- sequence numbers;
- timestamps;
- wall-clock time;
- monotonic time conceptually;
- ordering;
- local state;
- central state;
- authoritative state;
- distributed state;
- stale state;
- clock skew conceptually.

## Known → Unknown

Relate database primary keys and ETL record identifiers to message identity.

Compare:

```text
observation timestamp
```

with:

```text
message ID
```

These answer different questions.

## Systems Lens — Time Is Hard

Explore:

- Two machines may disagree about clock time.
- Network arrival order may differ from generation order.
- "Latest received" may not mean "latest generated."
- Timestamps are data and require semantics.

## Spatial Application

Each observation gains:

```text
message_id
station_id
sequence_number
observed_at
sent_at
received_at
location
measurement
```

## Experiment

Introduce random network delay.

Observe:

```text
generated order
A B C D E
```

but possibly:

```text
arrival order
A C B E D
```

## Portfolio Increment

Define an explicit observation/message contract.

Document:

- identity;
- temporal fields;
- ordering assumptions;
- spatial fields;
- authoritative source for each field.

Create the first API/data-contract document.

---

# Unit 5 — Delivery, Idempotency, and Synchronization

## Core Topics

- acknowledgements;
- delivery semantics;
- duplicates;
- retry;
- idempotency;
- deduplication;
- idempotency keys;
- sequence tracking;
- upserts;
- synchronization;
- local and central copies;
- reconciliation;
- eventual consistency.

## Known → Unknown

Use familiar idempotent ETL ideas.

A database upsert already asks:

> If I receive this logical record again, what should happen?

Distributed message delivery asks the same question under network uncertainty.

## Systems Lens — Did the Server Receive It?

Consider:

```text
node sends observation
        │
        ▼
server writes observation
        │
        ▼
acknowledgement is lost
```

The node cannot distinguish:

```text
server never received it
```

from:

```text
server received it, but response was lost
```

A retry may therefore create a duplicate.

This is a foundational distributed-systems problem.

## Spatial Application

Persist observations to PostgreSQL/PostGIS.

A conceptual table:

```sql
observations
------------
message_id
station_id
observed_at
received_at
geom
temperature_c
humidity
quality_flag
processing_stage
```

Use an appropriate uniqueness contract.

## Failure Experiment

Drop acknowledgements after successful writes.

Retry.

Confirm that the database remains correct.

## Portfolio Increment

Implement:

- stable message IDs;
- retry-safe central ingestion;
- idempotent persistence;
- duplicate detection metrics;
- synchronization status.

---

# Unit 6 — Failure, Retry, Offline Operation, and Recovery

## Core Topics

- transient versus permanent failure;
- timeouts;
- retry policies;
- exponential backoff;
- jitter;
- retry budgets;
- circuit-breaker conceptually;
- offline buffering;
- store-and-forward;
- process restart;
- checkpointing;
- graceful degradation;
- recovery.

## Systems Lens — Partial Failure

In a local script:

```text
success / failure
```

can feel binary.

In a distributed system:

```text
Node A       healthy
Node B       offline
Node C       slow
Network      intermittent
API          healthy
Database     degraded
```

The system is neither fully up nor fully down.

## Spatial Application

Give each node a local durable queue or buffer.

When the central service is unavailable:

```text
sensor observation
       │
       ▼
 local persistent buffer
       │
  network unavailable
       │
       X
```

When connectivity returns:

```text
local backlog
     │
     ▼
ordered/reconciled sync
     │
     ▼
central system
```

The exact storage mechanism should remain simple initially.

## Failure Experiments

Simulate:

- 30 seconds offline;
- 5 minutes offline;
- node restart while offline;
- server restart;
- repeated timeout;
- malformed record in the middle of a backlog;
- full local storage quota.

## Checkpoint 2 — Resilient Synchronization

The system now:

- persists observations centrally in PostGIS;
- assigns stable identities;
- handles duplicate delivery;
- retries transient failures;
- buffers while offline;
- survives process restart;
- synchronizes backlog after reconnect;
- records synchronization status;
- exposes failed/permanently rejected observations;
- contains tests for important failure paths.

Architecture:

```text
Rust Node
   │
   ├── generate
   ├── validate
   ├── persist locally
   ├── transmit
   ├── retry
   └── reconcile
           │
           ▼
      Python API
           │
           ▼
        PostGIS
```

This is the first truly distributed checkpoint.

---

# PHASE III — EDGE COMPUTING AND RESOURCE CONSTRAINTS

# Unit 7 — Constrained Nodes

## Core Topics

- resource budgets;
- CPU;
- memory;
- storage;
- bandwidth;
- latency;
- request rate;
- energy/power conceptually;
- bounded buffers;
- quotas;
- load shedding conceptually;
- graceful degradation;
- constrained simulation.

## Systems Lens — Resources Are Part of the Design

Desktop development can hide assumptions:

```text
memory is abundant
disk is abundant
network is fast
power is unlimited
```

Edge systems invalidate those assumptions.

The node should be treated as if it has a budget.

## Spatial Application

Define simulated node profiles.

Example:

```text
Profile: generous
memory budget: high
storage budget: high
network: reliable

Profile: constrained
memory budget: low
storage budget: limited
network quota: limited

Profile: remote
network: intermittent
latency: high
storage: moderate
```

The values should be chosen for experimentation, not realism theater.

## Experiments

Measure behavior while restricting:

- observation buffer size;
- maximum bytes transmitted;
- processing frequency;
- local storage;
- CPU usage where practical;
- request frequency.

## Portfolio Increment

Create a resource-policy configuration for each node.

Nodes should expose their current:

- backlog;
- storage use;
- message count;
- transmitted bytes;
- dropped/rejected observations;
- processing duration.

---

# Unit 8 — Edge vs Central Computation

## Core Topics

- local computation;
- centralized computation;
- aggregation;
- compression;
- quality control;
- filtering;
- feature extraction;
- local anomaly detection;
- information loss;
- latency tradeoffs;
- bandwidth tradeoffs;
- privacy conceptually;
- hybrid architectures.

## Central Experiment

### Architecture A — Raw Transmission

```text
sensor
   │
   │ raw observation every interval
   ▼
network
   │
   ▼
central platform
   │
   ├── QC
   ├── rolling statistics
   ├── aggregation
   └── anomaly analysis
```

### Architecture B — Edge Processing

```text
sensor
   │
   ▼
Rust node
   │
   ├── validation
   ├── QC
   ├── rolling statistics
   ├── aggregation
   └── compression
   │
   │ smaller derived payload
   ▼
network
   │
   ▼
central platform
```

## Systems Lens — Moving Compute versus Moving Data

Ask:

> Is it cheaper to move the data to the computation or move the computation closer to the data?

This becomes increasingly important for:

- imagery;
- raster chunks;
- point clouds;
- mobile sensors;
- future ML inference.

## Spatial Application

Nodes may compute:

- rolling temperature average;
- daily min/max;
- anomaly flags;
- spatially tagged summaries;
- quality summaries.

Later, `.spat` or other Rust systems-layer components from Course 1 may provide local persistence or chunked data access where useful.

## Benchmark

Compare architectures using:

- bytes transmitted;
- requests transmitted;
- CPU at edge;
- CPU centrally;
- latency to useful result;
- local storage;
- central storage;
- information retained;
- ability to reprocess historically.

## Portfolio Increment

Document an ADR:

> **ADR: Which weather computations belong at the edge?**

The decision must reference measured behavior.

---

# Unit 9 — Spatial Persistence and Data Movement

## Core Topics

- local persistence;
- central persistence;
- data lifecycle;
- hot versus historical data;
- batching;
- compression;
- transfer size;
- metadata;
- spatial indexing;
- PostGIS;
- Arrow/Parquet where justified;
- local analytical querying;
- retention;
- provenance;
- data contracts.

## Known → Unknown

Connect existing experience with:

- PostGIS;
- DuckDB;
- Parquet / GeoParquet;
- Zarr;
- Rust `.spat`.

The question is no longer simply:

> What format is fast?

It becomes:

> What representation is appropriate at each boundary in the system?

## Spatial Application

Design the lifecycle:

```text
raw observation
      │
      ▼
edge-local durable state
      │
      ▼
edge-derived summary
      │
      ▼
network transfer
      │
      ▼
central ingestion
      │
      ▼
PostGIS operational store
      │
      ▼
analytical export / query
```

## Systems Lens — Data Movement Is Work

Every boundary may involve:

- serialization;
- allocation;
- copying;
- compression;
- network transfer;
- deserialization;
- validation;
- database write.

Measure rather than treating movement as free.

## Checkpoint 3 — Measured Edge Architecture

The system now demonstrates:

- resource-constrained simulated nodes;
- local persistence;
- offline synchronization;
- edge computation;
- central computation;
- configurable edge/central strategies;
- PostGIS-backed spatial persistence;
- measured bandwidth and latency;
- documented data lifecycle;
- an ADR explaining edge-versus-central placement.

A reviewer should be able to run two architectures and compare them empirically.

---

# PHASE IV — OPERATING THE DISTRIBUTED SPATIAL SYSTEM

# Unit 10 — Concurrency, Queues, and Backpressure

## Core Topics

- concurrency;
- parallelism;
- asynchronous I/O;
- producers;
- consumers;
- work queues;
- bounded queues;
- backpressure;
- buffering;
- batching;
- flow control;
- rate limiting;
- slow consumers;
- overload.

## Known → Unknown

Connect:

- Python multiprocessing;
- asynchronous API requests;
- ETL worker pools;

to distributed producer/consumer behavior.

## Systems Lens — What Happens When Production Exceeds Consumption?

If:

```text
nodes generate 1,000 observations/sec
```

and:

```text
central system consumes 500 observations/sec
```

then something must happen.

Possibilities:

- queue grows;
- latency grows;
- memory grows;
- disk grows;
- producers slow down;
- messages are dropped;
- system fails.

Backpressure is therefore architecture, not merely performance tuning.

## Experiment

Deliberately slow the ingestion path.

Observe:

- queue depth;
- backlog age;
- memory;
- latency;
- recovery after load ends.

## Tool Evaluation Gate

Only now evaluate whether the existing direct communication model creates a problem that justifies a queue or broker.

Potential evaluation candidates may include lightweight messaging systems such as MQTT or another appropriate technology.

The exercise is:

```text
1. identify pain
2. state required semantics
3. evaluate candidate
4. measure complexity added
5. adopt or reject
```

There is no requirement to adopt a broker.

## Portfolio Increment

Implement bounded work handling and explicit overload behavior.

The node and central service should fail predictably rather than growing without bound.

---

# Unit 11 — Observability, Fault Injection, and System Benchmarking

## Core Topics

- logs;
- structured logging;
- metrics;
- traces conceptually;
- correlation IDs;
- service health;
- liveness;
- readiness;
- node status;
- dashboards conceptually;
- system benchmarking;
- fault injection;
- SLO/SLA concepts at a basic level.

## Known → Unknown

Existing logging experience becomes system-wide observability.

Instead of:

```text
what happened in this script?
```

ask:

```text
what happened to message 01J... as it moved through
Node C → network → ingestion → PostGIS?
```

## Systems Lens — Observability Is Not Logging

Three useful perspectives:

```text
LOGS
what happened?

METRICS
how much / how often?

TRACES
where did time/work move through the system?
```

Full distributed tracing infrastructure is optional.

The concepts are required.

## Required Metrics

Potential metrics include:

### Node

- observations generated;
- observations buffered;
- observations transmitted;
- retries;
- failures;
- local queue depth;
- local storage used;
- bytes transmitted;
- processing latency.

### Central Service

- request count;
- validation failures;
- duplicate count;
- ingest latency;
- DB write latency;
- backlog;
- error rate.

### System

- end-to-end observation latency;
- synchronization lag;
- throughput;
- recovery time after outage;
- data-loss rate;
- bandwidth;
- availability during fault scenarios.

## Fault-Injection Suite

Create reproducible scenarios:

```text
Scenario 1 — central API unavailable
Scenario 2 — 500 ms latency
Scenario 3 — 10% request failure
Scenario 4 — duplicate delivery
Scenario 5 — node restart
Scenario 6 — constrained storage
Scenario 7 — slow central consumer
Scenario 8 — burst traffic
```

## Portfolio Increment

Create a reproducible benchmark/fault harness and produce a concise performance report.

The report should explain results rather than merely print numbers.

---

# Unit 12 — Orchestration, Deployment, and System Architecture

## Core Topics

- reproducible startup;
- configuration;
- service discovery conceptually;
- health checking;
- dependency ordering;
- orchestration;
- deployment environments;
- local development;
- packaging;
- operational runbooks;
- rolling upgrade conceptually;
- schema/API versioning;
- architecture documentation.

## Systems Lens — Orchestration Coordinates Existing Capabilities

Orchestration is useful only after multiple components exist.

The course should distinguish:

```text
application logic
```

from:

```text
coordination of application components
```

## Tool Evaluation Gate — Docker

Evaluate Docker if reproducibility has become meaningfully difficult.

Questions:

- Are multiple services difficult to start consistently?
- Are dependencies diverging?
- Would isolation improve reproducibility?
- Does containerization clarify deployment?
- What complexity does Docker add?

Adopt it only if the answer justifies it.

## Tool Evaluation Gate — Kubernetes

Kubernetes is **not a default course requirement**.

Evaluate it only if the system evolves to a point where there is a genuine need to learn about:

- replicated services;
- scheduling;
- service discovery;
- health-managed restarts;
- rollout management;
- horizontal scaling.

A small portfolio system may rationally conclude:

> Kubernetes would be excessive for this architecture.

That conclusion demonstrates sound engineering judgment.

## Tool Evaluation Gate — Workflow Orchestration

Dagster or another workflow orchestrator should be introduced only if the system accumulates true workflows such as:

```text
daily edge summary
      ↓
central spatial aggregation
      ↓
analytical export
      ↓
model inference
      ↓
report
```

Long-running request-serving infrastructure should not be forced into a workflow orchestrator simply because the tool is familiar.

## Portfolio Increment

Produce:

- architecture diagram;
- service/data contracts;
- runbook;
- fault-recovery documentation;
- benchmark summary;
- ADR index;
- reproducible local startup;
- end-to-end test;
- design document describing current limitations and future evolution.

## Checkpoint 4 — Spatial Edge Platform v1

The course concludes with a portfolio-grade distributed spatial system that can:

- run multiple independent Rust edge nodes;
- generate spatially tagged observations;
- communicate over a defined network protocol;
- ingest through a Python control-plane/API layer;
- persist durable central spatial state in PostGIS;
- maintain local node state;
- operate during intermittent connectivity;
- synchronize after reconnect;
- tolerate duplicate delivery;
- retry transient failure safely;
- expose explicit failure states;
- operate under configurable resource constraints;
- perform meaningful computation at the edge;
- compare edge and centralized architectures;
- measure latency, throughput, memory, storage, and bandwidth;
- expose system health and observability;
- reproduce fault scenarios;
- recover from common failures;
- document architectural decisions; and
- provide a stable node contract that a future Swift/iPhone implementation can adopt.

---

# 9. Capstone Definition

## Working Capstone

**A simulated distributed geospatial edge-computing platform in which resource-constrained Rust weather-station nodes perform local processing and resilient synchronization with a Python/PostGIS central system.**

A concise project description:

> **A distributed spatial sensing platform built from simulated Rust edge nodes and a Python/PostGIS control plane, designed to explore networking, synchronization, intermittent connectivity, resource constraints, fault tolerance, observability, and measured tradeoffs between edge and centralized geospatial computation.**

The weather data is intentionally simple.

The systems behavior is the real subject.

---

# 9.1 What the Capstone Is For

The capstone is a learning vehicle for:

- distributed systems;
- networking;
- processes;
- services;
- APIs;
- protocols;
- serialization;
- node identity;
- distributed state;
- ordering;
- time;
- retries;
- idempotency;
- synchronization;
- fault tolerance;
- intermittent connectivity;
- local persistence;
- edge computing;
- resource constraints;
- concurrency;
- queues;
- backpressure;
- observability;
- orchestration;
- performance measurement;
- spatial data architecture;
- Rust/Python integration;
- PostGIS-backed central data;
- architecture documentation.

It is not intended to become a production weather company.

---

# 9.2 Deliberate Scope

Required:

- simulated nodes on one Mac;
- Rust edge agents;
- Python central service;
- PostGIS;
- network communication;
- local persistence;
- offline operation;
- retry-safe synchronization;
- resource constraints;
- edge-processing experiment;
- system metrics;
- fault injection;
- documentation.

Optional:

- Docker;
- MQTT or another broker;
- cloud deployment;
- object storage;
- analytical exports;
- `.spat` integration;
- lightweight model inference;
- workflow orchestration.

Not required:

- Kubernetes;
- Kafka;
- multi-cloud deployment;
- service mesh;
- production-scale telemetry stack;
- complex infrastructure-as-code;
- additional general-purpose programming languages.

---

# 9.3 The Core Capstone Experiment

The course should culminate in a controlled comparison.

## Architecture A — Centralized

```text
8 simulated stations
        │
        │ raw observations
        ▼
     network
        │
        ▼
 Python service
        │
        ├── validation
        ├── QC
        ├── aggregation
        ├── rolling stats
        └── persistence
```

## Architecture B — Edge-Heavy

```text
8 simulated stations
        │
        ▼
  Rust edge nodes
        │
        ├── validation
        ├── QC
        ├── aggregation
        ├── rolling stats
        ├── compression
        └── local buffering
        │
        │ derived observations
        ▼
      network
        │
        ▼
 Python service
        │
        ▼
      PostGIS
```

Compare:

- bytes transmitted;
- message count;
- edge CPU;
- central CPU;
- edge memory;
- local storage;
- central storage;
- end-to-end latency;
- synchronization delay;
- robustness during outage;
- reprocessing flexibility;
- information loss.

The capstone conclusion should answer:

> **For this workload, under these constraints, which computations belong at the edge, which belong centrally, and why?**

---

# 10. Relationship to the Rust Course

Course 1 ends with:

```text
Rust Systems Layer v1
        │
        ├── binary I/O
        ├── chunk-aware reads
        ├── spatial computation
        ├── performance measurement
        └── Python interoperability
```

Course 2 uses Rust differently.

The important Rust learning is no longer syntax.

Rust becomes an implementation language for the node:

```text
Rust edge agent
    │
    ├── observation model
    ├── local validation
    ├── local storage
    ├── local computation
    ├── network client
    ├── retry logic
    ├── synchronization
    ├── resource monitoring
    └── future .spat integration
```

Rust concepts may be reviewed as required, but the distributed-systems curriculum owns the architecture.

---

# 11. Relationship to Python and PostGIS

Python remains the primary control-plane and scientific environment.

Possible responsibilities:

```text
Python
│
├── API / ingestion
├── control plane
├── system administration
├── analytics
├── experimentation
├── ML
├── integration tests
└── benchmark analysis
```

PostGIS remains the durable central spatial system:

```text
PostGIS
│
├── station registry
├── observation history
├── spatial queries
├── central authoritative state
├── spatial aggregation
└── downstream analytics
```

The course should reinforce an important architectural principle:

> **Distributed systems engineering does not mean rewriting established strengths in Rust.**

Use Rust where its systems role is meaningful.

Use Python, SQL, and PostGIS where they remain the better primitives.

---

# 12. Relationship to the Future Swift Course

This course should create an explicit node contract that the later Swift curriculum can adopt.

At Course 2 completion:

```text
Central Platform
      ▲
      │
 ┌────┼────┬────┐
 │    │    │    │
Rust Rust Rust Rust
Node Node Node Node
```

The Swift course can eventually evolve this into:

```text
Central Platform
      ▲
      │
 ┌────┼────┬─────────┐
 │    │    │         │
Rust Rust Rust     iPhone
Node Node Node     Swift Node
```

The iPhone should then learn to:

- identify itself;
- collect real sensor/location data;
- persist locally;
- operate offline;
- synchronize;
- obey the same data contract;
- participate in the same observability model;
- perform local spatial computation;
- eventually perform on-device ML;
- operate under real latency, memory, battery, and connectivity constraints.

The Swift course should therefore begin from a working systems specification rather than a blank mobile application.

---

# 13. Portfolio Repository Standard

A likely repository may eventually evolve toward:

```text
spatial-edge-platform/
├── README.md
├── Cargo.toml
├── pyproject.toml
├── docker-compose.yml          # only if justified
│
├── edge/
│   ├── src/
│   │   ├── main.rs
│   │   ├── observation.rs
│   │   ├── storage.rs
│   │   ├── sync.rs
│   │   ├── network.rs
│   │   ├── processing.rs
│   │   ├── metrics.rs
│   │   └── config.rs
│   └── tests/
│
├── control_plane/
│   ├── app/
│   │   ├── api.py
│   │   ├── models.py
│   │   ├── persistence.py
│   │   ├── services.py
│   │   └── metrics.py
│   └── tests/
│
├── db/
│   ├── migrations/
│   └── schema/
│
├── simulation/
│   ├── stations/
│   ├── scenarios/
│   └── fault_injection/
│
├── benchmarks/
│   ├── scenarios/
│   ├── results/
│   └── analysis/
│
├── docs/
│   ├── architecture.md
│   ├── data-contract.md
│   ├── synchronization.md
│   ├── failure-model.md
│   ├── observability.md
│   ├── runbook.md
│   └── decisions/
│       ├── 0001-transport.md
│       ├── 0002-state-ownership.md
│       ├── 0003-edge-computation.md
│       └── ...
│
└── scripts/
```

The exact structure should evolve with implementation rather than being imposed prematurely.

---

# 14. Architecture Decision Records

The course should use short ADRs to make engineering judgment visible.

Likely decisions include:

### ADR 1 — Transport

Why HTTP/TCP initially?

What alternatives were considered?

### ADR 2 — Node Identity

How is a station uniquely identified?

### ADR 3 — Observation Identity

How are duplicate messages recognized?

### ADR 4 — Authoritative State

What lives at the node versus centrally?

### ADR 5 — Retry Policy

Which failures are retried?

### ADR 6 — Local Persistence

How does offline buffering work?

### ADR 7 — Edge Computation

What processing belongs locally?

### ADR 8 — Broker Evaluation

Does a broker solve an actual problem?

### ADR 9 — Containerization

Does Docker improve reproducibility enough to justify itself?

### ADR 10 — Orchestration

Is workflow orchestration necessary?

These documents should be concise and evidence-driven.

---

# 15. Failure Model

The repository should explicitly document expected failure classes.

## Node Failures

- crash;
- invalid configuration;
- local disk full;
- corrupt local record;
- CPU overload;
- memory pressure.

## Network Failures

- connection refused;
- timeout;
- high latency;
- dropped connection;
- intermittent connectivity;
- duplicate send;
- lost acknowledgement.

## Central Service Failures

- service unavailable;
- validation failure;
- slow response;
- overloaded service;
- restart.

## Database Failures

- unavailable database;
- transaction failure;
- uniqueness conflict;
- malformed geometry;
- slow query.

For each failure, document:

```text
detection
   ↓
local behavior
   ↓
retry / reject / buffer
   ↓
operator visibility
   ↓
recovery
```

---

# 16. Observability Standard

The project should make its own behavior inspectable.

Minimum node event fields may include:

```text
timestamp
level
station_id
message_id
event
attempt
queue_depth
latency_ms
bytes
status
error
```

Minimum service fields may include:

```text
timestamp
request_id
station_id
message_id
route
status_code
validation_status
db_latency_ms
total_latency_ms
duplicate
error
```

Metrics naming should remain simple and documented.

The goal is not to recreate a commercial monitoring stack.

The goal is to be able to answer:

- Is the system healthy?
- Which node is unhealthy?
- Where is latency occurring?
- Is backlog growing?
- Are duplicates increasing?
- How far behind synchronization is a node?
- What happened to a particular observation?
- What changed after an architecture modification?

---

# 17. Benchmark Standard

Every major performance investigation should state:

## Question

What are we trying to learn?

## Hypothesis

What behavior do we expect?

## Workload

What data volume, node count, message rate, and resource profile are used?

## Variables

What changes?

## Controls

What remains fixed?

## Measurements

Examples:

- latency;
- throughput;
- CPU;
- memory;
- bytes;
- storage;
- retries;
- queue depth.

## Result

What happened?

## Explanation

Why?

## Decision

Does the system architecture change?

This prevents benchmark theater.

---

# 18. Industry Connection Protocol

Relevant lessons may consult current signals from:

- modern geospatial systems roles;
- edge-computing roles;
- Apple Maps / on-device systems work;
- Paces-style large-scale geospatial infrastructure;
- Radar-style high-throughput location infrastructure;
- PostGIS;
- GeoRust;
- Arrow / GeoArrow;
- DuckDB;
- distributed spatial systems;
- modern open-source edge/network tooling.

Industry research should remain bounded.

The recurring question is:

> **Are we learning durable systems concepts that remain relevant to modern spatial engineering?**

Specific frameworks may change.

Core concepts such as failure, synchronization, latency, idempotency, resource constraints, and data movement should remain useful.

---

# 19. Interview Readiness

By the end of the course, the student should be able to discuss:

- What is a process?
- What makes a service different from a script?
- What happens when a function call becomes a network call?
- What is a socket conceptually?
- Why use TCP?
- What role does HTTP play?
- What is serialization?
- Why can distributed messages arrive late or out of order?
- Why is time difficult in distributed systems?
- What is idempotency?
- Why do retries create duplicate-delivery problems?
- What is an acknowledgement?
- What does at-least-once delivery mean?
- What is eventual consistency?
- How does offline synchronization work?
- What state belongs at the edge?
- What state belongs centrally?
- What happens during a network partition?
- What is exponential backoff?
- Why add jitter?
- What is backpressure?
- Why use a bounded queue?
- When does a message broker become useful?
- Why did this project use or reject MQTT?
- Why did this project use or reject Docker?
- Why would Kubernetes be excessive or justified?
- How do you measure end-to-end latency?
- How do you trace one observation across components?
- What metrics indicate a synchronization problem?
- How do CPU, memory, bandwidth, and storage constraints affect architecture?
- When should computation happen at the edge?
- What did the edge-versus-central benchmark show?
- What information was lost through aggregation?
- How did the system behave when the central service failed?
- How did a node recover after being offline?
- How are duplicate observations prevented?
- How does PostGIS fit into the architecture?
- Why is Python still used?
- Why is Rust used at the node?
- How could an iPhone join this architecture later?
- What would need to change to support hundreds or thousands of nodes?

Answers should come from the student's own implementation and measurements.

---

# 20. Assessment Model

There are no conventional exams.

Progress is assessed through:

## Conceptual Understanding

Can the student explain the systems behavior without relying on vocabulary alone?

## Prediction

Before running an experiment, can the student predict what will happen?

## Failure Reasoning

Can the student explain behavior under partial failure?

## Debugging

Can the student isolate whether a problem belongs to:

- node;
- network;
- service;
- database;
- data contract;
- resource limit?

## Distributed Correctness

Can the student reason about:

- duplication;
- ordering;
- retries;
- stale data;
- synchronization?

## Architecture

Can the student place responsibilities sensibly?

## Simplicity

Can the student reject unnecessary infrastructure?

## Measurement

Can the student design a fair benchmark?

## Spatial Correctness

Are spatial semantics preserved across components?

## Documentation

Can another engineer understand the architecture and decisions?

## Portfolio Quality

Does each checkpoint make the same system more capable and credible?

---

# 21. Course Non-Goals

This course does **not** attempt to:

- make the student a distributed-systems researcher;
- teach every networking protocol;
- reproduce a graduate distributed-systems curriculum;
- implement Raft or Paxos;
- build a distributed database from scratch;
- implement a message broker;
- teach every cloud service;
- require Kubernetes;
- require Kafka;
- require MQTT;
- require Redis;
- require Docker;
- require Terraform;
- require a service mesh;
- teach Go;
- teach Ruby;
- teach C++;
- add additional languages merely for breadth;
- replace Python;
- replace PostGIS;
- turn all computation into Rust;
- optimize every operation;
- build a production weather platform;
- simulate unrealistic scale merely to claim "distributed";
- add infrastructure before a problem requires it;
- create multiple unrelated portfolio projects.

Depth follows architectural usefulness.

---

# 22. Technology Selection Rule

Distinguish:

```text
FOUNDATIONAL
durable concepts
```

from:

```text
CORE PROGRAM TECHNOLOGY
deliberately chosen long-term tools
```

from:

```text
OPTIONAL INFRASTRUCTURE
introduced only if justified
```

from:

```text
CURRENT INDUSTRY SIGNAL
worth understanding but not automatically adopting
```

## Foundational

- processes;
- networking;
- protocols;
- state;
- time;
- serialization;
- retries;
- idempotency;
- synchronization;
- fault tolerance;
- resource constraints;
- concurrency;
- backpressure;
- observability;
- benchmarking;
- architecture.

## Core Program Technology

- Python;
- SQL / Spatial SQL;
- PostgreSQL / PostGIS;
- Rust;
- Swift in the later dedicated course.

## Supporting Technologies

Use where they naturally fit:

- DuckDB;
- Arrow / GeoArrow;
- Parquet / GeoParquet;
- `.spat`;
- Git;
- pytest / Rust tests.

## Optional Infrastructure

Potential examples:

- Docker;
- MQTT;
- NATS;
- Redis;
- orchestration frameworks;
- cloud services;
- Kubernetes.

A technology enters the portfolio only after answering:

1. What problem exists?
2. Why is the current design insufficient?
3. What capability does this tool add?
4. What new complexity does it introduce?
5. Can the improvement be measured?
6. Is learning this tool worth the opportunity cost?

This rule protects the program from uncontrolled scope growth.

---

# 23. Scope Discipline

The program's breadth should come from understanding a **whole spatial system**, not from collecting tools.

A useful distinction:

```text
BROAD SYSTEM UNDERSTANDING
good
```

does not require:

```text
BROAD TOOL INVENTORY
```

The intended depth profile is:

```text
                  SPATIAL SYSTEM
                        │
        ┌───────────────┼───────────────┐
        │               │               │
      DATA           SYSTEMS         PRODUCT
        │               │               │
   SQL/PostGIS         Rust            Swift
   Python              CS             Apple APIs
   spatial data     distributed         UI
   ML/data           systems
```

The student should become increasingly capable across the vertical while maintaining a limited, coherent technology stack.

---

# 24. Course Freshness

This syllabus reflects the Spatial Systems Engineering strategy of **September 2026**.

Foundational distributed-systems concepts should remain relatively stable.

Specific tooling may change.

When returning after a long pause, conduct an **Industry Refresh** only when current tooling materially affects the next architectural decision.

Do not refresh technologies for every lesson.

---

# 25. Unit Completion Records

At the end of each unit, ChatGPT should produce a concise **Unit Completion Record** containing:

- systems concepts learned;
- Systems Lens covered;
- exercises completed;
- failure experiments completed;
- portfolio changes;
- tests added;
- metrics/benchmarks added;
- architecture decisions made;
- Industry Connection covered;
- unresolved questions;
- recommended next unit.

This makes the course resilient to pauses.

---

# 26. Definition of Course Completion

The course is complete when the student can:

1. explain how independent programs become communicating services;
2. explain basic client/server networking and protocol boundaries;
3. design a stable observation/message contract;
4. run multiple independent edge-node processes;
5. reason about message identity, time, and ordering;
6. implement retry-safe and idempotent ingestion;
7. explain why duplicate delivery occurs;
8. persist spatial observations centrally in PostGIS;
9. maintain durable local edge state;
10. operate through intermittent connectivity;
11. synchronize correctly after reconnect;
12. distinguish transient and permanent failures;
13. reason about resource constraints;
14. enforce bounded behavior under overload;
15. explain backpressure;
16. compare edge and centralized computation;
17. measure bandwidth, latency, CPU, memory, and storage;
18. explain information-loss tradeoffs from edge aggregation;
19. instrument nodes and services with useful observability;
20. reproduce and diagnose fault scenarios;
21. document architecture and data contracts;
22. justify or reject additional infrastructure;
23. explain why Rust, Python, SQL/PostGIS, and later Swift have distinct responsibilities;
24. maintain a tested, reproducible multi-component system;
25. describe what would need to change at larger scale; and
26. confidently demonstrate and discuss the system with another engineer.

The ultimate test is not:

> **"Do I know distributed systems?"**

It is:

> **"Can I design, build, break, observe, measure, and explain a distributed spatial system—and make defensible decisions about where computation, state, and complexity belong?"**

---

# 27. Course Progression

```text
          SPATIAL SYSTEMS & DISTRIBUTED COMPUTING v0.1

PHASE I                               PHASE II
From Programs to Systems             Distributed State + Failure

1. Processes + Services              4. Identity + Time + State
2. Networking + APIs                 5. Delivery + Idempotency
3. Multiple Nodes                    6. Offline + Recovery
        │                                      │
        ▼                                      ▼
 CHECKPOINT 1                            CHECKPOINT 2
 connected spatial system               resilient synchronization
           \                                  /
            \                                /
             ▼                              ▼
                    PHASE III
           Edge Computing + Constraints

             7. Constrained Nodes
             8. Edge vs Central
             9. Spatial Data Movement
                    │
                    ▼
               CHECKPOINT 3
            measured edge architecture
                    │
                    ▼
                    PHASE IV
              Operating the System

          10. Concurrency + Backpressure
          11. Observability + Faults
          12. Orchestration + Architecture
                    │
                    ▼
               CHECKPOINT 4
          SPATIAL EDGE PLATFORM v1
                    │
                    ▼
               NEXT CURRICULUM
       Swift for Spatial & Edge Computing
                    │
                    ▼
          iPhone becomes a real node
```

---

# 28. Portfolio Narrative

A reviewer should be able to follow this story.

## The Starting Point

A Rust program can process spatial data efficiently.

But real spatial systems involve multiple components.

## The First System

Several simulated Rust weather stations send geospatial observations to a Python service.

## The First Failure

The network becomes unavailable.

The nodes must preserve data and recover.

## The Distributed Problem

Retries create duplicates.

Messages arrive late.

State exists in multiple places.

## The Architecture

Nodes receive stable identities, durable local buffers, retry policies, synchronization logic, and explicit contracts.

The Python control plane ingests data idempotently and persists authoritative spatial state in PostGIS.

## The Edge Question

Raw sensor transmission is compared with local processing.

Some validation, aggregation, and compression move onto the Rust nodes.

## The Measurement

The system measures:

- bandwidth;
- latency;
- CPU;
- memory;
- storage;
- throughput;
- synchronization lag;
- failure recovery.

## The Engineering Decision

Edge and central responsibilities are assigned based on measured constraints rather than ideology.

## The Operational System

Structured logs, metrics, fault injection, bounded queues, and runbooks make the distributed platform understandable.

## The Simplicity Decision

Infrastructure technologies are evaluated only when a concrete pain point appears.

Some are adopted.

Others are deliberately rejected.

## The Future

The system defines a node contract that an iPhone can later implement in Swift.

The simulated platform becomes the foundation for real edge computing.

---

# 29. Status

**Syllabus v0.1**

This course is the second concrete curriculum in the Spatial Systems Engineering learning program.

It assumes that Rust is no longer merely a language-learning exercise. The Rust systems layer now becomes part of a distributed spatial architecture.

The course intentionally limits technology sprawl.

Python, SQL/PostGIS, Rust, and later Swift form the durable language/core platform. Additional infrastructure is introduced only when a measured system need warrants it.

The initial portfolio domain is a simulated distributed weather-station network because simple observations allow the course to focus attention on the difficult engineering questions:

- communication;
- state;
- time;
- failure;
- synchronization;
- resource constraints;
- data movement;
- observability;
- orchestration; and
- edge-versus-central computation.

The next curriculum should be **Swift for Spatial & Edge Computing**, but only after this distributed architecture has been exercised enough that the Apple-native layer has clear responsibilities.

The intended progression is:

```text
Rust systems layer
        ↓
distributed spatial platform
        ↓
stable edge-node contract
        ↓
Swift / iPhone node
        ↓
real mobile sensing
        ↓
on-device computation
        ↓
later ML + 3D / LiDAR expansion
```

The guiding program question remains:

> **Does this help develop the ability to design, understand, measure, and build a complete spatial system—from constrained computation at the edge, through high-performance geospatial processing and data infrastructure, to machine learning and a polished user-facing application?**
