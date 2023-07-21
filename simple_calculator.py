import tkinter as tk
from tkinter import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        
        total = str(eval(expression))
        
        equation.set(total)
        
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
    
def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == "__main__":
    root = Tk()
    root.geometry('300x180')
    root.title("Simple calculator")

    equation = StringVar()

    showEntry = Entry(root, width=40, textvariable=equation)
    showEntry.grid(column=0, row=0, columnspan=5)

    numberButton0 = Button(root, text= " 0 ", height=1, width=7, command=lambda: press(0))
    numberButton0.grid(column=0, row=4, padx=5, pady=3)

    numberButton1 = Button(root, text= " 1 ", height=1, width=7, command=lambda: press(1))
    numberButton1.grid(column=0, row=1, padx=5, pady=3)

    numberButton2 = Button(root, text= " 2 ", height=1, width=7, command=lambda: press(2))
    numberButton2.grid(column=1, row=1, padx=5, pady=3)

    numberButton3 = Button(root, text= " 3 ", height=1, width=7, command=lambda: press(3))
    numberButton3.grid(column=2, row=1, padx=5, pady=3)

    numberButton4 = Button(root, text= " 4 ", height=1, width=7, command=lambda: press(4))
    numberButton4.grid(column=0, row=2, padx=5, pady=3)

    numberButton5 = Button(root, text= " 5 ", height=1, width=7, command=lambda: press(5))
    numberButton5.grid(column=1, row=2, padx=5, pady=3)

    numberButton6 = Button(root, text= " 6 ", height=1, width=7, command=lambda: press(6))
    numberButton6.grid(column=2, row=2, padx=5, pady=3)

    numberButton7 = Button(root, text= " 7 ", height=1, width=7, command=lambda: press(7))
    numberButton7.grid(column=0, row=3, padx=5, pady=3)

    numberButton8 = Button(root, text= " 8 ", height=1, width=7, command=lambda: press(8))
    numberButton8.grid(column=1, row=3, padx=5, pady=3)

    numberButton9 = Button(root, text= " 9 ", height=1, width=7, command=lambda: press(9))
    numberButton9.grid(column=2, row=3, padx=5, pady=3)

    clearButton = Button(root, text= " Clear ", height=1, width=7, command=clear)
    clearButton.grid(column=1, row=4)

    operatorButton0 = Button(root, text= " , ", height=1, width=7, command=lambda: press(" , ")) 
    operatorButton0.grid(column=0, row=5, padx=5, pady=3)

    operatorButton1 = Button(root, text= " + ", height=1, width=7, command=lambda: press(" + "))
    operatorButton1.grid(column=3, row=1, padx=5, pady=3)

    operatorButton2 = Button(root, text= " - ", height=1, width=7, command=lambda: press(" - "))
    operatorButton2.grid(column=3, row=2, padx=5, pady=3)

    operatorButton3 = Button(root, text= " * ", height=1, width=7, command=lambda: press(" * "))
    operatorButton3.grid(column=3, row=3, padx=5, pady=3)

    operatorButton4 = Button(root, text= " / ", height=1, width=7, command=lambda: press(" / "))
    operatorButton4.grid(column=3, row=4, padx=5, pady=3)

    operatorButton5 = Button(root, text= " = ", height=1, width=7, command=lambda: equalpress)
    operatorButton5.grid(column=2, row=4, padx=5, pady=3)

    root.mainloop()