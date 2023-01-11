# K.Hirv
# 10.01.23
# tkinter 1

from tkinter import *

aken = Tk()
aken.title('Kent Hirv')
aken.configure(background='black')
aken.iconbitmap('favicon.ico')
aken.geometry("")
aken.resizable(0,0)
Label(aken, text="Nimi: Kent Hirv", foreground="red", background="black", font="Tahoma 16 bold italic").pack()
Label(aken, text="Rühm: IT22", foreground="red", background="black", font="Tahoma 16 bold italic").pack()
Label(aken, text="2023", foreground="red", background="black", font="Tahoma 16 bold italic").pack()

aken.mainloop()