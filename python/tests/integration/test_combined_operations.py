"""
Integration tests that combine multiple modules.

These tests verify that different components work together correctly.
"""

import pytest

from centaur_example.calculator import add, divide, multiply
from centaur_example.text_utils import count_words, reverse_string, to_title_case


class TestCalculatorChaining:
    """Test chaining calculator operations."""

    def test_chain_arithmetic_operations(self) -> None:
        """Test chaining multiple arithmetic operations."""
        result = add(5, 3)  # 8
        result = multiply(result, 2)  # 16
        result = divide(result, 4)  # 4.0
        assert result == 4.0

    def test_complex_calculation(self) -> None:
        """Test a complex calculation using multiple operations."""
        # (10 + 5) * 2 / 3 = 10
        result = add(10, 5)
        result = multiply(result, 2)
        result = divide(result, 3)
        assert result == pytest.approx(10.0)


class TestTextProcessingPipeline:
    """Test text processing operations in sequence."""

    def test_reverse_and_title_case(self) -> None:
        """Test reversing then converting to title case."""
        text = "hello world"
        reversed_text = reverse_string(text)  # "dlrow olleh"
        titled = to_title_case(reversed_text)  # "Dlrow Olleh"
        assert titled == "Dlrow Olleh"

    def test_count_after_title_case(self) -> None:
        """Test that word count is preserved after title casing."""
        text = "hello world"
        original_count = count_words(text)
        titled = to_title_case(text)
        new_count = count_words(titled)
        assert original_count == new_count == 2


class TestCrossModuleIntegration:
    """Test integration across calculator and text_utils modules."""

    def test_calculate_word_count_operations(self) -> None:
        """Test using calculator operations on word counts."""
        text1 = "hello world"
        text2 = "foo bar baz"

        count1 = count_words(text1)  # 2
        count2 = count_words(text2)  # 3

        total = add(count1, count2)  # 5
        average = divide(total, 2)  # 2.5

        assert total == 5
        assert average == 2.5

    def test_string_length_arithmetic(self) -> None:
        """Test arithmetic operations on string lengths."""
        str1 = "hello"
        str2 = "world"

        len1 = len(str1)
        len2 = len(str2)

        total_length = add(len1, len2)
        product = multiply(len1, len2)

        assert total_length == 10
        assert product == 25
