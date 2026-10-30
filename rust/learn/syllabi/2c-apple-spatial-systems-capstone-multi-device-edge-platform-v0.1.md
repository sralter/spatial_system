# Apple Spatial Systems Capstone: Multi-Device Edge Platform

**Syllabus Version:** 0.1  
**Course / Track:** 3C within the broader Spatial Systems Engineering program  
**Filename Sequence:** `2c-apple-spatial-systems-capstone-multi-device-edge-platform-v0.1.md`  
**Course Format:** Self-paced, ChatGPT-guided, project-based capstone  
**Expected Commitment:** Up to 30 minutes per session; approximately 3–4 hours per unit, plus integration and real-device testing  
**Prerequisite:** *Swift for 3D Spatial & Edge Computing v0.1*  
**Earlier Foundations:** *Swift for Spatial & Edge Computing v0.1*, *Spatial Systems & Distributed Computing v0.1*, and *Rust for Geospatial Systems v0.2*  
**Portfolio Domain:** Multi-device Apple-native spatial edge platform using Apple Watch, iPhone, macOS, Rust, Python, PostGIS, simulated nodes, and real spatial sensor nodes  
**Course Vintage:** September 2026  

---

# 1. Course Purpose

This course is the **integration capstone for the Swift / Apple portion of the Spatial Systems Engineering program**.

The earlier courses progressively built:

```text
Rust spatial compute
        ↓
distributed spatial nodes
        ↓
real iPhone edge node
        ↓
3D sensing and point-cloud processing
```

Course 2C completes the Apple-native systems arc by introducing two new roles:

```text
Apple Watch
     ↓
lightweight constrained field node

macOS
     ↓
operator hub / control application
```

The objective is no longer primarily to add another algorithm, file format, sensor, or spatial representation.

The objective is to answer:

> **How do multiple heterogeneous spatial devices become one operable, observable, Apple-native distributed system?**

The student will extend the existing Spatial Edge Platform so that:

- simulated Rust nodes continue to run;
- the iPhone remains a rich mobile spatial edge node;
- an Apple Watch becomes a lightweight mobile sensor node;
- Watch and iPhone collect overlapping motion, altitude, pressure, and location-related observations where supported;
- the iPhone retains richer sensing, Core ML, and LiDAR/3D responsibilities;
- the macOS application becomes the human-facing system hub;
- the Mac hub displays simulated and real nodes together;
- the Mac hub shows identity, state, connectivity, observations, location, synchronization, and diagnostics;
- logs and errors can be inspected through the application;
- selected recovery/operator actions can be initiated where appropriate;
- the Python control plane, Rust systems layer, PostGIS database, and 3D storage remain backend components rather than being replaced by Swift; and
- the student experiences the transition from operating a project through VSCode, terminals, logs, and database clients to operating it through a purpose-built application.

The central course question is:

> **How can Watch, iPhone, Mac, Rust, Python, PostGIS, and simulated nodes behave as one coherent spatial computing platform?**

A second recurring question is:

> **What changes when a developer-facing distributed system becomes an operator-facing product?**

---

# 2. Strategic Role

The progression is:

```text
0  Rust for Geospatial Systems
        ↓
1  Spatial Systems & Distributed Computing
        ↓
2A Swift for Spatial & Edge Computing
        ↓
2B Swift for 3D Spatial & Edge Computing
        ↓
2C Apple Spatial Systems Capstone
        ↓
3  Spatial Systems Engineering Portfolio Capstone
```

Course 2C is the **systems-integration capstone before the final portfolio-packaging course**.

Course 3 will later focus on cleanup, technical debt, architecture stabilization, reproducibility, documentation, diagrams, demonstrations, release engineering, portfolio presentation, case-study writing, and interview storytelling.

Course 2C therefore remains an **engineering course**, not a presentation course.

---

# 3. Starting Architecture

Course 2C expands Spatial Edge Platform v3 into:

```text
                         macOS Spatial Hub
                               │
                ┌──────────────┼──────────────┐
                │              │              │
             nodes          spatial         diagnostics
             status          state          operations
                │              │              │
                └──────────────┼──────────────┘
                               │
                     Python Control Plane
                               │
             ┌─────────────────┼──────────────────┐
             │                 │                  │
          PostGIS         Rust systems        3D storage
             │                 │                  │
             └─────────────────┼──────────────────┘
                               │
              ┌────────────────┼─────────────────┐
              │                │                 │
        simulated nodes    Apple Watch         iPhone
        Rust A / B / C      real node          real node
              │                │                 │
              │          location/motion      location/motion
              │          altitude/pressure    altitude/pressure
              │          constrained sync     Core ML
              │                               LiDAR / 3D
              │                               richer compute
              └────────────────┼─────────────────┘
                               │
                         one node model
```

