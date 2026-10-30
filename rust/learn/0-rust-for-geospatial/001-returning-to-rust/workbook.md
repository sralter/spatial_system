# Lesson 001 — Returning to Rust

**Created:** October 30, 2026  
**Status:** Not started  
**Scope:** Review of Unit 1 and the covered portion of Unit 2  
**Time:** Approximately 30 minutes  
**Code:** [refresher.rs](refresher.rs)

This lesson resumes from the [Unit 2 checkpoint](../../progress/checkpoint/_CHECKPOINT_rust-for-geospatial-systems-unit-02-checkpoint-v3.md). Unit 1 is complete; we are rebuilding recall before continuing Unit 2. The final exercise is the exact unanswered geometry prediction exercise. No new concepts are required here.

Aim for about 8 minutes reading, 8 minutes on recall questions, 8 minutes coding, and 6 minutes on the final predictions. If a topic is rusty, record the gap and pause there. Finishing within the estimate is not an assessment criterion.

## 1. Rebuild the mental model

### The compiler is part of the learning loop

The normal Rust workflow turns source into a native executable before running it. Unlike Python's runtime type checks, Rust establishes many type and access rules before execution. Local type inference still produces concrete types: omitting a type annotation does not make a variable dynamically typed.

In Rust, a block can produce a value. Its final expression, without a semicolon, supplies that value. A semicolon discards the expression's result. Functions declare parameter and return types; expression-valued `if` branches must agree on their output type.

Bindings use immutable `let` by default. `mut` permits changing a binding's value while retaining its type. Shadowing creates a new binding and can change the type. Numeric conversions should be deliberate, particularly when coordinate precision matters.

Use the toolchain as feedback: `check` checks compilation, `fmt` formats, Clippy flags suspicious patterns, tests check selected behavior, and running shows actual execution. Passing one does not imply passing all the others.

### Representation communicates meaning

A tuple groups positional fields; a struct gives fields names. Both model values that exist together: an **AND**, or product, relationship. A database row or Python dataclass is a useful bridge. Named fields help distinguish quantities that happen to have the same primitive type.

An enum selects one variant from alternatives: an **OR**, or sum, relationship. A variant can carry data specific to that alternative. An enum is therefore more expressive than a string label whose meaning every downstream function must remember.

For example, a sensor reading could be a measured value or an unavailable reading. `Option<T>` represents `Some(T)` or `None`, making absence explicit rather than reserving an ordinary measurement such as `-9999`. It resembles Python's `None` or a nullable SQL field conceptually, but Rust requires handling its alternatives through the type system.

`match` destructures values by pattern and must cover every possible case. A wildcard `_` covers remaining cases, but explicit enum arms make each alternative visible. Do not assume the compiler knows which branch will be selected at runtime merely because it knows all the possible variants.

### Ownership controls access and duplication

For a `Copy` type such as `f64`, assignment can implicitly duplicate a value and leave the original usable. A tuple is `Copy` when all its components are `Copy`. A `String` or `Vec<T>` is not `Copy`: ordinary assignment transfers ownership rather than duplicating its heap buffer. Moving one non-`Copy` field out of a tuple or struct can leave the original only partially usable.

For `String` and vectors of coordinate tuples, `.clone()` explicitly creates an independent copy of the contents. This is a data movement decision, potentially substantial for a large spatial buffer. A move transfers ownership; it does not mean the entire heap buffer is duplicated.

An immutable borrow (`&T`) permits temporary reading without ownership transfer. A mutable borrow (`&mut T`) permits temporary modification. Our introductory rule is **many readers OR one writer**, with overlap determined by where the references are used, not simply by the closing brace of a block. This matters when a growing vector might reallocate its buffer.

These are review concepts from Unit 2, not a claim that ownership is finished. Unit 3 will develop them more systematically.

### Collections and missing values

An array `[T; N]` has a fixed length that is part of its type. A `Vec<T>` can grow while keeping one element type. `values[index]` may panic for an out-of-bounds index; `values.get(index)` returns an `Option` containing a reference when present. Lookup failure must be handled deliberately.

### CS Lens: representation and invariants

A representation determines which states you can express. Replacing a raw code with a purpose-specific enum narrows the alternatives. Naming coordinate fields improves interpretation. Neither automatically proves that coordinates share a CRS, have the correct axis order, or fall within valid ranges.

Keep three questions separate:

1. **Compiler correctness:** Is the program valid Rust?
2. **Algorithmic correctness:** Does it implement the intended computation?
3. **Geospatial correctness:** Are its CRS, units, coordinate conventions, and spatial assumptions valid?

One precision reminder when returning to the old code notes: `f64` occupies **64 bits, or 8 bytes**. A comment in `unit2_notes.rs` calls this “8 bits”; use the corrected units here.

## 2. Recall and prediction — attempt before compiling

Keep your first responses below. If you change your mind, add a revision rather than replacing them.

### R1 — Expressions and types

```rust
fn cell_count(width: u32, height: u32) -> u32 {
    width * height;
}
```

