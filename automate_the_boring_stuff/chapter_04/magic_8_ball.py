#!/usr/bin/env python3
"""
magic_8_ball.py

Simulates a Magic 8-Ball toy that gives fortune-telling answers.

Demonstrates:
  - Function definitions with return values
  - Random number generation
  - Mapping numbers to specific outcomes
"""

import random

def get_answer(answer_number: int) -> str:
    """
    Returns a fortune answer based on the input number.

    :param answer_number: An integer between 1 and 9.
    :return: A string with a fortune-telling message.
    """
    answers = {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        9: 'Very doubtful',
    }
    return answers.get(answer_number, 'Say again?')

def main():
    """Main function to get input from the user and display a fortune."""
    print('Ask a yes or no question:')
    input('> ')  # Capture the user's question (not used)
    r = random.randint(1, 9)  # Randomly choose a response number
    fortune = get_answer(r)
    print(fortune)

if __name__ == "__main__":
    main()