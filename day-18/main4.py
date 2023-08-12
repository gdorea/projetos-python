import turtle as t
import random

tim = t.Turtle()
colors = ["dark blue", "peru", "dark magenta", "misty rose", "blanched almond", "dark khaki", "dark cyan"]
moves = [0, 90, 180, 270]

tim.shape("classic")
tim.pensize(15)
tim.speed("fastest")


for n in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(moves))

screen = t.Screen()
screen.exitonclick()