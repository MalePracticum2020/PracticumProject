from tkinter import *

class Auditd:

    def __init__(self,parent=None):
        th = Label(text = 'Auditd',font=("Helvetica", 15),anchor = 'w',bg="pink",fg="white")
        th.pack(side=TOP,anchor = NW,fill=X)
        one = Label(root,bg="pink",fg="white",width=100,height=10)
#        one.place(anchor=NW,x=0,y=0)
        one.pack(fill=BOTH,expand=True)

root = Tk()
t = Auditd(root)
root.mainloop()
