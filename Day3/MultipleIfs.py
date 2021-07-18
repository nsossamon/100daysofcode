# Multiple if will check multiple if statements in succession and execute all of them if applicable. In example below,
# if all 3 conditions are met, A, B and C will all be done:
# if condition1:
#   do A
# if condition2:
#   do B
# if condition3:
#   do C
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.00")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.00")
    elif age <= 22:
        bill = 10
        print("College tickets are $10.00")
    elif 45 <= age <= 55:
        print("Your midlife crisis is awesome, and you're a winner! Free ride on us.")
    else:
        bill = 12
        print("Adult tickets are $12.00")

    wants_photo = (input("Do you want a photo taken? (Y or N): "))
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}.00")
else:
    print("Sorry you're a short little bitch and can't ride this!")
