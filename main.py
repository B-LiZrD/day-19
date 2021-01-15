from turtle import Turtle, Screen

tim = Turtle()

screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def counter_clockwise():
    tim.left(7)


def clockwise():
    tim.right(7)


def clear_screen():
    tim.reset()


screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
