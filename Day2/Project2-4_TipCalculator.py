# Tip Calculator - Output format below:
# Welcome to the tip calculator.
# What was the total bill?
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay: $00.00

print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

result = (total_bill / people) * (1 + (percentage / 100))
format_result = "{:.2f}".format(result)                    # {:.2f} will both change to string and format to 2 decimals)
print("Each person should pay: $" + format_result)
