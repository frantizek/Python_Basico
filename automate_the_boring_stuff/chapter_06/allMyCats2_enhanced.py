#!/usr/bin/env python3
"""
dynamic_cat_names.py

Prompts the user to enter cat names one by one until they choose to stop.
Then prints all collected cat names.

Demonstrates:
- Dynamic list creation
- Looping with a break condition
- String concatenation
"""

def main():
    """Collects cat names from user input and displays them."""
    cat_names = []  # Initialize an empty list to store cat names

    while True:
        # Prompt the user for the next cat name
        print('Enter the name of cat ' + str(len(cat_names) + 1) +
              ' (Or enter nothing to stop.):')
        name = input()

        # If the user enters nothing, exit the loop
        if name == '':
            break

        # Add the entered name to the list using list concatenation
        cat_names = cat_names + [name]

    # Display all collected cat names
    print('The cat names are:')
    for name in cat_names:
        print('  ' + name)

if __name__ == "__main__":
    main()