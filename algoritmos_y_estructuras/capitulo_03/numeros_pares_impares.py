def numeros_pares_impares(numero):
    """Muestra los numeros pares e impares."""
    cont_imp = 0
    for i in range(1, numero+1):
        if i%2 == 0:
            print(f"{numero} es par.")
        else:
            print(f"{numero} es impar.")
            cont_imp += 1
    print(f"Cantidad de numeros impares: {cont_imp}.")
