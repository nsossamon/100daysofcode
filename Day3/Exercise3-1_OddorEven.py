# Modulo Operation - Will provide the remainder of division
print(7 % 2)

# Write a program that determines if a given number is odd or even
# Even numbers can be divided by 2 without a remainder
number = int(input("Which number do you want to check? "))
number_remainder = number % 2
if number_remainder == 0:
    print("This is an even number")
else:
    print("This is an odd number")

# Instructor Example
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

