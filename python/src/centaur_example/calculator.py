"""
Calculator module providing basic arithmetic operations.

This module demonstrates:
- Type hints for better code clarity
- Comprehensive docstrings
- Error handling
- Edge case management
"""

Number = int | float


def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.

    Args:
        a: The first number
        b: The second number

    Returns:
        The sum of a and b

    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(2.5, 1.5)
        4.0
    """
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract b from a.

    Args:
        a: The number to subtract from
        b: The number to subtract

    Returns:
        The difference of a and b

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(3, 5)
        -2
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.

    Args:
        a: The first number
        b: The second number

    Returns:
        The product of a and b

    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(-2, 3)
        -6
        >>> multiply(2.5, 2)
        5.0
    """
    return a * b


def divide(a: Number, b: Number) -> float:
    """
    Divide a by b.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient of a and b

    Raises:
        ValueError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(5, 0)
        Traceback (most recent call last):
        ...
        ValueError: Cannot divide by zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
