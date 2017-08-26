#!c:\python34\python.exe

from random import *
from tkinter import *
import time

tk = Tk()

tk.title("Game")

tk.resizable(0, 1)

tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=500)

x3 = 5

y3 = 5

x4 = 5

y4 = 15

x5 = 13

y5 = 10

pos1 = [x3, y3]

pos2 = [x4, y4]

pos3 = [x5, y5]


tri=canvas.create_polygon(x3, y3, x4, y4, x5, y5)




tk.update()

canvas.pack()

def coords():
    pass