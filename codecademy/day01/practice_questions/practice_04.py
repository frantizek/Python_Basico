# Given a list of numbers, fin the maximum and minimum values.


def return_max_and_min_from_list(input_list: list[int]) -> tuple:
    if len(input_list) == 0:
        return None, None
    return max(input_list), min(input_list)


def main() -> None:

    print(return_max_and_min_from_list([]))
    print(return_max_and_min_from_list([1, 2, 3.66, 43, 5]))
    print(return_max_and_min_from_list([0, -1, -9, 0, 8, 8]))
    print(return_max_and_min_from_list([9, 9, 9, 9, 9]))


if __name__ == '__main__':
    main()
