from datetime import datetime, timedelta # Import necessary classes from the datetime module

def display_current_datetime():
    """
    Obtains the current date and time and prints it in a specified format.
    """
    current_date = datetime.now() # Get the current date and time
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_current_date}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date based on
    the current date, and prints it in a specified format.
    """
    while True:
        try:
            days_to_add_str = input("Enter the number of days to add (integer): ")
            days_to_add = int(days_to_add_str) # Convert user input to an integer
            break # Exit loop if conversion is successful
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    current_date_for_calculation = datetime.now() # Get the current date for calculation
    # Calculate the future date by adding a timedelta of specified days
    future_date = current_date_for_calculation + timedelta(days=days_to_add)
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future Date ({days_to_add} days from now): {formatted_future_date}")

def main():
    """
    Main function to run the datetime exploration script.
    """
    print("--- Part 1: Display Current Date and Time ---")
    display_current_datetime() # Call the function to display current datetime

    print("\n--- Part 2: Calculate a Future Date ---")
    calculate_future_date() # Call the function to calculate future date

if __name__ == "__main__":
    main()