#!/usr/bin/env python3
"""
pet_name_check.py

Prompts the user to enter a pet name and checks if it exists in a predefined list.

Demonstrates:
- List membership testing using `in` and `not in`
- Conditional branching
- Basic user input handling
"""


def main():
    """Checks if the entered pet name is in the list of known pets."""

    # Predefined list of pet names
    my_pets = ['Zophie', 'Pooka', 'Fat-tail']

    # Prompt the user to enter a pet name
    print('Enter a pet name:')
    name = input()

    # Check if the entered name is in the list
    if name not in my_pets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.')


if __name__ == "__main__":
    main()