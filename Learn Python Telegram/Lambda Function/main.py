"""
Lambda function is very powerful feature in python and it comes very handy when you are working with filter, map and reduce.

A lambda function is an anonymous function or a function having no name.

Just like a normal function, a lambda function can have multiple arguments but only one expression.

If you have a single expression to be executed, then the lambda function is handy if compared to the traditional function using the `def` keyword.

Syntax:

`lambda argument(s) : expression`

There can be a number of arguments but only one expression.

The lambda function comes in very handy when working with the map, filter and reduce functions in Python.
"""

# =============================================================================
# Example 1: Lambda vs Regular Function
# =============================================================================

# Regular function
def multiply_by_2(x):
    return x*2

# Lambda function
result = lambda x: x*2

print("Example 1: Lambda vs Regular Function")
print(f"  Regular function multiply_by_2(5) = {multiply_by_2(5)}")
print(f"  Lambda function result(5)         = {result(5)}")
print()

# =============================================================================
# Example 2: Lambda for (a+b)²
# =============================================================================

square = lambda a, b: a**2 + b**2 + 2*(a+b)

print("Example 2: (a+b)² using Lambda")
print(f"  square(2, 5) = {square(2, 5)}")
print(f"  Explanation: 2² + 5² + 2*(2+5) = 4 + 25 + 14 = 43")
print()

# =============================================================================
# Example 3: Lambda with filter, map, reduce
# =============================================================================

input_list = [2, 3, 4, 5, 6, 7]

# Using map function to square each list item
map_answer = map(lambda x: x*x, input_list)

print("Example 3a: Map with Lambda")
print(f"  Original list: {input_list}")
print(f"  Squared list:  {list(map_answer)}")
print()

# Using filter function to filter list item with value < 5
filter_answer = filter(lambda x: x < 5, input_list)

print("Example 3b: Filter with Lambda")
print(f"  Original list: {input_list}")
print(f"  Filtered (< 5): {list(filter_answer)}")
print()

# Using reduce function to sum all the list item
from functools import reduce

reduce_answer = reduce(lambda x, y: x + y, input_list)

print("Example 3c: Reduce with Lambda")
print(f"  Original list: {input_list}")
print(f"  Sum of all:    {reduce_answer}")
print()
