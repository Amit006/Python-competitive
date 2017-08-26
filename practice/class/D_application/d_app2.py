# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 10:55:13 2017

@author: Amit
"""

from  tkinter import *
from tkinter import messagebox


def Printit():
    messagebox.showinfo("a",radiovar.get())
    #print("printing the textbox value ")
    #name.delete(0,END)
    #name.insert(0,"you just click oky button")
def ReadRadioButton():
    value = radiovar.get()
    print(value)
    
root = Tk()
root.title("grab the radio button")
root.geometry("600x500+10+10")
radiovar = StringVar()
ok = Button(root, text ="okey",command=Printit, width=15)
cancel = Button(root,text="Cancel", command=root.destroy , width = 15)

lbl1 = Label(root,text="we practice txtBox Example",fg="black",bg="red")
namelb1 =Label(root, text = "name")

name = Entry(root, width=35, textvariable=radiovar)
name.insert(0,"Enter the name")
#defining redio button
radio1 = Radiobutton(root,text = "no 1 Choice",variable =radiovar, value = '1', command = ReadRadioButton)
radio2 = Radiobutton(root, text = "no 2 Choice", variable =radiovar,  value = "2", command = ReadRadioButton)
radio3 = Radiobutton(root, text= "no 3 Choice" , variable = radiovar, value = "3", command = ReadRadioButton)
#content.grid9column=0,row=0)
#gredig starts from here

lbl1.grid(column = 0, row = 1, columnspan=2)
ok.grid(column=1,row=2)
cancel.grid(column = 2, row = 2)
namelb1.grid(column =1, row = 3)
name.grid(column=2,row=3,columnspan=2)
#radio button grid
radio1.grid(column=3, row=3)
radio2.grid(column=3, row=4)
radio3.grid(column=3, row=5)
root.mainloop()