The goal is not to make every node identical.

The goal is to make every node **legible to the same platform**.

---

# 4. Device Roles

## 4.1 Apple Watch — Lightweight Field Node

The Watch is the most constrained real node.

Its role is to collect and communicate a bounded set of observations under real battery, storage, lifecycle, connectivity, background-execution, and sensor-availability constraints.

Potential observation families include:

- location;
- relative/absolute altitude where available;
- barometric pressure;
- accelerometer;
- gyroscope;
- magnetometer where available;
- device-motion-derived values;
- pedometer/activity-derived values where useful.

The Watch is not expected to perform LiDAR scanning, large point-cloud processing, heavy ML, or central orchestration.

Its systems question is:

> **What should a truly constrained spatial edge node do locally, retain locally, send elsewhere, and defer?**

## 4.2 iPhone — Rich Mobile Spatial Edge Node

The iPhone retains the responsibilities built in 2A and 2B:

- Core Location;
- Core Motion;
- pressure and altitude;
- accelerometer, gyroscope, and magnetometer;
- local persistence;
- offline synchronization;
- local spatial computation;
- Core ML;
- LiDAR/depth;
- point-cloud processing;
- Rust-backed 3D computation;
- chunked 3D storage and synchronization.

## 4.3 macOS — Spatial Hub

The Mac becomes the primary operator interface.

It should answer:

- Which nodes exist?
- Which are simulated or physical?
- Which are online, stale, degraded, or offline?
- When was each last seen?
- Where are spatial nodes?
- What observations have they produced?
- What is each node doing?
- Are observations or acquisitions synchronized?
- Are 3D acquisitions pending?
- Did processing fail?
- What error occurred?
- Which component emitted it?
- Can the operator safely retry or inspect the failed work?

The Mac app does **not** replace the backend:

```text
macOS Spatial Hub
        │
        ▼
platform APIs / contracts
        │
        ▼
Python + Rust + PostGIS + storage
```

> **The hub should operate the system, not secretly become the entire system.**

---

# 5. Sensor Scope and Freshness

Core Motion exposes motion- and environment-related data from available Apple hardware, including accelerometer and gyroscope data and, when available, magnetometer, barometer/altitude, pedometer, and processed device-motion data.

Every sensor path should begin with:

```text
capability check
      ↓
authorization check
      ↓
supported API
      ↓
sampling policy
      ↓
observation
```

The exact Apple APIs should be refreshed against current official documentation when each relevant unit begins.

Durable concepts matter more than memorizing an API surface:

- sensor capability;
- calibration;
- sampling;
- coordinate frames;
- uncertainty;
- permissions;
- energy;
- synchronization.

---

# 6. Governing Principles

## Integration Over Accumulation

This is intentionally shorter than 2A and 2B. Reuse existing contracts, services, synchronization mechanisms, and Swift components before adding frameworks.

## One Platform, Heterogeneous Nodes

A node contract should represent identity, type, capabilities, state, last contact, observation types, health, and synchronization rather than assuming every node has identical sensors.

## Capability Is Data

Conceptually:

```text
NodeCapabilities
├── location
├── altitude
├── pressure
├── accelerometer
├── gyroscope
├── magnetometer
├── lidar
├── core_ml
└── 3d_processing
```

The Mac should render functionality according to capability.

## The Watch Is an Edge-Computing Experiment

Measure sampling frequency, observation size, battery implications, local retention, batching, communication frequency, and data reduction.

The question is not how much the Watch can be forced to do, but what the smallest useful responsibility is.

## Shared Sensors Create Comparative Experiments

Watch and iPhone can produce overlapping pressure, altitude, motion, and location observations. Compare timestamps, sampling rates, trends, missing data, and the effect of device placement.

## macOS Is an Operator Interface, Not a Mock Dashboard

If the UI says a node is offline, has queued observations, or has a failed job, that should derive from real system state.

## Move Beyond VSCode Without Hiding the System

Developer tools remain useful, but normal operation should become possible through the hub.

## Operator Actions Must Be Explicit

Retry, refresh, acknowledge, or reprocess actions should correspond to documented state transitions. Avoid arbitrary remote execution.

## Health Is Derived State

Statuses such as healthy, degraded, stale, offline, and error should derive from measurable conditions such as last seen, queue depth, unresolved errors, and sync age.

## Native and Functional UI

The standard remains:

> **Native, clear, and functional—not ornamental.**

## Real Failures Reach the Hub

Watch disconnects, iPhone queues, Rust processing errors, database failures, and corrupt 3D chunks should become visible operational states.

## Course 2C Ends Feature Expansion

