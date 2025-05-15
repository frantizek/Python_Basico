from multiprocessing.reduction import duplicate

q = { 'NAME': 'JOHN', 'AGE': 43 }

# .get()
# Get the value of the specified key, if nothing present, return None

print("☐"*80)
print(q.get('NAME')) # Expected output = JOHN
print(q.get('AGE')) # Expected output = 43
print(q.get('STATE')) # Expected output = None

# .keys()
# Returns the list of dictionary keys

print("☐"*80)
print(q.keys()) # Expected output = dict_keys(['NAME', 'AGE'])

# .values()
# Returns the list of all dictionary values

print("☐"*80)
print(q.values()) # Expected output = dict_values(['JOHN', 43])

# .update()
# Updates the dictionary with specified key values

print("☐"*80)
q.update({ 'STATE': 'CA' })
print(q) # Expected output = {'NAME': 'JOHN', 'AGE': 43, 'STATE': 'CA'}

# .items()
# Converts the key value as a tuple and returns in an iterable (list)

print("☐"*80)
print(q.items()) # Expected output = dict_items([('NAME', 'JOHN'), ('AGE', 43), ('STATE', 'CA')])

# .copy()
# Duplicates specified dictionary

print("☐"*80)
new_q = {}
print(f"This is q {q} and this is new_q {new_q}.")
new_q = q.copy()
print(f"After q.copy - This is q {q} and this is new_q {new_q}.")

# .pop()
# Removes the value and key, whose keys are passed in the arguments

print("☐"*80)
print(f"This is q {q} BEFORE q.pop('STATE')")
q.pop('STATE')
print(f"This is q {q}  AFTER q.pop('STATE')")

# .popitem()
# Removes the last inserted key value pair

print("☐"*80)
print(f"This is q {q} BEFORE q.popitem()")
q.popitem()
print(f"This is q {q}  AFTER q.popitem()")

# .clear()
# Removes all the items from the dictionary

print("☐"*80)
print(f"This is q {q} BEFORE q.clear()")
q.clear()
print(f"This is q {q}  AFTER q.clear()")

# .setdefault()
# Returns the value of the key specified. If the key is not present, then adds the key (1st argument) and
# the value (2nd argument) provided through this method.

print("☐"*80)
print(f"This is q {q} BEFORE q.setdefault()")
q.setdefault('PIN', 58796)
print(f"This is q {q}  AFTER q.setdefault()")

# .fromkeys()
# Creates a new dictionary with specified keys and a default value.

print("☐"*80)
q.clear()
print(f"This is q {q} BEFORE q.fromkeys()")
q = dict.fromkeys(['NAME', 'AGE'], None)
print(f"This is q {q}  AFTER q.fromkeys()")