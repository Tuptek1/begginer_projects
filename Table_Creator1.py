import requests
from tkinter import *

counter = 10
lst = [] 
forname = input()
for i in range(0, counter):
    response = requests.get(f'https://ws-public.interpol.int/notices/v1/red?forename={forename}&resultPerPage=200')
    print(response.json()["results"][i]['gender'])
    gender = response.json()["results"][i]['gender']
    last_name = response.json()["results"][i]['name']['last']
    first_name = response.json()["results"][i]['name']['first']
    if gender == 'female':
        lst.append((first_name, last_name, gender))
    else:
        counter += 1
class Table:
    def __init__(self, root):
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg="blue", font=("Arial", 16, 'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


total_rows = len(lst)
total_columns = len(lst[0]) 
             
root = Tk()
t = Table(root)
root.mainloop()