from turtle import Turtle, Screen
import random
import secrets


number_of_sides=3
timmy=Turtle()
for _ in range (20):

    # print(random_color)

    for _ in range(number_of_sides):
        random_color = secrets.token_hex(3)
        random_color = "#" + random_color
        timmy.pencolor(random_color)
        timmy.forward(100)
        timmy.right(360/number_of_sides)
    number_of_sides+=1



screen=Screen()
screen.exitonclick()