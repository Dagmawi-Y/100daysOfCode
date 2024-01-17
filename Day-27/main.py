from tkinter import *


def button_clicked():
    my_label.config(text=input_from_user.get())


window = Tk()

window.title("GUI prog")
window.minsize(width=500, height=500)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a lable", font=('Arial', 24, 'bold'))
my_label['text'] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button1
button = Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

# Button2
button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Entry
input_from_user = Entry()
input_from_user.config(width=10)
print(input_from_user.get())
input_from_user.grid(column=3, row=3)

window.mainloop()
