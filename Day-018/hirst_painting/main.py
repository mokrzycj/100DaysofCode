import colorgram
import math
from turtle import Turtle, Screen
# from random_walk import another_random_color
import random
screen=Screen()
screen.colormode(255)

colors = colorgram.extract('pawbeats.jpg', 32)
print(len(colors))
rgb_colors=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    new_color=(r, g, b)
    rgb_colors.append(new_color)
print(rgb_colors)

tim=Turtle()
tim.speed("fastest")
tim.penup()
tim.setposition(-300,-300)
setx=-300
sety=-300
# tim.dot(30,"red")
print(screen.screensize())
print(len(rgb_colors))
# size=int(math.sqrt(len(rgb_colors)))
size=10
# print(size)

what_color=0
for y in range(size):
    for x in range(size):
        setx+=50
        tim.setx(setx)
        tim.dot(20, rgb_colors[what_color])
        what_color+=1
        if what_color>=len(rgb_colors):
            what_color=0
    sety+=50
    setx=-300
    tim.setx(-300)
    tim.sety(sety)




screen.exitonclick()