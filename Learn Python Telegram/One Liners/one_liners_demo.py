import math
from collections import Counter

print("=" * 50)
print("10 PYTHON ONE-LINERS WITH EXAMPLES")
print("=" * 50)

# 1. SWAP TWO VARIABLES
print("\n1. SWAP TWO VARIABLES")
a, b = 5, 10
print(f"Before: a = {a}, b = {b}")
a, b = b, a
print(f"After : a = {a}, b = {b}")

# 2. REVERSE A STRING
print("\n2. REVERSE A STRING")
s = "hello"
print(f"Original : {s}")
print(f"Reversed : {s[::-1]}")

# 3. CHECK PALINDROME
print("\n3. CHECK PALINDROME")
pal = "radar"
not_pal = "python"
print(f"'{pal}' is palindrome? {pal == pal[::-1]}")
print(f"'{not_pal}' is palindrome? {not_pal == not_pal[::-1]}")

# 4. GET FACTORIAL
print("\n4. GET FACTORIAL")
n = 5
print(f"Factorial of {n} = {math.prod(range(1, n+1))}")

# 5. FLATTEN A LIST
print("\n5. FLATTEN A LIST")
nested = [[1, 2], [3, 4, 5], [6]]
flat = [i for sub in nested for i in sub]
print(f"Nested list: {nested}")
print(f"Flattened : {flat}")

# 6. FIND EVEN NUMBERS
print("\n6. FIND EVEN NUMBERS (0-9)")
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens: {evens}")

# 7. MERGE TWO DICTS
print("\n7. MERGE TWO DICTIONARIES")
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
merged = {**d1, **d2}
print(f"d1 = {d1}")
print(f"d2 = {d2}")
print(f"Merged = {merged}")

# 8. COUNT ITEMS
print("\n8. COUNT ITEMS IN A LIST")
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
counts = Counter(items)
print(f"List: {items}")
print(f"Counts: {counts}")

# 9. GET UNIQUE ELEMENTS
print("\n9. GET UNIQUE ELEMENTS")
duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique = set(duplicates)
print(f"List with duplicates: {duplicates}")
print(f"Unique elements: {unique}")  # order not guaranteed

# 10. LIST TO STRING
print("\n10. LIST TO STRING (join with comma)")
words = ["Python", "is", "awesome"]
joined = " ".join(words)
print(f"List: {words}")
print(f"Joined string: '{joined}'")

print("\n" + "=" * 50)
print("All done!")