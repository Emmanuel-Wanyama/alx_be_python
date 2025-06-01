# Prompt User for Pattern Size
try:
    size_str = input("Enter the size of the pattern: ")
    size = int(size_str)

    # Check if the input is a positive integer
    if size <= 0:
        print("Please enter a positive integer for the pattern size.")
    else:
        # Initialize row counter for the outer while loop
        current_row = 0

        # Outer loop: iterates through each row of the pattern
        while current_row < size:
            # Inner loop: prints asterisks for the current row
            # It will print 'size' number of asterisks side by side
            for _ in range(size):
                print("*", end="") # Print an asterisk without moving to a new line
            
            # After printing all asterisks for the current row, move to the next line
            print() 
            
            # Increment the row counter
            current_row += 1

except ValueError:
    print("Invalid input. Please enter a whole number for the pattern size.")