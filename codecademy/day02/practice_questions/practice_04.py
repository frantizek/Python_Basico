# Create a function to reverse a given string.

def reverse_a_string(string_to_reverse: str) -> str:
    reversed_string = ""
    if len(string_to_reverse) == 0:
        return reversed_string
    else:
        for letter in range(len(string_to_reverse)-1,-1,-1):
            reversed_string += string_to_reverse[letter]
        return reversed_string


def main():
    print(reverse_a_string("Mexico"))
    print(reverse_a_string("hasta aqui llegaron"))
    print(reverse_a_string(""))
    print(reverse_a_string("PLAYA DEL CARMEN"))


if __name__ == '__main__':
    main()
