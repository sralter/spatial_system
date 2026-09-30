// /// Deliberately causes compile-time error to demonstrate variable immutability in Rust.
// fn main() {
//     let distance = 83.2;

//     println!("Original: {}", distance);

//     distance = distance * 2.0;

//     println!("Doubled: {}", distance);
// }

// fn main() {
//     let distance = 83.2;
//     let doubled = double_distance(distance);
//     println!("The doubled distance is: {}", doubled);
// 	// check the (inferred) type of the variable
//     println!("{}", std::any::type_name_of_val(&distance));
// }

// The following will throw a compile time error
// because fn expects i64 but we are passing i32
// fn count_buildings(count: i64) {
//     println!("Building count: {}", count);
// }

// fn main() {
//     let buildings: i32 = 42;
//     count_buildings(buildings);
// }

// fn main() {
//     let threshold = 100.0;

//     let label = {
//         let distance = 83.2;

//         if distance <= threshold {
//             "near"
//         } else {
//             "far"
//         }
//     };

//     println!("Building is: {}", label);
// 	println!("{}", std::any::type_name_of_val(&label));

// 	// python: label = "near" if distance <= threshold else "far"
// 	// rust: let label = if distance <= threshold { "near" } else { "far" };
// }

// This fails compilation because the two branches of the if statement return different types
// fn main() {
//     let distance = 83.2;
//     let threshold = 100.0;

//     let result = if distance <= threshold {
//         "near" // &str
//     } else {
//         500 // integer (i32)
//     };

//     println!("{}", result);
// }

// If compiled, it would throw an error. What would that be?
// fn main() {
// 	let building_count = 42;
// 	println!(
// 			"input building_count:{}",
// 			std::any::type_name_of_val(&building_count)
// 		);

// 	if building_count > 0 {
// 		println!("We have buildings");
// 	}
// }

// This is the worse implementation
// fn classify_distance(distance: f64) -> &'static str {
//     if distance <= 50.0 {
//         "very near"
//     } else if distance <= 100.0 {
//         "near"
//     } else {
//         "far"
//     }
// }

// fn main() {
//     let distance = -73.5;

// 	let label = if distance < 0.0 {
// 		"invalid"
// 	} else {
// 		classify_distance(distance)
// 	};

//     println!("Distance: {}", distance);
//     println!("Classification: {}", label);
// }

// This is the better implementation.
// fn classify_distance(distance: f64) -> &'static str {
//     if distance < 0.0 {
//         "invalid"
//     } else if distance <= 50.0 {
//         "very near"
//     } else if distance <= 100.0 {
//         "near"
//     } else {
//         "far"
//     }
// }

// fn main() {
//     let distance = -73.5;

//     let label = classify_distance(distance);

//     println!("Distance: {}", distance);
//     println!("Classification: {}", label);
// }

// This also brings up the concepts of:
// enums: model a fixed set of valid states
// Result: model success vesus failure explicitly

//
// # loops
//

// fn main() {
//     let distances = [25.0, 73.5, 125.0];

//     for distance in distances {
//         println!("{}", distance);
//     }
// }

// fn classify_distance(distance: f64) -> &'static str {
//     if distance < 0.0 {
//         "invalid"
//     } else if distance <= 50.0 {
//         "very near"
//     } else if distance <= 100.0 {
//         "near"
//     } else {
//         "far"
//     }
// }

// fn main() {
//     let distances = [-73.5, 25.0, 50.0, 83.2, 100.0, 142.7];
//     println!("{}", std::any::type_name_of_val(&distances));

//     for distance in distances {
//         let label = classify_distance(distance);
//         println!("Distance: {}, Classification: {}", distance, label);
//     }
// }

// default types:
// 42    → i32
// 42.0  → f64
// true  → bool

// fn main() {
//     for index in 1..=4 {
//         println!("index: {}", std::any::type_name_of_val(&index));
//         let distance = index * 25;
//         println!("{}: {}, distance type: {}", index, distance, std::any::type_name_of_val(&distance));
//     }
// }

// fn main() {
//     let mut distance = 0;

//     while distance < 100 {
//         println!("Before: {}", distance);
//         distance += 30
//     }

//     println!("Final: {}", distance);
// }

// fn main() {
//     let mut distance = 0;

//     loop {
//         distance += 30;

//         if distance >= 100 {
//             break;
//         }

//         println!("Inside: {}", distance);
//     }

//     println!("Final: {}", distance);
// }

// loops can be applied to an expression
// fn main() {
//     let mut distance = 10;

