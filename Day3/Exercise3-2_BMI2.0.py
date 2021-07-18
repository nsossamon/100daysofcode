# Program that interprets BMI and interprets into a statement based on the value:
# Under 18.5 they are underweight
# Over 18.5 but below 25 they have a normal weight
# Over 25 but below 30 they are slightly overweight
# Over 30 but below 35 they are obese
# Above 35 they are clinically obese.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
BMI = round(weight / height ** 2)

if BMI < 18.5:
    print("your BMI is " + str(BMI) + ", you are underweight.")
elif BMI < 25:
    print("your BMI is " + str(BMI) + ", you have a normal weight.")
elif BMI < 30:
    print("your BMI is " + str(BMI) + ", you are slightly overweight.")
elif BMI < 35:
    print("your BMI is " + str(BMI) + ", you are overweight.")
else:
    print("your BMI is " + str(BMI) + ", you are clinically obese.")