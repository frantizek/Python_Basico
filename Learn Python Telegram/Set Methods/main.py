"""
Demostración de métodos básicos en conjuntos (set) de Python.

Cada función implementa una operación común de conjuntos.
Se muestran el conjunto original, el resultado, el resultado esperado
y si la prueba pasa o falla.
"""

def set_add(s, value):
    """
    Añade un elemento al conjunto.
    Si el elemento ya está, no se añade otra vez.
    """
    s = set(s)
    s.add(value)
    return s

def set_discard(s, value):
    """
    Elimina un elemento del conjunto si existe.
    Si el elemento NO está, no lanza error.
    """
    s = set(s)
    s.discard(value)
    return s

def set_remove(s, value):
    """
    Elimina un elemento del conjunto si existe.
    Si el elemento NO está, lanza un KeyError.
    """
    s = set(s)
    s.remove(value)
    return s

def set_pop(s):
    """
    Elimina y retorna un elemento arbitrario del conjunto.
    (El elemento eliminado es aleatorio)
    """
    s = set(s)
    s.pop()
    return s

def set_intersection(s, other):
    """
    Retorna un nuevo conjunto con los elementos comunes a ambos conjuntos.
    """
    return set(s).intersection(set(other))

def set_difference(s, other):
    """
    Retorna un conjunto con los elementos del 1er conjunto que NO están en el segundo.
    """
    return set(s).difference(set(other))

def set_issubset(s, other):
    """
    Retorna True si el primer conjunto es subconjunto del segundo.
    """
    return set(s).issubset(set(other))

def set_issuperset(s, other):
    """
    Retorna True si el primer conjunto es superconjunto del segundo.
    """
    return set(s).issuperset(set(other))

def set_isdisjoint(s, other):
    """
    Retorna True si ambos conjuntos NO tienen elementos en común.
    """
    return set(s).isdisjoint(set(other))

def set_union(s, other):
    """
    Retorna un nuevo conjunto con los elementos de ambos conjuntos (sin repetidos).
    """
    return set(s).union(set(other))

def set_update(s, other):
    """
    Añade todos los elementos del segundo conjunto al primero (modifica el primero).
    Retorna el conjunto resultante.
    """
    s = set(s)
    s.update(set(other))
    return s

def main():
    test_cases = [
        # (func, input_args, resultado_esperado, descripcion)
        (set_add, [{5, 'Hello', 3.2}, 2], {2, 'Hello', 3.2, 5}, "Añadir 2"),
        (set_discard, [{5, 'Hello', 3.2}, 3.2], {'Hello', 5}, "Descartar 3.2"),
        (set_remove, [{5, 'Hello', 3.2}, 3.2], {'Hello', 5}, "Remover 3.2"),
        (set_pop, [{5, 'Hello', 3.2}], {3.2, 5}, "Pop (quita un elemento)"),
        (set_intersection, [{5, 2, 8}, {5, 1}], {5}, "Intersección"),
        (set_difference, [{5, 2, 8}, {5, 1}], {8, 2}, "Diferencia"),
        (set_issubset, [{1, -2}, {-2, 1, 3}], True, "Es subconjunto"),
        (set_issuperset, [{-2, 1, 3}, {1, -2}], True, "Es superconjunto"),
        (set_isdisjoint, [{-2, 1, 3}, {4, 6}], True, "Es disjunto"),
        (set_union, [{1, 2, 3}, {3, 1}], {1, 2, 3}, "Unión"),
        (set_update, [{1, 2, 3}, {'a', 'b'}], {1, 2, 3, 'b', 'a'}, "Update con {'a', 'b'}"),
    ]

    print(f"{'Test':<5} {'Función':<20} {'Descripción':<25} {'Original':<25} {'Resultado':<25} {'Esperado':<25} {'Estado':<7}")
    print('-' * 140)
    for i, (func, args, esperado, desc) in enumerate(test_cases):
        # Copia profunda del argumento original para mostrarlo en la tabla
        original = [a.copy() if isinstance(a, set) else a for a in args]
        try:
            resultado = func(*args)
            if isinstance(resultado, set) and isinstance(esperado, set):
                estado = "✅" if resultado == esperado else "❌"
            else:
                estado = "✅" if resultado == esperado else "❌"
            # Representamos sólo el principal argumento de entrada para el original
            str_original = f"{original[0]}"
            print(f"{i+1:<5} {func.__name__:<20} {desc:<25} {str_original:<25} {str(resultado):<25} {str(esperado):<25} {estado:<7}")
        except Exception as e:
            str_original = f"{original[0]}"
            print(f"{i+1:<5} {func.__name__:<20} {desc:<25} {str_original:<25} {'ERROR':<25} {str(esperado):<25} {'❌':<7}")

if __name__ == "__main__":
    main()