print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_or_right = input("You come upon a fork in the road. Which direction do you want to go? (Left or Right): ")

if left_or_right == "Left":
    swim_or_wait = input("Good choice!. You see a quaint looking stream. Do you swim across or wait a bit? (Swim or "
                         "Wait): ")
    if swim_or_wait == "Wait":
        door = input("Safety wins the day! You see three doors.  Which do you choose? (Blue, Red, or Yellow): ")
        if door == "Red":
            print("Burned by Fire. Game over bitch!")
        elif door == "Blue":
            print("Eaten by beasts. Game over bitch!")
        elif door == "Yellow":
            print("You Win! Golden shower party bitch!")
        else:
            print("Can you not type, heathen? Game over bitch!")
    else:
        print("Attacked by trout. Game over bitch!")
else:
    print("Fall into a hole, game over bitch!")
