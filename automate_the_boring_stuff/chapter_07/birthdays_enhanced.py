#!/usr/bin/env python3
"""
birthday_database.py

An interactive program that stores and retrieves birthday information
using a Python dictionary.

Demonstrates core concepts from Chapter 7 of "Automate the Boring Stuff with Python":
- Dictionary creation and usage
- Checking membership with `in`
- Adding new key-value pairs at runtime
- Basic input validation and user interaction

The program runs in a loop, allowing the user to:
- Look up existing birthdays
- Add new entries
- Quit by entering a blank name

Author: Inspired by "Automate the Boring Stuff with Python", Chapter 7
Compatibility: Python 3.6+
"""

# Initial birthday database (dictionary with name -> birthday mapping)
birthdays = {
    'Alice': 'Apr 1',
    'Bob': 'Dec 12',
    'Carol': 'Mar 4'
}


def main():
    """Main program loop for birthday lookup and entry."""
    print("Welcome to the Birthday Database!")
    print("You can look up or add birthdays. Enter a blank name to quit.\n")

    while True:
        # Prompt user for a name
        print('Enter a name: (blank to quit)')
        name = input().strip()  # Remove accidental whitespace

        # Exit condition: blank input
        if name == '':
            print("Goodbye!")
            break

        # Check if the name exists in the database
        if name in birthdays:
            print(f"{birthdays[name]} is the birthday of {name}")
        else:
            # Handle missing name: collect and store birthday
            print(f"I do not have birthday information for {name}.")
            print("What is their birthday?")
            bday = input().strip()

            # Only store if user provided a birthday
            if bday:
                birthdays[name] = bday
                print("Birthday database updated.")
            else:
                print("No birthday entered. Entry not saved.")

        print()  # Blank line for readability


if __name__ == "__main__":
    main()