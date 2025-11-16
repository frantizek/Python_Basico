#!/usr/bin/env python3
"""
potluck_inventory.py

Tracks and totals items brought by guests to a potluck party using nested dictionaries.

Demonstrates Chapter 7 concepts:
- Nested dictionaries (dictionaries inside dictionaries)
- Iterating over dictionary items with .items()
- Using .get(key, default) to safely access dictionary values
- Writing reusable functions
- Converting numbers to strings for clean output

Inspired by the "Total Brought" example in Chapter 7 of
"Automate the Boring Stuff with Python" (3rd Edition).
"""

# Dictionary of guests and what they brought (nested dictionary)
all_guests = {
    'Alice': {'apples': 5, 'pretzels': 12},
    'Bob': {'ham sandwiches': 3, 'apples': 2},
    'Carol': {'cups': 3, 'apple pies': 1}
}


def total_brought(guests, item):
    """
    Calculates the total number of a specific item brought by all guests.

    Parameters:
        guests (dict): A dictionary where each key is a guest name,
                       and each value is another dictionary of items and counts.
        item (str): The name of the item to total (e.g., 'apples').

    Returns:
        int: Total count of the item across all guests.
             Returns 0 if the item was not brought by anyone.
    """
    num_brought = 0
    for guest_name, items in guests.items():
        # Use .get() to avoid KeyError if guest didn't bring this item
        num_brought += items.get(item, 0)
    return num_brought


def main():
    """Prints a neatly formatted summary of all items brought to the potluck."""
    print('Number of things being brought:')

    # List of items we want to report (in display order)
    items_to_report = [
        ('Apples', 'apples'),
        ('Cups', 'cups'),
        ('Cakes', 'cakes'),
        ('Ham Sandwiches', 'ham sandwiches'),
        ('Apple Pies', 'apple pies')
    ]

    # Print each item with aligned formatting
    for display_name, lookup_key in items_to_report:
        count = total_brought(all_guests, lookup_key)
        # Format with consistent spacing (like original, but cleaner)
        print(f' - {display_name:<16} {count}')


if __name__ == '__main__':
    main()