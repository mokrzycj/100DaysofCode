import random
from turtle import Turtle, Screen

screen=Screen()
tim=Turtle()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet: ", prompt="Which turtle will win the race? Enter a color: ")
turtle_colors=["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles=[]

y_index=-100
for turtle_index in range(0, 6):
    tim=Turtle(shape="turtle")
    tim.color(turtle_colors[turtle_index])
    tim.penup()
    tim.goto(-230, y_index)
    y_index+=40
    all_turtles.append(tim)
    print(all_turtles)

race_on=True
while race_on:
    for tim in all_turtles:
        tim.forward(random.randint(1,10))
        print(tim.xcor())
        if tim.xcor()>=230:
            print(f"Race won {tim.color()[0]} turtle!")
            if user_bet==tim.color()[0]:
                print("You guessed correctly.")
            else:
                print("Your guess was wrong.")
            race_on=False
            break

screen.exitonclick()