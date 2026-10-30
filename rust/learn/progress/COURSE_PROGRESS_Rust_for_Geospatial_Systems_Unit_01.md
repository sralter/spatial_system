# Rust for Geospatial Systems --- Course Progress

## Unit 01 Boundary: From Python to Rust

**Course:** Rust for Geospatial Systems\
**Unit:** 01 --- From Python to Rust\
**Status:** COMPLETE\
**Completed:** September 30, 2026\
**Repository:** `spatial_system`\
**Rust package:** `rust/spatial-core`\
**Primary Unit 01 artifacts:** -
`rust/spatial-core/src/bin/unit1_experiments.rs` -
`rust/spatial-core/src/bin/unit1_consolidation.rs`

------------------------------------------------------------------------

## Purpose

This is the durable course-progress boundary for Unit 01. It supersedes
the detailed in-progress Unit 01 checkpoint files as the normal resume
point.

It preserves what was actually learned, the code and tooling exercised,
the main Python-to-Rust conceptual bridges, and the state from which the
next course unit should begin.

The course uses the student's existing Python, SQL, Spatial SQL,
PostGIS, GIS, and geospatial-processing experience as bridges into Rust.
The objective is not merely Rust syntax. The larger goal is
understanding correctness, memory-conscious computation, performance,
systems concepts, and how Rust can contribute to high-performance
geospatial systems.

A recurring distinction established in Unit 01 is:

``` text
compiler correctness
!= algorithmic correctness
!= geospatial correctness
```

Rust can enforce many structural properties of a program, but it cannot
automatically know whether a CRS is appropriate, whether coordinates
share a CRS, whether Euclidean distance is valid for the data, whether a
threshold is scientifically meaningful, or whether precision loss is
acceptable.

------------------------------------------------------------------------

## 1. Compilation and execution

The course began by contrasting Python's runtime-oriented workflow with
Rust's compiled workflow:

``` text
Python source -> Python interpreter/runtime -> execution

Rust source -> compiler -> native executable -> execution
```

The first programs were compiled directly with:

``` bash
rustc first_rust_script.rs
./first_rust_script
```

Central mental model:

> In Rust, the compiler is an active participant in writing the program.

The first working function pattern was:

``` rust
fn double_distance(distance: f64) -> f64 {
    distance * 2.0
}
```

This introduced `fn`, typed parameters, explicit return types, `main()`,
`println!`, and native compilation.

------------------------------------------------------------------------

## 2. Expressions, statements, and semicolons

Rust is expression-oriented.

Correct:

``` rust
fn double_distance(distance: f64) -> f64 {
    distance * 2.0
}
```

Incorrect for this return type:

``` rust
fn double_distance(distance: f64) -> f64 {
    distance * 2.0;
}
```

The semicolon turns the final expression into a statement and discards
its value. Blocks can also produce values:

``` rust
let doubled = {
    let distance = 83.2;
    distance * 2.0
};
```

This model was later reused with `if`, `match`, and `loop`.

The unit type `()` was introduced loosely as representing no meaningful
returned value.

------------------------------------------------------------------------

## 3. Scalar types and type inference

Scalar types introduced:

``` text
i32  signed 32-bit integer
i64  signed 64-bit integer
u32  unsigned 32-bit integer
f32  32-bit floating point
f64  64-bit floating point
bool Boolean
```

Otherwise-unconstrained literals normally fall back to:

``` text
42    -> i32
42.0  -> f64
true  -> bool
```

Surrounding context can constrain a different type.

The course used:

``` rust
std::any::type_name_of_val(&value)
```

as a learning/debugging aid. The meaning of `&` was intentionally
deferred until borrowing is formally taught.

Static typing does not mean every local variable must be manually
annotated. Rust can infer concrete types while still enforcing them at
compile time.

------------------------------------------------------------------------

## 4. `f32` versus `f64` in geospatial work

Approximate floating-point precision:

``` text
f32  ~7 decimal digits
f64  ~15-16 decimal digits
```

For projected coordinates such as `583421.734829`, `f32` can lose
meaningful sub-meter precision because many significant digits are
already used before the decimal point.

Working rule:

> Use `f64` as the default for general coordinate geometry unless there
> is a specific, understood reason to use `f32`.

`f32` may later be appropriate for large rasters, embeddings, or other
memory-intensive workloads where four bytes versus eight bytes per value
materially affects memory use.

------------------------------------------------------------------------

## 5. Immutability, mutation, scope, and shadowing

Bindings are immutable by default:

