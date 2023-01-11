# K.Hirv
# 11.01.23
# tkinter3

from tkinter import *



def arvuta():
    hind = sisestus.get()
    print()
    
aken = Tk()
aken.resizable(0, 0)
aken.title("KM kalkulaator")
aken.geometry("600x600")

tekst = Label(aken,
              text="Hind käibemaksuta",
              font="Tahoma 12",
              padx=2,
              pady=2)
aken.option_add('*Font', ('Tahoma', 12))
tekst.grid(row=1, column=0, columnspan=1)

tekst.grid(row=1,column=0)


tekst = Label(aken,
              text="Käibemaksumäär",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=2, column=0, columnspan=1)


#valikukast
var = IntVar()
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
              text="Käibemaks",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=6, column=0,sticky="w")

tekst = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=6, column=1, columnspan=3)


tekst = Label(aken,
              text="Hind Käibemksuga:",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=7, column=0,sticky="w")

tekst = Label(aken,
              text="0.00€",
              font="Tahoma 12",
              padx=2,
              pady=2)
tekst.grid(row=7, column=1, columnspan=3)



aken.mainloop()



