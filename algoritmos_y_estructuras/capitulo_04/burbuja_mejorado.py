from icecream import ic 

def burbuja_mejorado(lista: list[int]) -> list[int]:
    """Metodo de ordenamiento burbuja mejorado."""
    ic(lista)
    i = 0
    control = True
    while(i < len(lista)-2) and control:
        control = False
        for j in range(0, len(lista)-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                control = True
                ic(lista)
        i += 1
    return lista

def main():
    print(burbuja_mejorado([11,3,81,7,45]))


if __name__ == '__main__':
    main()
