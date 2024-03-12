# Create a program that generates the Fibonacci sequence up to a given number of terms.

def fibonacci_iterative(n):
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def main() -> None:
    print(fibonacci_iterative(0))
    print(fibonacci_iterative(1))
    print(fibonacci_iterative(2))
    print(fibonacci_iterative(20))


if __name__ == '__main__':
    main()