``` rust
let distance = 83.2;
```

Reassignment requires:

``` rust
let mut distance = 83.2;
distance = 100.0;
```

The compiler error `E0384` was intentionally triggered to learn this
rule.

Important distinction:

``` text
mutation
    same binding
    same type
    value may change

shadowing
    new binding
    same name reused
    type may change
```

Example:

``` rust
let distance = 50;
let distance = distance + 25;
let distance = distance as f64 / 2.0;
```

The final binding is `37.5_f64`.

Rust block scope was also introduced:

> Inner scopes can access bindings from surrounding scopes, but
> surrounding scopes cannot access bindings created only inside an inner
> scope.

This was contrasted with Python, where an `if` block does not create a
separate variable scope.

------------------------------------------------------------------------

## 6. Numeric casting, rounding, and information loss

Primitive numeric casting with `as` was introduced:

``` rust
let count: i32 = 42;
let count_as_float = count as f64;
```

A key distinction:

``` text
83.7_f64 as i32          -> 83
83.7_f64.round()         -> 84.0
83.7_f64.round() as i32  -> 84
```

Casting `f64` to an integer truncates the fractional portion; it does
not round.

Mixed numeric operations also require deliberate representation choices:

``` rust
let building_count = 42;
let average_area = 125.5;
let total_area = building_count as f64 * average_area;
```

Rust does not silently decide how `i32 * f64` should be handled.

Geospatial lesson:

> Rust permitting a cast does not mean the cast is appropriate for GIS.

Casting coordinate values from `f64` to integer may discard information
that matters for coordinate fidelity, distances, topology, spatial
joins, or geometry quality.

------------------------------------------------------------------------

## 7. Control flow

### `if` as an expression

``` rust
let label = if distance <= threshold {
    "near"
} else {
    "far"
};
```

Branches used as an expression must produce compatible types.

A deliberate error demonstrated an `E0308` mismatch when branches
produced incompatible types.

### Boolean conditions

Rust does not use Python-style truthiness.

Invalid:

``` rust
if building_count {
    ...
}
```

Valid:

``` rust
if building_count > 0 {
    ...
}
```

Conditions must evaluate to `bool`.

------------------------------------------------------------------------

## 8. Arrays, loops, and ranges

Arrays were introduced:

``` rust
let distances = [-73.5, 25.0, 50.0, 83.2, 100.0, 142.7];
```

The type contains both element type and length:

``` text
[f64; 6]
```

`Vec<T>` was deliberately deferred.

Loop constructs covered:

``` text
for
while
loop
```

Ranges:

``` rust
0..5    // upper bound excluded
0..=5   // upper bound included
```

A `while` exercise demonstrated that checking `distance < 100` before an
iteration does not prevent the loop body from moving the final value
beyond 100.

`loop` and `break` were introduced, including loops that produce values:

``` rust
let final_distance = loop {
    distance += 30;

    if distance >= 100 {
        break distance;
    }
};
```

------------------------------------------------------------------------

## 9. `match` and exhaustive pattern matching

Basic `match` syntax:

``` rust
match code {
    0 => "missing",
    1 => "poor",
    2 => "fair",
    3 => "good",
    _ => "unknown",
}
```

`=>` separates a pattern from the expression/action associated with it.
A useful SQL bridge is `WHEN ... THEN`.

Rust requires `match` to be exhaustive. Removing the catch-all
intentionally produced:

``` text
error[E0004]: non-exhaustive patterns
```

The compiler identified the uncovered ranges of the `i32` domain.

Pattern forms covered:

``` rust
1 => ...
1 | 2 => ...
0..=49 => ...
_ => ...
```

Important distinction:

``` text
1 | 2    pattern OR
a || b   Boolean OR
```

`match` established an important Rust principle:

> Exhaustive handling can make unhandled program states visible at
> compile time.

------------------------------------------------------------------------

## 10. Constants

Rust constants were introduced:

``` rust
const MAX_DISTANCE_M: f64 = 2_000.0;
```

Mental model:

``` text
immutable `let`
    ordinary binding
    cannot be reassigned
    can be shadowed by a new binding

const
    fixed constant
    explicit type required
    cannot be reassigned
```

Unlike uppercase Python "constants," Rust `const` is language-enforced.

------------------------------------------------------------------------

## 11. Documentation comments

Rust documentation comments use:

``` rust
/// Classifies distance in meters.
fn classify_distance(...) {
    ...
}
```

Documentation should emphasize assumptions that the type signature
cannot encode, especially in geospatial functions:

