from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(500, 500)


my_label = Label(text="I am a Lable", font=("Comic Sans MS", 24, "bold"))
my_label.grid(column=0, row=0)

def button_click():
    my_label["text"] = "Button got clicked!!!"
    my_label.config(text=my_entry.get())

my_button = Button(text="Click Me", command=button_click)
my_button.grid(column=1, row=1)

my_entry = Entry()
my_entry.grid(column=3, row=3)

new_button = Button(text="new Button")
new_button.grid(column=3, row=0)

window.mainloop()