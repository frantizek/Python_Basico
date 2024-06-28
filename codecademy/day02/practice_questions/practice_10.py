# Write a program to check if a number is prime.


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    num = int(input("Enter a number to check if it's prime: "))
    if is_prime(num):
        print(f"The number {num} is a prime number.")
    else:
        print(f"The number {num} is not a prime number.")


if __name__ == '__main__':
    main()
