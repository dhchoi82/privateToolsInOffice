#!/c/Users/TG/Anaconda3/python

from tkinter import Tk, Button, StringVar, LEFT

def add():
    num = int(count.get())
    num += 1
    count.set(str(num))

def reset():
    num = int(count.get())
    num = 0
    count.set(str(num))

root = Tk()
count = StringVar()
count.set("0")

addBtn = Button(root,textvariable=count,command=add, padx = 50)
addBtn.pack(side=LEFT)

resetBtn = Button(root,text="reset",command=reset)
resetBtn.pack(side=LEFT)

root.mainloop()
