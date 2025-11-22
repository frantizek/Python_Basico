#!/usr/bin/env python3
"""
fantasy_inventory.py

Practice Program: Fantasy Game Inventory

You are creating a medieval fantasy video game. The player’s inventory is
represented as a dictionary where keys are item names (strings) and values
are counts (integers).

Write a function named display_inventory(inventory) that prints:
    Inventory:
    <count> <item name>
    ...
    Total number of items: <total>

Example input: {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

Author: Practice Program from Chapter 7 — Automate the Boring Stuff with Python
"""


def display_inventory(inventory):
    """
    Prints a formatted listing of the player's inventory and total item count.

    Parameters:
        inventory (dict): Dictionary mapping item names (str) to counts (int).
    """
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")



# Test data as provided in the textbook
if __name__ == "__main__":
    stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    display_inventory(stuff)