-   CRS;
-   units;
-   transformations;
-   valid input domains;
-   algorithmic assumptions.

Cargo documentation commands were introduced:

``` bash
cargo doc
cargo doc --open
```

------------------------------------------------------------------------

## 12. Compiler diagnostics and learning workflow

Compiler diagnostics were treated as part of development rather than
merely obstacles.

Important errors encountered:

``` text
E0384
cannot assign twice to immutable variable
```

``` text
E0308
mismatched types
```

Examples included:

``` text
expected `i64`, found `i32`
expected `bool`, found integer
expected `&str`, found integer
expected `f64`, found `&str`
```

and:

``` text
E0004
non-exhaustive patterns
```

Useful command:

``` bash
rustc --explain E0308
```

Core learning loop:

``` text
predict -> compile -> read -> explain -> correct
```

------------------------------------------------------------------------

## 13. Cargo workflow

The Cargo package was confirmed at:

``` text
rust/spatial-core/
├── Cargo.toml
├── Cargo.lock
├── src/
└── target/
```

Cargo became the normal workflow instead of direct `rustc`.

Commands exercised:

``` bash
cargo check
cargo fmt
cargo fmt --check
cargo clippy
cargo run
cargo test
```

For a particular binary target:

``` bash
cargo check --bin unit1_consolidation
cargo clippy --bin unit1_consolidation
cargo run --bin unit1_consolidation
cargo test --bin unit1_consolidation
```

Basic terminology:

``` text
package
    Cargo-managed project described by Cargo.toml

crate
    Rust compilation unit

target
    something Cargo can build, such as a binary or library
```

The package contains multiple targets, including:

``` text
src/lib.rs
src/bin/unit1_experiments.rs
src/bin/unit1_consolidation.rs
```

A practical layered workflow was established:

``` text
cargo check
    valid Rust?

cargo fmt
    standard formatting?

cargo clippy
    suspicious or non-idiomatic patterns?

cargo test
    expected behavior preserved?

cargo run
    runtime behavior?
```

The development/test profiles were observed as unoptimized builds with
debug information. Release builds were mentioned but not explored in
depth.

------------------------------------------------------------------------

## 14. Formatting and Clippy

A deliberate formatting violation demonstrated:

``` text
cargo check success
!=
cargo fmt --check success
```

A deliberate unnecessary mutable binding:

``` rust
let mut distance = 42;
```

produced a warning that the variable did not need to be mutable.

This reinforced:

``` text
valid code
!= well-formatted code
!= idiomatic/high-quality code
```

Clippy was treated primarily as a linting and code-quality tool rather
than as a performance optimizer.

------------------------------------------------------------------------

## 15. Tests, macros, and attributes

The default library test generated by Cargo was inspected:

``` rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
```

Introductory concepts:

``` text
#[test]
    attribute marking a test

#[cfg(test)]
    conditionally include the module for testing

assert_eq!
    assertion macro

println!
    macro
```

A useful bridge was established:

``` text
Python @decorator
Rust   #[attribute]
```

with the explicit caveat that they are not equivalent mechanisms.

------------------------------------------------------------------------

## 16. Final Unit 01 consolidation artifact

The final exercise created:

``` text
rust/spatial-core/src/bin/unit1_consolidation.rs
```

It contains:

``` rust
const MAX_DISTANCE_M: f64 = 2_000.0;
```

A distance classifier implemented with an `if` expression:

``` text
negative          -> invalid
0 through 100     -> near
>100 through 500  -> medium
>500 through 2000 -> far
>2000             -> outside
```

A quality classifier implemented with `match`:

``` text
0       -> missing
1 | 2   -> usable
3       -> good
other   -> unknown
```

Final runtime output:

``` text
Classify distances:
-10: invalid
25: near
250: medium
1500: far
2500: outside
Classify qualities:
0: missing
1: usable
2: usable
3: good
9: unknown
```

The artifact passed:

``` bash
cargo fmt
cargo check --bin unit1_consolidation
cargo clippy --bin unit1_consolidation
cargo run --bin unit1_consolidation
```

without errors or Clippy warnings.

------------------------------------------------------------------------

## 17. Final Unit 01 tests

Two unit tests were added:

``` text
tests::classifies_distance_boundaries
tests::classifies_quality_codes
```

Distance tests deliberately exercise boundaries around:

``` text
0
100
500
MAX_DISTANCE_M
```

including fractional values immediately beyond boundaries.

Final result:

