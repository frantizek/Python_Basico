# 10 Python One‑Liners That Will Blow Your Mind!

A collection of 10 powerful and elegant Python one‑liners, each demonstrated with a practical example in a single runnable script.

---

## Overview

This repository contains a single Python script (`one_liners_demo.py`) that showcases 10 concise Python expressions for common programming tasks.  
From swapping variables to merging dictionaries—these snippets are not only fun to write but also make your code more readable and Pythonic.

Each one‑liner is illustrated with sample inputs and outputs, so you can see exactly how it works.

---

## The 10 One‑Liners

| # | Task | One‑Liner |
|---|------|-----------|
| 1 | Swap two variables | `a, b = b, a` |
| 2 | Reverse a string | `s[::-1]` |
| 3 | Check if a string is a palindrome | `s == s[::-1]` |
| 4 | Compute factorial | `math.prod(range(1, n+1))` |
| 5 | Flatten a nested list | `[i for sub in lst for i in sub]` |
| 6 | Find even numbers in a range | `[x for x in range(10) if x % 2 == 0]` |
| 7 | Merge two dictionaries | `{**d1, **d2}` |
| 8 | Count items in a list | `Counter(lst)` |
| 9 | Get unique elements from a list | `set(lst)` |
| 10 | Join a list of strings into one string | `' '.join(lst)` |

---

## Requirements

- Python 3.8+ (for `math.prod`, but the script works on older versions if you replace it with a loop)
- No external packages—only the standard library (`math` and `collections`).

---

## Usage

1. **Clone or download** this repository.
2. **Run the script**:
   ```bash
   python one_liners_demo.py
   ```
3. **Watch the output** each section prints the input and the result of the one‑liner.

---

## Full Script
Below is the complete script. Copy it into a file named one_liners_demo.py and run it.

```
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
```

---

## Sample Output
When you run the script, you’ll see something like this:

```text
==================================================
10 PYTHON ONE-LINERS WITH EXAMPLES
==================================================

1. SWAP TWO VARIABLES
Before: a = 5, b = 10
After : a = 10, b = 5

2. REVERSE A STRING
Original : hello
Reversed : olleh

... (and so on)
```

---

## Extending the Examples
Feel free to change the sample data inside the script to test your own cases.
Each one‑liner stands alone, so you can also copy any snippet directly into your own projects.

---

## License
This project is open‑source and available under the MIT License.

---

Enjoy the power of Python one‑liners! 🐍