//     let final_distance = loop {
//         distance += 20;

//         if distance >= 75 {
//             break distance;
//         }
//     };

//     println!("Distance: {}", distance);
//     println!("Final distance: {}", final_distance)
// }

// scope is the term used to define things like variables that the function knows and doesn't know
// this will throw an error when compiled:
// fn main() {
//     loop {
//         let temporary = 42;
//         break;
//     }

//     println!("{}", temporary);
// }
// Thus spake The Oracle (ChatGPT):
// A variable remains usable while execution is inside the scope where that binding is valid.

// fn main() {
//     let distance = 50;

//     if distance <= 100 {
//         let label = "near";
//         println!("Inside: {}", label);
//     }

//     println!("Outside: {}", label);
// }
// Inner scopes can access bindings from their surrounding scope,
// but surrounding scopes cannot access bindings created only inside an inner scope.

// fn main() {
//     let distance = 50;

//     let label = if distance <= 100 {
//         "near"
//     } else {
//         "far"
//     };

//     println!("{}", label);
// }

// this will throw a compiler error because E and F need access to variables out of scope
// fn main() {
//     let x = 10;

//     {
//         let y = 20;
//         let sum = x + y;

//         println!("A: {}", x);
//         println!("B: {}", y);
//         println!("C: {}", sum);
//     }

//     println!("D: {}", x);
//     println!("E: {}", y);
//     println!("F: {}", sum);
// }

// Shadowing versus mutation. Same end result:
// SHADOWING

// let distance = 50;
// let distance = distance + 25;
//     ↑
// creates a new binding

// MUTATION

// let mut distance = 50;
// distance += 25;
//     ↑
// changes the existing binding

// mutability
// same binding
// same type
// value can change

// shadowing
// new binding
// name reused
// type can change

// mut means binding's value can change, it doesn't mean that the type can change.

// note here how we can legally change the type
// fn main() {
// 	let distance = 50;
// 	let distance = distance + 25;
// 	let distance = distance as f64 / 2.0;

// 	println!("{}", distance);
// 	println!("{}", std::any::type_name_of_val(&distance));
// }

// as
// → explicit primitive cast

// .into()
// → broader type conversion mechanism

// fn main() {
//     let a = 83.7_f64 as i32;
//     let b = 83.7_f64.round() as i32;
//     let c = 83.2_f64.round() as i32;

//     println!("a: {}", a);
//     println!("b: {}", b);
//     println!("c: {}", c);
// }

// let building_count = 42;   // i32
// let average_area = 125.5;  // f64

// // temporarily cast building_count to f64 for this operation
// let total_area = building_count as f64 * average_area;

// let vs const
// let                         const
// ────────────────────────────────────────
// let threshold = 100.0;      const MAX_DISTANCE_M: f64 = 100.0;
// type often inferred         type annotation required
// ordinary variable binding   constant
// usually snake_case          conventionally SCREAMING_SNAKE_CASE

// const MAX_DISTANCE_M: f64 = 100.0;

// fn main() {
//     let distance = 83.2;

//     if distance <= MAX_DISTANCE_M {
//         println!("Within threshold");
//     } else {
//         println!("Outside threshold");
//     }

//     MAX_DISTANCE_M = 200.0;
// }

// immutable let
//     binding created at runtime
// 	can usually rely on inferred type
//     cannot be reassigned
//     can be shadowed by a new binding

// const
//     fixed constant value
// 	requires an explicit type
//     cannot be reassigned
//     intended as a program-wide/static constant

// introducting: Cargo
// instead of:
// rustc src/bin/unit1_experiments.rs
// ./unit1_experiments
// now we can just do: (from the package directory)
// cargo run --bin unit1_experiments
// this one command reads Cargo.toml, resolves package and target, compiles if needed, place build artifacts under target/, then runs the executable!

// to run a compiled version of this script, execute this:
// cargo run --manifest-path rust/spatial-core/Cargo.toml --bin unit1_experiments
// or, if we cd into the package:
// cd rust/spatial-core
// cargo run --bin unit1_experiments

// cargo check
// → type-check and compile-check the project without producing the final executable
// → usually much faster than a full build/run cycle

// cargo fmt --check
// → verify formatting without changing files

// cargo clippy
// → run Rust's linter for suspicious, non-idiomatic, or improvable code

// Important:
// cargo run --release
// Used when ready for heavy optimizing of machine code
// Enables the release profile and compiller optimizations

// package
//     Cargo-managed project described by Cargo.toml

// crate
//     Rust compilation unit

