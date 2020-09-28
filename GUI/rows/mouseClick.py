from tkinter import *

class MouseClick:

    def __init__(self,parent=None):
        th = Label(text = 'MouseClick',font=("Helvetica", 15),anchor = 'w',bg="purple",fg="white")
        th.pack(side=TOP,anchor = NW,fill=X)
        one = Label(root,bg="purple",fg="white",width=100,height=10)
#        one.place(anchor=NW,x=0,y=0)
        one.pack(fill=BOTH,expand=True)

root = Tk()
t = MouseClick(root)
root.mainloop()
