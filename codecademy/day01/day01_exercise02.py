# Calculate the sum of two numbers entered by the user.


def main() -> None:
    print("Calculate the sum of two numbers")
    print("-" * 60)

    while True:
        first_number = input("Please provide the first number : ")
        try:
            first_number = int(first_number)
            break
        except ValueError:
            try:
                first_number = float(first_number)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    while True:
        second_number = input("Please provide the second number : ")
        try:
            second_number = int(second_number)
            break
        except ValueError:
            try:
                second_number = float(second_number)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    print(f"Result : {first_number + second_number}")


if __name__ == '__main__':
    main()
