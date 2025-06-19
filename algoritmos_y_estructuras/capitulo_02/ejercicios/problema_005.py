#
# Desarrollar una función que permita convertir un número romano en un número decimal.

def romano_a_decimal(romano):
    pass


def main():
    # Casos de prueba: (romano, valor previsto)
    test_cases = [
        ("III", 3),  # Caso básico: III = 3
        ("IV", 4),  # Caso con resta: IV = 4
        ("IX", 9),  # Caso con resta: IX = 9
        ("LVIII", 58),  # Caso mixto: LVIII = 58
        ("MCMXCIV", 1994),  # Caso mixto con varios valores: MCMXCIV = 1994
        ("CDXLIV", 444)  # Caso mixto: CDXLIV = 444
    ]

    for i, (romano, previsto) in enumerate(test_cases):
        try:
            result = romano_a_decimal(romano)
            status = "✅" if result == previsto else "❌"
            print(f"{status} Test {i + 1}: romano_a_decimal({romano}) => {result} (previsto: {previsto})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i + 1}: romano_a_decimal({romano}) => Error: {str(e)} (previsto: {previsto})")


if __name__ == "__main__":
    main()

# Casos de borde (Edge Cases):
# - Números romanos con la máxima longitud válida.
# - Entradas vacías o no válidas (por ejemplo, caracteres no romanos).
# - Númros romanos mal formados (por ejemplo, IIV).

# Instrucciones estrictas:
# - La función debe ser eficiente, clara y robusta.
# - Los casos de prueba en el main deben ejecutarse y mostrar la salida en el formato especificado.
# - Documentar cualquier suposición (por ejemplo, cómo se manejan entradas no válidas).
# - La función no debe causar errores inesperados y debe manejar todas las entradas proporcionadas.

# Entrega:
# - Código en Python con la función implementada (debe ser completada por el estudiante).
# - Explicación breve de cómo se manejaron los casos de borde.
# - Resultados de las pruebas ejecutadas con el main, mostrando la salida en el formato especificado.