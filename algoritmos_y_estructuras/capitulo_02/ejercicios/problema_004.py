# Implementar una función para calcular la potencia dado dos números enteros,
# el primero representa la base y el segundo el exponente.

def potencia_sin_recursion(base, exponente):
    return pow(base, exponente)

def potencia(base, exponente):
    """
    Calcula la potencia de dos enteros 'base' y 'exponente' utilizando recursión.
    Este metodo descompone la potencia en una serie de multiplicaciones.
    """
    if not (isinstance(base, int) and isinstance(exponente, int)):
        raise TypeError("Las entradas deben ser enteros")
    # By mathematical law, any number (except zero) raised to the power of 0 is 1.
    # This is a universal truth, a point of perfect balance.
    # It requires no further calculation. It is our perfect base case.
    if exponente == 0:
        return 1
    elif exponente < 0 :
        return 1 / (potencia(base, abs(exponente)))
    else:
        return base * (potencia(base, exponente - 1))

def main():
    # Casos de prueba: (base, exponente, valor previsto)
    test_cases = [
        (2, 3, 8),  # Caso básico: 2^3 = 8
        (5, 0, 1),  # Caso con exponente cero: 5^0 = 1
        (1, 10, 1),  # Caso de base uno: 1^10 = 1
        (0, 5, 0),  # Caso de base cero: 0^5 = 0
        (-2, 3, -8),  # Caso de base negativa y exponente impar
        (-2, 2, 4),  # Caso de base negativa y exponente par
        (10, 2, 100)  # Caso con números grandes
    ]

    for i, (base, exponente, previsto) in enumerate(test_cases):
        try:
            result = potencia(base, exponente)
            status = "✅" if result == previsto else "❌"
            print(f"{status} Test {i + 1}: potencia({base}, {exponente}) => {result} (previsto: {previsto})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i + 1}: potencia({base}, {exponente}) => Error: {str(e)} (previsto: {previsto})")


if __name__ == "__main__":
    main()

# Casos de borde (Edge Cases):
# - Exponente cero que siempre debe devolver uno.
# - Base negativa con exponente par e impar.
# - Base cero.
# - Exponente negativo (si es relevante en contexto de definición de función).
# - Entradas no válidas (como floats o strings).

# Instrucciones estrictas:
# - La función debe ser eficiente, clara y robusta.
# - Los casos de prueba en el main deben ejecutarse y mostrar la salida en el formato especificado.
# - Documentar cualquier suposición (por ejemplo, cómo se manejan entradas no válidas).
# - La función no debe causar errores inesperados y debe manejar todas las entradas proporcionadas.

# Entrega:
# - Código en Python con la función implementada (debe ser completada por el estudiante).
# - Explicación breve de cómo se manejaron los casos de borde.
# - Resultados de las pruebas ejecutadas con el main, mostrando la salida en el formato especificado.