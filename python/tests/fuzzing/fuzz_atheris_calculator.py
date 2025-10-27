#!/usr/bin/env python3
"""
Atheris fuzzing test for calculator module.

This uses coverage-guided fuzzing to find edge cases and potential crashes.
Run with: python fuzz_atheris_calculator.py
"""

import sys
import atheris

from centaur_example.calculator import add, divide, multiply, subtract


def test_calculator(data: bytes) -> None:
    """
    Fuzz test for calculator operations.

    Args:
        data: Random bytes provided by the fuzzer
    """
    fdp = atheris.FuzzedDataProvider(data)

    # Generate random numbers
    a = fdp.ConsumeFloat()
    b = fdp.ConsumeFloat()

    # Test various operations
    try:
        _ = add(a, b)
        _ = subtract(a, b)
        _ = multiply(a, b)

        # Division might raise ValueError for zero
        if b != 0:
            _ = divide(a, b)
        else:
            try:
                _ = divide(a, b)
                # Should have raised an error
                raise AssertionError("divide by zero should raise ValueError")
            except ValueError:
                # Expected behavior
                pass

    except (OverflowError, ValueError) as e:
        # These are expected for certain inputs
        pass
    except Exception as e:
        # Any other exception is a problem
        print(f"Unexpected exception: {e}")
        raise


def main() -> None:
    """Run the fuzzer."""
    atheris.Setup(sys.argv, test_calculator)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
