# Prompt user to enter two number one after another
try:
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str) # Convert to float to handle decimal numbers

    num2_str = input("Enter the second number: ")
    num2 = float(num2_str) # Convert to float

    operation = input("Choose the operation (+, -, *, /): ")

    result = None # Initialize result to None

# Perform the calculation using Match Case
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}")
        case '-':
            result = num1 - num2
            print(f"The result is {result}")
        case '*':
            result = num1 * num2
            print(f"The result is {result}")
        case '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result is {result}")
        case _: # Default case for any other input
                print("Invalid operation. Please choose from +, -, *, or /.")

except ValueError:
    print("Invalid input. Please enter valid numbers.")