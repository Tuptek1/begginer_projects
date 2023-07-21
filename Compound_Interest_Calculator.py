from tkinter import *

def calculate_ci():
    principal = int(principal_field.get())    
    rate = float(rate_field.get())
    time = int(time_field.get())
      
    CI = principal * (pow((1 + rate / 100), time))
    compound_field.insert(10, CI)

def clearall():
    principal_field.delete(0, END)  
    rate_field.delete(0, END)
    time_field.delete(0, END)
    compound_field.delete(0, END)
   
    principal_field.focus_set()

root = Tk()
root.title("Compound Interest Calculator")
root.geometry('450x300')


principleLabel = Label(root, text="Principle Amount(Rs): ")
principleLabel.grid(row=1, column=0, padx=10, pady=10)

rateLabel = Label(root, text="Rate(%): ")
rateLabel.grid(row=2, column=0, padx=10, pady=10)

timeLabel = Label(root, text="Years: ")
timeLabel.grid(row=3, column=0, padx=10, pady=10)

interestLabel = Label(root, text="Compound Interest: ")
interestLabel.grid(row=5, column=0, padx=10, pady=10)

submitButton = Button(root, text="Submit", command=calculate_ci)
submitButton.grid(row=4, column=1, padx=10, pady=10)

clearButton = Button(root, text="Clear", command=clearall)
clearButton.grid(row=6, column=1, padx=10, pady=10)

principal_field = Entry(root) 
principal_field.grid(row = 1, column = 1, padx = 10, pady = 10) 

rate_field = Entry(root) 
rate_field.grid(row = 2, column = 1, padx = 10, pady = 10) 

time_field = Entry(root)
time_field.grid(row = 3, column = 1, padx = 10, pady = 10)

compound_field = Entry(root)
compound_field.grid(row = 5, column = 1, padx = 10, pady = 10)

 

root.mainloop()