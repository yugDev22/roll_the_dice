from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import random

main=Tk()
main.title('Roll The Dice')
main.geometry('430x450+50+40')
i1=ImageTk.PhotoImage(Image.open('dice1.png'))
i2=ImageTk.PhotoImage(Image.open('dice2.png'))
i3=ImageTk.PhotoImage(Image.open('dice3.png'))
i4=ImageTk.PhotoImage(Image.open('dice4.png'))
i5=ImageTk.PhotoImage(Image.open('dice5.png'))
i6=ImageTk.PhotoImage(Image.open('dice6.png'))
none=ImageTk.PhotoImage(Image.open('none.png'))
dicelb=Label(main)
toplb=Label(main,text='Roll the DICE',fg='white',bg='navy',font='none 16 bold').pack()
def close():
    m=messagebox.askyesno(title='EXIT',message='Are you sure to exit')
    if m==1:
        main.destroy()
def roll():
    r=random.randint(1,6)
    if r==1:
        dicelb.configure(image=i1)
        dicelb.pack()
    elif r==2:
        dicelb.configure(image=i2)
        dicelb.pack()
    elif r==3:
        dicelb.configure(image=i3)
        dicelb.pack()
    elif r==4:
        dicelb.configure(image=i4)
        dicelb.pack()
    elif r==5:
        dicelb.configure(image=i5)
        dicelb.pack()
    elif r==6:
        dicelb.configure(image=i6)
        dicelb.pack()
def reset():
    dicelb.configure(image=none)
    dicelb.pack()
bt=Button(text='Roll DICE',command=roll,fg='navy',font='none 12 bold').place(x=160,y=360)
clbt=Button(main,text='Exit',command=close).place(x=170,y=400)
resetbt=Button(main,text='Reset',command=reset).place(x=200,y=400)

main.mainloop()
