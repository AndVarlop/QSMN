from tkinter import font, messagebox
from tkinter import *
import random

def obvio():
    messagebox.showinfo(message="Lo Sabia", title="")

def Button_hover(event):
    x1 = random.randint(10,400)
    y1 = random.randint(10, 400)
    no.place(x=x1, y=y1)
    
def exit_(event):
    x1 = random.randint(10,400)
    y1 = random.randint(10, 400)
    no.place(x=x1, y=y1)

root=Tk()
root.geometry('600x400')
root.iconbitmap('icono.ico')
#root.configure(background='#D29BFD')
root.configure(background='#D29BFD')
root.title('Respondeme :3')

Label_0 = Label(root, text='¿Quieres ser mi novia?', bg='#D29BFD', fg='black', width=0, font=("BubbleGum", 30))
Label_0.place(x=90, y=60)

yes = Button(root, text="SI", width=5, height=1, font=("BubbleGum", 30), bg='#FF4141', fg='#D29BFD', command=obvio)
yes.place(x=100, y=220)

no = Button(root, text="NO", width=5, height=1, font=("BubbleGum", 30), bg='#FF4141', fg='#D29BFD')
no.place(x=350, y=220)

no.bind("<Enter>", Button_hover)
no.bind("<Leave>", exit_)

root.mainloop()

