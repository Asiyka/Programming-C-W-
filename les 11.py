from tkinter import *

def plusAction(event):
    file = open('new_file.txt', 'a')
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n + s_n)
    file.write(str(f_n + s_n)+ "\n")
    file.close()

def minusAction(event):
    file = open('new_file.txt', 'a')
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n - s_n)
    file.write(str(f_n - s_n)+ "\n")
    file.close()


def divAction(event):
    file = open('new_file.txt', 'a')
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n / s_n)
    file.write(str(f_n / s_n)+ "\n")
    file.close()

def manyAddsAction(event):
    file = open('new_file.txt', 'a')
    f_n = int(first_number.get())
    s_n = int(second_number.get())
    l["text"] = str(f_n * s_n)
    file.write(str(f_n * s_n) + "\n")
    file.close()

root = Tk()

first_number = Entry(bg="pink", width=50)
second_number = Entry(bg="lightyellow", width=50)
plus = Button(text="+", bg="lightblue", width=30, height=2)
minus = Button(text="-", bg="lightgreen", width=30, height=2)
div = Button(text="/",bg="orange", width=30, height=2)
many_adds = Button(text="*",bg="yellow", width=30, height=2)
l = Label(bg='red', fg='black', width=40,height=5)

plus.bind('<Button-1>', plusAction)
minus.bind('<Button-1>', minusAction)
div.bind('<Button-1>', divAction)
many_adds.bind('<Button-1>', manyAddsAction)


first_number.pack()
second_number.pack()
plus.pack()
minus.pack()
div.pack()
many_adds.pack()
l.pack()

root.mainloop()
