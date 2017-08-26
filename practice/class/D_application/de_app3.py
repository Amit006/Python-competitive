# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 11:46:10 2017

@author: Amit
"""
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:55:13 2017

@author: Amit
"""

from  tkinter import *
from tkinter import messagebox


def Printit():
    messagebox.showinfo("a",FName.get())
    print("printing the textbox value ")

root = Tk()
root.title("NSEC")
root.geometry("600x500")
FName = StringVar()
ok = Button(root, text ="okey",command=Printit, width=15)
cancel = Button(root,text="Cancel", command=root.destroy , width = 15)

lbl1 = Label(root,text="we practice txtBox Example",fg="black",bg="red")
namelb1 = Label(root, text = "name")

name = Entry(root, width=35, textvariable=FName)
name.insert(0,"Enter the name")
#content.grid9column=0,row=0)
#gredig starts from here
lbl1.grid(column = 0, row = 1, columnspan=2)

ok.grid(column=1,row=2)
cancel.grid(column = 2, row = 2)

namelb1.grid(column =1, row = 3)
name.grid(column=2,row=3,columnspan=2)

root.mainloop()
