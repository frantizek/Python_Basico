#!/usr/bin/env python3
"""
matrixscreensaver.py

Simulates a Matrix-style digital rain animation using binary digits.

Demonstrates:
- Infinite loop animation
- List-based column state tracking
- Randomized stream generation
- Graceful exit on keyboard interrupt
"""

import random, sys, time

WIDTH = 70  # Number of columns in the output; adjust based on terminal size

def main():
    """Runs the Matrix screensaver animation."""
    try:
        # Initialize each column with a counter value of 0 (no stream)
        columns = [0] * WIDTH

        while True:
            # Iterate over each column index
            for i in range(WIDTH):
                # 2% chance to start a new stream in this column
                if random.random() < 0.02:
                    # Stream length randomly chosen between 4 and 14 characters
                    columns[i] = random.randint(4, 14)

                # Print a character based on the column's counter
                if columns[i] == 0:
                    # Print a space if no stream is active
                    print(' ', end='')
                else:
                    # Print a random binary digit and decrement the stream counter
                    print(random.choice([0, 1]), end='')
                    columns[i] -= 1

            # Move to the next line after printing all columns
            print()
            # Pause briefly to control animation speed
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Exit gracefully when user presses Ctrl-C
        sys.exit()

if __name__ == "__main__":
    main()