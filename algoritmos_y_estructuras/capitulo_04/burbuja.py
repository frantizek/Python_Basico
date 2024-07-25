from icecream import ic 

def burbuja(lista):
    """Metodo de ordenamiento burbuja."""
    ic(lista)
    for i in range(0, len(lista)-1):
        for j in range(0, len(lista)-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                ic(lista)
    return lista

def main():
    print(burbuja([11,3,81,7,45]))


if __name__ == '__main__':
    main()
