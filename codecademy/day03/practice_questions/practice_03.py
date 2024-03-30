# Write a Python program to check if a given number is a prime number.

def is_this_number_prime(potential_prime_number: int) -> bool:
    if potential_prime_number < 2:
        return False
    elif potential_prime_number == 2:
        return True
    elif potential_prime_number % 2 == 0:
        return False
    else:
        for i in range(3, int(potential_prime_number ** 0.5) + 1, 2):
            if potential_prime_number % i == 0:
                return False
        return True


def main() -> None:
    print(is_this_number_prime(9))
    print(is_this_number_prime(19))
    print(is_this_number_prime(0))
    print(is_this_number_prime(1))
    print(is_this_number_prime(2))


if __name__ == '__main__':
    main()
