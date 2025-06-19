def es_primo(numero: int) -> bool:
    """Determina si un número entero positivo es primo o no."""
    if numero <= 1:
        return False
    else:
        cont = 0
        for i in range(2, numero+1):
            if (numero % 1 == 0):
                cont += 1
                if(cont == 1):
                    return True
                else:
                    return False
