from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_input = website_entry.get()
    email_input = email_entry.get()
    password_input = password_entry.get()
    if website_input == "" or password_input == "":
        messagebox.showerror(title="Oops", message="Please, don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_input, message=f"These are the details entered: \nEmail: {email_input} \nPassword: {password_input} \nIs it ok to save?")
        if is_ok:
            data = open("./password-manager-start/data.txt", "a")
            data.write(f"{website_input} | {email_input} | {password_input}\n")
            data.close()
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

generate_password = Button(text="Generate Password")
generate_password.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()