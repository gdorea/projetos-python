from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)


  password_letters = [random.choice(letters) for _ in range(nr_letters)]
  password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
  password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

  password_list = password_letters + password_numbers + password_symbols

  random.shuffle(password_list)

  password = "".join(password_list)

  password_entry.insert(0, password)
  pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    new_data = {
        website_input: {
            "email": email_input,
            "password": password_input,
        }
    }
    if len(website_input) == 0 or len(password_input) == 0:
        messagebox.showerror(title="Oops", message="Please, don't leave any fields empty!")
    else:
        with open("./password-manager-start/data.json", "r") as data_file:
            #Reading old data
            data = json.load(data_file)
            #Updating old data with new data
            data.update(new_data)

        with open("./password-manager-start/data.json", "w") as data_file:
            #Saving updated data
            json.dump(data, data_file, indent=4)
        
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
locker_img = PhotoImage(file="./password-manager-start/logo.png")
canvas.create_image(100, 100, image=locker_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:")
website.grid(column=0, row=1)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "gerzi@gmail.com")

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", command=password_generator)
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()