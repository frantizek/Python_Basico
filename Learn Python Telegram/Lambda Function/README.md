# 🔰 Python Lambda Function: Quick Guide.

Lambda function is very powerful feature in python and it comes very handy when you are working with filter, map and reduce.

In this post I shared some examples of lambda function for your better understanding.

## Introduction

A lambda function is an anonymous function or a function having no name.

Just like a normal function, a lambda function can have multiple arguments but only one expression.

If you have a single expression to be executed, then the lambda function is hangy if compared to the traditional function using the `def` keyword.



## Syntax

`lamda argument(s) : expression`

There cam be a number of arguments but only one expression.

The lambda function comes in very handy when working with the map, filter and reduce functions in Python.



## Examples

Comparison between lambda function an regular function.

```python

# regular function
def multiply_by_2(x):
    return x*2

# lambda function
result = lambda x: x*2

print(multiply_by_2(5)) # 10 
print(result(5))        # 10 
```

Python program to find a+b whole square using lambda.

```python

square = lambda a, b : a**2 + b**2 + 2*(a+b)
print(square(2,5))
# Output : 45
```


## Lambda with filter, map, reduce

```python

input_list = [2, 3, 4, 5, 6, 7] 

# using map function to square each list item 
map_answer = map(lambda x : x*x, input_list) 
print(list(map_answer)) 
# Output : [4, 9, 16, 25, 36, 49] 
 
# using filter function to filter list item with value < 5 
filter_answer = filter(lambda x : x<5, input_list) 
print(list(filter_answer)) 
# Output : [2, 3, 4]

# using reduce function to sum all the list item 
from functools import reduce 
reduce_answer = reduce(lambda x, y : x+y, input_list) 
print ( reduce_answer ) 
# Output : 27
```