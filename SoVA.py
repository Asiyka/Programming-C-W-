from tkinter import *

LIST=["Asiyka","Asiyka","Угорь","Asiyka","Asiyka","Asiyka","Угорь","Asiyka","Asiyka","Asiyka","Угорь","Asiyka","Asiyka"]

root = Tk()
var=IntVar()
variable = StringVar()
variable.set(LIST[0])

toolbox = Frame(root,bg="#F0ACFF",bd=2,height=120)
toolbox.pack(side=TOP,fill=X)

hardskill = Frame(root,bg="#FFFAEB",bd=2,height=100,width=100)
hardskill.pack(side=LEFT,ipady=140,ipadx=40,pady=10)

softskill = Frame(root,bg="#FFFAEB",bd=2,height=100,width=100)
softskill.pack(side=LEFT,ipady=140,ipadx=55,padx=25,pady=10)

eng = Frame(root,bg="#FFFAEB",bd=2,height=100,width=100)
eng.pack(side=RIGHT,ipady=140,ipadx=50,pady=10)

menu=OptionMenu(hardskill,variable,*LIST)
    
rbutton1=Radiobutton(hardskill,text='ТАК',variable=var,value=1,bg="#FFFAEB")
rbutton2=Radiobutton(hardskill,text='НІ',variable=var,value=2,bg="#FFFAEB")

prog = Label(hardskill,width=15,bg="#FFFAEB",fg="black",text="PROGRAMMING")
prog.pack()
pr = Label(hardskill,bg="#FFFAEB",fg="black",text="ПРИСУТНІСТЬ")
pr.place(x=50,y=70)
dz = Label(hardskill,bg="#FFFAEB",fg="black",text="ДОМАШНЄ ЗАВДАННЯ")
dz.place(x=25,y=130)
dzpoint = Entry(hardskill,width=20)
dzpoint.place(x=30,y=160)
cw = Label(hardskill,bg="#FFFAEB",fg="black",text="УРОК")
cw.place(x=70,y=190)
cwpoint = Entry(hardskill,width=20)
cwpoint.place(x=30,y=220)
send = Button(hardskill,width=20, bg="grey", text="Send")
send.place(x=20,y=265)

menu.pack(padx=1,pady=10,side=TOP)
rbutton1.place(x=40,y=100)
rbutton2.place(x=100,y=100)

root.title("SoVA")
root["bg"] = "black"
photo = PhotoImage(file = "fly.png")
root.iconphoto(False, photo)
root.geometry("650x450")
root.resizable(False,False)
root.mainloop()
