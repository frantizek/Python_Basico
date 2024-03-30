# Write a program that checks if a given number is positive, negative, or zero.

def main() -> None:
    while True:
        evaluated_number = input("Please provide the first number : ")
        try:
            evaluated_number = int(evaluated_number)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")
    if evaluated_number > 0:
        print("Positive")
    elif evaluated_number < 0:
        print("Negative")
    else:
        print("Zero")


if __name__ == '__main__':
    main()
