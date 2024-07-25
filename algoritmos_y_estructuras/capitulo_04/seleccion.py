def seleccion(lista: list[int]) -> list[int]:
    """Metodo de ordenamiento seleccion."""
    for i in range(0, len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if(lista[j] < lista[minimo]):
                minimo = j
        lista[i], lista[minimo] = lista[minimo], lista[i]
    return lista


def main():
    print(seleccion([11,3,81,7,45]))


if __name__ == '__main__':
    main()
