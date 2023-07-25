from tkinter import *

root = Tk()
root.title("Weight Converter")
root.geometry('450x100')

weightLabel = Label(root, text="Enter the weight in Kg ")
weightLabel.grid(row=0, column=0, padx=10, pady=10)

weightEntry = Entry(root)
weightEntry.grid(row=0, column=1, padx=10, pady=10)

convertButton = Button(root, text="Convert")
convertButton.grid(row=0, column=2, padx=10)

gramLabel  = Label(root, text="Gram")
gramLabel.grid(row=1, column=0, padx=10)

poundLabel = Label(root, text="Pound")
poundLabel.grid(row=1, column=1, padx=10)

ounceLabel = Label(root, text="Ounce")
ounceLabel.grid(row=1, column=2, padx=10)

gramEntry = Entry(root)
gramEntry.grid(row=2, column=0, padx=10)

poundEntry = Entry(root)
poundEntry.grid(row=2, column=1, padx=10)

ounceEntry = Entry(root)
ounceEntry.grid(row=2, column=2, padx=10)

root.mainloop()

