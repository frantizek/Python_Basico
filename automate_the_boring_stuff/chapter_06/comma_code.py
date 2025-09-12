"""
Comma Code

Say you have a list value like this:

spam = ['apples', 'bananas', 'tofu', 'cats']

Write a function that takes a list value as an argument and returns a string
with all the items separated by a comma and a space, with and inserted before the last item.

For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.

But your function should be able to work with any list value passed to it.

Be sure to test the case where an empty list [] is passed to your function.
"""


def comma_code(values: list) -> str:
    if not values:
        return ""
    if len(values) == 1:
        return str(values[0])
    else:
        new_str = str(values[0])
        for index in range(1, len(values) -1):
            new_str += f", {values[index]}"
        # the last element
        new_str += f", and {values[-1]}"
    return new_str



def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
    print(comma_code([]))
    print(comma_code([""]))
    print(comma_code(["Uno", "Dos"]))
    print(comma_code(['apples', 'bananas', 'tofu', 'cats']*12))


if __name__ == "__main__":
    main()