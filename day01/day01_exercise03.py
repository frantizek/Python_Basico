# Convert temperature from Celsius to Fahrenheit.


def main() -> None:
    print("Convert temperature from Celsius to Fahrenheit.")
    print("-" * 70)

    while True:
        celsius_temperature = input("Please provide the temperature in Celsius : ")
        try:
            celsius_temperature = int(celsius_temperature)
            break
        except ValueError:
            try:
                celsius_temperature = float(celsius_temperature)
                break
            except ValueError:
                print("This is not a number. Please enter a valid number")

    print(f"Temperature in Fahrenheit : {(celsius_temperature * (9 / 5)) + 32}")


if __name__ == '__main__':
    main()
