#![no_main]

use libfuzzer_sys::fuzz_target;
use centaur_example::calculator::{add, subtract, multiply, divide};

fuzz_target!(|data: &[u8]| {
    // Need at least 8 bytes for two i32s
    if data.len() < 8 {
        return;
    }

    // Extract two i32 values from the fuzzer input
    let a = i32::from_le_bytes([data[0], data[1], data[2], data[3]]);
    let b = i32::from_le_bytes([data[4], data[5], data[6], data[7]]);

    // Test all operations
    let _sum = add(a, b);
    let _diff = subtract(a, b);
    let _product = multiply(a, b);

    // Division might return an error for zero
    if b != 0 {
        let _quotient = divide(a, b).expect("division should succeed for non-zero divisor");
    } else {
        // Dividing by zero should return an error, not panic
        assert!(divide(a, b).is_err(), "division by zero should return error");
    }
});
