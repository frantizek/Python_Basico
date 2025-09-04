#!/usr/bin/env python3
"""
call_stack_demo.py

Demonstrates function calls and order of execution.
Illustrates a simple call stack with nested function calls.

Functions:
- a(): Calls functions b() and d()
- b(): Calls function c()
- c(): Simple function that prints start and return
- d(): Simple function that prints start and return
"""

def a():
    """Function a starts, calls b and d, then returns."""
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    """Function b starts, calls c, then returns."""
    print('b() starts')
    c()
    print('b() returns')

def c():
    """Function c starts and returns immediately."""
    print('c() starts')
    print('c() returns')

def d():
    """Function d starts and returns immediately."""
    print('d() starts')
    print('d() returns')

if __name__ == "__main__":
    a()