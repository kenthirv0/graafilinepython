# K.Hirv
# 11.01.23
# tkinter4


from tkinter import *
import time

#akna seaded
aken = Tk()
aken.title('Lipp')
aken.iconbitmap('favicon.ico')

#lõuendi loomine
louend = Canvas(aken, width=500, height=300)
louend.pack()

#kujundite loomine
louend.create_rectangle(0, 0, 500, 150,fill="white")
louend.create_rectangle(0, 150, 500, 300,fill="red")
louend.create_polygon(0, 0, 200, 150, 0, 300,fill="blue")

aken.mainloop()