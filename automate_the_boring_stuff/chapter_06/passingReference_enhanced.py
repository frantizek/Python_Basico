#!/usr/bin/env python3
"""
passingReference.py

Demonstrates how mutable objects (like lists) are passed by reference in Python.

Key Concepts:
- Function arguments are references to objects
- Mutable objects can be modified in place
- Changes inside a function affect the original object
"""

def eggs(some_parameter):
    """
    Appends 'Hello' to the passed list.

    Args:
        some_parameter (list): A list that will be modified in place.
    """
    some_parameter.append('Hello')  # Modifies the original list

def main():
    """Creates a list, passes it to a function, and prints the result."""
    spam = [1, 2, 3]  # Original list
    eggs(spam)        # Passes the list to the function
    print(spam)       # Prints the modified list: [1, 2, 3, 'Hello']

if __name__ == "__main__":
    main()