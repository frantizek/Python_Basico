# Implementar una función que reciba una cadena de caracteres y
# devuelva la cadena invertida.

def invertir_cadena(cadena):
    """
    Invierte una cadena de caracteres.
    - Si la entrada no es una cadena (string), debe lanzar un TypeError.
    """
    if not isinstance(cadena, str):
        raise TypeError("Entrada no válida")
    if len(cadena) == 0:
        return ""
    else:
        return cadena[-1] + invertir_cadena(cadena[0:len(cadena)-1])


def main():
    """Función principal para probar la implementación de invertir_cadena."""
    test_cases = [
        # Casos básicos
        ("hola", "aloh"),
        ("mundo", "odnum"),
        ("Python", "nohtyP"),
        # Caso con espacios
        ("hello world", "dlrow olleh"),
        # Caso que es un palíndromo
        ("reconocer", "reconocer"),
        # Casos de borde (edge cases)
        ("", ""), # Cadena vacía
        ("a", "a"),   # Cadena de un solo carácter
        (12345, "TypeError"), # Entrada no válida (número)
        (["a", "b"], "TypeError"), # Entrada no válida (lista)
        (None, "TypeError") # Entrada no válida (None)
    ]

    print("--- Probando invertir_cadena ---")
    for i, (entrada, previsto) in enumerate(test_cases):
        try:
            result = invertir_cadena(entrada)
            # Para los casos de error, si el código llega aquí, está mal
            if isinstance(previsto, str) and ("Error" in previsto):
                status = "❌"
                print(f"{status} Test {i+1}: invertir_cadena(\"{entrada}\") => No lanzó excepción (previsto: {previsto})")
            else:
                status = "✅" if result == previsto else "❌"
                print(f"{status} Test {i+1}: invertir_cadena(\"{entrada}\") => \"{result}\" (previsto: \"{previsto}\")")
        except TypeError as e:
            error_type = type(e).__name__
            if error_type == previsto:
                status = "✅"
                print(f"{status} Test {i+1}: invertir_cadena({entrada}) => Lanzó {error_type} correctamente (previsto: {previsto})")
            else:
                status = "❌"
                print(f"{status} Test {i+1}: invertir_cadena({entrada}) => Error: {str(e)} (previsto: {previsto})")
        except Exception as e:
            status = "❌"
            print(f"{status} Test {i+1}: invertir_cadena({entrada}) => Error inesperado: {str(e)} (previsto: {previsto})")

if __name__ == "__main__":
    main()