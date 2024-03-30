# Implement a program that finds the largest number in a list.

def find_the_largest_number_in_list(list_to_analize: list[int]) -> int:
    if len(list_to_analize) == 0:
        return None
    else:
        return max(list_to_analize)


def main() -> None:
    print(find_the_largest_number_in_list([1, 3, 5]))
    print(find_the_largest_number_in_list([7, 2, 1]))
    print(find_the_largest_number_in_list([9]))
    print(find_the_largest_number_in_list([-2, -5, -1]))
    print(find_the_largest_number_in_list([10, 10, 10]))
    print(find_the_largest_number_in_list([]))
    print(find_the_largest_number_in_list([1]))
    #print(find_the_largest_number_in_list([1, None, 3]))
    #print(find_the_largest_number_in_list([1 + 2j, 3, 5]))
    #print(find_the_largest_number_in_list([1.5, 2.2, 3.1]))
    #print(find_the_largest_number_in_list([True, False, 10]))
    #print(find_the_largest_number_in_list("hello"))
    print(find_the_largest_number_in_list([-1, -3, -5]))
    print(find_the_largest_number_in_list([-7, -2, 1]))
    print(find_the_largest_number_in_list([-9]))
    print(find_the_largest_number_in_list([0, -2, -1]))
    print(find_the_largest_number_in_list([-10, -10, -10]))
    print(find_the_largest_number_in_list([1000, 3000, 5000]))
    print(find_the_largest_number_in_list([7000, 2000, 1000]))
    print(find_the_largest_number_in_list([9000]))
    print(find_the_largest_number_in_list([-2000, -5000, -1000]))
    print(find_the_largest_number_in_list([10000, 10000, 10000]))
    #print(find_the_largest_number_in_list([1, None, 3]))
    print(find_the_largest_number_in_list([]))
    print(find_the_largest_number_in_list([1]))
    #print(find_the_largest_number_in_list("hello world"))


if __name__ == '__main__':
    main()