At completion, the platform is functionally complete enough to enter portfolio hardening. New ideas move to a backlog.

---

# 7. Multi-Device Systems Lens

The recurring question is:

> **What systems concept explains the behavior of multiple real and simulated devices participating in one operator-visible platform?**

Topics include:

- heterogeneous capabilities;
- identity;
- capability negotiation;
- session identity;
- clocks and timestamp alignment;
- sampling;
- sensor noise;
- device placement;
- batching;
- energy-aware computation;
- local versus remote state;
- stale state;
- liveness;
- health models;
- fan-in;
- event streams;
- command versus observation;
- eventual consistency;
- relay versus direct communication;
- operator read models;
- failure domains;
- control plane versus data plane;
- auditability;
- bounded recovery.

---

# 8. Learning Loop

A typical unit may contain:

1. Integration concept.
2. Known → Unknown bridge.
3. Small platform experiment.
4. Multi-Device Systems Lens.
5. Real-device test.
6. Failure experiment.
7. Operator experience.
8. Measurement.
9. Architecture review.
10. Portfolio increment.

The teaching cycle remains:

```text
teach
  ↓
predict
  ↓
build smallest path
  ↓
run on real/simulated node
  ↓
observe
  ↓
break
  ↓
diagnose from hub
  ↓
measure
  ↓
revise
  ↓
document
```

---

# 9. Course Architecture

Course 2C contains **8 units across three phases**.

```text
PHASE I — Complete the Device Network

1. watchOS and the Constrained Spatial Edge Node
2. Watch ↔ iPhone ↔ Platform Communication
3. Multi-Device Identity, Sessions, State, and Synchronization
        │
        ▼
CHECKPOINT 1
Apple Watch Joins the Spatial Edge Platform


PHASE II — Build the Operator Experience

4. macOS SwiftUI and Spatial Hub Architecture
5. Nodes, Maps, Observations, Acquisitions, and System State
6. Diagnostics, Logs, Health, Errors, and Operator Actions
        │
        ▼
CHECKPOINT 2
Operate the Platform Through the Spatial Hub


PHASE III — Integrate and Harden

7. End-to-End Multi-Device Failure and Performance Testing
8. Apple Spatial Systems Capstone Integration
        │
        ▼
CHECKPOINT 3
SPATIAL EDGE PLATFORM v4
MULTI-DEVICE APPLE SPATIAL SYSTEM
```

---

# PHASE I — COMPLETE THE DEVICE NETWORK

# Unit 1 — watchOS and the Constrained Spatial Edge Node

## Core Topics

- watchOS target/project structure;
- SwiftUI on Watch;
- lifecycle;
- Core Motion;
- Core Location where appropriate;
- capability checks;
- permissions;
- pressure;
- relative/absolute altitude where available;
- accelerometer;
- gyroscope;
- magnetometer where available;
- device motion;
- timestamps and units;
- sampling interval;
- constrained persistence;
- battery/energy;
- background limitations;
- minimal UI.

## Exercise

Create one bounded observation session using a model such as:

```text
observation_id
node_id
session_id
timestamp
observation_type
value(s)
units
accuracy / confidence if available
source
```

Collect a small set of pressure/altitude, motion, and location observations where appropriate.

## Systems Experiment

Compare multiple sampling intervals and measure observations/minute, bytes/minute, local storage growth, and practical resource implications.

## Failure Experiments

Test denied permission, unavailable sensor, interruption, lifecycle transitions, empty sessions, and persistence errors.

## Portfolio Increment

Add the real watchOS node to the platform.

---

# Unit 2 — Watch ↔ iPhone ↔ Platform Communication

## Core Topics

- Watch/iPhone relationship;
- current Watch communication APIs;
- direct versus relayed communication;
- reachability;
- durable versus immediate transfer;
- batching;
- queues;
- acknowledgements;
- retry;
- offline operation;
- duplicate handling;
- iPhone relay;
- energy/data tradeoffs.

Compare:

```text
A: Watch → iPhone → Platform

B: Watch → Platform

C: Hybrid
```

Choose based on reliability, lifecycle, energy, connectivity, complexity, and offline behavior.

## Systems Lens — Relay Nodes

The iPhone can be both a sensor producer and relay. Preserve the **originating Watch node** even when the iPhone forwards an observation.

## Required Failure Experiment

Collect Watch observations, disconnect the expected path, continue locally, reconnect, and verify:

```text
no lost acknowledged data
no duplicate logical observations
correct originating node
correct timestamps
```

## ADR

**Watch communication and relay strategy.**

---

# Unit 3 — Multi-Device Identity, Sessions, State, and Synchronization

## Core Topics

