//! Calculator module providing basic arithmetic operations.
//!
//! This module demonstrates:
//! - Comprehensive documentation
//! - Error handling with Result types
//! - Edge case management
//! - Unit testing

/// Adds two numbers together.
///
/// # Examples
///
/// ```
/// use centaur_example::calculator::add;
///
/// assert_eq!(add(2, 3), 5);
/// assert_eq!(add(-1, 1), 0);
/// ```
pub fn add(a: i32, b: i32) -> i32 {
    a.wrapping_add(b)
}

/// Subtracts b from a.
///
/// # Examples
///
/// ```
/// use centaur_example::calculator::subtract;
///
/// assert_eq!(subtract(5, 3), 2);
/// assert_eq!(subtract(3, 5), -2);
/// ```
pub fn subtract(a: i32, b: i32) -> i32 {
    a.wrapping_sub(b)
}

/// Multiplies two numbers together.
///
/// # Examples
///
/// ```
/// use centaur_example::calculator::multiply;
///
/// assert_eq!(multiply(4, 5), 20);
/// assert_eq!(multiply(-2, 3), -6);
/// ```
pub fn multiply(a: i32, b: i32) -> i32 {
    a.wrapping_mul(b)
}

/// Divides a by b.
///
/// # Errors
///
/// Returns an error if b is zero.
///
/// # Examples
///
/// ```
/// use centaur_example::calculator::divide;
///
/// assert_eq!(divide(10, 2), Ok(5));
/// assert_eq!(divide(7, 2), Ok(3)); // Integer division
/// assert!(divide(5, 0).is_err());
/// ```
pub fn divide(a: i32, b: i32) -> Result<i32, String> {
    if b == 0 {
        Err("Cannot divide by zero".to_string())
    } else {
        Ok(a / b)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_positive_positive() {
        assert_eq!(add(5, 3), 8);
    }

    #[test]
    fn test_add_positive_negative() {
        assert_eq!(add(5, -3), 2);
    }

    #[test]
    fn test_add_negative_negative() {
        assert_eq!(add(-5, -3), -8);
    }

    #[test]
    fn test_add_with_zero() {
        assert_eq!(add(5, 0), 5);
        assert_eq!(add(0, 5), 5);
    }

    #[test]
    fn test_add_overflow() {
        // Test wrapping behavior on overflow
        let result = add(i32::MAX, 1);
        assert_eq!(result, i32::MIN);
    }

    #[test]
    fn test_subtract_positive_positive() {
        assert_eq!(subtract(5, 3), 2);
    }

    #[test]
    fn test_subtract_result_negative() {
        assert_eq!(subtract(3, 5), -2);
    }

    #[test]
    fn test_subtract_with_zero() {
        assert_eq!(subtract(5, 0), 5);
        assert_eq!(subtract(0, 5), -5);
    }

    #[test]
    fn test_multiply_positive_positive() {
        assert_eq!(multiply(4, 5), 20);
    }

    #[test]
    fn test_multiply_positive_negative() {
        assert_eq!(multiply(4, -5), -20);
    }

    #[test]
    fn test_multiply_negative_negative() {
        assert_eq!(multiply(-4, -5), 20);
    }

    #[test]
    fn test_multiply_with_zero() {
        assert_eq!(multiply(5, 0), 0);
        assert_eq!(multiply(0, 5), 0);
    }

    #[test]
    fn test_multiply_with_one() {
        assert_eq!(multiply(5, 1), 5);
        assert_eq!(multiply(1, 5), 5);
    }

    #[test]
    fn test_divide_positive_positive() {
        assert_eq!(divide(10, 2), Ok(5));
    }

    #[test]
    fn test_divide_with_remainder() {
        assert_eq!(divide(7, 2), Ok(3)); // Integer division
    }

    #[test]
    fn test_divide_negative() {
        assert_eq!(divide(-10, 2), Ok(-5));
        assert_eq!(divide(10, -2), Ok(-5));
        assert_eq!(divide(-10, -2), Ok(5));
    }

    #[test]
    fn test_divide_by_zero() {
        assert!(divide(5, 0).is_err());
        assert_eq!(divide(5, 0).unwrap_err(), "Cannot divide by zero");
    }

    #[test]
    fn test_divide_zero_by_number() {
        assert_eq!(divide(0, 5), Ok(0));
    }
}
