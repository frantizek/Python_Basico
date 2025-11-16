#!/usr/bin/env python3
"""
character_frequency.py

Counts how many times each character appears in a given string.

Demonstrates core Chapter 7 concepts:
- Dictionary usage for tracking data
- The setdefault() method to avoid KeyError
- Iterating over strings
- Basic data accumulation pattern

This script uses only features introduced by Chapter 7 of
"Automate the Boring Stuff with Python" (3rd Edition).

Author: Inspired by Chapter 7 example
"""

# The message to analyze (from George Orwell's *1984*)
MESSAGE = 'It was a bright cold day in April, and the clocks were striking thirteen.'


def count_characters(text):
    """
    Returns a dictionary mapping each character in `text`
    to the number of times it appears.

    Uses dict.setdefault() as shown in Chapter 7.
    """
    count = {}
    for character in text:
        count.setdefault(character, 0)  # Initialize to 0 if not present
        count[character] += 1  # Increment the count
    return count


def display_counts(count_dict):
    """Prints the character counts in a readable format."""
    print("Character frequency count:")
    print("-" * 30)
    for char, freq in count_dict.items():
        # Represent special characters (like space) clearly
        display_char = repr(char) if char in (' ', '\t', '\n') else char
        print(f"{display_char:>5} : {freq}")


def main():
    """Main program logic."""
    char_count = count_characters(MESSAGE)
    display_counts(char_count)


if __name__ == "__main__":
    main()