- node identity/type;
- capability model;
- device metadata;
- field-session identity;
- observation identity;
- originating versus relay node;
- clocks;
- last seen;
- liveness;
- stale/online/offline state;
- sync state;
- multi-device correlation.

Conceptually:

```text
Node
├── node_id
├── node_type
├── display_name
├── capabilities
├── last_seen
├── health
└── metadata
```

and:

```text
FieldSession
├── session_id
├── started_at
├── ended_at
└── participating_nodes
```

## Multi-Device Field Experiment

Use Watch and iPhone during the same bounded walk or hike.

Potentially collect from both:

- location;
- pressure;
- altitude;
- motion.

Compare timestamps, altitude change, pressure trend, movement periods, track, missing intervals, and sampling frequency.

A key lesson is that physical sensor context matters:

```text
Watch → wrist
iPhone → pocket / hand / pack
```

## Checkpoint 1 — Apple Watch Joins the Spatial Edge Platform

The platform contains simulated Rust nodes plus real Watch and iPhone nodes. The Watch can identify itself, advertise capabilities, collect supported observations, persist bounded local state, participate in a field session, operate through disconnection, synchronize safely, preserve originating identity, and expose errors.

---

# PHASE II — BUILD THE OPERATOR EXPERIENCE

# Unit 4 — macOS SwiftUI and Spatial Hub Architecture

## Core Topics

- macOS SwiftUI;
- desktop lifecycle;
- navigation;
- sidebar/detail patterns;
- tables/lists;
- inspectors;
- toolbars;
- menus where useful;
- keyboard/mouse interaction;
- async loading;
- platform API client;
- domain models;
- caching;
- refresh strategy;
- UI/backend separation.

The Mac is an operator interface, not a new backend.

A first shell may include:

```text
Spatial Hub
├── Overview
├── Nodes
├── Map
├── Sessions
├── Observations
├── 3D Acquisitions
├── Diagnostics
└── Settings
```

## Systems Lens — Operator Read Models

Transform raw backend state into a derived representation useful to a human operator without changing authoritative state.

## Exercise

Display all real registered nodes with identity, type, capabilities, last seen, health, and synchronization state.

## Failure Tests

Start the Mac app with backend unavailable, database unavailable, no nodes, malformed responses, and request timeouts.

---

# Unit 5 — Nodes, Maps, Observations, Acquisitions, and System State

## Core Topics

- node list/detail;
- MapKit on macOS;
- last known location;
- field-session tracks;
- observation summaries;
- pressure/altitude history;
- synchronization state;
- 3D acquisition metadata;
- simulated-node visualization;
- filters;
- time ranges;
- capability-aware UI.

The hub must display simulated nodes, Watch, and iPhone through one operator model.

A node detail view may include:

```text
Identity
Capabilities
Last Seen
Location
Current State
Recent Observations
Queue / Sync State
Recent Errors
Recent Sessions
Acquisitions
```

## Map

Show simulated station locations, Watch/iPhone positions, field-session paths, acquisition locations, and node health where useful.

## Comparative Sensor View

For a shared Watch/iPhone session, display aligned elevation/altitude, pressure, location, and selected motion summaries.

## 3D Integration

Surface Course 2B acquisition metadata:

```text
acquisition ID
device
time
location
point count
processing level
chunk state
sync state
errors
storage state
```

A full native point-cloud renderer on macOS is optional; a useful acquisition operator view is required.

---

# Unit 6 — Diagnostics, Logs, Health, Errors, and Operator Actions

## Core Topics

- structured diagnostics;
- log events;
- severity;
- source component;
- correlation IDs;
- node/session/acquisition/chunk IDs;
- filtering and search;
- error detail;
- derived health;
- stale state;
- service health;
- queue depth;
- failed sync/processing;
- bounded operator actions;
- auditability.

The governing question is:

> **Can an engineer diagnose a real failure from the Spatial Hub before opening VSCode or a terminal?**

Potential sources include Watch, iPhone, simulated Rust nodes, Rust processing, Python control plane, PostGIS, 3D storage, and synchronization.

A simple health model might derive:

```text
HEALTHY
DEGRADED
STALE
OFFLINE
ERROR
```

from measurable state.

## Operator Actions

Implement only actions with clear contracts, such as retry failed synchronization, retry a processing job, refresh state, acknowledge a resolved error, or request safe reprocessing.

## Failure Drill

Cause a real failure, diagnose it from the Mac app, and document symptom, displayed health, logs, root cause, and recovery.

## Checkpoint 2 — Operate Through the Spatial Hub

The Mac can connect to the real backend; display simulated and real nodes; show capabilities, location, health, sessions, observations, pressure/altitude trends, 3D acquisitions, sync state, logs/errors, backend degradation; and perform at least one safe recovery action.

