#!/usr/bin/env python3
"""
buggy_coin_toss.py
A simple coin toss guessing game.
The player gets two guesses to match the coin toss result.
Note: This version contains bugs for debugging practice.
"""

import random  # Required for generating random numbers

def main():
    """
    Runs the coin toss guessing game.
    The player is prompted to guess heads or tails.
    The coin is tossed, and the player's guess is checked.
    If the first guess is incorrect, the player gets a second chance.
    """
    guess = ''  # Initialize the player's guess

    # Prompt the player for their first guess
    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    # Simulate a coin toss: 0 represents tails, 1 represents heads
    toss = random.randint(0, 1)
    number_guess = 0 if guess == "tails" else 1

    # Check if the player's guess matches the coin toss result
    if toss == number_guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()  # Prompt the player for a second guess
        number_guess = 0 if guess == "tails" else 1

        # Check if the second guess matches the coin toss result
        if toss == number_guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

if __name__ == "__main__":
    main()
