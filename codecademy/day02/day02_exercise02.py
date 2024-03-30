# Concatenate two strings and print the result.


def main() -> None:
    the_first_string = "Umpa"
    the_second_string = "lumpa"

    print(f"This is the first string {the_first_string.upper()} "
          f"and this the second string {the_second_string.upper()}...")
    print(f"and this is the concatenation of them : {the_first_string.upper() + the_second_string.upper()}")


if __name__ == '__main__':
    main()
