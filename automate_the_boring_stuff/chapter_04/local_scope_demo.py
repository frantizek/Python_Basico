#!/usr/bin/env python3
"""
local_scope_demo.py

Demonstrates local versus global scope in Python functions.

Key Concepts:
  - Variables defined inside functions have local scope.
  - The global variable remains unchanged by local assignments.
"""

def spam():
    """Defines and prints a local variable eggs."""
    eggs = 'spam local'
    print(eggs)  # Prints 'spam local'

def bacon():
    """Defines local variable eggs, calls spam(), and prints eggs."""
    eggs = 'bacon local'
    print(eggs)  # Prints 'bacon local'
    spam()       # Calls spam() which prints 'spam local'
    print(eggs)  # Prints 'bacon local' again

# Initialize eggs as a global variable
eggs = 'global'
bacon()         # Calls bacon(), executing its local logic
print(eggs)     # Prints 'global', showing global eggs is unchanged
