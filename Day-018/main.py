from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

timmy_the_turtle.left(90)

for i in range(15):
    if not timmy_the_turtle.isdown():
        timmy_the_turtle.forward(10)
        timmy_the_turtle.pendown()
    elif timmy_the_turtle.isdown():
        timmy_the_turtle.forward(10)
        timmy_the_turtle.penup()





screen = Screen()
screen.exitonclick()