from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine=MoneyMachine()
menu=Menu()
coffee_maker=CoffeeMaker()
print(money_machine)
print(menu.get_items())
is_on=True

while is_on:
    options=menu.get_items()
    choice = input((f"What would you like? ({options}): "))

    if choice=="off":
        is_on=False
    elif choice=="report":
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        choice = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(choice) and money_machine.make_payment(choice.cost):
                coffee_maker.make_coffee(choice)

