def complete_string_with_zeros(number_to_process: int) -> str:
    if 0 < len(str(number_to_process)) < 4:
        zeros_needed = 4 - len(str(number_to_process))
        return "0" * zeros_needed + str(number_to_process)
    return str(number_to_process)


def generate_entries_from_string(string_to_process: str):
    new_empty_list = []
    for digit in string_to_process:
        new_empty_list.append(digit)
    min_from_number = int("".join(sorted(new_empty_list)))
    max_from_number = int("".join(sorted(new_empty_list, reverse=True)))

    return max_from_number - min_from_number


def steps_to_kaprekars_constant(number: int) -> int:
    if number < 0 or number> 10000:
        return -1
    else:
        number_as_string = complete_string_with_zeros(number)

        if len(set(number_as_string)) == 1:
            # All the elements in the number are the same
            # Constant does not work here
            # or in case we are returning the steps needed to get to the constant
            # we return zero
            return 0
        else:
            for steps in range(1, 8):
                difference_between_max_min = generate_entries_from_string(number_as_string)
                if difference_between_max_min == 6174:
                    return steps
                else:
                    number_as_string = complete_string_with_zeros(difference_between_max_min)
                    continue
