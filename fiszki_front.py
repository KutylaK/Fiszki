from tkinter import *
okno=Tk()
okno.title("Fiszki")
okno.geometry("600x360")
ramka=Frame(okno)
ramka.grid()
etykieta1=Label(text="Dog")
etykieta1.grid(row=0,column=0,sticky=W)
pole1=Text(width=10,height=1)
pole1.grid(row=1,column=0,sticky=W)
przycisk1=Button(text="Sprawdz",width=10)
przycisk1.grid(row=2,column=0,sticky=W)
przycisk1["command"]=dzielniki
etykieta2=Label(text="Poprawna odpowied¿ to:")
etykieta2.grid(row=3,column=0,sticky=W)
pole2=Text("Pies")
pole2.grid(row=4,column=0,sticky=W)
okno.mainloop()