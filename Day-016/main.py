# import turtle, another_module

# from turtle import Turtle, Screen
#
# # print(another_module.another_variable)
#
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("cyan")
# timmy.forward(100)
# print(timmy)
#
# my_screen=Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table=PrettyTable()

print(table)

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)

table.align ="l"

print(table)