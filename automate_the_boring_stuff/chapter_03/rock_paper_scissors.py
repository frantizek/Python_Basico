#!/usr/bin/env python3
"""
rock_paper_scissors.py

A simple command-line rock-paper-scissors game.

Demonstrates:
  - Game loop and player input handling
  - Random choice for simulating computer moves
  - Tracking wins, losses, and ties
"""

import random
import sys

def get_computer_move() -> str:
    """Randomly select the computer's move (rock, paper, or scissors)."""
    return random.choice(['r', 'p', 's'])

def display_move(move: str) -> None:
    """Display the full name of the move."""
    names = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}
    print(names[move])

def main():
    """Main game loop."""
    print('ROCK, PAPER, SCISSORS')

    wins, losses, ties = 0, 0, 0

    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')

        player_move = ''
        while player_move not in ('r', 'p', 's', 'q'):
            player_move = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit > ')
            if player_move == 'q':
                print('Thanks for playing!')
                sys.exit()

        print(f'\nYou chose:', end=' ')
        display_move(player_move)
        print('versus...')

        computer_move = get_computer_move()
        print('Computer chose:', end=' ')
        display_move(computer_move)

        # Determine the outcome
        if player_move == computer_move:
            print("It's a tie!")
            ties += 1
        elif (player_move, computer_move) in [('r', 's'), ('p', 'r'), ('s', 'p')]:
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1

        print()

if __name__ == "__main__":
    main()