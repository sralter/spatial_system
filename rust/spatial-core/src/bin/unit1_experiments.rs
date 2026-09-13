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

fn main() {
    for index in 1..=4 {
        println!("{}", std::any::type_name_of_val(&index));
        let distance = index * 25;
        println!("{}: {}, distance type: {}", index, distance, std::any::type_name_of_val(&distance));
    }
}