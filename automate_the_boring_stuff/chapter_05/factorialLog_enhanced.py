#!/usr/bin/env python3
"""
factorial_with_logging.py
Calculates the factorial of a number and logs the process for debugging.
Demonstrates:
  - Logging for debugging and tracing
  - Correct factorial calculation
  - String formatting for log messages
  - Input validation
"""
import logging

# Configure logging to display time, level, and message
logging.basicConfig(
    filename='myProgramLog.txt',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n.

    :param n: A non-negative integer.
    :return: The factorial of n.
    :raises ValueError: If n is negative.
    """
    logging.debug(f"Start of factorial({n})")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    total = 1
    for i in range(1, n + 1):  # Start from 1, not 0
        total *= i
        logging.debug(f"i is {i}, total is {total}")
    logging.debug(f"End of factorial({n})")
    return total

def main():
    """Demonstrates the factorial function with logging."""
    logging.debug("Start of program")
    try:
        result = factorial(5)
        print(f"The factorial of 5 is: {result}")
    except ValueError as e:
        logging.error(f"Error: {e}")
    logging.debug("End of program")

if __name__ == "__main__":
    main()
