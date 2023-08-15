from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
# w -> forwards
# s -> backwards
# a -> counter-clockwise (left)
# d -> clockwise (right)
# c -> clear drawing


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)

def move_right():
    tim.right(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
