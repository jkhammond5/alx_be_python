# temp_conversion_tool.py

# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Implement Conversion Functions
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    temp_input = input(float("Enter the temperature to convert (Celsius/Fahrenheit): ")



    if temp_input == "F":
        converted = convert_to_celsius(fahrenheit)
        print(converted)
    elif unit == "C":
        converted = convert_to_fahrenheit(celsius)
        print(converted)
    else:
        print("Invalid temperature. Please enter a numeric value")

if __name__ == "__main__":
    main()
