from tkinter import *
import json

def register(event):
    file=open("users.json","w")
    file.write(username,password)
    file.close()

def login(event):
    file=open("users.json","r")
    for user in json.loads((users.json).content):
        if username == user['username']:
            if password == user['password']:
                message = 'You login'
                break
            else:
                message = 'Not correct password'
                break
            print(message)
    file.close()

root=Tk()

reg_username = Entry(bg="pink", width=50)
reg_password = Entry(bg="lightyellow", width=50)
regist = Button(text="/",bg="orange", width=30, height=2)
log_username = Entry(bg="pink", width=50)
log_password = Entry(bg="lightyellow", width=50)
log = Button(text="*",bg="yellow", width=30, height=2)
l = Label(bg='red', fg='black', width=40,height=5)

root.mainloop()
