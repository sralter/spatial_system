// 2.1: Tuples

// the shape of the data is part of its type

// fn main() {
//     let coordinate = (583421.73, 4512398.12); // (f64, f64)

//     println!("{:?}", coordinate);
// }

// This is legal Rust:
// let observation = (583421.73, 4512398.12, "building");

// Arrays like
// let coordinate = [583421.73, 4512398.12];
// have the type: [f64; 2]
// Arrays must all be the same type. Tuples can be collections of different types.

// Imagine a database row:
// SELECT
//     longitude,
//     latitude,
//     elevation_m
// FROM observations;
// 
// one row would be: (-73.9857, 40.7484, 12.7)
// resembling a tuple: let observation = (-73.9857, 40.7484, 12.7); // (f64, f64, f64)
// You can access tuple fields by position (zero-index):
// fn main() {
//     let coordinate = (583421.73, 4512398.12);

//     println!("{}", coordinate.0);
//     println!("{}", coordinate.1);
// }
// coordinate.0
// (coordinate.x will come into play when we reach structs)

// Also, tuples' values can have the same type even though they represent different CRS/Units:
// let projected = (583421.73, 4512398.12); // Easting, northing, units: meters, CRS: UTM
// let geographic = (-73.9857, 40.7484); // longitude, latitude, units: degrees, CRS: EPSG:4326

// fn main() {
// 	let observation = (-73.9857, 40.7484, 12);

// 	println!("{}", observation.0);
// 	println!("{}", observation.1);
// 	println!("{}", observation.2);
// }

// tuple / struct → AND relationships → product types
// enum           → OR relationships  → sum types

// A tuple can encode longitude and latitude, but it won't be able to determine if the value is impossible:
// (9000.0, -8127.0) // illegal lon/lat values
// compiler correctness ≠ domain correctness ≠ geospatial correctness

// 2.2: Tuple destructuring

// let observation = (-73.9857, 40.7484, 12);
// let (longitude, latitude, building_count) = observation;
// (-73.9857, 40.7484, 12)
//       │        │     │
//       ▼        ▼     ▼
//  longitude latitude building_count
// This is called "pattern destructuring"
// Like in Python: observation = (-73.9857, 40.7484, 12); longitude, latitude, building_count = observation

// fn main() {
//     let coordinate = (583421.73, 4512398.12);

//     let (x, y) = coordinate;

//     println!("coordinate: {:?}", coordinate);
//     println!("x: {}", x);
//     println!("y: {}", y);
// }

// fn main() {
//     let observation = (
//         String::from("building"),
//         583421.73,
//         4512398.12,
//     );

//     let (feature_type, x, y) = observation;

//     println!("type: {}", feature_type);
//     println!("x: {}", x);
//     println!("y: {}", y);

//     // println!("observation: {:?}", observation);
// }
// "{:?}" is Rusts' debug formatting, like the f-string in Python
// let point = (1.0, 2.0);
// println!("{:?}", point);

// Concept of "::"
// Think:
// A::B
// B belonging to / associated with / located under A
// (this is casting: value as f64)
// It's very roughly like Python's Class.method() architecture: SomeClass.some_method(...)

// A String can be: "road", "buliding", "Washington Monument", and all of these have different sizes.
// String type contains metadata including:
// - where its character bytes live
// - how many bytes are currently used
// - how much memory has been allocated

// 2.3 Move semantics

// an f64 coordinate is easy to copy, it's only 8 bits:
// let x = 583421.73;
// But imagine a 4 GB raster, or a table of points 200 million rows long.
// This is where Rust shines, being a systems language, because it forces us to think about whether operations mean:
// copy the data
// move ownership
// borrow the data
// share the data

// Some types are 'Copy' types and others are not:
// f64     → Copy
// i32     → Copy
// bool    → Copy
// String  → not Copy

// fn main() {
// 	let feature_type = String::from("building");

// 	let another_name = feature_type;
// //  let another_name = feature_type.clone(); // safe implementation if you want to copy the value

// 	println!("another: {}", another_name);
// 	println!("original: {}", feature_type);
// }

// Move vs Copy vs Clone
// Moves reassign the metadata to the newest binding. It doesn't duplicate everything.
// Move ≈ O(1)
// Deep copy ≈ O(n)
// This is valid:
// let x = 42;
// let y = x;
// Because types liek i32, f64, and bool can be copied.
// For something like String, use .clone() if you want to duplicate it, but it must be explicit.
// Copy
//     implicit duplication is allowed
// Clone
//     explicit duplication is available

