Prompt User for a Number:

try:
    number_str = input("Enter a number to see its multiplication table: ")
    number = float(number_str) # Use float to allow for decimal numbers too

    print(f"\nMultiplication Table for {number}:\n")

    # Generate and print the multiplication table from 1 to 10
    for i in range(1, 11): # Loop from 1 up to and including 10
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    print("Invalid input. Please enter a valid number.")