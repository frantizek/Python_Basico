import math
import sys

def get_integer_input(prompt):
    """
    Prompt the user to enter an integer and validate the input.

    :param prompt: The input prompt to show to the user.
    :return: The validated integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def get_positive_integer_input(prompt):
    """
    Prompt the user to enter a positive integer greater than 0 and validate the input.

    :param prompt: The input prompt to show to the user.
    :return: The validated positive integer input from the user.
    """
    while True:
        value = get_integer_input(prompt)
        if value > 0:
            return value
        else:
            print("Invalid input. Please enter a positive integer greater than 0.")


def approximate_square_root(n):
    """
    Approximate the square root of a given positive integer using an algorithm.

    :param n: The positive integer to find the square root of.
    :return: The approximate square root of the integer.
    """
    integer_part = int(math.sqrt(n))  # Integer part of the square root
    fractional_part = (n - (integer_part ** 2)) / (2 * integer_part)  # Fractional part for approximation
    return integer_part + fractional_part


def main():
    # Prompt the user to enter a positive integer
    user_input = get_positive_integer_input("Please enter a positive integer greater than 0 : ")
    print(f"You entered: {user_input}")

    # Calculate the approximate square root using the custom algorithm
    approx_sqrt = approximate_square_root(user_input)
    print(f"Approximate square root (using the algorithm) of {user_input} is: {approx_sqrt:.5f}")

    # Calculate the exact square root using the math library
    exact_sqrt = math.sqrt(user_input)
    print(f"Exact square root (using math.sqrt) of {user_input} is: {exact_sqrt:.5f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by user.")
