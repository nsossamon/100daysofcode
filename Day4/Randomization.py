# Python uses a Pseudorandom Number Generating Algorithm for generating random numbers
# The Python Random module has a bunch of functions for generating random number
import random

random_integer = random.randint(0, 4)
print(random_integer)

random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# random decimal between 0 and 5 (multiply float times the end range digit):
print(random_float * 5)

