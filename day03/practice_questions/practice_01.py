# Create a program that takes a year as input and checks if it is a leap year or not.

def leap_year(year: int) -> bool:
    return year % 4 == 0 and (not (year % 100 == 0) or year % 400 == 0)


def main() -> None:
    print(leap_year(2024))
    print(leap_year(4010))


if __name__ == '__main__':
    main()
