from tkinter import *

def create(parent):
    o=Tk(parent)
    o.title("Dodaj kategorie")
    o.geometry("400x240")
    r=Frame(o)
    r.grid()

    l = Label(o)
    l["text"]="Podaj nazwę nowej kategorii"
    l.grid(row=3,column=1)

    uI = Entry(o)
    uI.grid(row=4,column=1)

    addCategoryButton = Button(o,text="Dodaj",)
    addCategoryButton.grid(row=6,column=1)
