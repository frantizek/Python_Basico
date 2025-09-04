#!/usr/bin/env python3
"""
hello_user.py

A simple interactive script that:
  1. Greets the user.
  2. Asks for their name, then reports its length.
  3. Asks for their age, then tells them how old they'll be next year.

Demonstrates:
  - Using functions to structure code
  - Docstrings for documentation
  - Basic input validation
  - f-strings for formatting
"""


def get_nonempty_string(prompt: str) -> str:
    """
    Prompt the user until they enter a non-empty string.

    :param prompt: The text to display to the user.
    :return: A non-empty string entered by the user.
    """
    while True:
        response = input(prompt).strip()
        if response:
            return response
        print("Please enter at least one character.\n")


def get_positive_int(prompt: str) -> int:
    """
    Prompt the user until they enter a valid positive integer.

    :param prompt: The text to display to the user.
    :return: The integer parsed from the user's input.
    """
    while True:
        value_str = input(prompt).strip()
        if value_str.isdigit():
            return int(value_str)
        print("That's not a valid positive integer. Try again.\n")


def main():
    """Main entry point for the script."""
    print("Hello, world!\n")

    # Ask for the user's name and report its length
    name = get_nonempty_string("What is your name? ")
    print(f"\nIt is good to meet you, {name}!")
    print(f"The length of your name is: {len(name)} characters.\n")

    # Ask for the user's age and calculate next year’s age
    age = get_positive_int("What is your age? ")
    next_age = age + 1
    print(f"\nYou will be {next_age} years old next year.")


if __name__ == "__main__":
    main()