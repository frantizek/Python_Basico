#!/usr/bin/env python3
"""
alternating_case_enhanced.py
Takes text from the clipboard, converts it to alternating case (e.g., "AlTeRnAtInG"),
and copies the result back to the clipboard.
Demonstrates:
  - Clipboard interaction with pyperclip
  - String manipulation
  - Iteration over characters
  - Modular code structure
"""

import pyperclip

def convert_to_alternating_case(text: str) -> str:
    """
    Converts the input text to alternating case (e.g., "AlTeRnAtInG").

    :param text: The input string to convert.
    :return: The converted string in alternating case.
    """
    alt_text = ''  # Initialize the result string
    make_uppercase = True  # Flag to alternate case

    for character in text:
        # Alternate the case of each character
        if make_uppercase:
            alt_text += character.upper()
        else:
            alt_text += character.lower()
        # Toggle the case flag
        make_uppercase = not make_uppercase

    return alt_text

def main():
    """Converts clipboard text to alternating case and copies it back."""
    try:
        # Get text from the clipboard
        text = pyperclip.paste()
        if not text:
            print("Error: Clipboard is empty.")
            return

        # Convert the text to alternating case
        alt_text = convert_to_alternating_case(text)

        # Copy the result back to the clipboard
        pyperclip.copy(alt_text)

        # Print the result for user feedback
        print("Converted text (copied to clipboard):")
        print(alt_text)

    except pyperclip.PyperclipException:
        print("Error: Could not access the clipboard. Make sure it is available.")

if __name__ == "__main__":
    main()
