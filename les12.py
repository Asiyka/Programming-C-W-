from tkinter import *
import json

def  jsonAction(event):
    file=open("json.json","a")
    file.write(str(pole.get()) +" \n")
    file.close()

icon = Tk()

pole = Entry(bg="pink", width=50)
json = Button(text="json", bg="lightblue", width=30, height=2)

json.bind('<Button-1>', jsonAction)

pole.pack()
json.pack()

pole.mainloop()
