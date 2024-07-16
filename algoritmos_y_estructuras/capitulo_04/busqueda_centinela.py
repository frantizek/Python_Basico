def centinela(lista: list[int], buscado: int) -> int:
    """Metodo de busqueda secuencial con centinela."""
    posicion = -1
    for indice in range(0, len(lista)):
        if lista[indice] == buscado:
            posicion = indice
            break
    return posicion
