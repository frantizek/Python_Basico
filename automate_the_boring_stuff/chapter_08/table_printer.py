#!/usr/bin/env python3
"""
table_printer_template.py
A template for the `printTable()` function, which prints a list of lists as a right-justified table.
"""

def printTable(tableData: list[list[str]]) -> None:
    """
    Prints a list of lists of strings as a right-justified table.

    Args:
        tableData: A list of lists of strings, where each inner list represents a column.
    """
    # Step 1: Initialize a list to store the maximum width of each column.
    colWidths = [0] * len(tableData)  # Example: [0, 0, 0] for 3 columns

    # Step 2: Calculate the maximum width for each column.
    # Iterate over each column (inner list) in tableData.
    for col in range(len(tableData)):
        for element in tableData[col]:
            colWidths[col] = max(colWidths[col], len(element))



    # Step 3: Print the table row by row.
    # Iterate over the rows (assuming all columns have the same number of rows).
    for row in range(len(tableData[0])):
        new_format = []
        for col in range(len(tableData)):
            new_format.append(tableData[col][row].rjust(colWidths[col], ' '))
        print(" ".join(new_format), end="\n")

def main():
    """Demonstrates the printTable() function with sample data."""
    tableData = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
    ]
    printTable(tableData)

if __name__ == "__main__":
    main()
