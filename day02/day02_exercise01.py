# Create variables for storing a person's name, age and average test score.

def main() -> None:
    # Original and simplest version without validation:
    # user_name = input("Enter your name >>> ")
    # user_age = input("Enter your age >>> ")
    # user_average_test_score = input("Enter your average test score >>> ")

    while True:
        user_name = input("Enter your name >>> ")
        try:
            user_name = str(user_name)
            if len(user_name) > 3 and user_name.isalpha():
                break
            else:
                print("This is not a valid entry. Please enter a valid name")
        except ValueError:
            print("This is not a valid entry. Please enter a valid name")

    while True:
        user_age = input("Enter your age >>> ")
        try:
            user_age = int(user_age)
            break
        except ValueError:
            print("This is not a valid number. Please enter a valid number")

    while True:
        user_average_test_score = input("Enter your average test score >>> ")
        try:
            user_average_test_score = int(user_average_test_score)
            break
        except ValueError:
            try:
                user_average_test_score = float(user_average_test_score)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    print(f"Hello {user_name}. "
          f"Use wisely your {user_age} years of experience. "
          f"Congrats on your {user_average_test_score} score. ")


if __name__ == '__main__':
    main()
