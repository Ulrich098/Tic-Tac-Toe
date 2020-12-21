from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic Tac Toe')


def checker(buttons):
	pass
	


        
        
button1 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button1))
button1.grid(row=1, column=0)

button2 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button2))
button2.grid(row=1, column=1)

button3 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button3))
button3.grid(row=1, column=2)

button4 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button4))
button4.grid(row=2, column=0)

button5 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button5))
button5.grid(row=2, column=1)

button6 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button6))
button6.grid(row=2, column=2)

button7 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button7))
button7.grid(row=3, column=0)

button8 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button8))
button8.grid(row=3, column=1)

button9 = Button(tk,text=' ', font=('Times 26 bold'), height = 4, width =8, command=lambda:checker(button9))
button9.grid(row=3, column=2)

button10 = Button(tk,text='Clear', font=('Times 26 bold'), height = 2, width =8, command=lambda:clear())
button10.grid(row=4, columnspan=3)

tk.mainloop()
