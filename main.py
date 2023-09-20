#Калькулятор
from tkinter import *
def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(number))

def button_clear():
    entry.delete(0, END)

def button_equal():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

root = Tk()
root.title("Calculator")
root.geometry('223x269+800+300')
root.resizable (width=False, height=False)

entry = Entry(root, width=25, borderwidth=5, background="#000000", fg="#00FF00", font="Arial 10")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0),
    ("8", 1, 1),
    ("9", 1, 2),
    ("/", 1, 3),
    ("4", 2, 0),
    ("5", 2, 1),
    ("6", 2, 2),
    ("*", 2, 3),
    ("1", 3, 0),
    ("2", 3, 1),
    ("3", 3, 2),
    ("-", 3, 3),
    ("0", 4, 0),
    (".", 4, 1),
    ("+", 4, 3)
]

for button_data in buttons:
    button_text, row, column = button_data
    button = Button(root, text=button_text, padx=20, pady=10, background="#CCCCFF", width=1, command=lambda button_text=button_text: button_click(button_text))
    button.grid(row=row, column=column)

clear_button = Button(root, text="C", padx=20, pady=10, background="#FF0033", width=1, command=button_clear)
clear_button.grid(row=5, column=0)

equal_button = Button(root, text="=", padx=20, pady=10, background="#CCCCFF", command=button_equal)
equal_button.grid(row=5, column=2)

root.mainloop()