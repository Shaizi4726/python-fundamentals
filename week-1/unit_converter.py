def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371
    return miles


def kilograms_to_pounds(kilograms):
    pounds = kilograms * 2.20462
    return pounds


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def input_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def input_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return None


def main():
    print("Hello Shahzad! Welcome to the Unit Converter.")

    print("What would you like to convert?")
    print("1. Kilometers to Miles")
    print("2. Kilograms to Pounds")
    print("3. Celsius to Fahrenheit")

    choice = input_int("Enter the number corresponding to your choice: ")

    if choice == 1:
        kilometers = input_float("Enter the distance in kilometers: ")
        if kilometers is None:
            return
        miles = kilometers_to_miles(kilometers)
        print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")

    elif choice == 2:
        kilograms = input_float("Enter the weight in kilograms: ")
        if kilograms is None:
            return
        pounds = kilograms_to_pounds(kilograms)
        print(f"{kilograms} kilograms is equal to {pounds:.2f} pounds.")

    elif choice == 3:
        celsius = input_float("Enter the temperature in Celsius: ")
        if celsius is None:
            return
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(
            f"{celsius} degrees Celsius is equal to {fahrenheit:.2f} degrees Fahrenheit.")

    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
