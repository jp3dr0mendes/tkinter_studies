from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.filedialog

def test_function():
    print('Hello World!')

def change_cont():
    text_cont["text"]+=1
root = Tk()
frm = ttk.Frame(root,padding=100)
frm.grid()

text_cont=Label(frm,text=0)
text_cont.grid(column=0,row=2)

# photo = Tk.PhotoImage(file=r"C:\Users\joaop\Documents\PDF_auto\Imagens\Image13.png")
photo = PhotoImage(file=r"C:\Users\joaop\Documents\PDF_auto\Imagens\Image13.png")

ttk.Label(frm, text="Hello World!").grid(column=0,row=0)
ttk.Button(frm, text='Increment',command=change_cont).grid(column=0,row=1)
ttk.Button(frm, text='Quit', command=root.destroy).grid(column=0, row=3)

#gerando uma imagem na janela
ttk.Label(frm,image=photo).grid(column=0,row=4)
# PhotoImage(frm, file=r"C:\Users\joaop\Documents\PDF_auto\Imagens\Image13.png")

#rodando o código na janela
root.mainloop()