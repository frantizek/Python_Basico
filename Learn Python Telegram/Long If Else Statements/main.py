"""
You can use dictionary in place of long if-else statement to make your code clean.

Although you can use match-case statemensts as well.
"""

"""
Food Price Lookup Demo

This module demonstrates three different ways to get the price of a food item:

1. Using an if-elif-else block (`getPrice_if_else`)
2. Using a dictionary for lookup (`getPrice_dictionary`)
3. Using a match-case statement (Python 3.10+) (`getPrice_match_case`)

All approaches return the price associated with the item, or 0 if the item is not found.
"""


def getPrice_if_else(food_item: str) -> int:
    """
    Return the price of a food item using if-elif-else statements.

    Args:
        food_item (str): The name of the food item.

    Returns:
        int: The price of the item, or 0 if not recognized.

    Examples:
        >>> getPrice_if_else("Burger")
        100
        >>> getPrice_if_else("Sandwich")
        0
    """
    if food_item == "Burger":
        return 100
    elif food_item == "Pizza":
        return 200
    elif food_item == "Juice":
        return 50
    elif food_item == "Tofu":
        return 150
    else:
        return 0
    
def getPrice_dictionary(food_item: str) -> int:
    """
    Return the price of a food item using a dictionary for lookup.

    Args:
        food_item (str): The name of the food item.

    Returns:
        int: The price of the item, or 0 if not recognized.

    Examples:
        >>> getPrice_dictionary("Pizza")
        200
        >>> getPrice_dictionary("Water")
        0
    """
    food_items_dict = {
        "Burger": 100,
        "Pizza": 200,
        "Juice": 50,
        "Tofu": 150
    }
    return food_items_dict.get(food_item, 0)

    
def getPrice_match_case(food_item: str) -> int:
    """
    Return the price of a food item using a match-case statement.

    Args:
        food_item (str): The name of the food item.

    Returns:
        int: The price of the item, or 0 if not recognized.

    Examples:
        >>> getPrice_match_case("Tofu")
        150
        >>> getPrice_match_case("Milk")
        0
    """
    match food_item:
        case "Burger":
            return 100
        case "Pizza":
            return 200
        case "Juice":
            return 50
        case "Tofu":
            return 150
        case _:
            return 0


def main():
    """
    Simple command-line interface to get price of a food item using three methods.
    """
    food_item = input("Enter Food Item Name : ")
    print(f"Item: {food_item} = ${getPrice_if_else(food_item)}")
    print(f"Item: {food_item} = ${getPrice_dictionary(food_item)}")
    print(f"Item: {food_item} = ${getPrice_match_case(food_item)}")


if __name__ == "__main__":
    main()
