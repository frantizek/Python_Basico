# Create a program that takes a user's name and age as input and prints a greeting message.


def main() -> None:
    while True:
        name = input("Please enter your name : ")
        try:
            name = str(name)
            if len(name) > 3 and name.isalpha():
                break
            else:
                print("This is not a valid entry. Please enter a valid name")
        except ValueError:
            print("This is not a valid entry. Please enter a valid name")

    while True:
        age = input("Please provide your age : ")
        try:
            age = int(age)
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid number")

    print(f"Greetings {name}, lets start planning your {age + 1}th birthday.")


if __name__ == '__main__':
    main()
