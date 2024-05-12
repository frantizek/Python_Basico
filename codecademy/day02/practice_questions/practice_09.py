# Create a function to count the number of vowels in a given string.
#

def vowel_counter(given_string: str) -> int:
    vowels_in_given_string = 0
    for letter in given_string.lower():
        if letter in "aeiou":
            vowels_in_given_string += 1
    return vowels_in_given_string


def main():
    print(vowel_counter("K"))


if __name__ == '__main__':
    main()
