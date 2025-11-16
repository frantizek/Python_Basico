#!/usr/bin/env python3
"""
chess_validator.py

Practice Program: Chess Dictionary Validator

Write a function named isValidChessBoard() that takes a dictionary argument
and returns True or False depending on whether the board is valid.

A valid board must satisfy the following:
- Exactly one black king ('bK') and exactly one white king ('wK')
- Each player has at most 16 pieces total
- Each player has at most 8 pawns
- All pieces are on valid squares: '1a' to '8h' (i.e., files 'a'–'h', ranks '1'–'8')
- Piece names must start with 'w' (white) or 'b' (black), followed by one of:
    'pawn', 'knight', 'bishop', 'rook', 'queen', 'king'

Example valid board:
{'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}

This function should detect bugs that result in an invalid chessboard.

Author: Practice Program from Chapter 7 — Automate the Boring Stuff with Python
"""


def isValidChessBoard(board: dict) -> bool:
    """
    Validates whether the given chess board dictionary represents a legal
    configuration according to the rules outlined in the practice problem.

    Parameters:
        board (dict): Keys are strings like 'a1', 'h8'; values are piece codes
                      like 'wK', 'bQ', etc.

    Returns:
        bool: True if the board is valid, False otherwise.
    """
    # print(board)
    positions = []
    white_pieces = []
    black_pieces = []
    for position, piece in board.items():
        #print(f"Processing: {position} {piece}")
        if position[0] in 'abcdefgh' and 1 <= int(position[1]) <=8 :
            #print(f"{position} is valid")
            positions.append(position)
        else:
            return False
        if piece[0] == "b" and piece[1] in 'PNBRQK':
            black_pieces.append(piece)
        elif piece[0] == "w"and piece[1] in 'PNBRQK':
            white_pieces.append(piece)
        else:
            return False



    # print(positions, white_pieces, black_pieces)
    # Exactly one black king ('bK') and exactly one white king ('wK')
    if white_pieces.count("wK") != 1 or black_pieces.count("bK") != 1:
        return False
    # Each player has at most 16 pieces total
    if len(white_pieces) > 16 or len(black_pieces) > 16:
        return False
    # Each player has at most 8 pawns
    if white_pieces.count("wP") > 8 or black_pieces.count("bP") > 8:
        return False

    return True



# Example test cases (uncomment to test your function)
if __name__ == "__main__":
    # Valid board
    valid_board = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
    print("Valid board test:", isValidChessBoard(valid_board))  # Should return True

    # Invalid board: two white kings
    invalid_board = {'h1': 'bK', 'e3': 'wK', 'a1': 'wK'}
    print("Invalid board test:", isValidChessBoard(invalid_board))  # Should return False

    # Invalid board: two white kings
    invalid_board = {'h0': 'bK', 'e3': 'wK', 'a1': 'wK'}
    print("Invalid board test:", isValidChessBoard(invalid_board))  # Should return False

    # Invalid board: two white kings
    invalid_board = {'h0': 'bK', 'e3': 'wK', 'a1': 'wK'}
    print("Invalid board test:", isValidChessBoard(invalid_board))  # Should return False

    # Valid board
    valid_board = {'h1': 'bK', 'c6': 'wQ', 'g2': 'bB', 'h5': 'bQ', 'e3': 'wK'}
    print("Valid board test:", isValidChessBoard(valid_board))  # Should return True

    # Invalid board: two white kings
    invalid_board = {'h1': 'bK', 'e3': 'wK', 'a1': 'wK'}
    print("Invalid board test:", isValidChessBoard(invalid_board))  # Should return False

    # Invalid board: invalid square 'h0'
    invalid_board = {'h0': 'bK', 'e3': 'wK'}
    print("Invalid square test:", isValidChessBoard(invalid_board))  # Should return False

    # Invalid board: too many white pawns
    too_many_pawns = {f'a{i}': 'wp' for i in range(1, 10)}  # 9 pawns
    too_many_pawns['e1'] = 'wK'
    too_many_pawns['e8'] = 'bK'
    print("Too many pawns test:", isValidChessBoard(too_many_pawns))  # Should return False

    # Invalid board: duplicate square
    duplicate_square = {'e1': 'wK', 'e1': 'wQ', 'e8': 'bK'}  # Note: dict can't have dup keys,
    # but if constructed differently (e.g., via mutation), this check matters
    # For demo, we skip since Python dict literal removes duplicates

    # Invalid piece: 'wZ'
    invalid_piece = {'e1': 'wK', 'e8': 'bK', 'd4': 'wZ'}
    print("Invalid piece test:", isValidChessBoard(invalid_piece))  # Should return False