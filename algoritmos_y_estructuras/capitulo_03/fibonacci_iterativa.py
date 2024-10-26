def fibonacci(numero: int) -> int:
    """Cálculo el valor de un nunero en la sucesión de Fibonacci."""
    fib1 = 0
    fib2 = 1
    if(numero == 0):
        return fib1
    elif(numero == 1):
        return fib2
    else:
        resultado = 0
        for i in range(2, numero+1):
            resultado = fib1 + fib2
            fib1 = fib2
            fib2 = resultado
        return resultado