// fn main() {
// 	let feature_type = String::from("building");

// 	let another_name = feature_type.clone();

// 	println!("original: {}", feature_type);
// 	println!("another: {}", another_name);
// }

// if a: Vec<(f64, f64)>:
// let b = a;
// is much cheaper than:
// let b = a.clone();

// copy vs move vs clone redux:
// 	copy
	// let x = 42;
	// let y = x;
	// x valid
	// y valid
	// implicit duplicate
	// cheap Copy type
// move
	// let a = String::from("building");
	// let b = a;
	// a no longer usable
	// b owns original resource
	// no deep duplication
// clone
	// let a = String::from("building");
	// let b = a.clone();
	// a valid
	// b valid
	// explicit independent duplicate

// language semantics become systems architecture

// 2.4 Why borrowing needs to exist

// a move transfers ownership. A borrow does not.
// concept of &
// for now, think of & as roughly "borrow/reference this value rather than transfer ownership"

// the & here is saying: Give this function temporary read access to the vector, because all we need is to ask the .len() of the points.
// fn point_count(points: &Vec<(f64, f64)>) -> usize {
//     points.len()
// }

// fn main() {
//     let points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//         (-73.9825, 40.7501),
//     ];

//     let count = point_count(&points);

//     println!("count: {}", count);
//     println!("points: {:?}", points);
// }

// Vec vs Array

// Vec<T> means a dynamically-sized vector containing values of type T
// Vec<(f64, f64)> means a dynamically-sized vector of coordinate-like (f64, f64) tuples.

// [f64; 3] is an array of exactly three f64 values.

// array
// [T; N]
// fixed length
// fixed types

// Vec
// Vec<T>
// dynamic length
// fixed types

// Move: ownership changed
	// let b = a;
	// before: a owns data
	// after: a  X
// 		  b owns data
// Clone: makes two independent owned resources
	// let b = a.clone();
	// a owns data A
	// b owns duplicated data B
// Borrow: a still owns resource, b merely has permission to access it
	// let b = &a;
	// a
	// │
	// │ owns
	// ▼
	// data
	// ▲
	// │
	// │ temporarily refers to
	// b

// Systems design principle:
// Request the weakest capability necessary to perform the operation.

// 2.5 The first borrowing rule
// An immutable reference lets you read a value without taking ownership.

// Concept of lifetime in resources, especially relevant in borrowing
// Compare:

// Version A
// fn point_count(points: Vec<(f64, f64)>) -> usize {
//     points.len()
// }

// fn main() {
//     let points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//         (-73.9825, 40.7501),
//     ];

//     let count = point_count(points);

//     println!("count: {}", count);
//     println!("points: {:?}", points);
// }

// Version B
// fn point_count(points: &Vec<(f64, f64)>) -> usize {
//     points.len()
// }

// fn main() {
//     let points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//         (-73.9825, 40.7501),
//     ];

//     let count = point_count(&points);

//     println!("count: {}", count);
//     println!("points: {:?}", points);
// }

// This will not compile
// fn add_point(points: &Vec<(f64, f64)>) {
//     points.push((-73.9810, 40.7510));
// }

// fn main() {
//     let points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     add_point(&points);

//     println!("{:?}", points);
// }
// It won't compile because add_point wants a borrow but points.push is attempting a mutation.

// If T = Vec<(f64, f64)>, then &T = &Vec<(f64, f64)>
// (T is the conventional generic type T, in the way that foo() is the generic function name)

// Rust separates read access from write access

// 2.6 Mutable borrowing

// This will compile (compare to line ~296 above)
// note the two `mut`s!
// fn add_point(points: &mut Vec<(f64, f64)>) {
// 	points.push((-73.9810, 40.7510));
// }

// fn main() {
// 	let mut points = vec![
// 		(73.9857, 40.7484),
// 		(73.9840, 40.7490),
// 	];

// 	add_point(&mut points);

// 	println!("{:?}", points);
// }

// owner: let mut points // &T    : permission to read
// borrower: &mut points // &mut T: permission to read and write

// Compare these two. First only needs read access, second needs to modify. API documentation in code itself and enforced by compiler!
// fn point_count(points: &Vec<(f64, f64)>)
// fn add_point(points: &mut Vec<(f64, f64)>)

