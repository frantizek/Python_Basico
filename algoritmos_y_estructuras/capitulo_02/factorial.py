def factorial(numero: int) -> float:
    """Calculo recursivo del factorial."""
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)

def pythonic_factorial(numero: int) -> float:
    """Calculo recursivo del factorial."""
    return 1 if numero == 0 else numero * factorial(numero-1)

def main():
    print(factorial(5))
    print(pythonic_factorial(5))


if __name__ == '__main__':
    main()
