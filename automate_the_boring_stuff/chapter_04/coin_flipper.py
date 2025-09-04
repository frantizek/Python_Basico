#!/usr/bin/env python3
"""
coin_flipper.py

Simulates 100 coin flips and displays the results.

Demonstrates:
  - Looping with a range
  - Random number generation
  - Collecting and displaying results in a single line
"""

import random

def main():
    """Simulate 100 coin flips and print the result."""
    for _ in range(100):  # Perform 100 coin flips.
        # Randomly choose between 0 and 1, representing heads or tails.
        if random.randint(0, 1) == 0:
            print('H', end=' ')
        else:
            print('T', end=' ')
    print()  # Print one newline at the end.

if __name__ == "__main__":
    main()