Normal inspection no longer requires VSCode.

---

# PHASE III — INTEGRATE AND HARDEN

# Unit 7 — End-to-End Multi-Device Failure and Performance Testing

## Core Topics

- end-to-end test design;
- controlled field tests;
- simulated-node scaling;
- Watch/iPhone coexistence;
- connectivity transitions;
- stale state;
- queue buildup;
- recovery;
- end-to-end latency;
- event fan-in;
- resource measurement;
- Watch sampling cost;
- hub responsiveness;
- failure matrix.

## Required Scenario Matrix

Test:

### A — Normal Operation
Simulated nodes, Watch, iPhone, Mac, and backend healthy.

### B — Watch Disconnects
Local behavior remains bounded; hub reports stale/offline; reconnect synchronizes safely.

### C — iPhone Disconnects
Local observations/3D work remain safe; reconnect resumes synchronization.

### D — Backend Stops
Edge nodes preserve valid local state; Mac reports degradation; recovery is visible.

### E — Rust Processing Failure
Acquisition remains identifiable; error reaches diagnostics; safe recovery exists.

### F — PostGIS Failure
Persistence failure is visible; clients do not pretend data was committed.

### G — Queue Growth
Generate a visible backlog; observe queue depth and drain behavior.

### H — Mixed Session
Watch and iPhone participate in one field session while simulated nodes continue operating.

## Measurements

Measure representative Watch observation rate and bytes, Watch transfer latency, iPhone latency, queue-drain rate, Mac API/refresh latency, ingestion throughput, 3D status latency, and error-propagation latency.

The goal is an end-to-end performance model, not extreme benchmark numbers.

---

# Unit 8 — Apple Spatial Systems Capstone Integration

## Core Topics

- architecture review;
- contract review;
- capability model review;
- multi-device integration;
- service boundaries;
- configuration;
- startup/shutdown;
- reproducible local environment;
- operator runbook;
- integration tests;
- real-device smoke tests;
- final failure drill;
- final benchmark;
- feature freeze;
- Course 3 handoff.

Review each responsibility:

```text
Swift / watchOS
→ constrained sensor node

Swift / iOS
→ rich spatial/ML/3D edge node

Swift / macOS
→ operator experience

Rust
→ high-performance spatial systems + simulated nodes

Python
→ control plane + orchestration + scientific/ML workflows

PostGIS
→ authoritative relational/spatial metadata

3D storage
→ heavy point-cloud payloads
```

If responsibilities drifted, correct the most important problems.

## Feature Freeze

Create a feature-freeze record containing:

- completed capabilities;
- known bugs;
- technical debt;
- deferred ideas;
- future possibilities;
- items intentionally postponed to Course 3.

Course 3 should begin with a bounded artifact.

---

# 10. Final Capstone

## Spatial Edge Platform v4 — Multi-Device Apple Spatial System

The completed platform contains:

```text
REAL EDGE NODES
├── Apple Watch
└── iPhone

SIMULATED EDGE NODES
└── Rust nodes

NATIVE OPERATOR APPLICATION
└── macOS Spatial Hub

SYSTEMS / COMPUTE
└── Rust

CONTROL / SCIENTIFIC LAYER
└── Python

SPATIAL STATE
└── PostGIS

3D PAYLOADS
└── point-cloud storage
```

A concise project description:

> **A multi-device spatial edge-computing platform integrating simulated Rust nodes, a real Apple Watch sensor node, a real iPhone spatial/ML/LiDAR node, a Python control plane, PostGIS, Rust spatial computation, 3D storage, and a native macOS Spatial Hub for mapping, monitoring, diagnostics, and operation of the distributed system.**

The portfolio transition is:

```text
developer-operated repository
          ↓
operator-visible system
          ↓
multi-device spatial product
```

---

# 11. Required Capstone Demonstration

## Scenario A — Start the Platform

Start PostGIS, Python control plane, simulated Rust nodes, required Rust processing services, and the Mac hub. Simulated nodes appear as active.

## Scenario B — Join Real Devices

Start Watch and iPhone nodes. Both appear as distinct physical nodes with different capabilities.

## Scenario C — Field Session

Begin a shared Watch/iPhone walk or hike session. Collect supported location, altitude, pressure, and selected motion observations. Inspect route, observations, trends, participation, missing intervals, and sync state on the Mac.

## Scenario D — iPhone 3D Acquisition

Capture a bounded LiDAR/depth scene and run the Course 2B path. Inspect acquisition identity, location, point count, processing, chunks, sync, and errors from the Mac.

## Scenario E — Disconnect a Real Node

Disconnect Watch or iPhone. The Mac displays stale/offline state. Local work remains valid. Reconnect and observe recovery.

