'''
Created on 02.11.2017

@author: Nico
'''
'''
imports
'''
from tkinter import *
import random
from numpy.f2py.crackfortran import charselector

'''
window
'''
root = Tk()
root.title("CharGen")

'''
window dimension
'''
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 2)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 40, padx = 50)

GENDER = IntVar()
RACE = IntVar()
HAIRCOLOR = StringVar()
EYECOLOR = StringVar()
HAIRSTYLE = StringVar()
BEARD = StringVar()

choices = {'dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human'}
RACE.set('human') #default option

'''
dropdown race selection
'''
popupMenu = OptionMenu(mainframe, RACE, *choices)
Label(mainframe, text="Choose Race").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

'''
radiobuttons for gender selection
'''
w1 = Label(root, 
      text="""Choose a gender:""",
      justify = LEFT,
      padx = 0).pack()

Radiobutton(root, 
            text="male",
            padx = 20, 
            variable=GENDER, 
            value=1).pack(anchor=W)
Radiobutton(root, 
            text="female",
            padx = 20, 
            variable=GENDER, 
            value=2).pack(anchor=W)


'''
textbox
'''
T = Text(root, height=6, width=30)  # darin soll die Ausgabe erscheinen
T.pack()

'''
lists
'''
if GENDER == "male":
    if RACE == "dwarf":
        HAIRCOLOR = ["black", "brown", "gray", "red", "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown","green", "blue-green",
                    "blue-grey", "grey"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["full beard", "goatee", "braided beard",
                 "full beard", "braided beard"]
        
    if RACE == "elf":
        HAIRCOLOR = ["green", "green-blonde", "blonde", "brown", "gray",
                     "red", "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-gray", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "golden", "silver"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard",
                 "no beard", "no beard", "no beard", "no beard", "no beard",
                 "no beard", "no beard", "no beard", "no beard"]
        
    if RACE == "gnome":
        HAIRCOLOR = ["green", "red", "blue", "orange", "purple", "white",
                     "silver", "pink", "green", "red", "blue", "orange",
                     "purple", "white", "silver", "pink", "blonde",
                     "black", "brown"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet", "red", "golden", "silver"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard",]
        
    if RACE == "half-elf":
        HAIRCOLOR = ["green-blonde", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-gray", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "blue", "brown",
                    "green", "blue-green", "heterochrome", "blue-gray",
                    "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet",]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head",
                     "wild hair", "short hair", "sidecut", "long hair",
                     "shaved head", "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard",
                 "stubble", "mustache", "full beard", "goatee",
                 "chin beard", "braided beard", "shaved"]
        
    if RACE == "halfling":
        HAIRCOLOR = ["black", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]
        
    if RACE == "half-orc":
        HAIRCOLOR = ["black", "brown", "gray", "red", "auburn"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown", "green", "blue-green",
                    "blue-grey", "red"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]
        
    if RACE == "human":
        HAIRCOLOR = ["black", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]

elif GENDER == "female":
    if RACE == "dwarf":
        HAIRCOLOR = ["black", "brown", "gray", "red", "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown", "green", "blue-green",
                    "blue-grey", "grey"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = ["full beard", "goatee", "braided beard", "braided beard",
                 "braided beard", "fullbeard", "fullbeard", "goatee",
                 "braided beard", "braided beard", "braided beard",
                 "fullbeard", "shaved"]
        
    if RACE == "elf":
        HAIRCOLOR = ["green", "green-blonde", "blonde", "brown", "gray",
                     "red", "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown","green", "blue-green",
                    "heterochrome", "blue-gray", "blue", "brown","green",
                    "blue-green", "blue-grey", "violet", "golden", "silver"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "gnome":
        HAIRCOLOR = ["green", "red", "blue", "orange", "purple", "white",
                     "silver", "pink", "green", "red", "blue", "orange",
                     "purple", "white", "silver", "pink", "blonde",
                     "black", "brown"]
        
        EYECOLOR = ["blue", "brown","green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown","green", "blue-green",
                    "blue-grey", "violet", "red", "golden", "silver"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "half-elf":
        HAIRCOLOR = ["green-blonde", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown","green", "blue-green",
                    "heterochrome", "blue-gray", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "blue", "brown",
                    "green", "blue-green", "heterochrome", "blue-gray",
                    "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet",
                    "heterochrome"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "halfling":
        HAIRCOLOR = ["black", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown","green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown","green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "half-orc":
        HAIRCOLOR = ["black", "brown", "gray", "red", "auburn"]
        
        EYECOLOR = ["blue", "brown","green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown","green", "blue-green",
                    "blue-grey", "red"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "human":
        HAIRCOLOR = ["black", "blonde", "brown", "gray", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown","green", "blue-green", "heterochrome",
                    "blue-gray", "blue", "brown","green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        

class Appearance: #function
    '''
    classdocs
    '''
    gender = []
    race = []
    haircolor = []
    eyecolor = []
    hairstyle = []
    beard = []

    def __init__(self, gender, race, haircolor, eyecolor, hairstyle, beard):
        '''
        Constructor
        '''
        self.gender = gender
        self.race = race
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.hairstyle = hairstyle
        self.beard = beard
        
    def generate(self):
        
        '''
        Generating character appearance
        '''
        '''
        if GENDER == "male":
            print("male")
        else:
            print("female")
        print(self.race)
        print(random.choice(self.haircolor) + " hair")
        print(random.choice(self.eyecolor) + " eyes")
        print(random.choice(self.hairstyle))
        print(random.choice(self.beard))
        '''
        if GENDER == "male":
            T.insert("male")
        else:
            T.insert("female")
        T.insert(self.race)
        T.insert(random.choice(self.haircolor) + " hair")
        T.insert(random.choice(self.eyecolor) + " eyes")
        T.insert(random.choice(self.hairstyle))
        T.insert(random.choice(self.beard))
        

'''
Buttons
'''
Button(text ='Generate', command = lambda: Appearance(GENDER, RACE, HAIRCOLOR, EYECOLOR, HAIRSTYLE, BEARD).generate()).pack(fill=X)
Button(text ='Quit', command = quit).pack(fill=X)
T.insert
name = StringVar()

mainloop()