from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./flash-card-project/data/french_words.csv")
data_dict = data.to_dict(orient="records")

def next_card():
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
flash_card_front = PhotoImage(file="./flash-card-project/images/card_front.png")
canvas.create_image(405, 270, image=flash_card_front)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

wrong_img = PhotoImage(file="./flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_img, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./flash-card-project/images/right.png")
right_button = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
right_button.grid(column=1, row=1)

next_card()




window.mainloop()