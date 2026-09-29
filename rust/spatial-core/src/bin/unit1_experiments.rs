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

fn main() {
    let a = 83.7_f64 as i32;
    let b = 83.7_f64.round() as i32;
    let c = 83.2_f64.round() as i32;

    println!("a: {}", a);
    println!("b: {}", b);
    println!("c: {}", c);
}