# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(f"{names[random.randint(0, (len(names) - 1))]} is going to buy the meal today!")

# The choice function of random can do this much more easily:
paying_person = random.choice(names)
print(paying_person + " is going to buy the meal today!")

print(type(paying_person))

