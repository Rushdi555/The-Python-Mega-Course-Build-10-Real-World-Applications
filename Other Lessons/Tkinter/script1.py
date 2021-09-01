from tkinter import *

window=Tk()

def from_kg():
    print(e2_value.get())
    gram = float(e2_value.get())*1000
    ounce = float(e2_value.get())*35.274
    pounds = float(e2_value.get())*2.20462
    t1.delete("1.0", END)
    t1.insert(END, gram)
    t2.delete("1.0", END)
    t2.insert(END, ounce)
    t3.delete("1.0", END)
    t3.insert(END, pounds)


e1=Label(window,text="Kg")
e1.grid(row=0,column=0)

e2_value=StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

b1 = Button(window, text="Convert", command=from_kg)
b1.grid(row=0, column=2)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)


window.mainloop()