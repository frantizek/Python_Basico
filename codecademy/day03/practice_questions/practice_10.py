# Calculate the sum of digits of a given number.


def sum_of_digits(num_to_process: int):
    sum_digits = 0
    for element in str(num_to_process):
        if element.isdecimal():
            sum_digits += int(element)
    return sum_digits


def main() -> None:
    print(sum_of_digits(-1111))
    print(sum_of_digits(10000000000000000000000000000000000000000))


if __name__ == '__main__':
    main()
