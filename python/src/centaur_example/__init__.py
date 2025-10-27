"""
Centaur Example Package

This is an example package demonstrating the structure and testing approach
for the Centaur template. You can delete this package and create your own.
"""

__version__ = "0.1.0"

from centaur_example.calculator import add, divide, multiply, subtract
from centaur_example.text_utils import count_words, reverse_string, to_title_case


__all__ = [
    "add",
    "subtract",
    "multiply",
    "divide",
    "reverse_string",
    "count_words",
    "to_title_case",
]
