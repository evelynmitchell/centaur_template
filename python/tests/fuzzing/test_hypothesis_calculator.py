"""
Property-based tests using Hypothesis for calculator module.

Hypothesis generates test cases automatically to find edge cases.
"""

import pytest
from hypothesis import given
from hypothesis import strategies as st

from centaur_example.calculator import add, divide, multiply, subtract


class TestCalculatorProperties:
    """Property-based tests for calculator functions."""

    @given(st.integers(), st.integers())
    def test_add_commutative(self, a: int, b: int) -> None:
        """Test that addition is commutative: a + b = b + a."""
        assert add(a, b) == add(b, a)

    @given(st.integers())
    def test_add_identity(self, a: int) -> None:
        """Test that adding zero doesn't change the value."""
        assert add(a, 0) == a
        assert add(0, a) == a

    @given(st.integers(), st.integers(), st.integers())
    def test_add_associative(self, a: int, b: int, c: int) -> None:
        """Test that addition is associative: (a + b) + c = a + (b + c)."""
        assert add(add(a, b), c) == add(a, add(b, c))

    @given(st.integers(), st.integers())
    def test_multiply_commutative(self, a: int, b: int) -> None:
        """Test that multiplication is commutative: a * b = b * a."""
        assert multiply(a, b) == multiply(b, a)

    @given(st.integers())
    def test_multiply_by_zero(self, a: int) -> None:
        """Test that multiplying by zero always gives zero."""
        assert multiply(a, 0) == 0
        assert multiply(0, a) == 0

    @given(st.integers())
    def test_multiply_by_one(self, a: int) -> None:
        """Test that multiplying by one doesn't change the value."""
        assert multiply(a, 1) == a
        assert multiply(1, a) == a

    @given(st.integers())
    def test_subtract_self(self, a: int) -> None:
        """Test that subtracting a number from itself gives zero."""
        assert subtract(a, a) == 0

    @given(st.integers())
    def test_subtract_zero(self, a: int) -> None:
        """Test that subtracting zero doesn't change the value."""
        assert subtract(a, 0) == a

    @given(st.integers(min_value=-1000000, max_value=1000000).filter(lambda x: x != 0))
    def test_divide_by_self(self, a: int) -> None:
        """Test that dividing a number by itself gives one."""
        assert divide(a, a) == pytest.approx(1.0)

    @given(
        st.integers(min_value=-1000000, max_value=1000000),
        st.integers(min_value=1, max_value=1000000),
    )
    def test_divide_positive_denominator(self, a: int, b: int) -> None:
        """Test division with positive denominator always succeeds."""
        result = divide(a, b)
        assert isinstance(result, float)

    @given(st.integers())
    def test_divide_by_zero_raises(self, a: int) -> None:
        """Test that dividing by zero always raises ValueError."""
        with pytest.raises(ValueError):
            divide(a, 0)

    @given(
        st.integers(min_value=-1000, max_value=1000),
        st.integers(min_value=-1000, max_value=1000),
    )
    def test_add_subtract_inverse(self, a: int, b: int) -> None:
        """Test that subtract is the inverse of add."""
        result = add(a, b)
        assert subtract(result, b) == a
