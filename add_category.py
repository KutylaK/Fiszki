from tkinter import *
import shelve
import load_fiszki as loadFiszki
from tkinter import messagebox


def zapiszk():
    if(uI.get() in loadFiszki.getCategories()):
        messagebox.showinfo("Niestety", "Podana kategoria juz istnieje")
        return
    sh = shelve.open(uI.get())   
    uI.delete(0, 'end')
    sh.sync()
    sh.close()
    
    
def create(parent):
    o=Tk(parent)
    o.title("Dodaj kategorie")
    o.geometry("400x240")
    r=Frame(o)
    r.grid()


    l = Label(o)
    l["text"]="Podaj nazwę nowej kategorii"
    l.grid(row=3,column=1)

    global uI
    uI = Entry(o)
    uI.grid(row=4,column=1)

    addCategoryButton = Button(o,text="Dodaj",)
    addCategoryButton.grid(row=6,column=1)
    addCategoryButton["command"] = zapiszk
