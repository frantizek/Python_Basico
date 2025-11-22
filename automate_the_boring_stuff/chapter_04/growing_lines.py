#!/usr/bin/env python3
"""
growing_lines.py
Animates a pattern of lines that grow and shrink.
Demonstrates:
  - Nested loops for animation
  - String multiplication for dynamic patterns
  - Graceful exit on user interruption
"""
import time
import sys

def animate_growing_lines(max_size: int = 8, delay: float = 0.1):
    """
    Animates a pattern of lines that grow and shrink.

    :param max_size: The maximum number of lines (default: 8).
    :param delay: The delay between frames in seconds (default: 0.1).
    """
    try:
        while True:
            # Draw lines with increasing length
            for i in range(1, max_size + 1):
                print('-' * (i * i))
                time.sleep(delay)

            # Draw lines with decreasing length
            for i in range(max_size - 1, 0, -1):
                print('-' * (i * i))
                time.sleep(delay)

    except KeyboardInterrupt:
        print("\nAnimation stopped by user.")
        sys.exit()

if __name__ == "__main__":
    animate_growing_lines()
