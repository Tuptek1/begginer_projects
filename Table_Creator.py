import requests
from tkinter import *

response = requests.get('https://randomuser.me/api')

gender = response.json()["results"][0]['gender']
last_name = response.json()["results"][0]['name']['last']
first_name = response.json()["results"][0]['name']['first']

class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg="blue", font=("Arial", 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


lst = [first_name, last_name, gender] 
  
total_rows = len(lst)
total_columns = len(lst[0]) 
             
root = Tk()
t = Table(root)
root.mainloop()