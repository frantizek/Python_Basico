"""
Demonstration of basic Python set methods.

Each helper function demonstrates a set method or operation.
The test suite displays the original set, the function name, description, result, expected value, and the test status.
"""

def set_add(s, value):
    """
    Adds an element to the set. If the element already exists, nothing happens.
    """
    s = set(s)
    s.add(value)
    return s

def set_clear(s):
    """
    Removes all elements from the set, leaving it empty.
    """
    s = set(s)
    s.clear()
    return s

def set_copy(s):
    """
    Returns a shallow copy of the set.
    """
    return set(s).copy()

def set_difference(s, other):
    """
    Returns a set containing elements in the first set but not in the second.
    """
    return set(s).difference(set(other))

def set_difference_update(s, other):
    """
    Removes elements found in another set from this set (in-place).
    """
    s = set(s)
    s.difference_update(set(other))
    return s

def set_discard(s, value):
    """
    Removes an element from the set if present. Does not raise an error if missing.
    """
    s = set(s)
    s.discard(value)
    return s

def set_intersection(s, other):
    """
    Returns a set with elements common to both sets.
    """
    return set(s).intersection(set(other))

def set_intersection_update(s, other):
    """
    Updates the set with elements common to itself and another (in-place).
    """
    s = set(s)
    s.intersection_update(set(other))
    return s

def set_isdisjoint(s, other):
    """
    Returns True if sets have no common elements.
    """
    return set(s).isdisjoint(set(other))

def set_issubset(s, other):
    """
    Returns True if set is a subset of another.
    """
    return set(s).issubset(set(other))

def set_issuperset(s, other):
    """
    Returns True if set is a superset of another.
    """
    return set(s).issuperset(set(other))

def set_pop(s):
    """
    Removes and returns an arbitrary element. The set shrinks by one.
    """
    s = set(s)
    s.pop()
    return s

def set_remove(s, value):
    """
    Removes a specified element; raises KeyError if not present.
    """
    s = set(s)
    s.remove(value)
    return s

def set_symmetric_difference(s, other):
    """
    Returns a set with elements in either set, but not in both.
    """
    return set(s).symmetric_difference(set(other))

def set_symmetric_difference_update(s, other):
    """
    Updates the set with symmetric difference (in-place).
    """
    s = set(s)
    s.symmetric_difference_update(set(other))
    return s

def set_union(s, other):
    """
    Returns a set with elements from both sets (no duplicates).
    """
    return set(s).union(set(other))

def set_update(s, other):
    """
    Updates a set, adding elements from another set.
    """
    s = set(s)
    s.update(set(other))
    return s

def main():
    test_cases = [
        # (function, arguments, expected, description)
        (set_add,               [{1,2,3}, 4],               {1,2,3,4}, "Add 4 to {1,2,3}"),
        (set_clear,             [{1,2,3}],                  set(),     "Clear all elements from {1,2,3}"),
        (set_copy,              [{1,2,3}],                  {1,2,3},   "Copy the set"),
        (set_difference,        [{1,2,3}, {2,3}],           {1},       "Difference between {1,2,3} and {2,3}"),
        (set_difference_update, [{1,2,3}, {2}],             {1,3},     "Difference update: remove {2}"),
        (set_discard,           [{1,2,3}, 2],               {1,3},     "Discard 2 from set"),
        (set_intersection,      [{1,2,3}, {2,3}],           {2, 3},    "Intersection of {1,2,3} and {2,3}"),
        (set_intersection_update,[{1,2,3}, {2,3}],          {2, 3},    "Intersection update with {2,3}"),
        (set_isdisjoint,        [{1,2,3}, {4,5}],           True,      "Is {1,2,3} disjoint with {4,5}?"),
        (set_issubset,          [{1,2}, {1,2,3}],           True,      "Is {1,2} a subset of {1,2,3}?"),
        (set_issuperset,        [{1,2,3}, {2}],             True,      "Is {1,2,3} a superset of {2}?"),
        (set_pop,               [{1,2,3}],                  {2,3},     "Pop one element"),
        (set_remove,            [{1,2,3}, 3],               {1,2},     "Remove 3 from set"),
        (set_symmetric_difference, [{1,2,3}, {2,3,4}],      {1,4},     "Symmetric difference with {2,3,4}"),
        (set_symmetric_difference_update, [{1,2,3}, {2,3,4}], {1,4},   "Symmetric difference update with {2,3,4}"),
        (set_union,             [{1,2,3}, {4,5}],           {1,2,3,4,5}, "Union with {4,5}"),
        (set_update,            [{1,2,3}, {4,5}],           {1,2,3,4,5}, "Update with {4,5}"),
        (set_difference,        [{1,2,3}, {2,4}],           {1,3},    "Difference with {2,4}"),
        (set_intersection,      [{1,2,3}, {2,3}],           {2,3},   "Intersection with {2,3}"),
    ]

    print(f"{'Test':<4} {'Original':<20} {'Function':<35} {'Result':<20} {'Expected':<20} {'Status':<6}")
    print('-'*110)
    for idx, (func, args, expected, desc) in enumerate(test_cases, 1):
        # keep a deep copy of first arg for presentation (if it's a set)
        orig = args[0].copy() if isinstance(args[0], set) else args[0]
        try:
            result = func(*args)
            status = "✅" if (result == expected if isinstance(result, set) else result == expected) else "❌"
            print(f"{idx:<4} {str(orig):<20} {desc:<35} {str(result):<20} {str(expected):<20} {status:<6}")
        except Exception as e:
            print(f"{idx:<4} {str(orig):<20} {desc:<35} {'ERROR':<20} {str(expected):<20} {'❌':<6}")

if __name__ == "__main__":
    main()