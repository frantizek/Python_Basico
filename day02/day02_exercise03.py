# Create a list of fruits and access elements using indexing.


def main() -> None:
    fruits_from_the_world = [
        "Apple",
        "Banana",
        "Orange",
        "Grape",
        "Mango",
        "Pineapple",
        "Watermelon",
        "Strawberry",
        "Avocado",
        "Kiwi",
        "Lemon",
        "Peach",
        "Pear",
        "Melon",
        "Grapefruit",
        "Papaya",
        "Cherry",
        "Plum",
        "Apricot",
        "Coconut",
        "Lychee",
        "Rambutan",
        "Dragonfruit",
        "Passionfruit",
        "Starfruit",
        "Mango",
        "Guava",
        "Persimmon",
        "Pomegranate",
        "Date",
        "Fig",
        "Olive",
    ]

    print("-" * 60)
    # first item
    print(fruits_from_the_world[0])
    print("-" * 60)
    # last item
    print(fruits_from_the_world[len(fruits_from_the_world) - 1])
    print("-" * 60)
    for num in range(3, 18, 2):
        print(fruits_from_the_world[num])
    print("-" * 60)
    for index, fruit in enumerate(fruits_from_the_world):
        print(f"Index: {index}, Fruit: {fruit}")


if __name__ == '__main__':
    main()
