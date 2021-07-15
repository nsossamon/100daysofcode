# Program using math/fstrings that tells us how many days, weeks, months we have left if we live to 90 years
# Example output: You have 12410 days, 1768 weeks and 408 months left.
age = int(input("What is your current age? "))
years_left = 90 - age
days = years_left * 365
weeks = years_left * 52
months = years_left * 12
result = f"You have {days} days, {weeks} weeks and {months} months left."
print(result)

# Instructor answer was exact same, GO ME
