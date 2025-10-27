"""
Unit tests for text_utils module.
"""

import pytest

from centaur_example.text_utils import count_words, reverse_string, to_title_case


class TestReverseString:
    """Tests for reverse_string function."""

    def test_reverse_simple_string(self) -> None:
        """Test reversing a simple string."""
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self) -> None:
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    def test_reverse_single_character(self) -> None:
        """Test reversing a single character."""
        assert reverse_string("a") == "a"

    def test_reverse_with_spaces(self) -> None:
        """Test reversing string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"

    def test_reverse_palindrome(self) -> None:
        """Test reversing a palindrome."""
        assert reverse_string("racecar") == "racecar"

    @pytest.mark.parametrize(
        "input_str,expected",
        [
            ("abc", "cba"),
            ("12345", "54321"),
            ("Hello!", "!olleH"),
            ("  ", "  "),
        ],
    )
    def test_reverse_parametrized(self, input_str: str, expected: str) -> None:
        """Test reverse_string with various inputs."""
        assert reverse_string(input_str) == expected


class TestCountWords:
    """Tests for count_words function."""

    def test_count_simple_sentence(self) -> None:
        """Test counting words in a simple sentence."""
        assert count_words("hello world") == 2

    def test_count_empty_string(self) -> None:
        """Test counting words in empty string."""
        assert count_words("") == 0

    def test_count_single_word(self) -> None:
        """Test counting single word."""
        assert count_words("hello") == 1

    def test_count_with_multiple_spaces(self) -> None:
        """Test counting with multiple spaces between words."""
        assert count_words("  multiple   spaces  ") == 2

    def test_count_whitespace_only(self) -> None:
        """Test counting whitespace-only string."""
        assert count_words("   ") == 0

    def test_count_with_newlines(self) -> None:
        """Test counting with newlines."""
        assert count_words("hello\nworld") == 2

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("one", 1),
            ("one two", 2),
            ("one two three", 3),
            ("a b c d e", 5),
            ("", 0),
        ],
    )
    def test_count_words_parametrized(self, text: str, expected: int) -> None:
        """Test count_words with various inputs."""
        assert count_words(text) == expected


class TestToTitleCase:
    """Tests for to_title_case function."""

    def test_title_case_lowercase(self) -> None:
        """Test converting lowercase to title case."""
        assert to_title_case("hello world") == "Hello World"

    def test_title_case_uppercase(self) -> None:
        """Test converting uppercase to title case."""
        assert to_title_case("HELLO WORLD") == "Hello World"

    def test_title_case_mixed(self) -> None:
        """Test converting mixed case to title case."""
        assert to_title_case("hElLo WoRlD") == "Hello World"

    def test_title_case_empty(self) -> None:
        """Test converting empty string."""
        assert to_title_case("") == ""

    def test_title_case_single_word(self) -> None:
        """Test converting single word."""
        assert to_title_case("hello") == "Hello"
