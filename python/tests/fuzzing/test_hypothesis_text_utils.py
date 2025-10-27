"""
Property-based tests using Hypothesis for text_utils module.
"""

from hypothesis import given
from hypothesis import strategies as st

from centaur_example.text_utils import count_words, reverse_string, to_title_case


class TestTextUtilsProperties:
    """Property-based tests for text utilities."""

    @given(st.text())
    def test_reverse_reverse_is_identity(self, text: str) -> None:
        """Test that reversing twice returns the original string."""
        assert reverse_string(reverse_string(text)) == text

    @given(st.text())
    def test_reverse_preserves_length(self, text: str) -> None:
        """Test that reversing preserves string length."""
        assert len(reverse_string(text)) == len(text)

    @given(st.text())
    def test_count_words_non_negative(self, text: str) -> None:
        """Test that word count is always non-negative."""
        assert count_words(text) >= 0

    @given(st.text(min_size=1).filter(lambda s: not s.isspace()))
    def test_count_words_non_empty_text(self, text: str) -> None:
        """Test that non-empty text has at least one word."""
        # Filter out pure whitespace
        assert count_words(text) >= 1

    @given(st.text())
    def test_title_case_preserves_word_count(self, text: str) -> None:
        """Test that title casing preserves word count."""
        original_count = count_words(text)
        titled_count = count_words(to_title_case(text))
        assert original_count == titled_count

    @given(st.text())
    def test_title_case_idempotent(self, text: str) -> None:
        """Test that applying title case twice gives same result."""
        once = to_title_case(text)
        twice = to_title_case(once)
        assert once == twice

    @given(st.lists(st.text(min_size=1, max_size=10).filter(lambda s: " " not in s)))
    def test_count_words_with_spaces(self, words: list[str]) -> None:
        """Test word counting with known word count."""
        if not words:
            return
        text = " ".join(words)
        assert count_words(text) == len(words)