Does this compile? Explain what the function body produces and what the signature requires. Describe the smallest correction, without running it first.

**Student response:**

> Write here.

### R2 — Access and ownership

Treat these as two independent programs. Predict whether each compiles and explain why. For B, identify which use of `reader` matters to the borrow.

**A**

```rust
fn main() {
    let source = String::from("station-a");
    let destination = source;
    println!("{}", destination);
    println!("{}", source);
}
```

**B**

```rust
fn main() {
    let mut elevations = vec![12.5, 18.2];
    let reader = &elevations;
    println!("{:?}", reader);
    elevations.push(9.7);
    println!("{:?}", elevations);
}
```

**Student response — A:**

> Write here.

**Student response — B:**

> Write here.

### R3 — What does the model guarantee?

```rust
struct Coordinate {
    x: f64,
    y: f64,
}
```

What does this improve over an unnamed coordinate tuple? Name two geospatial assumptions that remain unenforced. Is `Coordinate { x: 9000.0, y: -8127.0 }` necessarily a Rust type error? Explain without assuming a CRS that the code has not specified.

**Student response:**

> Write here.

## 3. C1 — Small runnable exercise

Use [refresher.rs](refresher.rs). Write a program that:

1. Creates a vector of elevations in meters: `12.5`, `18.2`, and `9.7`.
2. Uses `.get()` and `match` to inspect index `1`, printing the elevation if present or a clear absence message otherwise.
3. Repeats the lookup for index `5`, handling both alternatives explicitly.

Use the concepts already covered. No `unwrap`, external crates, or new abstractions are needed. Both outcomes should be handled as ordinary program states.

Before running, record which lookup should find a value, which should not, and whether either should panic. Then compile and compare the result with your prediction.

**Student prediction:**

> Write here before running.

Run these commands from the repository root, `/Users/sra/files/projects/spatial_system`. The starter file compiles but has no behavior until you write your attempt. The executable goes into a temporary directory.

```sh
lesson_build_dir=$(mktemp -d /tmp/rust-lesson-001.XXXXXX)
rustc --edition 2024 rust/learn/0-rust-for-geospatial/001-returning-to-rust/refresher.rs -o "$lesson_build_dir/refresher"
# Run the next command only if compilation succeeds.
"$lesson_build_dir/refresher"
```

To inspect formatting without changing your submission:

```sh
rustfmt --edition 2024 --check rust/learn/0-rust-for-geospatial/001-returning-to-rust/refresher.rs
```

**Student observations — output or diagnostics, and how they compare with the prediction:**

```text
Paste observations here.
```

**Student explanation:** What does `.get()` let you express that a panic or a numeric sentinel would not? Does a successful lookup by itself prove that the elevation has a known vertical datum?

> Write here.

## 4. G1–G6 — Resume the exact stopping exercise

These six questions were still unanswered at the October 1 checkpoint. Predict from the code before using compiler inspection or asking for solutions.

```rust
enum Geometry {
    Point(f64, f64),
    LineString(Vec<(f64, f64)>),
}

let a = Geometry::Point(-73.9857, 40.7484);

let b = Geometry::LineString(vec![
    (-73.9857, 40.7484),
    (-73.9840, 40.7490),
]);
```

The `let` bindings are an excerpt from a function body. If you later experiment with this code, put the bindings inside `fn main()`.

For comparison, the earlier model contained only labels:

```rust
enum GeometryType {
    Point,
    LineString,
    Polygon,
}
```

**G1. What is the type of `a`?**

> Write here.

**G2. What is the active variant of `a`?**

> Write here.

**G3. What are the payload types inside `Geometry::Point(...)`?**

> Write here.

**G4. What is the type of `b`?**

> Write here.

**G5. What is the payload type inside `Geometry::LineString(...)`?**

> Write here.

**G6. Why is this representation closer to WKT than the earlier `GeometryType` enum?**

> Write here.

## 5. Submit and resume

- [ ] Recorded R1–R3 predictions and explanations.
- [ ] Attempted C1 and recorded prediction plus observed behavior.
- [ ] Attempted G1–G6 without receiving solutions.
- [ ] Identified any uncertainty below.
- [ ] Changed the lesson status to `Awaiting review` when ready.

**Student questions or confidence gaps:**

> Write here, or say “none identified.”

Ask for review of Lesson 001 when ready. Your answers and code will be reviewed here, with your original attempt preserved. New material begins after that review and any needed revision.

## Instructor review

Pending student attempt. No assessment or completion has been recorded.

Future feedback will be dated and reference R1–R3, C1, and G1–G6. It will distinguish correctness, Rust idiom, and systems/geospatial reasoning as relevant.

## Student revisions after review

Leave original answers intact. Add question IDs and revised reasoning here after feedback.

## Resume record

**Current next action:** Student begins the refresher and submits an attempt.  
**Unresolved:** Review recall and code; all six historical geometry predictions await student answers.  
**Next lesson:** Not generated. After review, continue Unit 2 gradually with structured enum payloads and structs combined with enums.
