//! Integration tests for centaur_example.
//!
//! These tests verify that different components work together correctly.

use centaur_example::{add, count_words, divide, multiply, reverse_string, to_title_case};

#[test]
fn test_chain_arithmetic_operations() {
    let result = add(5, 3); // 8
    let result = multiply(result, 2); // 16
    let result = divide(result, 4).unwrap(); // 4
    assert_eq!(result, 4);
}

#[test]
fn test_complex_calculation() {
    // (10 + 5) * 2 / 3 = 10
    let result = add(10, 5);
    let result = multiply(result, 2);
    let result = divide(result, 3).unwrap();
    assert_eq!(result, 10);
}

#[test]
fn test_reverse_and_title_case() {
    let text = "hello world";
    let reversed = reverse_string(text); // "dlrow olleh"
    let titled = to_title_case(&reversed); // "Dlrow Olleh"
    assert_eq!(titled, "Dlrow Olleh");
}

#[test]
fn test_count_after_title_case() {
    let text = "hello world";
    let original_count = count_words(text);
    let titled = to_title_case(text);
    let new_count = count_words(&titled);
    assert_eq!(original_count, new_count);
    assert_eq!(original_count, 2);
}

#[test]
fn test_calculate_word_count_operations() {
    let text1 = "hello world";
    let text2 = "foo bar baz";

    let count1 = count_words(text1) as i32; // 2
    let count2 = count_words(text2) as i32; // 3

    let total = add(count1, count2); // 5
    let average = divide(total, 2).unwrap(); // 2

    assert_eq!(total, 5);
    assert_eq!(average, 2);
}

#[test]
fn test_string_length_arithmetic() {
    let str1 = "hello";
    let str2 = "world";

    let len1 = str1.len() as i32;
    let len2 = str2.len() as i32;

    let total_length = add(len1, len2);
    let product = multiply(len1, len2);

    assert_eq!(total_length, 10);
    assert_eq!(product, 25);
}
