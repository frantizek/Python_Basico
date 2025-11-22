#!/usr/bin/env python3
"""
loot_converter.py

Practice Program: List-to-Dictionary Loot Conversion

In your fantasy game, a vanquished dragon’s loot is given as a list of strings,
e.g., ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'].

Write a function add_to_inventory(inventory, added_items) that:
- Takes an inventory dict (like in the previous program)
- Takes a list of loot items
- Returns an updated inventory dict with the new items added

Then use your display_inventory() function (from the previous exercise) to
show the result.

Expected output after adding dragon_loot:
    Inventory:
    45 gold coin
    1 rope
    1 ruby
    1 dagger

    Total number of items: 48

Author: Practice Program from Chapter 7 — Automate the Boring Stuff with Python
"""


def add_to_inventory(inventory, added_items):
    """
    Adds items from a list to the player's inventory dictionary.

    Parameters:
        inventory (dict): Current inventory (item name → count)
        added_items (list): List of item names (strings) to add

    Returns:
        dict: Updated inventory with new items included
    """
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


# You'll need to copy your working display_inventory() function here
# or import it if you've structured your project accordingly.
def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    print(f"Total number of items: {item_total}")


# Test as described in the textbook
if __name__ == "__main__":
    inv = {'gold coin': 42, 'rope': 1}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)