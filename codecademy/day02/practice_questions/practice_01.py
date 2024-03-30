# Given a list of numbers, find the sum and average.

def sum_and_average_from_a_list(input_list: list):
    if len(input_list) <= 0:
        return 0, 0
    else:
        return sum(input_list), sum(input_list)/len(input_list)


def main() -> None:
    print(sum_and_average_from_a_list([]))
    print(sum_and_average_from_a_list([0, 0, 0, 0, 0, -1]))
    print(sum_and_average_from_a_list([-6, -0, -99, 2]))
    print(sum_and_average_from_a_list([2, 4, 5, 6, 0, -8]))


if __name__ == '__main__':
    main()
