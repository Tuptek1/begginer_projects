from tkinter import *
import time
import random

COLOURS = ['red', 'blue', 'green', 'black', 'pink']
TIMER = 30
SCORE = 0

def change_colour():
    global COLOURS
    global SCORE
    chose = random.choice(COLOURS)
    colour = answer.get()
    if colour  == chose:
        SCORE += 1
        var.set("Score: "+str(SCORE))
        TIMER = 30
    colourLabel.config(fg= chose)
    


def submit():
    global TIMER
    while TIMER >-1:
         
        timevar.set("Time left: "+"{0:2d}".format(TIMER))
  
        root.update()
        time.sleep(1)
        
        TIMER -= 1
        if TIMER == -1:
            root.destroy()

def change():
    global SCORE
    SCORE += 1
    var.set("Score: "+str(SCORE))
    
root = Tk()
root.geometry('400x400')
root.title("Colour_guess_game")

var = StringVar()
timevar = StringVar()
answer = StringVar()

titleLabel = Label(root, text= "Type in the colour of the words, and no the word text!", font= ('Times', 13))

scoreButton = Button(root, text= "Click to add 1 to score", command=change)
scoreLabel = Label(root, textvariable= var, font= ('Times', 13))

timeLabel = Label(root, textvariable= timevar, font= ('Times', 13))
timeButton = Button(root, text="Start", command=submit)

colourLabel = Label(root, text="Black", font= ('Times', 30))
colourEntry = Entry(root, textvariable= answer)


colourSubmit = Button(root, text= "Submit", command= change_colour)

titleLabel.grid(column= 0, row= 0, pady= 2)
titleLabel.place(relx= 0.5, rely= 0.1, anchor= CENTER)

scoreButton.grid(column= 1, row= 0, pady= 2)
scoreLabel.grid(column= 2, row= 3, pady= 2)
scoreLabel.place(relx= 0.5, rely= 0.2, anchor= CENTER)

timeButton.grid(column= 2, row= 0, pady= 2)
timeLabel.grid(column= 2, row= 4, pady= 2)
timeLabel.place(relx= 0.5, rely= 0.3, anchor= CENTER)

colourLabel.place(relx= 0.5, rely= 0.4, anchor= CENTER)
colourEntry.place(relx= 0.5, rely= 0.5, anchor= CENTER)
colourSubmit.place(relx= 0.6, rely= 0.5, anchor= CENTER)

root.mainloop()