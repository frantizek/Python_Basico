# Create a loop that prints all prime numbers between 1 and 50.

def es_primo(num: int) -> bool:
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def main() -> None:
    for number in range(1, 51):
        if es_primo(number):
            print(number)


if __name__ == '__main__':
    main()

