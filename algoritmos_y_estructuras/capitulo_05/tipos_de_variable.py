# variables estaticas

num1 = 1
num2 = num1
num2 = num2 + 3
print(f"valor num1 {num1} valor num2 {num2}")

# variables dinamicas

lista1 = [1, 2, 3]
lista2 = lista1
lista2[1] = 7
lista2.append(87)
print(f"valor lista1 {lista1} valor lista2 {lista2}")

puntero1 = [0,1]
puntero2 = [0,1]

if puntero1 == puntero2:
    print("Apuntan a la misma variable dinamica")
else:
    print("Apuntan a diferentes variables dinamicas")

puntero2 = {}
puntero1 = puntero2

if puntero1 == puntero2:
    print("Apuntan a la misma variable dinamica")
else:
    print("Apuntan a diferentes variables dinamicas")