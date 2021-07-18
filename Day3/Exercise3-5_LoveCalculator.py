# lower function changes letters in a string to lowercase:
print("Angela".lower())

# "count" function will give you number of times a letter occurs in a string (case sensitive)
print("Angela".count("a"))

# example to count all letters (non case-sensitive)
lower_case_name = "Angela".lower()
print(lower_case_name.count("a"))

# Program to check compatibility between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the
# number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_lowercase = name1.lower() + name2.lower()
TRUE = combined_lowercase.count("t") + combined_lowercase.count("r") + combined_lowercase.count("u") + \
       combined_lowercase.count("e")
LOVE = combined_lowercase.count("l") + combined_lowercase.count("o") + combined_lowercase.count("v") + \
       combined_lowercase.count("e")
TRUE_LOVE = int(str(TRUE) + str(LOVE))

if (TRUE_LOVE < 10) or (TRUE_LOVE > 90):
    print(f"Your score is {TRUE_LOVE}, you go together like coke and mentos.")
elif 40 <= TRUE_LOVE <= 50:
    print(f"Your score is {TRUE_LOVE}, you are alright together.")
else:
    print(f"Your score is {TRUE_LOVE}.")
