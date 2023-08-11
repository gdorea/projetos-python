import turtle as t

tim = t.Turtle()

triangle = 360/3
square = 360/4
pentagon = 360/5
hexagon = 360/6
heptagon = 360/7
octagon = 360/8
nonagon = 360/9
decagon = 360/10

tim.color('blue')
for n in range(3):
    tim.forward(100)
    tim.right(triangle)
tim.color('red')
for n in range(4):
    tim.forward(100)
    tim.right(square)
tim.color('brown')
for n in range(5):
    tim.forward(100)
    tim.right(pentagon)
tim.color('BlueViolet')
for n in range(6):
    tim.forward(100)
    tim.right(hexagon)
tim.color('burlywood3')
for n in range(7):
    tim.forward(100)
    tim.right(heptagon)
tim.color('azure4')
for n in range(8):
    tim.forward(100)
    tim.right(octagon)
tim.color('DeepPink3')
for n in range(9):
    tim.forward(100)
    tim.right(nonagon)
tim.color('gold4')
for n in range(10):
    tim.forward(100)
    tim.right(decagon)

screen = t.Screen()
screen.exitonclick()