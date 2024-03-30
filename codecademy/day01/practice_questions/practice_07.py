# Write a program that converts a given number of days into years, weeks and days.

def convert_days_into_years_weeks_days(total_days: int) -> tuple[int, int, int]:
    years = total_days // 365
    rem_from_years = total_days % 365
    weeks = rem_from_years // 7
    days = rem_from_years % 7
    return years, weeks, days


def main() -> None:
    print("Converts a given number of days into years, weeks and days.")
    print("-" * 70)

    while True:
        total_number_days = input("Please provide the number of days : ")
        try:
            total_number_days = int(total_number_days)
            break
        except ValueError:
            print("This is not a number. Please enter a valid number")

    my_years, my_weeks, my_days = convert_days_into_years_weeks_days(total_number_days)

    print(f"You entered a total of {total_number_days}, and that is exactly:")
    print(f"  - {my_years} years, {my_weeks} weeks, {my_days} days.")


if __name__ == '__main__':
    main()
