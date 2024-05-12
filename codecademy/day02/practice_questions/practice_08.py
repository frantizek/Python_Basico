# Implement a program that converts a given number of minutes into hours and minutes.
#

def main() -> None:
    print("Convert a given number of minutes into hours and minutes.")
    print("-" * 60)

    while True:
        number_of_minutes = input("Please provide the number or minutes : ")
        try:
            number_of_minutes = int(number_of_minutes)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")

    print(f"Hours:  {number_of_minutes//60}, Minutes: {number_of_minutes%60}")


if __name__ == '__main__':
    main()