## Scenario F — Break the Backend

Stop or impair a backend component. The Mac displays central degradation. Restart it and observe recovery.

## Scenario G — Processing Error

Cause a controlled Rust or 3D-processing failure. Diagnose it from the Mac using source, correlation/acquisition ID, error, state, and recovery path.

## Scenario H — Full System View

End with:

```text
simulated Rust nodes
+
Watch
+
iPhone
+
Mac
+
Python
+
Rust
+
PostGIS
+
3D storage
```

participating in one architecture.

The student should answer:

> **How do the responsibilities and constraints of Watch, iPhone, Mac, Rust, Python, and PostGIS differ, and why is the system stronger because those responsibilities are explicit?**

---

# 12. Movement / Hiking Systems Experiment

A bounded field experiment creates a useful overlap between spatial systems and movement/fitness sensing.

Potential observations:

```text
timestamp
location
relative altitude
absolute altitude where available
pressure
acceleration
rotation
device motion
pedometer/activity summaries where useful
```

Questions include:

- How does pressure change with elevation?
- How closely do Watch and iPhone altitude trends agree?
- How do sampling intervals differ?
- How does wrist motion differ from pocket/hand motion?
- What should be retained or summarized?
- Which data belongs centrally?
- What does a useful Mac visualization look like?

This remains a **systems and sensing exercise**, not medical interpretation.

The same engineering ideas are relevant to movement-oriented Apple systems:

```text
person
+
device
+
location
+
motion
+
time
+
environment
```

That creates problems in trajectories, altitude, sensor fusion, sampling, coordinate frames, energy, local inference, privacy, offline operation, synchronization, and multi-device coordination.

---

# 13. Observability Standard

A generic operational event may contain:

```text
timestamp
severity
component
node_id
session_id
observation_id
acquisition_id
chunk_id
event_type
message
correlation_id
metadata
```

The hub should support meaningful filtering and tracing.

The student should be able to trace:

```text
Watch observation
      ↓
Watch local queue
      ↓
iPhone relay or direct path
      ↓
control plane
      ↓
PostGIS
      ↓
Mac display
```

and:

```text
iPhone LiDAR acquisition
      ↓
Rust processing
      ↓
chunk storage
      ↓
sync
      ↓
central metadata
      ↓
Mac acquisition view
```

---

# 14. Security and Privacy

The platform handles precise location, movement, device identity, activity patterns, and 3D scans of physical spaces.

Required principles include:

- least-privilege permissions;
- clear usage descriptions;
- local data minimization;
- secure credentials/tokens;
- TLS;
- appropriate Keychain use;
- avoiding unnecessary raw-data retention;
- careful logs;
- no secrets in diagnostics;
- bounded operator actions;
- explicit retention/deletion reasoning;
- privacy-aware demo data.

---

# 15. Architecture Decision Records

Likely ADRs:

1. Watch node responsibilities.
2. Watch communication strategy.
3. Multi-device capability model.
4. Field-session contract.
5. Node liveness and health.
6. Mac hub backend/read-model contract.
7. Operational event model.
8. Operator actions.
9. Sensor sampling policy.
10. Feature freeze.

Every ADR should remain concise and evidence-driven.

---

# 16. Course Non-Goals

Course 2C does **not** attempt to:

- become a comprehensive watchOS or macOS curriculum;
- build a commercial fitness application;
- provide medical interpretation;
- replace HealthKit or Apple Fitness;
- add every Apple sensor;
- build a production IoT fleet manager;
- build a production observability vendor;
- provide arbitrary remote execution;
- redesign the Python control plane from scratch;
- rewrite Rust in Swift;
- put the backend inside the Mac app;
- substantially deepen LiDAR algorithms;
- add another ML specialization;
- create elaborate UI animation/design systems;
- optimize for App Store growth;
- support every Apple device family;
- require cloud deployment, Kubernetes, or Kafka;
- continue unlimited feature expansion.

---

# 17. Technology Selection Rule

Core existing technologies:

- Swift / SwiftUI;
- Rust;
- Python;
- PostgreSQL/PostGIS;
- MapKit;
- Core Location;
- Core Motion;
- Core ML;
- ARKit/3D tooling from 2B.

New Apple platform areas:

- watchOS;
- current Watch/iPhone communication APIs;
- macOS SwiftUI/application APIs.

Before adding anything else:

1. What integration problem exists?
2. Can an existing component solve it?
3. Is the dependency platform-native?
4. What does it simplify?
5. How will it be tested?
6. How will it fail?
7. Does it help the capstone?
8. Is it needed before Course 3?

If #8 is no, put it in the backlog.

---

# 18. Portfolio Repository Evolution

An illustrative structure:

