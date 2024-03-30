# Write a program to check if a number is even or odd.


def main() -> None:
    while True:
        is_this_number_even_or_odd = input("Enter a number : ")
        try:
            is_this_number_even_or_odd = int(is_this_number_even_or_odd)
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid number")

    if is_this_number_even_or_odd % 2 == 0:
        print(f"{is_this_number_even_or_odd} is even.")
    else:
        print(f"{is_this_number_even_or_odd} is odd.")


if __name__ == '__main__':
    main()
