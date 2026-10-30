# Rust for Geospatial Systems --- Unit 02 Checkpoint

**Course:** Rust for Geospatial Systems  
**Unit:** 02 --- Data Has Shape  
**Status:** In progress  
**Progress saved:** October 1, 2026  
**Repository:** `spatial_system`

## Purpose

This checkpoint preserves Unit 02 through the introduction of structs, product-versus-sum type modeling, and enum variants carrying geospatial payload data.

The course continues to use Python, SQL, PostGIS, GIS, and geospatial-processing concepts as bridges into Rust.

Teaching sequence:

```text
introduce one concept at a time
→ connect it to Python / SQL / GIS
→ predict compiler/runtime behavior
→ attempt the exercise
→ inspect the result
→ refine the mental model
```

Recurring distinction:

```text
compiler correctness
≠ algorithmic correctness
≠ geospatial correctness
```

---

## 1. Unit 02 theme: data has shape

Unit 02 focuses on how representation affects:

- correctness;
- invariants;
- memory behavior;
- performance;
- readability;
- API design;
- geospatial semantics.

Central question:

> How far can we improve correctness by choosing better representations?

---

## 2. Topics covered so far

Substantially introduced:

```text
tuples
product types
tuple destructuring
Copy
String
moves
partial moves
Clone
Vec<T>
immutable borrowing
mutable borrowing
aliasing
many-readers / one-writer rule
non-lexical lifetime intuition
Vec indexing
bounds checking
runtime panic
.get()
Option<T>
Some / None
match
pattern matching
exhaustive matching
wildcard `_`
nested match
enum basics
enum exhaustiveness
application-specific CRS modeling
enum variants carrying data
struct basics
structs as product types
structs containing enums
sum types nested inside product types
```

---

## 3. Product types

A product type represents:

```text
A AND B AND C
```

Examples:

```rust
(f64, f64, i32)
```

and:

```rust
struct Observation {
    x: f64,
    y: f64,
    elevation_m: f64,
}
```

A valid `Observation` contains:

```text
x
AND
y
AND
elevation_m
```

All fields exist together.

---

## 4. Sum types

A sum type represents:

```text
A OR B OR C
```

Example:

```rust
enum SupportedCrs {
    Wgs84,
    Utm18N,
    Nad83Utm18N,
}
```

A `SupportedCrs` value is exactly one of:

```text
Wgs84
OR
Utm18N
OR
Nad83Utm18N
```

Another example:

```rust
enum SpatialValue {
    Elevation(f64),
    BuildingCount(i32),
}
```

A `SpatialValue` is:

```text
Elevation(f64)
OR
BuildingCount(i32)
```

---

## 5. Structs

Example:

```rust
struct Observation {
    x: f64,
    y: f64,
    elevation_m: f64,
}
```

Creating a value:

```rust
let obs = Observation {
    x: 583421.73,
    y: 4512398.12,
    elevation_m: 18.2,
};
```

Important distinction:

```text
type:
    Observation

fields:
    x: f64
    y: f64
    elevation_m: f64
```

The type of `obs` is simply:

```rust
Observation
```

not:

```text
Observation(f64, f64, f64)
```

---

## 6. Struct versus tuple

Tuple representation:

```rust
let obs = (583421.73, 4512398.12, 18.2);
```

Field access:

```rust
obs.0
obs.1
obs.2
```

Struct representation:

```rust
let obs = Observation {
    x: 583421.73,
    y: 4512398.12,
    elevation_m: 18.2,
};
```

Field access:

```rust
obs.x
obs.y
obs.elevation_m
```

The struct communicates semantic field names instead of relying on positional meaning.

---

## 7. Python dataclass bridge

Rust struct:

```rust
struct Observation {
    x: f64,
    y: f64,
    elevation_m: f64,
}
```

is conceptually similar to:

```python
@dataclass
class Observation:
    x: float
    y: float
    elevation_m: float
```

Both are product-type-like structures:

```text
x AND y AND elevation
```

Important distinction from enums:

```text
struct / dataclass
    product type
    fields exist together

enum
    sum type
    one variant or another
```

---

## 8. Structs still do not automatically encode all GIS semantics

This struct:

```rust
struct Observation {
    x: f64,
    y: f64,
    elevation_m: f64,
}
```

still does not encode:

- CRS;
- horizontal units;
- axis order;
- geographic versus projected coordinates;
- timestamp;
- source/sensor;
- uncertainty;
- vertical datum;
- whether elevation is orthometric or ellipsoidal.

Important principle:

> A stronger representation can improve correctness without being a complete domain model.

---

## 9. Struct containing an enum

A struct can contain an enum field.

Example:

```rust
enum GeometryType {
    Point,
    LineString,
    Polygon,
}

struct Clinic {
    id: i64,
    x: i64,
    y: i64,
    geom: GeometryType,
}
```

Creating a value:

```rust
let clinic = Clinic {
    id: 123,
    x: 75,
    y: -45,
    geom: GeometryType::Point,
};
```

Important nested-type interpretation:

```text
Clinic
=
id
AND x
AND y
AND geom
```

while:

```text
GeometryType
=
Point
OR LineString
OR Polygon
```

This is a **sum type nested inside a product type**.

---

## 10. Enum path syntax

If a field has type:

