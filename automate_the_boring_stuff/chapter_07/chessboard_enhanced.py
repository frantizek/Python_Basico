#!/usr/bin/env python3
"""
interactive_chess_board.py

An interactive command-line chess board viewer and editor.

This program displays a standard 8x8 chess board using ASCII art and allows the user
to manipulate pieces via simple text commands. It demonstrates core Python concepts:
- Dictionary usage for board state
- String formatting for visual layout
- User input parsing and command dispatch

Commands:
  move <from> <to>    — Move a piece from one square to another
  remove <square>     — Remove the piece on a square
  set <square> <piece>— Place a piece on a square
  reset               — Restore board to standard starting position
  clear               — Remove all pieces
  fill <piece>        — Fill entire board with the given piece
  help                — Show this help message
  quit                — Exit the program

Piece notation:
  Color: 'w' = white, 'b' = black
  Type:  'P' = Pawn, 'N' = Knight, 'B' = Bishop,
         'R' = Rook, 'Q' = Queen, 'K' = King

Example: 'wK' = white king, 'bN' = black knight

Note: This program does not validate chess rules (e.g., legal moves).
It is a board state editor only.

Author: Inspired by Al Sweigart (inventwithpython.com)
Compatibility: Python 3.6+
"""

import sys
import copy

# Standard starting position for a chess game (note: contains typos as in original)
# TODO: 'c1': 'ww' and 'f1': 'ww' appear to be errors; should likely be 'wB'
STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',
    'a1': 'wR', 'b1': 'wN', 'c1': 'ww', 'd1': 'wQ',  # ← likely typo
    'e1': 'wK', 'f1': 'ww', 'g1': 'wN', 'h1': 'wR',  # ← likely typo
    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'
}

# ASCII art template for the chess board
# Each `{}` will be replaced by a piece code or a square indicator
BOARD_TEMPLATE = """
    a    b    c    d    e    f    g    h
   ____ ____ ____ ____ ____ ____ ____ ____
  ||||||    ||||||    ||||||    ||||||    |
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
  ||||||    ||||||    ||||||    ||||||    |
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
  |    ||||||    ||||||    ||||||    ||||||
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

# Visual representations for empty squares
WHITE_SQUARE = '||'  # Represents a light-colored empty square
BLACK_SQUARE = '  '  # Represents a dark-colored empty square


def print_chess_board(board):
    """
    Prints the current state of the chess board using the BOARD_TEMPLATE.

    The board alternates between light and dark squares (starting with light on a8).
    For each square (from a8 to h1, row by row), it checks if a piece is present.
    If so, it displays the piece code (e.g., 'wK'); otherwise, it shows the square color.

    Parameters:
        board (dict): A dictionary mapping square names (e.g., 'e4') to piece codes.
    """
    squares = []  # Will hold 64 entries for the 8x8 board
    is_white_square = True  # a8 is a light square in standard chess board representation

    # Traverse rows from 8 (top) down to 1 (bottom)
    for y in '87654321':
        # Traverse columns from a (left) to h (right)
        for x in 'abcdefgh':
            square = x + y
            # If piece exists on this square, use its code
            if square in board:
                squares.append(board[square])
            else:
                # Otherwise, show empty square using alternating pattern
                squares.append(WHITE_SQUARE if is_white_square else BLACK_SQUARE)
            # Toggle square color for next column
            is_white_square = not is_white_square
        # After each row, toggle again to maintain checkerboard pattern
        is_white_square = not is_white_square

    # Insert the 64 square values into the template and print
    print(BOARD_TEMPLATE.format(*squares))


def print_help():
    """Displays the help message explaining commands and piece notation."""
    print('Interactive Chess Board')
    print('by Al Sweigart al@inventwithpython.com')
    print()
    print('Pieces:')
    print('  w - White, b - Black')
    print('  P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
    print('Commands:')
    print('  move e2 e4 - Moves the piece at e2 to e4.')
    print('  remove e2 - Removes the piece at e2.')
    print('  set e2 wP - Sets square e2 to a white pawn.')
    print('  reset - Reset pieces back to their starting squares.')
    print('  clear - Clear the entire board.')
    print('  fill wP - Fill entire board with white pawns.')
    print('  help - Show this help information.')
    print('  quit - Quits the program.')


# Main program logic
if __name__ == "__main__":
    # Initialize the board with starting position (shallow copy is sufficient)
    main_board = copy.copy(STARTING_PIECES)
    print_help()

    # Main command loop
    while True:
        print_chess_board(main_board)
        user_input = input('> ').strip()

        # Skip empty input
        if not user_input:
            continue

        # Split into command and arguments
        response = user_input.split()

        # Dispatch based on first word (the command)
        if response[0] == 'move':
            if len(response) == 3:
                from_square, to_square = response[1], response[2]
                # Move piece (overwrites any existing piece at destination)
                main_board[to_square] = main_board[from_square]
                del main_board[from_square]
            else:
                print("Usage: move <from> <to>")

        elif response[0] == 'remove':
            if len(response) == 2:
                square = response[1]
                if square in main_board:
                    del main_board[square]
                else:
                    print(f"No piece on {square}")
            else:
                print("Usage: remove <square>")

        elif response[0] == 'set':
            if len(response) == 3:
                square, piece = response[1], response[2]
                main_board[square] = piece
            else:
                print("Usage: set <square> <piece>")

        elif response[0] == 'reset':
            main_board = copy.copy(STARTING_PIECES)

        elif response[0] == 'clear':
            main_board = {}

        elif response[0] == 'fill':
            if len(response) == 2:
                piece = response[1]
                main_board = {x + y: piece for y in '87654321' for x in 'abcdefgh'}
            else:
                print("Usage: fill <piece>")

        elif response[0] == 'help':
            print_help()

        elif response[0] == 'quit':
            sys.exit()

        else:
            print("Unknown command. Type 'help' for available commands.")