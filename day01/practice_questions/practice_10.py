# Implement a program that swaps the values of two variables.

def swap_variable_content(var1, var2):
    temp = var1
    var1 = var2
    var2 = temp
    return var1, var2


print("\n\n\n")

first_variable = 9990
second_variable = 1010101

print(f" Variable 1 = {first_variable} - Variable 2 = {second_variable}")

temp = first_variable
first_variable = second_variable
second_variable = temp

print("-"*80)
print("After swap")
print("-"*80)
print(f" Variable 1 = {first_variable} - Variable 2 = {second_variable}")


print("\n\n\n")

f_variable = 8878
s_variable = 23

print(f" Variable 1 = {f_variable} - Variable 2 = {s_variable}")

f_variable, s_variable = swap_variable_content(f_variable, s_variable)

print("-"*80)
print("After swap using the function")
print("-"*80)
print(f" Variable 1 = {f_variable} - Variable 2 = {s_variable}")
