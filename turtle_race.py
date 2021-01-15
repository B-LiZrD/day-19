from turtle import Turtle, Screen
from tkinter import *
import random
is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n 'red',"
                                                          "'orange', 'yellow', 'green', 'blue', or 'purple'. ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=-y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} won the race!")
                is_race_on = False
            else:
                print(f"Sorry, wrong bet..The winning turtle was {winning_color}")
                is_race_on = False


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()


