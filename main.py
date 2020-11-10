from tkinter import *
from tkinter.ttk import *

expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    exp.set(expression)


def evaluate():
    try:
        global expression
        total = str(eval(expression))
        exp.set(total)
        expression = total

    except:
        exp.set("Error in expression")
        expression = ""


def cl():
    global expression
    expression = ""
    exp.set("")


def dl():
    global expression
    expression = expression[:-1]
    exp.set(expression)


root = Tk()

root.title("Calculator")

root.geometry("300x300")
exp = StringVar()
exp_field = Entry(root, textvariable=exp)
exp_field.grid(columnspan=5, ipadx=80)
# exp_field.grid(row = 0, column = 0, pady = 2)
# exp_field.place(relx = 1, x = -1, y = 2, anchor = NE)
exp.set('Enter Expression: ')

buttons = [0] * 10
buttons[0] = Button(root, text=0, command=lambda: press(num=0), width=7)
buttons[0].grid(row=2, column=0)
buttons[1] = Button(root, text=1, command=lambda: press(num=1), width=7)
buttons[1].grid(row=2, column=1)
buttons[2] = Button(root, text=2, command=lambda: press(num=2), width=7)
buttons[2].grid(row=2, column=2)
buttons[3] = Button(root, text=3, command=lambda: press(num=3), width=7)
buttons[3].grid(row=3, column=0)
buttons[4] = Button(root, text=4, command=lambda: press(num=4), width=7)
buttons[4].grid(row=3, column=1)
buttons[5] = Button(root, text=5, command=lambda: press(num=5), width=7)
buttons[5].grid(row=3, column=2)
buttons[6] = Button(root, text=6, command=lambda: press(num=6), width=7)
buttons[6].grid(row=4, column=0)
buttons[7] = Button(root, text=7, command=lambda: press(num=7), width=7)
buttons[7].grid(row=4, column=1)
buttons[8] = Button(root, text=8, command=lambda: press(num=8), width=7)
buttons[8].grid(row=4, column=2)
buttons[9] = Button(root, text=9, command=lambda: press(num=9), width=7)
buttons[9].grid(row=5, column=0)

plus = Button(root, text=" + ", command=lambda: press("+"), width=7)
plus.grid(row=2, column=3)
minus = Button(root, text=" - ", command=lambda: press("-"), width=7)
minus.grid(row=3, column=3)
multiply = Button(root, text=" * ", command=lambda: press("*"), width=7)
multiply.grid(row=4, column=3)
divide = Button(root, text=" / ", command=lambda: press("/"), width=7)
divide.grid(row=5, column=3)
equal = Button(root, text=" = ", command=lambda: evaluate(), width=7)
equal.grid(row=5, column=2)
clear = Button(root, text=" C ", command=lambda: cl(), width=7)
clear.grid(row=6, column=3)
decimal = Button(root, text=" . ", command=lambda: press("."), width=7)
decimal.grid(row=5, column=1)
delete = Button(root, text=" D ", command=lambda: dl(), width=7)
delete.grid(row=6, column=2)
root.mainloop()
