#!/usr/bin/env python3
"""
spam_handler.py

Prints different greetings based on the value of `spam`.

Demonstrates:
  - Conditional statements
  - Iterating over a list
"""

def main():
    """Main entry point for the script."""
    content_of_spam = [1, 2, 3]

    for spam in content_of_spam:
        if spam == 1:
            print("Hello")
        elif spam == 2:
            print("Howdy")
        else:
            print("Greetings!")

if __name__ == "__main__":
    main()