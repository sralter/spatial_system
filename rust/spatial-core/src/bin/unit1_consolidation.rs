// Build a small 'spatial quality classifier' with these requirements:
// Constants
// - MAX_DISTANCE_M: f64 = 2_000.0

// Function 1: classify_distance
// - accepts distance_m: f64
// - returns &'static str
// - negative          -> "invalid"
// - 0 through 100     -> "near"
// - >100 through 500  -> "medium"
// - >500 through 2000 -> "far"
// - >2000             -> "outside"

// Function 2: classify_quality
// - accepts code: i32
// - returns &'static str
// - 0       -> "missing"
// - 1 | 2   -> "usable"
// - 3       -> "good"
// - anything else -> "unknown"

// Then in main(), start with:
// let distances = [-10.0, 25.0, 250.0, 1500.0, 2500.0];
// let quality_codes = [0, 1, 2, 3, 9];

// Use for loops to print every classification

// A few constraints make this a true consolidation exercise:
// * Use at least one match.
// * Use at least one if expression.
// * Do not use unnecessary mut.
// * Keep numeric types appropriate.
// * Let Rust infer types where that is clear, but use explicit function signatures.
// * Add /// documentation comments to both functions.
// * Run cargo fmt, cargo check, cargo clippy, and cargo run --bin unit1_consolidation.
// * If Clippy flags something, reason about it before changing the code.

// Do not add tests yet. Once your program runs cleanly, we’ll add a small test module as the final step.

// workflow when complete:
// cargo check --bin unit1_consolidation
// rustfmt --check src/bin/unit1_consolidation.rs
// 		rustfmt src/bin/unit1_consolidation.rs // implements the formatting
// cargo clippy --bin unit1_consolidation
// cargo run --bin unit1_consolidation

const MAX_DISTANCE_M: f64 = 2_000.0;

/// Classifies distance in meters based on its value
fn classify_distance(distance_m: f64) -> &'static str {
    if distance_m < 0.0 {
        "invalid"
    } else if distance_m <= 100.0 {
        "near"
    } else if distance_m <= 500.0 {
        "medium"
    } else if distance_m <= MAX_DISTANCE_M {
        "far"
    } else {
        "outside"
    }
}

/// Classifies the code into defined buckets
fn classify_quality(code: i32) -> &'static str {
    match code {
        0 => "missing",
        1 | 2 => "usable",
        3 => "good",
        _ => "unknown",
    }
}

fn main() {
    let distances = [-10.0, 25.0, 250.0, 1500.0, 2500.0];
    let quality_codes = [0, 1, 2, 3, 9];

    println!("Classify distances:");
    for distance in distances {
        let distance_result = classify_distance(distance);
        println!("{}", distance_result);
    }

    println!("Classify qualities:");
    for qcode in quality_codes {
        let code_result = classify_quality(qcode);
        println!("{}", code_result);
    }
}
