def fibonacciR(n: int) -> int:
    """Calculo fibonacci recursivo."""
    if n==0 or n==1:
        return n
    else:
        return fibonacciR(n-1) + fibonacciR(n-2)

def pythonic_fibonacciR(n: int) -> int:
    """Calculo fibonacci recursivo."""
    return n if n==0 or n==1 else fibonacciR(n-1) + fibonacciR(n-2)


def main():
    print(fibonacciR(10))
    print(pythonic_fibonacciR(10))


if __name__ == '__main__':
    main()
