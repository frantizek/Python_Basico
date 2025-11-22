"""
Practice Programs
My 'optimized' version
"""


def collatz(number: int):
    return number // 2 if number % 2 == 0 else 3 * number + 1


def main() -> None:
    while True:
        input_str = input("Teclea un numero entero : ")
        try:
            input_integer = int(input_str)
            if input_integer <= 0:
                print("¡Solo números *positivos*! Intenta otra vez.")
                continue
            break
        except ValueError:
            print(f"¡{input_str} no es un número entero! Intenta otra vez.")
    results = []
    result = input_integer
    results.append(result)
    while result != 1:
        result = collatz(result)
        results.append(result)
    print(" ".join(str(c) for c in results))


if __name__ == '__main__':
    main()
