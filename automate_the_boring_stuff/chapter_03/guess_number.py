#!/usr/bin/env python3
"""
guess_number.py

A simple number guessing game.

Demonstrates:
  - Random number generation
  - User input processing
  - Loop control with conditional break
"""

import random

def main():
    """Main game loop."""
    secret_number = random.randint(1, 20)
    print('I am thinking of a number between 1 and 20.')

    # Allow the player 6 guesses
    for guesses_taken in range(1, 7):
        guess = int(input('Take a guess: '))

        if guess < secret_number:
            print('Your guess is too low.')
        elif guess > secret_number:
            print('Your guess is too high.')
        else:
            break  # Correct guess

    if guess == secret_number:
        print(f'Good job! You guessed the number in {guesses_taken} tries!')
    else:
        print(f'Sorry, the number I was thinking of was {secret_number}.')

if __name__ == "__main__":
    main()