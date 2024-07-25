# Implementar una función para calcular 
# la potencia dado dos números enteros, 
# el primero representa la base y segundo el exponente.
import math

def potencia_de_dos_numeros(base: int, exponente: int) -> float:
    """Producto de dos numeros enteros."""
    return math.pow(base, exponente)


def main():
    print(potencia_de_dos_numeros(3,3))


if __name__ == '__main__':
    main()
