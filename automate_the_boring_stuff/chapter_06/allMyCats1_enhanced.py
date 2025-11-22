#!/usr/bin/env python3
"""
cat_names_input.py

Prompts the user to enter names for four cats and prints them all together.

Demonstrates:
- Basic user input handling
- Variable assignment
- String concatenation
"""


def main():
    """Main function to collect and display four cat names."""

    # Prompt the user for each cat's name
    print('Enter the name of cat 1:')
    cat_name_1 = input()

    print('Enter the name of cat 2:')
    cat_name_2 = input()

    print('Enter the name of cat 3:')
    cat_name_3 = input()

    print('Enter the name of cat 4:')
    cat_name_4 = input()

    # Display all cat names in a single line
    print('The cat names are:')
    print(cat_name_1 + ' ' + cat_name_2 + ' ' + cat_name_3 + ' ' + cat_name_4)


if __name__ == "__main__":
    main()