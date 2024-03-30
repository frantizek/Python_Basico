# Write a program that calculates the factorial of a given number.

def factorial(n):
    """
    Calculates the factorial of a number using a recursive function.

    Args:
      n: The number to calculate the factorial of.

    Returns:
      The factorial of the number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def main() -> None:
    for number in range(0, 35):
        print(f"The factorial of {number} is {factorial(number)}")


if __name__ == '__main__':
    main()

