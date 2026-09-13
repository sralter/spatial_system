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
fn main() {
    let distance = 83.2;
    let threshold = 100.0;

    let result = if distance <= threshold {
        "near" // &str
    } else {
        500 // integer (i32)
    };

    println!("{}", result);
}