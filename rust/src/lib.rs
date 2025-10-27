//! Centaur Example Library
//!
//! This is an example library demonstrating the structure and testing approach
//! for the Centaur template. You can delete these modules and create your own.
//!
//! # Modules
//!
//! - [`calculator`]: Basic arithmetic operations
//! - [`text_utils`]: String manipulation utilities

pub mod calculator;
pub mod text_utils;

// Re-export commonly used items
pub use calculator::{add, divide, multiply, subtract};
pub use text_utils::{count_words, reverse_string, to_title_case};
