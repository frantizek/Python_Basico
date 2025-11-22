#!/usr/bin/env python3
"""
magic8Ball2.py

Simulates a Magic 8-Ball toy that gives random answers to yes/no questions.

Demonstrates:
- List usage for storing possible responses
- Random selection from a list
- Basic user interaction
"""

import random


def main():
    """Prompts the user for a yes/no question and prints a random response."""

    # List of possible Magic 8-Ball responses
    messages = [
        'It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful'
    ]

    # Prompt the user to ask a yes/no question
    print('Ask a yes or no question:')
    input('>')  # We don't store the input; it's just for interaction

    # Select and display a random response from the list
    print(messages[random.randint(0, len(messages) - 1)])


if __name__ == "__main__":
    main()