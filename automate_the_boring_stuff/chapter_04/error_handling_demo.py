#!/usr/bin/env python3
"""
error_handling_demo.py
Demonstrates how to handle division by zero errors in Python.
Shows the difference between crashing and graceful error recovery.
"""
def safe_divide(divide_by: float) -> float:
    """
    Safely divides 42 by the given number.
    :param divide_by: The number to divide by.
    :return: The result of 42 divided by divide_by.
    :raises ValueError: If divide_by is zero.
    """
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        raise ValueError("Error: Cannot divide by zero.")

def unsafe_divide(divide_by: float) -> float:
    """
    Divides 42 by the given number, but may crash on division by zero.
    :param divide_by: The number to divide by.
    :return: The result of 42 divided by divide_by.
    """
    return 42 / divide_by

def main():
    """Demonstrates safe and unsafe division."""
    # Test cases
    test_values = [2, 12, 0, 1]

    print("Using safe_divide (with error handling):")
    for value in test_values:
        try:
            result = safe_divide(value)
            print(f"42 / {value} = {result}")
        except ValueError as e:
            print(e)

    print("\nUsing unsafe_divide (no error handling):")
    for value in test_values:
        try:
            result = unsafe_divide(value)
            print(f"42 / {value} = {result}")
        except ZeroDivisionError:
            print("Error: Invalid argument.")

if __name__ == "__main__":
    main()
