#!/usr/bin/env python3
"""
global_demo.py

Demonstrates the use of global variables within a function.

Key Concepts:
  - Using global variables to modify state
  - Impact of global variables on code readability
"""

def spam():
    """Set the global variable eggs to 'spam'."""
    global eggs
    eggs = 'spam'

# Initialize eggs as a global variable
eggs = 'global'
spam()
print(eggs)  # Prints 'spam' because spam() changes the global eggs.
