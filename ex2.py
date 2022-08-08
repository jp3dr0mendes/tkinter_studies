'''
Exemplo para criar um imput na aplicação e resgatar o texto passado pelo usuários
'''

from lib2to3.pgen2.token import LESSEQUAL
from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.filedialog

def say_hi():
    l3["text"] = Entry
    for e in Entry:
        print(Entry)

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

l1 = Label(frm,text='Hello World!').grid(column=0,row=0)
l2 = Label(frm,text='Digite um Texto:').grid(column=0,row=1)
l3 = Label(frm,text="Texto digitado: ")
l3.grid(column=0,row=3)

Entry(frm,bd=5).grid(column=0,row=2)

Button(frm,text="Submit",command=say_hi).grid(column=0,row=4)
Button(frm, text="Exit",command=root.destroy).grid(column=0,row=5)

root.mainloop()