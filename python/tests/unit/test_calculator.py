"""
Unit tests for calculator module.

These tests demonstrate:
- Testing positive, negative, and zero cases
- Testing edge cases
- Testing error conditions
- Using pytest fixtures
- Parametrized tests
"""

import pytest

from centaur_example.calculator import add, divide, multiply, subtract


class TestAdd:
    """Tests for the add function."""

    def test_add_positive_positive(self) -> None:
        """Test adding two positive numbers."""
        assert add(5, 3) == 8

    def test_add_positive_negative(self) -> None:
        """Test adding positive and negative numbers."""
        assert add(5, -3) == 2

    def test_add_negative_negative(self) -> None:
        """Test adding two negative numbers."""
        assert add(-5, -3) == -8

    def test_add_with_zero(self) -> None:
        """Test adding zero."""
        assert add(5, 0) == 5
        assert add(0, 5) == 5

    def test_add_floats(self) -> None:
        """Test adding floating point numbers."""
        assert add(2.5, 1.5) == 4.0
        assert add(0.1, 0.2) == pytest.approx(0.3)

    @pytest.mark.parametrize(
        "a,b,expected",
        [
            (1, 1, 2),
            (0, 0, 0),
            (-1, 1, 0),
            (100, 200, 300),
            (-50, -50, -100),
        ],
    )
    def test_add_parametrized(self, a: int, b: int, expected: int) -> None:
        """Test add with various inputs."""
        assert add(a, b) == expected


class TestSubtract:
    """Tests for the subtract function."""

    def test_subtract_positive_positive(self) -> None:
        """Test subtracting two positive numbers."""
        assert subtract(5, 3) == 2

    def test_subtract_result_negative(self) -> None:
        """Test subtraction resulting in negative."""
        assert subtract(3, 5) == -2

    def test_subtract_with_zero(self) -> None:
        """Test subtracting zero."""
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5


class TestMultiply:
    """Tests for the multiply function."""

    def test_multiply_positive_positive(self) -> None:
        """Test multiplying two positive numbers."""
        assert multiply(4, 5) == 20

    def test_multiply_positive_negative(self) -> None:
        """Test multiplying positive and negative."""
        assert multiply(4, -5) == -20

    def test_multiply_negative_negative(self) -> None:
        """Test multiplying two negative numbers."""
        assert multiply(-4, -5) == 20

    def test_multiply_with_zero(self) -> None:
        """Test multiplying by zero."""
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0

    def test_multiply_with_one(self) -> None:
        """Test multiplying by one."""
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5


class TestDivide:
    """Tests for the divide function."""

    def test_divide_positive_positive(self) -> None:
        """Test dividing two positive numbers."""
        assert divide(10, 2) == 5.0

    def test_divide_with_remainder(self) -> None:
        """Test division with remainder."""
        assert divide(7, 2) == 3.5

    def test_divide_negative(self) -> None:
        """Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0

    def test_divide_by_zero_raises_error(self) -> None:
        """Test that dividing by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)

    def test_divide_zero_by_number(self) -> None:
        """Test dividing zero by a number."""
        assert divide(0, 5) == 0.0
