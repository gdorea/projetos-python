import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


for n in range(180):
    tim.color(random_color())
    tim.circle(90)
    tim.left(2)
    


screen = t.Screen()
screen.exitonclick()
