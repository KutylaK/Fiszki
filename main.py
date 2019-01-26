from tkinter import *
import shelve, random
import add_category as addCat
import add_fiszka as addFisz
import load_fiszki as loadFisz


def showCorrect(): 
    correct["text"]=loadFisz.readValue(variable.get(), task["text"])
    if (correct["text"] == userInput.get()):        
        userInput.config(bg="#00F000")
    else:
        userInput.config(bg="#F00000")
        

def goNext():
    correct["text"]=""      
    task["text"]=loadFisz.readKey(variable.get())

def add_category():
    addFisz.create("okno")
    #addCat.create("okno")


okno=Tk()
okno.title("Fiszki")
okno.geometry("400x240")
ramka=Frame(okno)
ramka.grid()


label = Label(okno)
label["text"]="Wybierz kategorie"
label.grid(row=0,column=0,sticky=W)

variable = StringVar(okno)


w = OptionMenu(okno, variable, "one", "two", "three")
w.grid(row=1,column=0)




task = Label(okno)
task.grid(row=0,column=3)

userInput = Entry(okno)
userInput.grid(row=1,column=3)

addCategoryButton = Button(text="Dodaj kategorie")
addCategoryButton.grid(row=0,column=5)
addCategoryButton["command"]=add_category


checkButton = Button(text="Sprawdz")
checkButton.grid(row=1,column=5)
checkButton["command"]=showCorrect

correct =  Label(okno)
correct.grid(row =3, column=3)

nextButton = Button(text="Następna fiszka")
nextButton.grid(row=3,column=5)
nextButton["command"]=goNext



mainloop()
