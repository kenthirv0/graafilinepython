# K.Hirv
# Tkinter KT
# 17.01.23

from tkinter import *
import time

list=[]
def alarm():
    alarm_count = int(e1.get())
    i = 0
    while i < alarm_count:
        list.append("Tõuse ja sära!\n")
        vahe=""
        lause=vahe.join(list)
        l2.config(text=lause)
        i += 1
    
root = Tk()
root.geometry("300x200")
root.title("Alarm")

l1 = Label(root, text="Mitu korda äratada:")
l1.grid(row=0, column=0)

e1 = Entry(root)
e1.grid(row=0, column=1)

b1 = Button(root, text="Ärata", command=alarm)
b1.grid(row=1, column=0, columnspan=2)

l2 = Label(root, text="")
l2.grid(row=2, column=0, columnspan=2)

list.clear()

root.mainloop()