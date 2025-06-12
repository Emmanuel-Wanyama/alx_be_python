# Define global conversion factors
# Factor to convert Fahrenheit to Celsius: (F - 32) * (5/9)
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
# Factor to convert Celsius to Fahrenheit: (C * 9/5) + 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using a global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Use the global FAHRENHEIT_TO_CELSIUS_FACTOR for conversion
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using a global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Use the global CELSIUS_TO_FAHRENHEIT_FACTOR for conversion
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays result.
    Handles invalid input.
    """
    print("Temperature Conversion Tool")

    while True:
        try:
            # Prompt for temperature input
            temperature_str = input("Enter the temperature value: ").strip()
            temperature = float(temperature_str) # Convert input to a float
            break # Exit loop if conversion is successful
        except ValueError:
            # Raise an error if input is not a numeric value
            print("Invalid temperature. Please enter a numeric value.")
            continue # Continue loop to ask for input again

    while True:
        # Prompt for the unit (C for Celsius, F for Fahrenheit)
        unit = input("Enter the unit (C for Celsius, F for Fahrenheit): ").strip().upper()
        if unit in ['C', 'F']:
            break # Exit loop if unit is valid
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")

    # Perform the conversion based on the entered unit
    if unit == 'C':
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
    else: # unit == 'F'
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")

if __name__ == "__main__":
    main()