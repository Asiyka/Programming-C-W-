from tkinter import *
import json

def read():
    file = open("phones.json", "r")
    file_text = file.read()
    file.close()
    return file_text

def write(data):
    file = open("phones.json", "w")
    file.write(json.dumps(data))
    file.close()

phone_list = {"items" : {}, }

file_text = read()

if file_text == "":
    write(phone_list)

def shearch_func(event):
    item = json.loads(read())["items"]
    try:
        label['text'] = item[shearch_name.get()]
    except KeyError:
        label['text'] = "NotFound"
        
        
    
def save_func(event):
    items = read()
    items = json.loads(items)
    username = name.get()
    phone = phone_number.get()
    items['items'][username] = phone
    write(items)
    label['text'] = "Saved"
    name.pack_forget()
    phone_number.pack_forget()
    save.pack_forget()

def watch_func(event):
    all_phones = read()
    all_phones = json.loads(all_phones)['items']
    str = ""
    for name in all_phones:
        str += "\n" + name + " : " + all_phones[name] + "\n" 
    label['text'] = str

def add_two_func(event):
    name.pack()
    phone_number.pack()
    save.pack()
    

root = Tk()
shearch_name = Entry(width=30 , text="Shearch")
phone_number = Entry(width=30)
name = Entry(width=30)
add_new_two = Button(width=40, bg="lightpink", text="AddNew")
shearch = Button(width=40, bg="lightpink", text="Shearch")
save = Button(width=40, bg="lightblue", text="Save")
watch = Button(width=40, bg="lightgreen", text="Watch all phones")
phone_number_two = Entry(width=30 , text="Shearch")
label = Label(width=40, bg="white", fg="black")

add_new_two.bind("<Button-1>", add_two_func)
shearch.bind("<Button-1>", shearch_func)
save.bind("<Button-1>", save_func)
watch.bind("<Button-1>", watch_func)

shearch_name.pack()
shearch.pack()
add_new_two.pack()
watch.pack()
label.pack()



root.mainloop()