```rust
GeometryType
```

the variant is normally written as:

```rust
GeometryType::Point
```

not merely:

```rust
Point
```

unless the variant has been separately imported into scope.

`::` remains Rust's path separator.

---

## 11. Geometry type versus geometry value

This enum:

```rust
enum GeometryType {
    Point,
    LineString,
    Polygon,
}
```

only stores the geometry **kind**.

For example:

```rust
GeometryType::Point
```

means:

> this is a point geometry

but it does not encode:

- coordinate values;
- coordinate sequence;
- CRS;
- actual location.

This distinction became the bridge to WKT.

---

## 12. WKT analogy

WKT carries both:

```text
geometry kind
+
geometry coordinates
```

Examples:

```text
POINT (x y)

LINESTRING (x1 y1, x2 y2, ...)

POLYGON ((...))
```

Therefore a Rust geospatial model becomes stronger if each geometry variant carries the data appropriate to that geometry type.

---

## 13. Enum variants carrying geometry data

Latest concept introduced:

```rust
enum Geometry {
    Point(f64, f64),
    LineString(Vec<(f64, f64)>),
}
```

Example values:

```rust
let a = Geometry::Point(-73.9857, 40.7484);

let b = Geometry::LineString(vec![
    (-73.9857, 40.7484),
    (-73.9840, 40.7490),
]);
```

Conceptually:

```text
Geometry
=
Point(x AND y)
OR
LineString(sequence of x,y pairs)
```

This combines:

```text
sum type at the outer level
+
product / collection payload inside each variant
```

It is closer to the WKT idea than a geometry-type-only enum.

---

## 14. Current mental model for enum payloads

Earlier example:

```rust
enum SpatialValue {
    Elevation(f64),
    BuildingCount(i32),
}
```

For:

```rust
let value = SpatialValue::Elevation(18.2);
```

the correct interpretation is:

```text
type    = SpatialValue
variant = Elevation
payload = 18.2_f64
```

Likewise:

```rust
let a = Geometry::Point(-73.9857, 40.7484);
```

should be reasoned about as:

```text
type    = Geometry
variant = Point
payload = two f64 values
```

The student has **not yet answered the prediction exercise for this geometry example**.

---

## 15. Six unanswered prediction questions

Resume from this exact exercise.

Do **not** provide the answers before the student attempts them.

Given:

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

The student still needs to predict:

1. What is the type of `a`?
2. What is the active variant of `a`?
3. What are the payload types inside `Geometry::Point(...)`?
4. What is the type of `b`?
5. What is the payload type inside `Geometry::LineString(...)`?
6. Why is this representation closer to WKT than the earlier `GeometryType` enum?

This is the exact stopping point.

---

## 16. Earlier ownership and borrowing concepts that remain active

### Copy

```text
cheap implicit duplication
original remains usable
```

### Move

```text
ownership transfers
original becomes unusable
```

### Clone

```text
explicit duplication
original remains usable
```

### Immutable borrow

```rust
&T
```

Temporary read access without ownership transfer.

### Mutable borrow

```rust
&mut T
```

Temporary read/write access without ownership transfer.

Simplified borrowing rule:

```text
many readers
OR
one writer
```

---

## 17. `Vec<T>` concepts that remain active

Dynamic vector:

```rust
Vec<T>
```

Example:

```rust
Vec<(f64, f64)>
```

means:

> dynamically sized vector of coordinate tuples.

Contrast:

```text
[T; N]
    fixed-length array

Vec<T>
    dynamically sized vector
```

Rust uses zero-based indexing.

Direct indexing:

```rust
values[index]
```

may panic if out of bounds.

Safe lookup:

```rust
values.get(index)
```

returns an `Option`.

---

## 18. `Option<T>` and `match`

Conceptually:

```text
Option<T>
=
Some(T)
OR
None
```

Example:

```rust
match value {
    Some(x) => ...,
    None => ...,
}
```

`match` must be exhaustive.

The compiler may not know the runtime value, but it knows the state space allowed by the type.

Wildcard:

```rust
_
```

can cover all remaining cases.

---

## 19. Compiler-assisted domain modeling

Recurring Unit 02 insight:

```text
raw primitive types
    permit many semantically invalid states

stronger domain types
    narrow the representable state space
```

Examples:

```text
raw EPSG i32
vs
SupportedCrs enum

-9999 sentinel
vs
Option<T>

(f64, f64, f64)
vs
Observation struct

GeometryType::Point
vs
Geometry::Point(x, y)
```

The type system can enforce only what has actually been encoded into the type model.

---

## 20. Current course position

Unit 02 is in progress.

The next move is **not** to jump ahead.

Resume by asking the student to answer the six unanswered geometry prediction questions above.

After those are reviewed, continue gradually into:

```text
enum variants carrying structured payloads
structs combined with enums
methods / impl
Option<T> and match reinforcement
if let
```

Do not assume mastery yet of:

- explicit lifetime syntax;
- slices such as `&[T]`;
- `String` versus `&str` in depth;
- advanced ownership;
- traits in depth;
- `Result<T, E>`;
- geospatial crates;
- Cargo architecture;
- PyO3.

The immediate conceptual anchor remains:

```text
struct
    A AND B

enum
    A OR B

enum variant with payload
    one selected state carrying state-specific data
```
