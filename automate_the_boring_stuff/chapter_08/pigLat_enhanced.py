#!/usr/bin/env python3
"""
pig_latin_enhanced.py
Translates an English message into Pig Latin.
Demonstrates:
  - String manipulation
  - Iteration over words and characters
  - Handling punctuation and capitalization
  - Modular code structure
"""

def translate_to_pig_latin(message: str) -> str:
    """
    Translates an English message into Pig Latin.

    :param message: The English message to translate.
    :return: The translated message in Pig Latin.
    """
    VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
    pig_latin = []  # List to store translated words

    for word in message.split():
        # Separate non-letters at the start of the word
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        if len(word) == 0:
            pig_latin.append(prefix_non_letters)
            continue

        # Separate non-letters at the end of the word
        suffix_non_letters = ''
        while not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]

        # Preserve the original capitalization
        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()  # Convert to lowercase for translation

        # Separate consonants at the start of the word
        prefix_consonants = ''
        while len(word) > 0 and word[0] not in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        # Add the Pig Latin ending
        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'yay'

        # Restore the original capitalization
        if was_upper:
            word = word.upper()
        if was_title:
            word = word.title()

        # Add non-letters back to the word
        pig_latin.append(prefix_non_letters + word + suffix_non_letters)

    return ' '.join(pig_latin)  # Join the translated words into a single string

def main():
    """Prompts the user for an English message and translates it to Pig Latin."""
    print('Enter the English message to translate into Pig Latin:')
    message = input()
    translated_message = translate_to_pig_latin(message)
    print(translated_message)

if __name__ == "__main__":
    main()
