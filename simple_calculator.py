import tkinter as tk
from tkinter import *

root = Tk()
root.geometry('300x175')
root.title("Simple calculator")

frame = Frame(root)

infoLabel = Label(frame, text= "Hello World!")

numberButton0 = Button(root, text= "0", height=1, width=7)
numberButton1 = Button(root, text= "1", height=1, width=7)
numberButton2 = Button(root, text= "2", height=1, width=7)
numberButton3 = Button(root, text= "3", height=1, width=7)
numberButton4 = Button(root, text= "4", height=1, width=7)
numberButton5 = Button(root, text= "5", height=1, width=7)
numberButton6 = Button(root, text= "6", height=1, width=7)
numberButton7 = Button(root, text= "7", height=1, width=7)
numberButton8 = Button(root, text= "8", height=1, width=7)
numberButton9 = Button(root, text= "9", height=1, width=7)

clearButton = Button(root, text= "Clear", height=1, width=7)

operatorButton0 = Button(root, text= ",", height=1, width=7)
operatorButton1 = Button(root, text= "+", height=1, width=7)
operatorButton2 = Button(root, text= "-", height=1, width=7)
operatorButton3 = Button(root, text= "*", height=1, width=7)
operatorButton4 = Button(root, text= "/", height=1, width=7)
operatorButton5 = Button(root, text= "=", height=1, width=7)

numberButton0.grid(column=0, row=4, padx=5, pady=3)
numberButton1.grid(column=0, row=1, padx=5, pady=3)
numberButton2.grid(column=1, row=1, padx=5, pady=3)
numberButton3.grid(column=2, row=1, padx=5, pady=3)
numberButton4.grid(column=0, row=2, padx=5, pady=3)
numberButton5.grid(column=1, row=2, padx=5, pady=3)
numberButton6.grid(column=2, row=2, padx=5, pady=3)
numberButton7.grid(column=0, row=3, padx=5, pady=3)
numberButton8.grid(column=1, row=3, padx=5, pady=3)
numberButton9.grid(column=2, row=3, padx=5, pady=3)

operatorButton0.grid(column=0, row=5, padx=5, pady=3)
operatorButton1.grid(column=3, row=1, padx=5, pady=3)
operatorButton2.grid(column=3, row=2, padx=5, pady=3)
operatorButton3.grid(column=3, row=3, padx=5, pady=3)
operatorButton4.grid(column=3, row=4, padx=5, pady=3)
operatorButton5.grid(column=2, row=4, padx=5, pady=3)

clearButton.grid(column=1, row=4)

infoLabel.grid(column=0, row=0)
root.mainloop()