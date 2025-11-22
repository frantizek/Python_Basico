#!/usr/bin/env python3
"""
capacity_checker.py

A simple interactive script that:
  1. Asks the user to choose between TB or GB (advertised units).
  2. Prompts for the advertised capacity (decimal-based).
  3. Calculates the “real” (binary-based) capacity.
  4. Displays the result rounded to two decimal places.

Demonstrates:
  - Modular code (functions for each task)
  - Docstrings & type hints
  - Input validation loops
  - Constants for clarity
  - f-strings for clean output
"""

from typing import Literal

# Constants for decimal vs. binary definitions
DECIMAL_TB = 10**12
BINARY_TB  = 2**40
DECIMAL_GB = 10**9
BINARY_GB  = 2**30

def get_unit(prompt: str = "Enter TB or GB for the advertised unit: ") -> Literal["TB", "GB"]:
    """
    Prompt until the user enters 'TB' or 'GB' (case-insensitive).

    Returns the uppercase unit string.
    """
    while True:
        choice = input(prompt).strip().upper()
        if choice in ("TB", "GB"):
            return choice
        print("Invalid unit! Please enter either TB or GB.\n")

def get_positive_float(prompt: str) -> float:
    """
    Prompt until the user enters a positive floating-point number.

    Returns the parsed float.
    """
    while True:
        val_str = input(prompt).strip()
        try:
            value = float(val_str)
            if value > 0:
                return value
            else:
                print("Please enter a number greater than zero.\n")
        except ValueError:
            print("That's not a valid number. Try again.\n")

def calculate_discrepancy(unit: Literal["TB", "GB"]) -> float:
    """
    Given the advertised unit ('TB' or 'GB'), return
    the ratio between decimal and binary definitions.
    """
    if unit == "TB":
        return DECIMAL_TB / BINARY_TB
    # unit == "GB"
    return DECIMAL_GB / BINARY_GB

def main():
    """Main entry point for the script."""
    print("\n--- Capacity Discrepancy Calculator ---\n")

    unit = get_unit()
    advertised = get_positive_float(f"Enter the advertised capacity in {unit}: ")

    discrepancy = calculate_discrepancy(unit)
    real_capacity = advertised * discrepancy

    # Display with two decimal places
    print(f"\nThe actual capacity is {real_capacity:.2f} {unit}.")

if __name__ == "__main__":
    main()