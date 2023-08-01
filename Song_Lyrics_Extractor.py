from lyrics_extractor import SongLyrics
from tkinter import *

def get_lyrics():
    textlabel.delete(1.0 , END)
    extract_lyrics = SongLyrics("AIzaSyCBZHXigBymV1utxKV6oI3sNLceK693CdE", "30796381ecf94465b")
    data = extract_lyrics.get_lyrics(str(mainEntry.get()))
    songname.set(data['title'])
    res = data['lyrics']
    textlabel.insert(END, str(res))

root = Tk()
root.geometry('700x310')

songname = StringVar()

mainLabel = Label(root, text= "Enter the name of the song: ")
mainLabel.grid(column=1, row=0)

mainEntry = Entry(root)
mainEntry.grid(column=2, row=0)

submitButton = Button(root, text="Submit", command=get_lyrics)
submitButton.grid(column=3, row=0)

songLabel = Label(root, text='What you searched: ' , textvariable=songname)
songLabel.grid(column=4, row=1, padx= 10)


textlabel = Text(root, height=10, width=80)
textlabel.tag_configure('tag_name', justify = 'center')
textlabel.grid(column=1, row=1, sticky=W, columnspan=3)



root.mainloop()

 