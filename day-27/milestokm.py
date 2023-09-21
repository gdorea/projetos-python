import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

input = tkinter.Entry(width=8)
input.grid(column=1, row=0)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = tkinter.Label(text="0")
label3.grid(column=1, row=1)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=1)

def button_clicked():
    km = float(input.get()) * 1.6
    label3.config(text=round(km))


button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)


window.mainloop()