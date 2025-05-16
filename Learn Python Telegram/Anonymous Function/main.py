# Anonymous Function
# In Python an anonymous function is a function that is defined without a name.
# In Python, anonymous functions are defined using the lambda keyword.
# Hence, anonymous functions are also called lambda functions.
# A lambda function can take any number of arguments, but can have only one expression.
# Syntax:
# lambda arguments: expression

#Comparison of normal function and lambda function.
# Normal function
def add(x, y):
    return x+y

print(add(10, 20))

# Lambda function
add_lambda = lambda x, y: x+y
print(add_lambda(10, 20))