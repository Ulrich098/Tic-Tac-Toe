from tkinter import *
import tkinter.messagebox as tmsg
import os
import time

root=Tk()
canvas_width=400
canvas_height=400
root.geometry(f'{canvas_width}x{canvas_height}')
root.maxsize(canvas_width,canvas_height)
root.minsize(canvas_width,canvas_height)
root.title('Calculator ')
root.call('wm', 'iconphoto', root._w, PhotoImage(file='logo.png'))

root.mainloop()
