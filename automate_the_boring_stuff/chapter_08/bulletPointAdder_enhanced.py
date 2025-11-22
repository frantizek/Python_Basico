#!/usr/bin/env python3
"""
add_stars_enhanced.py
Takes text from the clipboard, adds a star (*) to the beginning of each line,
and copies the modified text back to the clipboard.
Demonstrates:
  - Clipboard interaction with pyperclip
  - String manipulation (splitting and joining)
  - Iteration over lists
  - Error handling for clipboard access
"""

import pyperclip

def add_stars_to_lines(text: str) -> str:
    """
    Adds a star (*) to the beginning of each line in the input text.

    :param text: The input string to process.
    :return: The modified string with stars at the beginning of each line.
    """
    lines = text.split('\n')  # Split the text into a list of lines
    for i in range(len(lines)):
        lines[i] = '* ' + lines[i]  # Add a star to each line
    return '\n'.join(lines)  # Join the lines back into a single string

def main():
    """Adds stars to clipboard text and copies the result back."""
    try:
        # Get text from the clipboard
        text = pyperclip.paste()
        if not text:
            print("Error: Clipboard is empty.")
            return

        # Add stars to each line
        modified_text = add_stars_to_lines(text)

        # Copy the modified text back to the clipboard
        pyperclip.copy(modified_text)

        # Print the result for user feedback
        print("Modified text (copied to clipboard):")
        print(modified_text)

    except pyperclip.PyperclipException:
        print("Error: Could not access the clipboard. Make sure it is available.")

if __name__ == "__main__":
    main()
