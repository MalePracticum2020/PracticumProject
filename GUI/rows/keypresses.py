from tkinter import *

class Keypresses:

    def __init__(self,parent=None):
        th = Label(text = 'Keypresses',font=("Helvetica", 15),anchor = 'w',bg="green",fg="white")
        th.pack(side=TOP,anchor = NW,fill=X)
        one = Label(root,bg="green",fg="white",width=100,height=10)
#        one.place(anchor=NW,x=0,y=0)
        one.pack(fill=BOTH,expand=True)

root = Tk()
t = Keypresses(root)
root.mainloop()
