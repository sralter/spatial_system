/// Deliberately causes compile-time error to demonstrate variable immutability in Rust.
fn main() {
    let distance = 83.2;

    println!("Original: {}", distance);

    distance = distance * 2.0;

    println!("Doubled: {}", distance);
}