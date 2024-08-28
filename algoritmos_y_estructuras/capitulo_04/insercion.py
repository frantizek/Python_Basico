def insercion(lista: list[int]) -> list[int]:
    """Metodo de ordenamiento seleccion."""
    for i in range(1, len(lista)+1):
        k = i-1
        while (k>0) and (lista[k] < lista[k-1]):
            lista[k], lista[k-1] = lista[k-1], lista[k]
            k -= 1
    return lista


def main():
    print(insercion([11,3,81,7,45]))


if __name__ == '__main__':
    main()
