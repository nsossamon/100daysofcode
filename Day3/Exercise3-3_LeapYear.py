# Program that determines if a given year is a leap year or not. Formula:
# on every year that is evenly divisible by 4:
#     **except** every year that is evenly divisible by 100
#          **unless** the year is also evenly divisible by 400
#
# e.g. The year 2000: (is divisible by 4, is divisible by 100 so normally would be an exception, but is divisible by 400
# so it is still a leap year)
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
#
# e.g. The year 2100: (meets exception statement as well as unless statement, so not a leap year)
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    year_except = year % 100
    if year_except == 0:
        year_unless = year % 400
        if year_unless == 0:
            print("This is a leap year.")
        else:
            print("This is not a leap year.")
    else:
        print("This is a leap year.")
else:
    print("This is not a leap year.")
