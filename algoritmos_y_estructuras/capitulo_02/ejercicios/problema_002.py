# Implementar una función que calcule la suma de todos los números
# enteros comprendidos entre cero y un número entero positivo dado.
# Por ejemplo, si n = 3, la función debe devolver 0 + 1 + 2 + 3 = 6.

def suma_hasta_n(n):
    return n if n == 0 else n + suma_hasta_n(n - 1)


def main():
    # Casos de prueba: (entrada, valor previsto)
    test_cases = [
        (0, 0),  # Caso base: suma hasta 0
        (1, 1),  # Suma hasta 1: 0 + 1
        (3, 6),  # Suma hasta 3: 0 + 1 + 2 + 3
        (5, 15),  # Suma hasta 5: 0 + 1 + 2 + 3 + 4 + 5
        (10, 55),  # Suma hasta 10: 0 + 1 + ... + 10
    ]

    for i, (n, previsto) in enumerate(test_cases):
        try:
            result = suma_hasta_n(n)
            status = "✅" if result == previsto else "❌"
            print(f"{status} Test {i + 1}: suma_hasta_n({n}) => {result} (previsto: {previsto})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i + 1}: suma_hasta_n({n}) => Error: {str(e)} (previsto: {previsto})")


if __name__ == "__main__":
    main()