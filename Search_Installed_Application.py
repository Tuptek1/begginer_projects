from tkinter import *
import winapps

def app():
    for item in winapps.search_installed(entry1.get()):
        name.set(item.name)
        version.set(item.version)
        Install_date.set(item.install_date)
        publisher.set(item.publisher)
        uninstall_string.set(item.uninstall_string)

root = Tk()
root.geometry("400x250")

name = StringVar()
version = StringVar()
Install_date = StringVar()
publisher = StringVar()
uninstall_string = StringVar()

label1 = Label(root, text="Enter App name: ")
label1.grid(row=0, column=0, pady=20)

Label(root, text="Name : ",).grid(row=2, sticky=W)
Label(root, text="Version :",).grid(row=3, sticky=W)
Label(root, text="Install date :",).grid(row=4, sticky=W)
Label(root, text="publisher :",).grid(row=5, sticky=W)
Label(root, text="Uninstall string :",).grid(row=6, sticky=W)

Label(root, text="", textvariable=name).grid(row=2, column=1, sticky=W)
Label(root, text="", textvariable=version).grid(row=3, column=1, sticky=W)
Label(root, text="", textvariable=Install_date).grid(row=4, column=1, sticky=W)
Label(root, text="", textvariable=publisher).grid(row=5, column=1, sticky=W)
Label(root, text="", textvariable=uninstall_string).grid(row=6, column=1, sticky=W)


entry1 = Entry(root)
entry1.grid(row=0, column=1, pady=20)

showButton = Button(root, text='Show', command=app)
showButton.grid(row=0, column=2, pady=20)

root.mainloop()