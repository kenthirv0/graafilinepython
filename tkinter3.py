# K.Hirv
# 11.01.23
# tkinter3

from tkinter import *
from tkinter import ttk


def arvuta():
    hind = float(sisestus.get())
    kmaks = var.get()
    arvutus = hind*kmaks
    tekst2.config(text=arvutus)
    arvutus2 = hind+arvutus
    tekst3.config(text=arvutus2)
    print(arvutus)
    
aken = Tk()
aken.resizable(0, 0)
aken.title("KM kalkulaator")
aken.geometry("300x300")


#sisestusväljad
sisestus = Entry(aken)
sisestus.grid(row=1, column=1)

tekst = Label(aken,
              text="Hind käibemaksuta:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=1, column=0, columnspan=1)

tekst.grid(row=1,column=0)


tekst = Label(aken,
              text="Käibemaksumäär:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=2, column=0, columnspan=1)


#valikukast
var = DoubleVar()
valikukast = Radiobutton(aken,text="9%", variable=var, value=0.09)
valikukast.grid(row=3, column=1)
valikukast = Radiobutton(aken,text="20%", variable=var, value=0.2)
valikukast.grid(row=4, column=1)

joon = Label(aken,
              text="__________________________",
              font="Tahoma 12",
              padx=2,
              pady=2)
joon.grid(row=5, column=0, columnspan=2)

tekst = Label(aken,
              text="Käibemaks:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=6, column=0, sticky="w")

tekst2 = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst2.grid(row=6, column=1, columnspan=3)


tekst = Label(aken,
              text="Hind Käibemksuga:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=7, column=0, sticky="w")

tekst3 = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst3.grid(row=7, column=1, columnspan=3)

nupp1 = Button(aken, text="Arvuta", width=10, command=arvuta)
nupp1.grid(row=8, column=1)


aken.mainloop()



