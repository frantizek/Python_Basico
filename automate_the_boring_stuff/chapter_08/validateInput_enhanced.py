#!/usr/bin/env python3
"""
validate_input_enhanced.py
Prompts the user for valid age and password inputs.
Demonstrates:
  - Input validation using string methods
  - Looping until valid input is provided
  - User-friendly error messages
"""

def get_valid_age() -> str:
    """
    Prompts the user for their age and validates that it is a decimal number.

    :return: The user's age as a string of digits.
    """
    while True:
        print('Enter your age:')
        age = input().strip()
        if age.isdecimal():
            return age
        print('Error: Please enter a number for your age.')

def get_valid_password() -> str:
    """
    Prompts the user for a new password and validates that it contains only letters and numbers.

    :return: The user's password as a string of alphanumeric characters.
    """
    while True:
        print('Select a new password (letters and numbers only):')
        password = input().strip()
        if password.isalnum():
            return password
        print('Error: Passwords can only have letters and numbers.')

def main():
    """Prompts the user for valid age and password inputs."""
    print("=== Input Validation Demo ===")

    # Get and validate user age
    age = get_valid_age()
    print(f"Valid age entered: {age}")

    # Get and validate user password
    password = get_valid_password()
    print("Valid password entered.")

if __name__ == "__main__":
    main()
