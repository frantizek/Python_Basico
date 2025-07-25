import sys
# Implementar una función que calcule la suma de todos
# los números enteros comprendidos entre cero 
# y un número entero positivo dado.

def suma_de_enteros(numero: int) -> int:
    """Suma de numeros enteros."""
    if numero == 0:
        return numero
    else:
        return numero + suma_de_enteros(numero-1)

def otra_suma_de_enteros(numero: int) -> int:
    """Suma de numeros enteros."""
    return numero if numero == 0 else numero + suma_de_enteros(numero-1)


def main():
    print(suma_de_enteros(99))
    print(otra_suma_de_enteros(99))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit("\nInterrupted by user.")