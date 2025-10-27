"""
Text utilities module providing string manipulation functions.

This module demonstrates working with strings and text processing.
"""


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
        >>> reverse_string("a")
        'a'
    """
    return text[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a string.

    Words are defined as sequences of characters separated by whitespace.

    Args:
        text: The string to count words in

    Returns:
        The number of words

    Examples:
        >>> count_words("hello world")
        2
        >>> count_words("  multiple   spaces  ")
        2
        >>> count_words("")
        0
        >>> count_words("   ")
        0
    """
    return len(text.split())


def to_title_case(text: str) -> str:
    """
    Convert a string to title case.

    Title case capitalizes the first letter of each word.

    Args:
        text: The string to convert

    Returns:
        The string in title case

    Examples:
        >>> to_title_case("hello world")
        'Hello World'
        >>> to_title_case("HELLO WORLD")
        'Hello World'
        >>> to_title_case("")
        ''
    """
    return text.title()
