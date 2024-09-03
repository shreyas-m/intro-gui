from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize(width=300, height=200)

def calculate():
    miles = float(miles_entry.get())
    km_label.config(text=f"{miles*1.609}")

miles_entry = Entry()
miles_entry.grid(column=2, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=3, row=0)

info_label = Label(text="is equal to ")
info_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=2, row=1)

km_info_label = Label(text="Km")
km_info_label.grid(column=3, row=1)

submit = Button(text="Submit", command=calculate)
submit.grid(column=2, row=2)

window.mainloop()