// target
//     something Cargo can build, such as a binary or library

// const MAX_SEARCH_DISTANCE_M: f64 = 2_000.0; // underscore only for readability

// fn classify_candidate(distance_m: f64) -> &'static str {
//     if distance_m <= MAX_SEARCH_DISTANCE_M {
//         "candidate"
//     } else {
//         "too far"
//     }
// }

// fn main() {
//     //    f64            &str
//     // let distance: f64 = "83.2"; // experiment for cargo check
//     classify_candidate(42.0);

// 	let mut distance = 42;
// 	println!("{}", distance)
// }

// cargo check
// → is the code valid Rust?

// cargo fmt --check
// → is it formatted according to rustfmt?

// cargo clippy
// → is it written in a suspicious, unnecessarily awkward, or non-idiomatic way?

// The new workflow:
// write Rust
//    ↓
// cargo check       ← does it compile/check?
//    ↓
// cargo fmt         ← standardize formatting
//    ↓
// cargo clippy      ← anything suspicious/non-idiomatic?
//    ↓
// cargo run         ← actually execute it

// Fun fact: Rust can test code examples within documentation :mind-blow emoji:

// tests

// basic structure
// #[test]
// fn test_name() {
//     arrange values
//     call code
//     assert expected behavior
// }

// println!()      // macro
// assert_eq!()    // macro
// #[test]         // attribute
// #[cfg(test)]    // attribute

// match
// match is like Python's match or SQL's CASE but is more important due to enums and exhaustive handling.
// match must be exhaustive, and include every potential pattern (it could be a catch-all, see below)
// first, think of something like this:
// fn classify_distance(distance: f64) -> &'static str {
//     if distance < 0.0 {
//         "invalid"
//     } else if distance <= 50.0 {
//         "very near"
//     } else if distance <= 100.0 {
//         "near"
//     } else {
//         "far"
//     }
// }

// now with match:
// the "=>", if read aloud, is like "then" or "maps to", like so:
// fn describe_zone(zone: i32) -> &'static str {
//     match zone {
//         1 => "residential", // if the pattern is 1, then produce "missing"
//         2 => "commercial",
//         3 => "industrial",
//         _ => "unknown", // anything else then produce "unknown". '_' is a catch-all pattern.
//     }
// }

// "_" is like case... when... else in SQL:
// case zone
//     when 1 then 'residential'
//     when 2 then 'commercial'
//     when 3 then 'industrial'
//     else 'unknown'
// end

// match is an expression so it can produce a value, just like if.
// let label = match zone {
//     1 => "residential",
//     2 => "commercial",
//     3 => "industrial",
//     _ => "unknown",
// };

// fn describe_quality(code: i32) -> &'static str {
//     match code {
//         0 => "missing",
//         1 => "poor",
//         2 => "fair",
//         3 => "good",
//         _ => "unknown",
//     }
// }

// fn main() {
//     for code in 0..=4 {
//         let quality = describe_quality(code);
//         println!("{}: {}", code, quality);
//     }
// }

// match pattern:
// 1 | 2       → pattern 1 OR pattern 2

// Boolean expression:
// a || b      → a OR b

// if distance < 0.0 || distance > 100.0 {
//     println!("Outside range");
// }

// fn classify_score(score: i32) -> &'static str {
//     match score {
//         0..=49 => "low",
//         50..=79 => "medium",
//         80..=100 => "high",
//         _ => "invalid",
//     }
// }

// fn describe_quality(code: i32) -> &'static str {
//     match code {
//         0 => "missing",
//         1 | 2 => "usable",
//         3 => "good",
//         _ => "unknown",
//     }
// }

// 0..49     // 0 through 48; 49 excluded
// 0..=49    // 0 through 49; 49 included
// a..b     → a <= x < b
// a..=b    → a <= x <= b

// match requires inclusive range patterns like 0..=49
// ranges as values/iterators can be exclusive:
// for x in 0..50 {
//     // x = 0 through 49
// }

// fn classify_score(score: i32) -> &'static str {
//     match score {
//         0..=49 => "low",
//         50..=79 => "medium",
//         80..=100 => "high",
//         _ => "invalid",
//     }
// }

// fn main() {
//     let scores = [-1, 0, 49, 50, 79, 80, 100, 101];

//     for score in scores {
//         println!("{}: {}", score, classify_score(score));
//     }
// }

// match wrap-up:
// single value      1 => ...
// or-pattern        1 | 2 => ...
// inclusive range   0..=49 => ...
// catch-all         _ => ...

