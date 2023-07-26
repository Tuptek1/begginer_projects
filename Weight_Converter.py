from tkinter import *

def convert():
    gram = float(weightEntry.get())*1000
     
    pound = float(weightEntry.get())*2.20462
     
    ounce = float(weightEntry.get())*35.274
     
    t1.delete("1.0", END)
    t1.insert(END,gram)
     
    t2.delete("1.0", END)
    t2.insert(END,pound)
     
    t3.delete("1.0", END)
    t3.insert(END,ounce)

root = Tk()
root.title("Weight Converter")
root.geometry('450x100')

weightLabel = Label(root, text="Enter the weight in Kg ")
weightLabel.grid(row=0, column=0, padx=10, pady=10)

weightEntry = Entry(root)
weightEntry.grid(row=0, column=1, padx=10, pady=10)

convertButton = Button(root, text="Convert", command=convert)
convertButton.grid(row=0, column=2, padx=10)

gramLabel  = Label(root, text="Gram")
gramLabel.grid(row=1, column=0, padx=10)

poundLabel = Label(root, text="Pound")
poundLabel.grid(row=1, column=1, padx=10)

ounceLabel = Label(root, text="Ounce")
ounceLabel.grid(row=1, column=2, padx=10)

t1 = Text(root, height = 1, width = 20)
t1.grid(row = 2, column = 0)

t2 = Text(root, height = 1, width = 20)
t2.grid(row = 2, column = 1)

t3 = Text(root, height = 1, width = 20)
t3.grid(row = 2, column = 2)

root.mainloop()

