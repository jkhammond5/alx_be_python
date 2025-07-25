# match_case_calculator.py

# Prompt the user for the first and second numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt the user for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Use match-case to handle the operations
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation selected.")
