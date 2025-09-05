#!/usr/bin/env python3
"""
coin_flip_simulation.py
Simulates flipping a coin 1,000 times and counts how many times heads appears.
Demonstrates:
  - Random number generation for simulations
  - Looping with range()
  - Conditional logic (if statements)
  - String concatenation for output
  - Progress reporting during long loops
"""

import random

def simulate_coin_flips(num_flips: int) -> int:
    """
    Simulates flipping a coin a specified number of times and counts heads.

    :param num_flips: The number of coin flips to simulate.
    :return: The number of times heads appeared.
    """
    heads = 0  # Initialize heads counter

    for i in range(1, num_flips + 1):
        # Randomly generate 0 (tails) or 1 (heads)
        if random.randint(0, 1) == 1:  # ❶ Check for heads
            heads += 1

        # Report progress halfway through
        if i == num_flips // 2:  # ❷ Halfway point
            print('Halfway done!')

    return heads

def main():
    """Runs the simulation and prints the result."""
    num_flips = 1000
    heads = simulate_coin_flips(num_flips)

    # Print the result
    print('Heads came up ' + str(heads) + ' times out of ' + str(num_flips) + ' flips.')

if __name__ == "__main__":
    main()
