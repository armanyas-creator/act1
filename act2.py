from tkinter import *
from datetime import date

window=Tk()
window.title("demo window")
window.geometry('400x300')
lbl=Label(text="hey there!",fg="white",bg="#074EA4",height=1,width=300)
name_lbl=Label(text="Full name",bg="#3895D3")

def display():
    name=name_entry.get()
    global message
    message="Welcome to the app /ndate today: "
    greet="hello"+name+"/n"

    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(height=3)

btn=Button(text="Begin",command=display,height=1,bg="#1261A0",fg="white")

name_entry=Entry()
name_entry.pack()
lbl.pack()
name_lbl.pack()
btn.pack()
text_box.pack()

window.mainloop()

