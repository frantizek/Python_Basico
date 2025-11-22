#!/usr/bin/env python3
"""
box_print.py
Draws a box using a given symbol, width, and height.
Demonstrates:
  - Input validation with custom exceptions
  - String manipulation for pattern drawing
  - Error handling for user feedback
"""
def box_print(symbol: str, width: int, height: int) -> None:
    """
    Prints a box made of the given symbol with the specified width and height.

    :param symbol: A single character used to draw the box.
    :param width: The width of the box (must be > 2).
    :param height: The height of the box (must be > 2).
    :raises ValueError: If symbol is not a single character, or if width/height are too small.
    """
    if len(symbol) != 1:
        raise ValueError("Symbol must be a single character.")
    if width <= 2:
        raise ValueError("Width must be greater than 2.")
    if height <= 2:
        raise ValueError("Height must be greater than 2.")

    # Draw top border
    print(symbol * width)
    # Draw middle section
    for _ in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    # Draw bottom border
    print(symbol * width)

def main():
    """Demonstrates box_print with various inputs and error handling."""
    test_cases = [
        ('*', 4, 4),
        ('O', 20, 5),
        ('x', 1, 3),  # Expected to raise ValueError (width too small)
        ('ZZ', 3, 3), # Expected to raise ValueError (symbol too long)
    ]

    for symbol, width, height in test_cases:
        try:
            print(f"\nDrawing box with symbol='{symbol}', width={width}, height={height}:")
            box_print(symbol, width, height)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
