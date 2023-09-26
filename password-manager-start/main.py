from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

email = Label(text="Email/Username:")
email.grid(column=0, row=2)

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()