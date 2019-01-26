from tkinter import *
from tkinter import messagebox
import shelve


def zapisz():
    sh = shelve.open(variable.get())
    if(newKey.get() in sh.keys()):
        messagebox.showinfo("Niestety", "Podane slowo jest juz w tej katergorii fiszek")
        return
    if(newKey.get()=="" or newValue.get()==""):
        messagebox.showinfo("Niestety", "Nie mozna wprowadzac pustych wartosci")
        return
    sh[newKey.get()] = newValue.get()
    newKey.delete(0, 'end')
    newValue.delete(0, 'end')
    sh.sync()
    sh.close()

def create(parent):
    o=Tk(parent)
    o.title("Dodaj fiszke")
    o.geometry("400x240")
    r=Frame(o)
    r.grid()

    label = Label(o)
    label["text"]="Wybierz kategorie"
    label.grid(row=0,column=0,sticky=W)

    global variable
    variable = StringVar(o)
    
    w = OptionMenu(o, variable, "one", "two", "three")
    w.grid(row=1,column=0)

    global newKey
    newKey = Entry(o)
    newKey.grid(row=1,column=3)

    global newValue
    newValue = Entry(o)
    newValue.grid(row=2,column=3)

    addCategoryButton = Button(o,text="Dodaj")
    addCategoryButton.grid(row=6,column=1)
    addCategoryButton["command"] = zapisz
    


