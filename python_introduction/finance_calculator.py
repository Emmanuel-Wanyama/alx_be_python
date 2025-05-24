# Prompt the user for their monthly income 
monthly_income_str = input("Enter Monthly Income: ")
monthly_income = float(monthly_income_str) # Convert the string input to an integer

# Prompt the user for their monthly expenses
monthly_expenses_str = input("Enter Monthly Expense:  ")
monthly_expenses = float(monthly_expenses_str) # Convert the string input to an integer



# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses 

#Calculate Projected Savings
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)


# Print the monthly savings and projected savings
print(f"Your monthly saving is ${monthly_savings}")
print(f"Your projected savings in a year will be ${projected_savings}")