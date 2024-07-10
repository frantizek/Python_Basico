def quicksort(lista: list[int], primero: int, ultimo: int) -> list[int]:
    """Metodo de ordenamiento quicksort."""
    izquierda = primero
    derecha = ultimo-1
    pivote = ultimo
    while (izquierda<derecha):
        while (lista[izquierda] < lista[pivote]) and (izquierda <= derecha):
            izquierda+=1
        while (lista[derecha] > lista[pivote]) and (derecha >= izquierda):
            derecha-=1
        if(izquierda<derecha):
            lista[izquierda], lista[derecha] = lista[derecha], lista[izquierda]
    if(lista[pivote]<lista[izquierda]):
        lista[izquierda], lista[pivote] = lista[pivote], lista[izquierda]
    if(primero<izquierda):
        quicksort(lista, primero, izquierda-1)
    if(ultimo> izquierda):
        quicksort(lista, izquierda+1, ultimo)
    return lista
