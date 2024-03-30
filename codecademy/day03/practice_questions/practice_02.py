# Given a list of integers, find all the even numbers and store them in a new list.


def store_even_numbers_from_integer_list(list_with_integers: list[int]) -> list[int]:
    even_numbers_from_integer_list = []
    if len(list_with_integers) == 0:
        return even_numbers_from_integer_list
    else:
        for number in list_with_integers:
            if number % 2 == 0:
                even_numbers_from_integer_list.append(number)
    return even_numbers_from_integer_list


def main() -> None:
    print(store_even_numbers_from_integer_list([]))
    print(store_even_numbers_from_integer_list([2,3,4,5,6]))
    print(store_even_numbers_from_integer_list([9,7,5,3,1]))
    print(store_even_numbers_from_integer_list([1,2,3,4,5,6,7,8,9]))


if __name__ == '__main__':
    main()
