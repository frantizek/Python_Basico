# Write a short program that prints the numbers 1 to 10 using a for loop.

for i in range(1, 11, 1):
    print(f" - {i} (for loop)")


# Then, write an equivalent program that prints the numbers 1 to 10 using a while loop.

my_while_integer = 1
while True:
    print(f" - {my_while_integer} (while loop)")
    if my_while_integer > 9:
        break
    my_while_integer += 1