'''
Dwarfs and Elfs


'''
import sys
import time
import random

def typewrite(string,newline=False):
    '''
    Types stuff one letter at a time

    '''
    for i in list(str(string)):
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.04)
    if newline:
        print()
def typewrite_prompt(prompt):
    '''
    Typewrite, but for prompts
    '''

    typewrite(prompt)
    return input()
def y_n_prompt(prompt):
    try:
        if list(typewrite_prompt(prompt))[0].lower()=='y':
            return True
        return False
    except:
        return False
def roll_weighted(things):
    options=[]
    try:
        for i in things:
            for j in range(i[1]):
                options.append(i[0])
        return random.choice(options)
    except:
        return False
def create_creature(type):
    if type=="Dwarf":
        return (random.randint(5,20), # Strength
                random.randint(1,7), # Magic
                random.randint(1,5), # Luck
                random.randint(1,10), # Wisdom
                random.randint(1,15), # Agility
                random.randint(1,6)) # Speed
    if type=="Elf":
        return (random.randint(3,10), # Strength
                random.randint(5,15), # Magic
                random.randint(6,15), # Luck
                random.randint(10,20), # Wisdom
                random.randint(10,17), # Agility
                random.randint(6,10)) # Speed
    if type=="Human":
        return (random.randint(3,15), # Strength
                random.randint(1,3), # Magic
                random.randint(3,10), # Luck
                random.randint(3,8), # Wisdom
                random.randint(13,17), # Agility
                random.randint(6,10)) # Speed
    if type=="Hobbit":
        return (random.randint(3,10), # Strength
                random.randint(5,10), # Magic
                random.randint(6,15), # Luck
                random.randint(1,13), # Wisdom
                random.randint(1,7), # Agility
                random.randint(1,7)) # Speed
    if type=="Ent":
        return (random.randint(10,35), # Strength
                random.randint(5,10), # Magic
                random.randint(6,15), # Luck
                random.randint(10,40), # Wisdom
                random.randint(1,7), # Agility
                random.randint(1,7)) # Speed
    if type=="Eagle":
        return (random.randint(5,15), # Strength
                random.randint(10,17), # Magic
                random.randint(6,15), # Luck
                random.randint(10,40), # Wisdom
                random.randint(20,35), # Agility
                random.randint(35,60)) # Speed

class Card:
    def __init__(self):
        self.race=roll_weighted((("Dwarf", 20),
                                 ("Elf",20),
                                 ("Human",20),
                                 ("Hobbit",15),
                                 ("Ent",5),
                                 ("Eagle",1)))
        stats=create_creature(self.race)
        self.strength=stats[0]
        self.magic=stats[1]
        self.luck=stats[2]
        self.wisdom=stats[3]
        self.agility=stats[4]
        self.speed=stats[5]
    def info(self):
        typewrite("I am a "+self.race, True)
        typewrite("Stregth "+str(self.strength),True)
        typewrite("Magic "+str(self.magic),True)
        typewrite("Luck "+str(self.luck),True)
        typewrite("Wisdom "+str(self.wisdom),True)
        typewrite("Agility "+str(self.agility),True)
        typewrite("Speed "+str(self.speed),True)

typewrite('Welcome to', True)
time.sleep(0.5)
typewrite("Dwarfs and Elfs",True)
time.sleep(0.5)
if y_n_prompt("Would you like to play a game? "):
    typewrite("Alright, let's go.",True)
else:
    typewrite("I guess this isn't for you then.",True)
    sys.exit()

democard=Card()
democard.info()
