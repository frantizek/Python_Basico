def binaria(lista: list[int], buscado: int) -> int:
    """Metodo de busqueda binaria."""
    posicion = -1
    primero = 0
    ultimo = len(lista)
    while primero < ultimo and posicion == -1:
        medio = (primero + ultimo) // 2
        if lista[medio] == buscado:
            posicion = medio
        else:
            if buscado < lista[medio]:
                ultimo = medio -1
            else:
                primero = medio + 1
    return posicion
