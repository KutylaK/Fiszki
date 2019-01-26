import shelve
import random
import glob

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

def getCategories():
    mylist = [f for f in glob.glob("*.dat")]
    mylist1 = []
    for item in mylist:        
        mylist1.append(item.replace('.dat',''))    
    return mylist1



