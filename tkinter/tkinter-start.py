from tkinter import *

window = Tk()


def km_to_grams():
    grams.delete('1.0', END)
    grams.insert(END, float(inputKg_value.get()) * 1000)


def km_to_pounds():
    pounds.delete('1.0', END)
    pounds.insert(END, float(inputKg_value.get()) * 2.20462)


def km_to_ounces():
    ounces.delete('1.0', END)
    ounces.insert(END, float(inputKg_value.get()) * 35.274)


def convert_km():
    km_to_grams()
    km_to_pounds()
    km_to_ounces()


input_label = Label(text="Kg: ")
input_label.grid(row=0, column=0)


inputKg_value = StringVar()
inputKg = Entry(window, textvariable=inputKg_value)
inputKg.grid(row=0, column=1, sticky="W")


submit = Button(window, text="Convert", command=convert_km)
submit.grid(row=0, column=2, pady=20)


grams_label = Label(text="Grams: ")
grams_label.grid(row=1, column=0)
grams = Text(window, height=1, width=20)
grams.grid(row=1, column=1)

pounds_label = Label(text="Pounds: ")
pounds_label.grid(row=1, column=2)
pounds = Text(window, height=1, width=20)
pounds.grid(row=1, column=3, pady=20)

ounces_label = Label(text="Ounces: ")
ounces_label.grid(row=1, column=4)
ounces = Text(window, height=1, width=20)
ounces.grid(row=1, column=5)


window.mainloop()
