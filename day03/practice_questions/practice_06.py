# Implement a program that prints the multiplication table of a given number.


def print_multiplication_table(base_number: int):
    for pivot in range(0, 13):
        print(f"| {base_number:>2} x {pivot:>2} = {base_number*pivot:>3} |")


def main() -> None:
    print("="*17)
    for number in range(1, 13):
        print_multiplication_table(number)
    print("="*17)


if __name__ == '__main__':
    main()
