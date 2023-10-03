from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
data_dict = {}

try:
    data = pd.read_csv("./flash-card-project/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("./flash-card-project/data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer) #está em vermelho pq esperava um comando e não uma variável, mas está funcionando
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(flash_card_front, image=flash_card_front_img)
    flip_timer = window.after(3000, update_card)

def update_card():
    canvas.itemconfig(flash_card_front, image=flash_card_back)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")

def is_known():
    data_dict.remove(current_card)
    data = pd.DataFrame(data_dict)
    data.to_csv("./flash-card-project/data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

flip_timer = window.after(3000, update_card)

canvas = Canvas(width=800, height=526)
flash_card_front_img = PhotoImage(file="./flash-card-project/images/card_front.png")
flash_card_front = canvas.create_image(405, 270, image=flash_card_front_img)
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

flash_card_back = PhotoImage(file="./flash-card-project/images/card_back.png")

wrong_img = PhotoImage(file="./flash-card-project/images/wrong.png")
wrong_button = Button(image=wrong_img, background=BACKGROUND_COLOR, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./flash-card-project/images/right.png")
right_button = Button(image=right_img, background=BACKGROUND_COLOR, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
