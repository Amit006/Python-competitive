from Tkinter import *
from Test import Test
import mysql.connector
def dinsert():
    db  = mysql.connector.connect(host='localhost',
        password='',port='3306',user='root',
                    database='bist_python')
    s = "insert into student (name, course,fees) values('"+sname.get()+"','"+course.get()+"','"+ fees.get()+"');"
    c = db.cursor()
    c.execute(s)
    c.close()
    db.commit()
    db.close()
    sname.set("")   
    messagebox.showinfo("Python", "Data inserted successfully")
def NewFile():
    t=Test()
    t.getGui()
def OpenFile():
    name = askopenfilename()
    print( name)
def About():
    #print ("This is a simple example of a menu")
    lbl_heading=Label(root,text="NEW STUDENT ENTRY", fg="red")
    lbl_name=Label(root,text="Enter Name:")
    lbl_course=Label(root,text="Course Name:")
    lbl_fees=Label(root,text="Enter Fees:")
    
    global nm,crs,fs
    nm=Entry(root,width=25,textvariable=sname)
    crs=Entry(root,width=25,textvariable=course)
    fs=Entry(root,width=25,textvariable=fees)
    button1=Button(root,text="INSERT",width=15, command=dinsert)

    lbl_heading.grid(column=2,row=1,columnspan=5)
    lbl_name.grid(column=1,row=4)
    nm.grid(column=2,row=4)
    lbl_course.grid(column=3,row=4)
    crs.grid(column=4,row=4)
    lbl_fees.grid(column=1,row=5)
    fs.grid(column=2,row=5)
    button1.grid(column=2,row=10)
def About2():
    #print ("This is a simple example of a menu")
    lbl_heading=Label(root,text="NEW STUDENT ENTRY2", fg="red")
    lbl_name=Label(root,text="Enter Name2:")
    lbl_course=Label(root,text="Course Name2:")
    lbl_fees=Label(root,text="Enter Fees2:")
    
    global nm,crs,fs
    nm=Entry(root,width=25,textvariable=sname)
    crs=Entry(root,width=25,textvariable=course)
    fs=Entry(root,width=25,textvariable=fees)
    button1=Button(root,text="INSERT",width=15, command=dinsert)

    lbl_heading.grid(column=2,row=1,columnspan=5)
    lbl_name.grid(column=1,row=4)
    nm.grid(column=2,row=4)
    lbl_course.grid(column=3,row=4)
    crs.grid(column=4,row=4)
    lbl_fees.grid(column=1,row=5)
    fs.grid(column=2,row=5)
    button1.grid(column=2,row=10)    
 
root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Students", menu=filemenu)
filemenu.add_command(label="New Entry", command=About2)
filemenu.add_command(label="Update...", command=NewFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
sname=StringVar()
course=StringVar()
fees=StringVar()  
mainloop()
