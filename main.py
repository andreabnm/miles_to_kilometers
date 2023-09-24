from tkinter import *

FONT = ("Arial", 14, "normal")

window = Tk()
window.title("Miles to Kilometers Converter")
window.minsize(width=250, height=150)

input_miles = Entry(width=10)
input_miles.config(justify="center")
input_miles.grid(column=1, row=0)
miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=0)

equal_to_label = Label(text="is equal to", font=FONT)
equal_to_label.grid(column=0, row=1)

result_label = Label(text="0", font=FONT)
result_label.grid(column=1, row=1)
km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)


def calculate():
    km = round(float(input_miles.get()) * 1.60934, 2)
    result_label.config(text=km)


button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
