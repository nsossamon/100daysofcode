#
# Round will round a float into a whole number:
print(round(8 / 3))

# A comma followed by a digit will round to that # of decimals:
print(round(8 / 3, 2))

# Double division (//) will automatically turn the quotient into an integer rather than a floating point:
print(8 // 3)

# Using an operator with an equal sign on a variable will perform the action on itself, e.g.:
score = 0
score += 1
print(score)

# instead of:
score = 0
score = score + 1
print(score)

# F Strings - type f in front of a string and use curly brackets to automatically convert all variables into a string
score = 0
height = 1.8
isWinning = True

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