```text
spatial-edge-platform/
├── edge/
│   ├── rust/
│   └── apple/
│       ├── Shared/
│       │   ├── Domain/
│       │   ├── Networking/
│       │   ├── Contracts/
│       │   └── Observability/
│       ├── iOS/
│       │   └── SpatialEdge/
│       ├── watchOS/
│       │   └── SpatialEdgeWatch/
│       └── macOS/
│           └── SpatialHub/
├── control_plane/
├── db/
├── pointcloud/
├── storage/
├── benchmarks/
└── docs/
    ├── architecture.md
    ├── node-contract.md
    ├── capability-model.md
    ├── field-session-contract.md
    ├── health-model.md
    ├── operator-model.md
    ├── failure-model.md
    ├── observability.md
    ├── runbook.md
    ├── course-2c-feature-freeze.md
    └── decisions/
```

Do not reorganize the repository merely to match this diagram.

---

# 19. Interview Readiness

By the end, the student should be able to discuss:

- why use a Watch as an edge node;
- watchOS constraints;
- sampling versus battery/data volume;
- sensor capability checks;
- pressure and relative altitude;
- accelerometer versus gyroscope versus magnetometer;
- processed device motion;
- why Watch and iPhone measurements differ;
- originating versus relay node;
- capability models;
- heterogeneous node contracts;
- multi-device field sessions;
- liveness, stale state, and health;
- disconnect/recovery behavior;
- why build a Mac hub;
- why the Mac should not become the backend;
- operator read models;
- MapKit's operational role;
- 3D acquisition metadata;
- structured diagnostics and correlation IDs;
- safe operator actions;
- Rust, Python, PostGIS, and Swift responsibilities;
- the most instructive failure;
- the system bottleneck;
- deliberate non-goals;
- why the project is ready for portfolio hardening.

Answers should come from the student's own system.

---

# 20. Assessment Model

There are no conventional exams.

Assessment covers:

- watchOS constrained-node understanding;
- sensor semantics and sampling;
- multi-device modeling;
- distributed correctness;
- macOS application architecture;
- operational health/liveness;
- observability and diagnosis;
- spatial inspection;
- architecture boundaries;
- integration/reuse of earlier work;
- scope discipline.

The most important assessment question is:

> **Can the student understand and operate the whole system rather than only individual components?**

---

# 21. Hardware and Tooling Milestones

## Phase I

Strongly preferred:

- Apple Watch capable of running the course app;
- paired iPhone;
- Xcode;
- current watchOS/iOS SDKs.

Real devices are important for lifecycle and sensor behavior.

## Phase II

Use Mac, macOS SwiftUI, MapKit, existing backend, simulated Rust nodes, Watch, and iPhone.

## Phase III

Use the full local platform:

```text
Mac
Watch
iPhone
Rust
Python
PostGIS
3D storage
```

under controlled failure scenarios.

---

# 22. Course Freshness

This syllabus reflects the program strategy of **September 2026**.

Before implementing units involving Core Motion sensor availability, Core Location on watchOS, Watch/iPhone communication, watchOS background behavior, macOS SwiftUI, or platform security/privacy, perform a bounded official Apple documentation refresh.

Durable concepts remain:

- constrained nodes;
- capability;
- sampling;
- identity;
- state;
- liveness;
- synchronization;
- observability;
- operator models;
- device responsibility.

---

# 23. Unit Completion Records

At the end of each unit, produce a concise record containing:

- concepts learned;
- Multi-Device Systems Lens covered;
- Known → Unknown bridges;
- Watch work;
- iPhone integration;
- Mac work;
- backend changes;
- portfolio changes;
- failure experiments;
- tests;
- measurements;
- ADRs;
- unresolved questions;
- technical debt;
- backlog items deliberately deferred;
- recommended next unit.

---

# 24. Definition of Course Completion

Course 2C is complete when the student can:

