# Implementar una función para calcular el producto de dos números enteros dados.
# La función debe recibir dos enteros a y b, y devolver su producto (a * b).

def el_producto(a, b):
    return a * b

def producto(a, b):
    """
    Calcula el producto de dos enteros 'a' y 'b' utilizando recursión.
    Este metodo descompone la multiplicación en una serie de sumas.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Las entradas deben ser enteros")
    if a == 0 or b == 0:
        return 0
    elif a == 1:
        return b
    elif b == 1:
        return a
    # Manejo de signos
    elif a>0 and b>0:
        # Ambos positivos
        return a + producto(a, b - 1)
    elif a<0 and b<0:
        # Ambos negativos
        return producto(abs(a), abs(b))
    elif a > 0 > b:
        # a positivo, b negativo
        return -(producto(a, abs(b)))
    elif a < 0 < b:
        # a negativo, b positivo
        return -(producto(abs(a), b))




def main():
    # Casos de prueba: (a, b, valor previsto)
    test_cases = [
        (2, 3, 6),  # Caso básico: 2 * 3 = 6
        (0, 5, 0),  # Caso con cero: 0 * 5 = 0
        (-2, 4, -8),  # Caso con negativo: -2 * 4 = -8
        (-3, -3, 9),  # Caso con dos negativos: -3 * -3 = 9
        (10, 0, 0),  # Caso con cero: 10 * 0 = 0
        (100, 100, 10000)  # Caso con números grandes
    ]

    for i, (a, b, previsto) in enumerate(test_cases):
        try:
            result = producto(a, b)
            status = "✅" if result == previsto else "❌"
            print(f"{status} Test {i + 1}: producto({a}, {b}) => {result} (previsto: {previsto})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i + 1}: producto({a}, {b}) => Error: {str(e)} (previsto: {previsto})")


if __name__ == "__main__":
    main()