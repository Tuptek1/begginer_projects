from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=2, row=4)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=3, row=6)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=4, row=8)
root.mainloop()