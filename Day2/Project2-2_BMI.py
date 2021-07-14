# Use height and weight as input and produce BMI as output:

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
Result = str(int(int(weight) / int(height) ** 2))
print("Your BMI is " + Result)
