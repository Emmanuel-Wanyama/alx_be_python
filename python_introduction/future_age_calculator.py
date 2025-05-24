# Prompt the user for their current age and convert the input to an integer
current_age_str = input("How old are you? ")
current_age = int(current_age_str) # Convert the string input to an integer

# Calculate the age in 2050
# Assuming current year is 2023, the difference to 2050 is 2050 - 2023 = 27 years
future_age = current_age + 27

# Print the user's age in 2050
print(f"In 2050, you will be {future_age} years old.")