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
    for i in list(string):
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
        return (random.randint(5,20),
                random.randint(1,7),
                random.randint(1,5),
                random.randint(1,10),
                random.randint(1,15),
                random,randint(1,6))
class Card:
    def __init__(self):
        self.race=roll_weighted((("Dwarf", 20),
                                 ("Elf",20),
                                 ("Human",20),
                                 ("Hobbit",15),
                                 ("Ent",5),
                                 ("Eagle",1)))
    def info(self):
        typewrite("I am a "+self.race, True)

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
