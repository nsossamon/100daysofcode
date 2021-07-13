# double/single quotes are a string, tells it not to run as code
# print is a function
print("Hello World!")

# day 1-1 Exercise (can use " or ' as a string, must alternate for string within a string)
print('Day 1 - Python Print Function')
print('The function is declared like this:')
print("print('what to print')")

# \n will cut output to a new line
print("Hello World!\nHello World!")

# + will concatenate two or multiple strings together
print("Hello" + " " + "Angela")
print("Hello" + " Angela")

# day 1-2 Debugging Exercise
print('Day 1 - String Manipulation')
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print('New lines can be created with a backslash and n.')

# input function places a cursor at the end of the line expecting a response, which can then be used in your code
# input function can be placed in a print function
input('What is your name?')
print("Hello " + input("What is your name?"))

# day 1-3 Inputs Exercise - function that uses name as input and length as output (use len function with a variable)
x = input('What is your name? ')
print(len(x))

# other option
print(len(input("What is your name ")))

