import math, os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

AVAILABLE_COMMANDS={"espresso", "cappuccino", "latte", "off", "report"}

ACCEPTED_COINS={
    "quarters": .25,
    "dimes": .10,
    "nickels": .05,
    "pennys": .01    
}

''' this is badly written function, because due to recursion, value of choice variable is lost in recursion stack. Better way of implementing this is with while loop'''
# def validate_user_choice():
#     choice = input("What would you like? espresso/latte/cappuccino: ")
#     if choice not in AVAILABLE_COMMANDS:
#         print("Please provide proper choice.")
#         # choice=""
#         choice = validate_user_choice()
#     else:
#         return choice

def validate_user_choice():
    while True:
        choice = input("What would you like? espresso/latte/cappuccino: ")
        if choice in AVAILABLE_COMMANDS:
            return choice
        else:
            print("Please provide proper choice.")

    
def accept_payment(beverage):
    payment=0
    for coin in ACCEPTED_COINS:
        insertedCoins=int(input(f"How many {coin}? "))
        payment+=insertedCoins * ACCEPTED_COINS[coin]
    resources["money"]+=round(MENU[beverage]["cost"], 2)
    # print(payment)
    if beverage in MENU:
        if payment>=MENU[beverage]["cost"]:
            change=round((payment-MENU[beverage]["cost"]), 2)
            print(f"Your change is {change}")
            print(f"Here is your {beverage} ☕️. Enjoy!")
        else:
            print("Not enough money, try again.")
            print(f"Your change is {payment}")
        
def is_enough_resources(choice):
    for ingredient in MENU[choice]["ingredients"]:
        if resources[ingredient]-int(MENU[choice]["ingredients"][ingredient])>=0:
            resources[ingredient]=resources[ingredient]-int(MENU[choice]["ingredients"][ingredient])
        else:
            print(f"There is no enough {ingredient} in coffee machine.")
            return False
    return True


def coffe_machine():
    os.system("clear")
    shouldContinue=True
    while shouldContinue:
        userChoice=validate_user_choice()

        if userChoice=="off":
            return
        elif userChoice=="report":
            for resource in resources:
                print(f"{resource}: {resources[resource]}")
    
        if not (userChoice in ["off", "report"]) and is_enough_resources(userChoice):
            accept_payment(userChoice)

coffe_machine()