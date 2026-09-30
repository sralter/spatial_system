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
fn point_count(points: &Vec<(f64, f64)>) -> usize {
    points.len()
}

fn main() {
    let points = vec![
        (-73.9857, 40.7484),
        (-73.9840, 40.7490),
        (-73.9825, 40.7501),
    ];

    let count = point_count(&points);

    println!("count: {}", count);
    println!("points: {:?}", points);
}

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

