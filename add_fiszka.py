from tkinter import *

def create(parent):
    o=Tk(parent)
    o.title("Dodaj fiszke")
    o.geometry("400x240")
    r=Frame(o)
    r.grid()

    label = Label(o)
    label["text"]="Wybierz kategorie"
    label.grid(row=0,column=0,sticky=W)

    variable = StringVar(o)
    
    w = OptionMenu(o, variable, "one", "two", "three")
    w.grid(row=1,column=0)

    newKey = Entry(o)
    newKey.grid(row=1,column=3)

    newValue = Entry(o)
    newValue.grid(row=2,column=3)



    addCategoryButton = Button(o,text="Dodaj",)
    addCategoryButton.grid(row=6,column=1)
