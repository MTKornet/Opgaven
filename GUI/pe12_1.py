import math
from tkinter import *

def clicked1():
    grondtal=int(entry.get())
    kwadraat=grondtal**2
    tekst='Kwadraat: van {} = {}'
    label['text'] = tekst.format(grondtal, kwadraat)

def clicked2():
    grondtal = int(entry.get())
    wortel = math.sqrt(grondtal)
    tekst = 'Wortel: van {} = {}'
    label['text'] = tekst.format(grondtal, wortel)

root=Tk()

label=Label(master=root,
            text='Hello World',
            background='yellow',
            foreground='blue',
            font=('Helvetica',16,'bold italic'),
            height=3)
label.pack()

button1=Button(master=root,
              text='Kwadraat',
              command=clicked1)
button1.pack(side=LEFT, pady=10)

button2=Button(master=root,
              text='Wortel',
              command=clicked2)
button2.pack(side=RIGHT, pady=10)

entry=Entry(master=root)
entry.pack(padx=10, pady=10)

root.mainloop()