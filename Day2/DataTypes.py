# Data Types
# Subscripting - brackets can show position of a character in a string (always starts with 0)
# Below function will result in H

print("Hello"[0])

# Integer - whole numbers, just write a number without any formatting
# Below function will add the two digits:

print(1+1)

# Underscores in an integer can represent commas (common in USA/UK)

print(1_000+1_000)

# Float - floating point number using decimals (e.g. 3.14)

print(3.5+3.5)

# Boolean - True or False data types, always capitalized

# TypeErrors - using a data type in a function that isn't appropriate (e.g. an integer in a len function)
# TypeErrors - another example, can't use an integer to concatenate a string, see below example
# Below will result in - TypeError: can only concatenate str (not "int") to str

num_char = len(input("What is your name?"))
print("there are " + num_char + " letters in your name")

# type() will show you the data type

type(num_char)

# Type Casting - converting one data type into another
# Below example will turn num_char from an integer to a string:

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print("there are " + new_num_char + " letters in your name")