// fn add_point(points: &mut Vec<(f64, f64)>) {
//     points.push((-73.9810, 40.7510));
// }

// fn main() {
//     let mut points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

// 	println!("Before: {:?}", points);

//     add_point(&mut points);

//     println!("{:?}", points);
// }

// 2.7: Many readers one writer rule
// Roughly speaking: Rust allows aliasing, but only allows it if there are either A: many readers OR B: one writer. Not many readers and writers.

// This will compile:
// fn main() {
//     let points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     let first_reader = &points;
//     let second_reader = &points;

//     println!("{:?}", first_reader);
//     println!("{:?}", second_reader);
// }

// This will not:
// fn main() {
//     let mut points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     let writer = &mut points;
//     let reader = &points;

//     println!("{:?}", writer);
//     println!("{:?}", reader);
// }
// The conflict is about simultaneous access permissions

// A borrow's lifetime can end at its last actual use, rather than automatically lasting until the end of the surrounding block.

// fn main() {
//     let mut points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     let reader = &points;

//     println!("reader: {:?}", reader);

//     points.push((-73.9810, 40.7510));

//     println!("points: {:?}", points);
// }

// This will fail because a mutation can invalidate existing references.
// fn main() {
//     let mut points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     let reader = &points;

//     points.push((-73.9810, 40.7510));

//     println!("reader: {:?}", reader);
// }

// fn main(/*here's some comment, woah inline comments using SQL multiline block comment syntax!*/) {
// 	println!("Testing here!")
// }

// This works because each iteration of reader safely uses the version of points to make the print statement.
// let reader = &points;
// println!("{:?}", reader);

// points.push((-73.9810, 40.7510));

// let reader2 = &points;
// println!("{:?}", reader2);

// This compiles:
// fn main() {
//     let mut points = vec![
//         (-73.9857, 40.7484),
//         (-73.9840, 40.7490),
//     ];

//     let reader1 = &points;
//     println!("reader1: {:?}", reader1);

//     points.push((-73.9810, 40.7510));

//     let reader2 = &points;
//     println!("reader2: {:?}", reader2);
// }

// fn calculate_bbox(points: &Vec<(f64, f64)>)
// this function gets access
// this function does not own the Vec
// this reference cannot mutate the Vec
// the owner remains responsible for the Vec

// fn reproject(points: &mut Vec<(f64, f64)>)
// this function does not own the Vec
// BUT
// it receives temporary mutation rights

// fn consume_points(points: Vec<(f64, f64)>)
// this function receives ownership

// mutable borrowing is useful when you want in-place modification while preserving ownership in the caller.

// 2.8 Vec<T>

// basic Vec operations:
// points.len()
// points.push(...)
// points[0]

// fn main() {
//     let mut elevations = vec![12.5, 18.2, 9.7];

//     println!("length: {}", elevations.len());
//     println!("first: {}", elevations[0]);

//     elevations.push(21.4);

//     println!("length: {}", elevations.len());
//     println!("last: {}", elevations[3]);
// }

// compile-time errors vs. runtime panics vs. valid execution
// fn main() {
//     let elevations = vec![12.5, 18.2, 9.7];

//     println!("{}", elevations[1]);
//     println!("{}", elevations[3]);
// }

// static information
// 		known from program/type structure before execution
//  vs 
// dynamic information
// 		determined while the program runs

// fn main() {
//     let elevations = vec![12.5, 18.2, 9.7];

//     let first = elevations.get(1);
//     let missing = elevations.get(3);

//     println!("{:?}", first);
//     println!("{:?}", missing);
// }

// product types vs sum types:
// product type:
// A AND B

// sum type: Option<T> like Option<&f64>
// A OR B
// it can be destructured like how we do let (a, b) = value; --> Some(T) OR None --> can be destructured --> match value { Some(x) => ..., None => ..., }

// instead of having a sentinel value of -9999, which would require downstream functions to remember what -9999 means,
// we could encode the missingness as part of the representation itself.

// fn main() {
//     let elevations = vec![12.5, 18.2, 9.7];

//     let value = elevations.get(1);

//     match value { // "if value has the shape Some(...), do this, otherwise if it has the shape None, do that". It's pattern matching.
//         Some(elevation) => println!("Elevation: {}", elevation),
//         None => println!("No elevation found"),
//     }
// }

// for match, Rust requires 'exhaustive matching', meaning every possible variant needs to be handled.

