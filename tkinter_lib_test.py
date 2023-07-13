from tkinter import *
import tkinter as tk

chkstate = "Geeks for Geeks updated !!!"
def counter():
    global chkstate
    valid.config(text= chkstate)
    
def check(var, index, mode):
    if chbox_var.get() == 1:
        chkstate = "The checkbox is checked"
    else:
        chkstate = "The checkbox is not checked"

def submit():
    
    name=name_var.get()
    password = passw_var.get()
        
    print("The name is : " + name)
    print("The password is : " + password)
        
    name_var.set("")
    passw_var.set("")

root = Tk() 
root.geometry('400x150')
root.title("Username")

menu_bar = Menu(root)
menu_1 = Menu(menu_bar, tearoff = 0)

menu_bar.add_cascade(label = "Menu1", menu = menu_1)
menu_1.add_command(label = 'Nigger')
menu_1.add_separator()
menu_1.add_command(label = 'Quit', command= root.quit)

root.config(menu=menu_bar)

name_var = tk.StringVar()
passw_var = tk.StringVar()
chbox_var = tk.IntVar()

    
usernameLabel = Label(root, text = "Enter your username")
usernameEntry = Entry(root, textvariable = name_var)
passwordLabel = Label(root, text = "Enter your password")
passwordEntry = Entry(root, textvariable = passw_var, show = "*")
valid = Label(root, text = "geeksforgeeks")

quitButton = Button(root, text = "Quit", command = root.quit)

submitButton1 = Button(root, text = "Submit", command = submit)

chbox_var.trace("w", check)
checkButton = Checkbutton(root, command= counter,   text= "Please update")

usernameLabel.grid(column=0, row=0)
usernameEntry.grid(column=1, row=0)
passwordLabel.grid(column=0, row=1)
passwordEntry.grid(column=1, row=1)

submitButton1.grid(column=3, row=0, pady= 2)
quitButton.grid(column=4, row=0, pady= 2)
checkButton.grid(column=0, row=3, pady= 2)
valid.grid(column=0, row=4, pady= 2)

root.mainloop()