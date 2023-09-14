import turtle
import pandas

data = pandas.read_csv("./us-states-game/50_states.csv")
all_states = data.state.to_list()
guessed_states = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", 
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        states_data = pandas.DataFrame(all_states)
        states_data.to_csv("./us-states-game/states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        all_states.remove(answer_state)
