import shelve
from tkinter import *
from tkinter import messagebox

def zapisz(parent):
    sh = shelve.open(parent.variable.get())
    sh[newKey.get()] = newValue.get()
    newKey.delete(0, 'end')
    newValue.delete(0, 'end')
    sh.sync()
    sh.close()