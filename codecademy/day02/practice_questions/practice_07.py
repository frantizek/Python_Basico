# Calculate the area and circumference of a circle given its radius.
#
import math

# Area
# A = π · (r · r)

# Circumference
# L = 2 · π · r


def area_of_a_circle(radius: float) -> float:
    return round(math.pi * pow(radius, 2),2)


def circumference_of_a_circle(radius: float) -> float:
    return round(2 * radius * math.pi,2)


def main() -> None:
    print("Calculate the area and circumference of a circle.")
    print("-" * 60)

    while True:
        circle_s_radius = input("Please provide the circle's radius : ")
        try:
            circle_s_radius = int(circle_s_radius)
            break
        except ValueError:
            try:
                circle_s_radius = float(circle_s_radius)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    print(f"Area:  {area_of_a_circle(circle_s_radius)}, Circunference: {circumference_of_a_circle(circle_s_radius)}")


if __name__ == '__main__':
    main()
