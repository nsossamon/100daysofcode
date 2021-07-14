# First Pass - Input a two digit number and output the two digits added together
# Number input as a string, digit variables created from subscripting, new digit variables type casted to integers

number = input("Type a two digit number: ")
digit_one = number[0]
digit_two = number[1]
digit_one_new = int(digit_one)
digit_two_new = int(digit_two)
print(digit_one_new+digit_two_new)

# Instructor Solution:

number = input("Type a two digit number: ")
digit_one = number[0]
digit_two = number[1]
result = int(digit_one) + int(digit_two)
print(result)

