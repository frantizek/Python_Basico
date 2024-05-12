#
# Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).
#
def is_pangram(given_string: str) -> bool:
    alfabeto: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                           'h', 'i', 'j', 'k', 'l', 'm', 'n',
                           'o', 'p', 'q', 'r', 's', 't', 'u',
                           'v', 'w', 'x', 'y', 'z']
    already_removed: list[str] = []
    modified_given_string: str = ''.join(e for e in given_string.lower() if e.isalpha())
    for letter in modified_given_string:
        if len(alfabeto) > 0:
            if letter in already_removed:
                # there might be some duplicates in the phrase.
                continue
            else:
                alfabeto.remove(letter)
                already_removed.append(letter)
    if len(alfabeto) == 0 and len(already_removed) == 26:
        return True
    return False


def main():
    print(is_pangram("The quick brown fox jumps over the lazy dog."))
    print(is_pangram("The quick brown font jumps over the lazy dog."))
    print(is_pangram("Portez ce vieux whisky au juge blond qui fume."))
    print(is_pangram("Portez ce vieux whisky au juge blond oui fume."))


if __name__ == '__main__':
    main()
