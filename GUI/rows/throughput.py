from tkinter import *

class Throughput:

    def __init__(self,parent=None):
        th = Label(text = 'Throughput',font=("Helvetica", 15),anchor = 'w',bg="blue",fg="white")
        th.pack(side=TOP,anchor = NW,fill=X)
        one = Label(root,bg="blue",fg="white",width=100,height=10)
#        one.place(anchor=NW,x=0,y=0)
        one.pack(fill=BOTH,expand=True)

root = Tk()
t = Throughput(root)
root.mainloop()
