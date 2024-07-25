def centinela(lista: list[int], buscado: int) -> int:
    """Metodo de busqueda secuencial con centinela."""
    posicion = -1
    indice = 0
    while indice < len(lista) and posicion == -1:
        if lista[indice] == buscado:
            posicion = indice
        indice += 1
    return posicion
