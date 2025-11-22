#!/usr/bin/env python3
"""
opposite_day.py

Determines if today is Opposite Day by toggling state.

Demonstrates:
  - Boolean toggling
  - Simplifying redundant conditions
"""


def main():
    """Main entry point for the script."""
    today_is_opposite_day = True

    # Simplify the logic with direct assignment and toggle
    say_it_is_opposite_day = today_is_opposite_day

    # Toggle for Opposite Day logic
    if today_is_opposite_day:
        say_it_is_opposite_day = not say_it_is_opposite_day

    # Determine and print the result
    if say_it_is_opposite_day:
        print('Today is Opposite Day.')
    else:
        print('Today is not Opposite Day.')


if __name__ == "__main__":
    main()