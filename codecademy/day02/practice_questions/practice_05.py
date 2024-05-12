# Given a list of names, concatenate them into a single string separated by spaces.

def concatenate_into_single_string(list_of_names: list[str]) -> str:
    if len(list_of_names) < 1:
        return ""
    else:
        return ' '.join(list_of_names)


def main():
    print(concatenate_into_single_string(["Wenceslao", "Natasha"]))
    print(concatenate_into_single_string(["Kakaroto", "Roberto"]))
    print(concatenate_into_single_string([" ", " ", ""]))


if __name__ == '__main__':
    main()