``` text
running 2 tests
test tests::classifies_distance_boundaries ... ok
test tests::classifies_quality_codes ... ok

test result: ok. 2 passed; 0 failed; 0 ignored
```

The final consolidation binary therefore compiles, formats, lints, runs,
and passes its tests.

------------------------------------------------------------------------

## 18. Python/SQL-to-Rust bridges established

These are intuition bridges, not exact equivalences:

``` text
Python / SQL                    Rust

def                             fn
type hints                      enforced static types
x = value                       let x = value;
mutable-by-default thinking     immutable-by-default binding
if / elif / else                if / else if / else
conditional expression          if expression
for x in values                 for x in values
while                           while
while True                      loop
break                           break
fixed homogeneous collection    array [T; N]
Python match / SQL CASE         match
@decorator                      #[attribute] (similar role, different mechanism)
pytest                          cargo test
Black                           cargo fmt
Ruff-style linting              cargo clippy
pyproject-style metadata        Cargo.toml
```

------------------------------------------------------------------------

## 19. Principles to carry into later units

1.  **Predict before compiling.** Use the compiler to test a mental
    model rather than blindly following diagnostics.

2.  **Make meaningful representation changes explicit.** Numeric casts,
    mutation, function signatures, and control-flow outputs should
    reveal intent.

3.  **Prefer immutability unless mutation is genuinely part of the
    algorithm.**

4.  **Compiler correctness is not domain correctness.** Rust cannot
    protect against an incorrect CRS, inappropriate spatial algorithm,
    or scientifically invalid assumption unless those constraints are
    deliberately represented.

5.  **Preserve precision deliberately.** Representation choices matter
    for coordinates and geometry.

6.  **Put invariants close to the operation responsible for them.**

7.  **Use the Rust toolchain as layered feedback:** check, format, lint,
    test, run.

8.  **Exhaustive handling is a correctness tool.** `match` can make
    unhandled states visible.

9.  **Inference is constraint-driven, not guessing.**

10. **Do not optimize representation merely because a smaller type
    exists.** Understand the tradeoff first.

------------------------------------------------------------------------

## 20. Topics intentionally not yet taught

The following have been previewed or incidentally seen but should still
be treated as new material:

-   ownership;
-   moves;
-   borrowing;
-   references;
-   lifetimes beyond incidental syntax;
-   `String` versus `&str` in depth;
-   `Vec<T>`;
-   structs;
-   enums in depth;
-   `Option<T>`;
-   `Result<T, E>`;
-   traits;
-   generics;
-   `.into()`, `From`, and `TryFrom` in depth;
-   iterators in depth;
-   closures;
-   modules and visibility in depth;
-   heap versus stack in depth;
-   geospatial Rust crates and algorithms;
-   Arrow / GeoArrow integration;
-   Python/Rust interoperability;
-   PyO3;
-   performance profiling;
-   concurrency and parallelism.

Do not assume these are understood merely because some related syntax
appeared in Unit 01.

------------------------------------------------------------------------

## 21. Course handoff

### Unit 01 --- From Python to Rust: COMPLETE

The next course thread should use the canonical
`0-rust-for-geospatial-systems-syllabus-v0.2.md` syllabus and begin with
the unit that follows Unit 01.

The student should enter the next unit comfortable with:

``` text
fn and main()
scalar types
type inference
immutable let and mut
expressions and semicolons
if expressions
for / while / loop
ranges
scope
shadowing
numeric casts
const
arrays
match
compiler diagnostics
Cargo workflow
cargo fmt
cargo clippy
basic unit tests
attributes at an introductory level
```

Do **not** repeat Unit 01 from scratch.

The durable repository evidence for Unit 01 is:

``` text
rust/spatial-core/src/bin/unit1_experiments.rs
rust/spatial-core/src/bin/unit1_consolidation.rs
```

The consolidation artifact was verified on September 30, 2026 to:

``` text
compile successfully
format successfully
pass Clippy without warnings
run with expected output
pass 2/2 unit tests
```

### Recommended new-thread bootstrap

Upload this file in the new course thread and say:

> Continue my Rust for Geospatial Systems course from this boundary
> document. Unit 01 is complete. Use the canonical v0.2 syllabus and
> begin the next unit. Continue the same teaching style: introduce one
> concept at a time using Python/SQL/GIS bridges, have me predict or
> attempt exercises before giving solutions, and emphasize compiler
> reasoning, systems concepts, and geospatial correctness. Also make 
> sure to sprinkle in computer science concepts throughout, 
> as appropriate, following the cs lens directive of the other 
> course documents.
