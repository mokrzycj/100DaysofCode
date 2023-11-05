"""Program created to train with if/elif/else."""

chest = '''
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
'''

print(chest)
print('''Welcome to Treasure Island. 
Your mission is to find the treasure.''')

decision = input("Are you going to left or right?\n")

if decision == "left":
    decision = input("Are you waiting for a boat or you choose to swim on your own? 'wait' or 'swim'\n")
    if decision == "wait":
        decision = input("Are you choosing Red, Yellow or Blue doors?\n")
        if decision == "yellow":
            print("You Win!")
        elif decision == "red":
            print("Burned by fire. \nGame Over.")
        elif decision == "blue":
            print("Eaten by beasts. \nGame Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. \nGameOver")
else:
    print("Fall into a hole. \nGame Over.")