// fn main() {
//     let elevations = vec![12.5, 18.2, 9.7];

//     let value = elevations.get(10);

//     match value {
//         Some(elevation) => println!("Elevation: {}", elevation),
//     }
// }

// 2.9 Wildcard matching
// NOTE: I am using an AI which can be fallible. We covered "_" before.
// match requires that all possible states must be covered (some + the rest can be caught by the _ wildcard)

// fn main() {
//     let crs_code = 26918;

//     match crs_code {
//         4326 => println!("WGS 84"),
//         32618 => println!("UTM Zone 18N"),
//         _ => println!("Other CRS"),
//     }
// }

// concept of closed versus open sets. i32 is basically open, compared to enum which is closed.

// enum

// enum SupportedCrs {
//     Wgs84,
//     Utm18N,
//     Nad83Utm18N,
// }

// fn describe_crs(crs: SupportedCrs) {
//     match crs {
//         SupportedCrs::Wgs84 => println!("EPSG:4326"),
//         SupportedCrs::Utm18N => println!("EPSG:32618"),
//         SupportedCrs::Nad83Utm18N => println!("EPSG:26918"),
//     }
// }

// fn main() {
//     let crs = SupportedCrs::Nad83Utm18N;

//     describe_crs(crs);
// }

// 2.10 Enums can also carry data, not just variants:
// enum SpatialValue {
//     Elevation(f64),
//     BuildingCount(i32),
// }
// SpatialValue::Elevation(18.2)
// SpatialValue::BuildingCount(42)

// enum SpatialValue {
//     Elevation(f64),
//     BuildingCount(i32),
// }

// fn describe(value: SpatialValue) {
//     match value {
//         SpatialValue::Elevation(x) => {
//             println!("Elevation: {}", x);
//         }
//         SpatialValue::BuildingCount(n) => {
//             println!("Buildings: {}", n);
//         }
//     }
// }

// fn main() {
//     let value = SpatialValue::Elevation(18.2);

//     describe(value);
// }
// here, Elevation(18.2) is a type SpatialValue, variant Elevation, and payload 18.2_f64
// enums are OR (product type), so SpatialValue can be Elevation(f64) OR BuildingCount(i32)

// 2.11 Structs: product types with names

// struct Observation { // Observation = x: f64 AND y: f64 AND elevation_m: f64
//     x: f64,
//     y: f64,
//     elevation_m: f64,
// }

// Structs are closer to dataclass from Python.
// Python:
// from dataclasses import dataclass

// @dataclass
// class Observation:
//     x: float
//     y: float
//     elevation_m: float
// obs = Observation(
//     x=583421.73,
//     y=4512398.12,
//     elevation_m=18.2,
// )
// Rust:
// let obs = Observation {
//     x: 583421.73,
//     y: 4512398.12,
//     elevation_m: 18.2,
// };

// tuples are fine for geospatial data, but structs are much better given that we will be building domain-oriented software
// obs.0 is not as good as obs.x or obs.elevation_m

// CS Lens: modeling a building record. If every building must have id, x, and y, then a struct makes sense:
// struct Building {
// 	id: i64,
// 	x: i64,
// 	y: i64,
// }

// struct Observation {
//     x: f64,
//     y: f64,
//     elevation_m: f64,
// }

// fn main() {
//     let obs = Observation {
//         x: 583421.73,
//         y: 4512398.12,
//         elevation_m: 18.2,
//     };

//     println!("x: {}", obs.x);
//     println!("y: {}", obs.y);
//     println!("elevation: {}", obs.elevation_m);
// }

// You could put an enum within a struct!
// enum GeometryType {
//     Point,
//     LineString,
//     Polygon,
// }

// struct Clinic {
//     id: i64,
//     x: i64,
//     y: i64,
//     geom: GeometryType,
// }
// let clinic = Clinic {
//     id: 123,
//     x: 75,
//     y: -45,
//     geom: GeometryType::Point,
// };
// Clinic (product)
// =
// id
// AND x
// AND y
// AND geom
// GeometryType
// =
// Point (sum)
// OR LineString
// OR Polygon

// enum variants carrying geometry data
// enum Geometry {
//     Point(f64, f64),
//     LineString(Vec<(f64, f64)>),
// }
// let a = Geometry::Point(-73.9857, 40.7484);
// let b = Geometry::LineString(vec![
//     (-73.9857, 40.7484),
//     (-73.9840, 40.7490),
// ]);

