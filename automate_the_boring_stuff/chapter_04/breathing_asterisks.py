#!/usr/bin/env python3
"""
breathing_asterisks.py
Animates a row of asterisks that "breathes" by expanding and contracting.
Demonstrates:
  - Infinite loops with user interruption handling
  - Conditional logic for state changes
  - String multiplication for dynamic indentation
  - Graceful exit on KeyboardInterrupt
"""
import time
import sys

def animate_asterisks():
    """Animates a row of asterisks that expands and contracts."""
    indent = 0
    indent_increasing = True
    max_indent = 20  # Maximum indentation level

    try:
        while True:
            print(' ' * indent, end='')
            print('********')
            time.sleep(0.1)  # Pause for animation effect

            if indent_increasing:
                indent += 1
                if indent == max_indent:
                    indent_increasing = False
            else:
                indent -= 1
                if indent == 0:
                    indent_increasing = True
    except KeyboardInterrupt:
        print("\nAnimation stopped by user.")
        sys.exit()

if __name__ == "__main__":
    animate_asterisks()
