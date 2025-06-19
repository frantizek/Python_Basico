def fibonacci(n):
    return n if n==0 or n==1 else fibonacci(n-1) + fibonacci(n-2)

def main():
    # Casos de prueba: (entrada, valor esperado)
    test_cases = [
        (0, 0),  # Caso base: F(0) = 0
        (1, 1),  # Caso base: F(1) = 1
        (2, 1),  # F(2) = F(1) + F(0) = 1 + 0 = 1
        (5, 5),  # F(5) = F(4) + F(3) = 3 + 2 = 5
        (10, 55),  # F(10) = F(9) + F(8) = 34 + 21 = 55
    ]

    for i, (n, expected) in enumerate(test_cases):
        try:
            result = fibonacci(n)
            status = "✅" if result == expected else "❌"
            print(f"{status} Test {i+1}: fibonacci({n}) => {result} (expected: {expected})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i+1}: fibonacci({n}) => Error: {str(e)} (expected: {expected})")


if __name__ == "__main__":
    main()