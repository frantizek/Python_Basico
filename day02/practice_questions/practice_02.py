# Create a program that takes a temperature in Celsius and
# converts it to Kelvin.

def main() -> None:
    print("Convert temperature from Celsius to Kelvin.")
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

    print(f"Temperature in Kelvin : {celsius_temperature + 273.15}")
    print(f"or {celsius_temperature + 273.15} K")


if __name__ == '__main__':
    main()