1. explain the Watch's constrained edge-node role;
2. build/run the Watch app on real hardware;
3. check sensor capability and authorization;
4. collect supported pressure/altitude and motion observations;
5. preserve timestamps and units;
6. select defensible sampling intervals;
7. measure observation data volume;
8. persist bounded Watch state;
9. continue through temporary disconnection;
10. synchronize Watch observations safely;
11. preserve originating identity through relay paths;
12. explain the Watch communication architecture;
13. represent node capabilities explicitly;
14. distinguish Watch, iPhone, and simulated-node capabilities;
15. associate Watch and iPhone with a shared field session;
16. compare overlapping observations;
17. explain device-placement effects;
18. model last-seen and health state;
19. build a native macOS SwiftUI application;
20. connect it to the real backend;
21. display simulated and real nodes;
22. display capabilities and spatial locations;
23. display field-session paths;
24. inspect sensor observations and pressure/altitude history;
25. inspect iPhone 3D acquisition metadata;
26. inspect synchronization and structured diagnostics;
27. trace observations and 3D acquisitions across the system;
28. detect stale/offline nodes and service degradation;
29. expose Rust/processing failures through the hub;
30. implement at least one safe recovery action;
31. survive Watch/iPhone/backend disconnection;
32. recover queued observations without duplicate logical records;
33. run an end-to-end mixed-node scenario;
34. measure representative observation, transfer, and recovery latency;
35. identify an end-to-end bottleneck;
36. explain Swift/watchOS, Swift/iOS, Swift/macOS, Rust, Python, PostGIS, and 3D-storage responsibilities;
37. document capability, health, operator, and communication models;
38. maintain an integration runbook;
39. perform a final multi-device failure drill;
40. establish a feature freeze and Course 3 technical-debt/backlog handoff; and
41. operate and explain the platform without using VSCode as the primary interface.

The ultimate test is:

> **"Can I operate a heterogeneous spatial edge platform made of simulated and real devices through a native application, understand what every component is doing, diagnose failures across the system, and explain why each device and technology owns the responsibilities it does?"**

---

# 25. Course Progression

```text
        APPLE SPATIAL SYSTEMS CAPSTONE v0.1
                     COURSE 3C

PHASE I
Complete the Device Network

1. watchOS Constrained Edge Node
2. Watch ↔ iPhone ↔ Platform
3. Identity + Sessions + Synchronization
             │
             ▼
        CHECKPOINT 1
    APPLE WATCH JOINS
 SPATIAL EDGE PLATFORM
             │
             ▼
PHASE II
Build the Operator Experience

4. macOS Spatial Hub Architecture
5. Nodes + Maps + Observations + 3D
6. Diagnostics + Health + Operations
             │
             ▼
        CHECKPOINT 2
   OPERATE THROUGH THE
       SPATIAL HUB
             │
             ▼
PHASE III
Integrate and Harden

7. Multi-Device Failure + Performance
8. Capstone Integration + Feature Freeze
             │
             ▼
        CHECKPOINT 3

    SPATIAL EDGE PLATFORM v4
  MULTI-DEVICE APPLE SPATIAL SYSTEM
```

---

# 26. Capstone Narrative

A reviewer should be able to follow one continuous story:

```text
Rust
high-performance spatial computation
        ↓
Distributed Systems
independent spatial nodes
        ↓
Swift / iPhone
real mobile edge node
        ↓
Core ML
local spatial intelligence
        ↓
LiDAR / 3D
physical-world 3D sensing
        ↓
watchOS
constrained wearable edge node
        ↓
Multi-Device Sensing
Watch + iPhone field sessions
        ↓
macOS
native operator hub
        ↓
Integrated Platform
Rust + Python + PostGIS + Watch + iPhone + Mac
```

The project is no longer best described as a collection of scripts and applications.

It is:

> **a small heterogeneous spatial computing platform.**

---

# 27. Handoff to Course 3

Course 2C deliberately ends with a working but imperfect engineering artifact.

Course 3 should focus on:

```text
architecture cleanup
        ↓
technical debt review
        ↓
contract stabilization
        ↓
repository cleanup
        ↓
test-suite cleanup
        ↓
benchmark reproduction
        ↓
security/configuration review
        ↓
documentation
        ↓
architecture diagrams
        ↓
demo data + automation
        ↓
application presentation polish
        ↓
README
        ↓
technical case study
        ↓
portfolio materials
        ↓
resume bullets
        ↓
interview walkthrough
        ↓
release / tag v1.0
```

The governing transition is:

```text
Course 2C
Does the complete system work?

        ↓

Course 3
Can another engineer understand,
reproduce, evaluate, and appreciate it?
```

No major new technical domain should be required for Course 3.

---

# 28. Status

**Syllabus v0.1**

This syllabus completes the Swift / Apple systems arc.

Its destination is:

> **Transform the existing spatial edge platform into a coherent multi-device Apple-native system with a constrained Watch node, a rich iPhone spatial/3D node, simulated Rust nodes, and a macOS operator hub over the Rust/Python/PostGIS backend.**

The curriculum progression is now:

```text
0  Rust for Geospatial Systems
        ↓
1  Spatial Systems & Distributed Computing
        ↓
2A Swift for Spatial & Edge Computing
        ↓
2B Swift for 3D Spatial & Edge Computing
        ↓
2C Apple Spatial Systems Capstone
        ↓
3  Spatial Systems Engineering Portfolio Capstone
```

Course 3 will complete the circle by turning that engineering journey into a stable, reproducible, well-documented, portfolio-ready artifact.
