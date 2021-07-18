# Nested if/else allows for multiple conditions to be checked if first condition is met
# Example - must be taller than 120cm, and pay $12 if over 18 years old or $7 if under 18

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age <= 18:
        print("Please pay $7.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry you're a short little bitch and can't ride this!")

# elif statements allow checking for more initial "if" conditions before redirecting to the else condition
# Example - multiple price tiers instead of just 18/under 18:

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.00")
    elif age <= 18:
        print("Please pay $7.00")
    elif age <= 22:
        print("Please pay $10.00")
    else:
        print("Please pay $12.00")
else:
    print("Sorry you're a short little bitch and can't ride this!")
