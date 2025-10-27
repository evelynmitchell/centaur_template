//! Text utilities module providing string manipulation functions.
//!
//! This module demonstrates working with strings and text processing in Rust.

/// Reverses a string.
///
/// # Examples
///
/// ```
/// use centaur_example::text_utils::reverse_string;
///
/// assert_eq!(reverse_string("hello"), "olleh");
/// assert_eq!(reverse_string(""), "");
/// assert_eq!(reverse_string("a"), "a");
/// ```
pub fn reverse_string(text: &str) -> String {
    text.chars().rev().collect()
}

/// Counts the number of words in a string.
///
/// Words are defined as sequences of characters separated by whitespace.
///
/// # Examples
///
/// ```
/// use centaur_example::text_utils::count_words;
///
/// assert_eq!(count_words("hello world"), 2);
/// assert_eq!(count_words("  multiple   spaces  "), 2);
/// assert_eq!(count_words(""), 0);
/// assert_eq!(count_words("   "), 0);
/// ```
pub fn count_words(text: &str) -> usize {
    text.split_whitespace().count()
}

/// Converts a string to title case.
///
/// Title case capitalizes the first letter of each word.
///
/// # Examples
///
/// ```
/// use centaur_example::text_utils::to_title_case;
///
/// assert_eq!(to_title_case("hello world"), "Hello World");
/// assert_eq!(to_title_case("HELLO WORLD"), "Hello World");
/// assert_eq!(to_title_case(""), "");
/// ```
pub fn to_title_case(text: &str) -> String {
    text.split_whitespace()
        .map(|word| {
            let mut chars = word.chars();
            match chars.next() {
                None => String::new(),
                Some(first) => {
                    first.to_uppercase().collect::<String>() + &chars.as_str().to_lowercase()
                }
            }
        })
        .collect::<Vec<_>>()
        .join(" ")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_reverse_simple_string() {
        assert_eq!(reverse_string("hello"), "olleh");
    }

    #[test]
    fn test_reverse_empty_string() {
        assert_eq!(reverse_string(""), "");
    }

    #[test]
    fn test_reverse_single_character() {
        assert_eq!(reverse_string("a"), "a");
    }

    #[test]
    fn test_reverse_with_spaces() {
        assert_eq!(reverse_string("hello world"), "dlrow olleh");
    }

    #[test]
    fn test_reverse_palindrome() {
        assert_eq!(reverse_string("racecar"), "racecar");
    }

    #[test]
    fn test_reverse_unicode() {
        assert_eq!(reverse_string("hello 🌍"), "🌍 olleh");
    }

    #[test]
    fn test_count_simple_sentence() {
        assert_eq!(count_words("hello world"), 2);
    }

    #[test]
    fn test_count_empty_string() {
        assert_eq!(count_words(""), 0);
    }

    #[test]
    fn test_count_single_word() {
        assert_eq!(count_words("hello"), 1);
    }

    #[test]
    fn test_count_with_multiple_spaces() {
        assert_eq!(count_words("  multiple   spaces  "), 2);
    }

    #[test]
    fn test_count_whitespace_only() {
        assert_eq!(count_words("   "), 0);
    }

    #[test]
    fn test_count_with_newlines() {
        assert_eq!(count_words("hello\nworld"), 2);
    }

    #[test]
    fn test_title_case_lowercase() {
        assert_eq!(to_title_case("hello world"), "Hello World");
    }

    #[test]
    fn test_title_case_uppercase() {
        assert_eq!(to_title_case("HELLO WORLD"), "Hello World");
    }

    #[test]
    fn test_title_case_mixed() {
        assert_eq!(to_title_case("hElLo WoRlD"), "Hello World");
    }

    #[test]
    fn test_title_case_empty() {
        assert_eq!(to_title_case(""), "");
    }

    #[test]
    fn test_title_case_single_word() {
        assert_eq!(to_title_case("hello"), "Hello");
    }
}
