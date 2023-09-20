import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text="New Text")

#Button

def button_clicked():
    #my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry()
input.pack()

window.mainloop()