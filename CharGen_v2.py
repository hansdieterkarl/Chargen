'''
Created on 25.10.2017

@author: Nico
'''
import random
'''
Lists
'''
GENDER = input("Put in your gender (female or male): ")
RACE = input("Put in your race: ")
if GENDER == "male":
    if RACE == "dwarf":
        HAIRCOLOR = ["black", "brown", "grey", "red", "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "grey"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["full beard", "goatee", "braided beard",
                 "full beard", "braided beard"]
        
    if RACE == "elf":
        HAIRCOLOR = ["green", "green-blonde", "blonde", "brown", "grey",
                     "red", "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-grey", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "golden", "silver"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard",
                 "no beard", "no beard", "no beard", "no beard", "no beard",
                 "no beard", "no beard", "no beard", "no beard", "mustache"]
        
    if RACE == "gnome":
        HAIRCOLOR = ["green", "red", "blue", "orange", "purple", "white",
                     "silver", "pink", "green", "red", "blue", "orange",
                     "purple", "white", "silver", "pink", "blonde",
                     "black", "brown"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet", "red", "golden", "silver"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard", "mustache", "mustache"]
        
    if RACE == "half-elf":
        HAIRCOLOR = ["green-blonde", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-grey", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "blue", "brown",
                    "green", "blue-green", "heterochrome", "blue-grey",
                    "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet",]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head",
                     "wild hair", "short hair", "sidecut", "long hair",
                     "shaved head", "wild hair", "short hair"]
        
        BEARD = ["braided beard", "no beard", "no beard", "no beard",
                 "stubble", "mustache", "full beard", "goatee",
                 "chin beard", "braided beard", "shaved"]
        
    if RACE == "halfling":
        HAIRCOLOR = ["black", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]
        
    if RACE == "half-orc":
        HAIRCOLOR = ["black", "brown", "grey", "red", "auburn"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "red"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]
        
    if RACE == "human":
        HAIRCOLOR = ["black", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["balding head", "long hair", "shaved head", "wild hair",
                     "short hair", "sidecut", "long hair", "shaved head",
                     "wild hair", "short hair"]
        
        BEARD = ["stubble", "mustache", "full beard", "goatee", "chin beard",
                 "braided beard", "shaved"]

elif GENDER == "female":
    if RACE == "dwarf":
        HAIRCOLOR = ["black", "brown", "grey", "red", "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
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
        HAIRCOLOR = ["green", "green-blonde", "blonde", "brown", "grey",
                     "red", "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-grey", "blue", "brown", "green",
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
                    "blue-grey", "blue", "brown","green", "blue-green",
                    "blue-grey", "violet", "red", "golden", "silver"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "half-elf":
        HAIRCOLOR = ["green-blonde", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["silver", "blue", "brown", "green", "blue-green",
                    "heterochrome", "blue-grey", "blue", "brown", "green",
                    "blue-green", "blue-grey", "violet", "blue", "brown",
                    "green", "blue-green", "heterochrome", "blue-grey",
                    "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet", "heterochrome"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "halfling":
        HAIRCOLOR = ["black", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "half-orc":
        HAIRCOLOR = ["black", "brown", "grey", "red", "auburn"]
        
        EYECOLOR = ["blue", "brown","green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "red"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
    if RACE == "human":
        HAIRCOLOR = ["black", "blonde", "brown", "grey", "red",
                     "auburn", "white"]
        
        EYECOLOR = ["blue", "brown", "green", "blue-green", "heterochrome",
                    "blue-grey", "blue", "brown", "green", "blue-green",
                    "blue-grey", "violet"]
        
        HAIRSTYLE = ["braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "braided hair", "long hair", "short hair", "wild hair",
                     "sidecut", "sidecut", "shaved"]
        
        BEARD = [""]
        
else:
    print("Next time, please put in male or female as a gender")

class Appearance:
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
        if GENDER == "male":
            print("male")
        else:
            print("female")
        print(self.race)
        print(random.choice(self.haircolor) + " hair")
        print(random.choice(self.eyecolor) + " eyes")
        print(random.choice(self.hairstyle))
        print(random.choice(self.beard))
        
Appearance(GENDER, RACE, HAIRCOLOR, EYECOLOR, HAIRSTYLE, BEARD).generate()