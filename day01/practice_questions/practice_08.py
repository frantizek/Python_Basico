# Given a list of integers, find the sum of all positive numbers.

def sum_all_positive_numbers(input_list: list) -> int:
    the_result = 0
    if len(input_list) <= 0:
        return 0
    else:
        for number in input_list:
            if number >= 0:
                the_result += number
        return the_result


def main() -> None:
    print(sum_all_positive_numbers([]))
    print(sum_all_positive_numbers([0,0,0,0,0,-1]))
    print(sum_all_positive_numbers([-6,-0,-99,2]))
    print(sum_all_positive_numbers([2,4,5,6,0,-8]))


if __name__ == '__main__':
    main()
