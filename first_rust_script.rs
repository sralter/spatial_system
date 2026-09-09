/// My first function: double_distance
/// Doubles a distance in meters (accepts all units right now).
fn double_distance(distance: f64) -> f64 {
    distance * 2.0
}


fn main() {
    let value = double_distance(83.2);
    println!("The doubled distance is: {}", value);
}
