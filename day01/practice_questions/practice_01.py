# Write a python program to calculate the area of a rectangle
# given its length and width.


def main() -> None:
    while True:
        rectangle_length = input("What is the rectangle's length? : ")
        try:
            rectangle_length = int(rectangle_length)
            break
        except ValueError:
            try:
                rectangle_length = float(rectangle_length)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    while True:
        rectangle_width = input("What is the rectangle's width? : ")
        try:
            rectangle_width = int(rectangle_width)
            break
        except ValueError:
            try:
                rectangle_width = float(rectangle_width)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    print("-" * 80)
    print(f"The area of the rectangle is {rectangle_width * rectangle_length}")


if __name__ == '__main__':
    main()
