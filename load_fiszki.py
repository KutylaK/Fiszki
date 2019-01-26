import shelve
import random

def readKey(n):
    polka = shelve.open(n)    
    a = random.choice(list(polka.keys()))    
    polka.close()
    return a
def readValue(n, s):
    polka = shelve.open(n)
    a = polka[s]
    polka.close()
    return a



