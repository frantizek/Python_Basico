#!/usr/bin/env python3
"""
add_three_numbers.py
Takes three numbers as input from the user and prints their sum.
Demonstrates:
  - User input handling
  - Type conversion (string to float)
  - Basic arithmetic
  - Input validation
"""
def main():
    """Prompts the user for three numbers and prints their sum."""
    print('Enter the first number to add:')
    first = input()
    print('Enter the second number to add:')
    second = input()
    print('Enter the third number to add:')
    third = input()

    try:
        # Convert input strings to floats
        num1 = float(first)
        num2 = float(second)
        num3 = float(third)
        total = num1 + num2 + num3
        print(f"The sum is {total}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()