from turtle import Turtle, Screen

timmy = Turtle() #cria o objeto chamado timmy a partir da classe Turtle
print(timmy)
timmy.shape("turtle")
timmy.color("DarkViolet")
timmy.forward(100)

my_screen = Screen() #cria o objeto da tela a partir da classe Tela, tambem dentro da biblioteca turtle
print(my_screen.canvheight)
my_screen.exitonclick()

