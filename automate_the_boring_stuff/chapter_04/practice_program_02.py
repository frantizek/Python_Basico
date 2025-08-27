"""
Practice Programs
For practice, write programs to do the following tasks.

Input Validation
Add try and except statements to the previous project to detect whether the user entered a non-integer string.
Normally, the int() function will raise a ValueError error if it is passed a non-integer string, as in int('puppy').
In the except clause, print a message to the user saying they must enter an integer.
"""

def collatz(number: int):
    # If number is even, then collatz() should print number // 2 and return this value.
    if number % 2 == 0:
        return number // 2
    # If number is odd, then collatz() should print and return 3 * number + 1.
    if number % 2 == 1:
        return 3 * number + 1

def main():

    input_integer = input("Teclea un numero entero : ")
    results = []
    try:
        result = int(input_integer)
        results.append(result)
        while result != 1:
            result = collatz(result)
            results.append(result)
        print(" ".join(str(c) for c in results))
    except ValueError:
        print(f'Error: {input_integer} no es un numero entero.')



if __name__ == '__main__':
    main()

