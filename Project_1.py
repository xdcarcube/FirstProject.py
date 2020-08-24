# Copyright (c) 2018 Copyright Holder All Rights Reserved.
import time
# import random comes later on
from random import randint
#Later(not yet)
import tkinter

# Funktions\Classes

class Ex(Exception):
    pass

class PlayerOne():
    def __init__(self):
        pass
    MoneyListvar = [0]
    inventoryvar = ["/100xp"]
    def Inventory(self):
        return inventoryvar[0]
    def money(self):
        return MoneyListvar[0]

class Tutorials():
    def TutorialDE(self):
        tutDE = print(str("Schreibe *Links* um einen Schritt nach Links zu gehen, *Rechts* um nach rechts zu gehen, \
                        *Geradeaus* um Geradeaus zu gehen und *Unten* um nach Unten zu gehen."))
        return tutDE

    def TutorialEN(self):
        tutEN = print(str("Type (Forward) to go Forward, Type (Right) to go Right, (Left) to go left and (Down) to go Backwards."))
        return tutEN

    def Help(self):
        hlp = print(str("You can always type quit to quit()/TutorialEN/money/inventory/TutorialDE <--(I´d would´nt recommend typing this if you dont have knowlegde besides the German Language)"))
        return hlp

Help = ["TutorialEN", "money" "inventory"] # (if the class is not working ;-;)


# CHANGES ON "def Help()" AND "def Tutorial()" DESIRED!!!
# GERMAN LANG. NEEDS TO BE EXPANDED


# Lists


# Some Strings
Lets_Go = "Lets Go! "

greeting = "Hey, "

first_story_DE = "Es war einmal ein Kleiner Zwerg, der wie sein Vater sein Wollte. Einige Zeit später Hat er sich " \
                 "Respekt und Coins Verdient. "

first_story_EN = 'Once Upon a time a little Witcher wanted to be like his Dad. Later on he travelled around the World ' \
                 'and gained Respect and Coins '

this_is_for_going_event_1 = 0 # isnt used lol

forvar = " of 5 actions"

# LANG SELECT
Language_Select = input(str("Select your Language! Wähle deine Sprache! (Deutsch ist bei weitem nicht Vollständig!) (DE/EN) \n"))
if Language_Select == "DE":
    print(str("Hallo, dies ist mein erstes kleines Projekt, Viel Spaß =]"))
elif Language_Select == "EN":
    print(str("Hi, This is my First Project im currently working on! "))
elif Language_Select != "EN" or "DE":
    print(str("What are you doing?! Restart..."))
    quit()
time.sleep(2)


#start?
if Language_Select == "EN":
    startgameEN = input(str("Do you want to Start the Game? Y/N \n"))
elif Language_Select == "DE":
    startgameDE = input(str("Willst du das Spiel starten? J/N \n"))


# Before the start
for i in range(6, 0):
    print(int(i))
    time.sleep(1)


# playername
if Language_Select == "EN":
    Playername_1 = str(input("Please Type your Name: \n"))
elif Language_Select == "DE":
    Playername_1 = str(input("Bitte gebe deinen Namen ein: \n"))
else:
    print(str("What are you doing?! Restart..."))
time.sleep(1.5)


# (Placeholder)


# "Story" Part (no more)
time.sleep(2.5)
if Language_Select == "DE" or "EN":
    print(str(greeting + Playername_1 + "!"))

time.sleep(1.5)
if Language_Select == "EN":
    print(str("This is the beginning of a big Story of " + Playername_1))
elif Language_Select == "DE":
    print(str("Das ist der Anfang Einer Geschichte von " + Playername_1))
time.sleep(0.5)

# So, i will add the german Language Later on, as i did before (Firstly: EN)
print(str("The God of Dices has chosen you ...(*°O°)ノ"))
time.sleep(2)
# Dice Randint
Dice_Roll = randint(1, 6)
#            1=1000Coins 2=800 3=600 4=400 5=200 6=100
if Dice_Roll == 1:
    instanz1 = PlayerOne
    listDEL1 = instanz1.MoneyListvar.remove(0)
    listADD1 = instanz1.MoneyListvar.append(int(1000))
    print(str("Nice! You Hit the Max  "))
elif Dice_Roll == 2:
    instanz2 = PlayerOne
    listDEL2 = instanz2.MoneyListvar.remove(0)
    listADD2 = instanz2.MoneyListvar.append(int(800))
    print(str("Two? Thats good!"))
elif Dice_Roll == 3:
    instanz3 = PlayerOne
    listDEL3 = instanz3.MoneyListvar.remove(0)
    listADD3 = instanz3.MoneyListvar.append(int(600))
    print(str("Three is viable"))
elif Dice_Roll == 4:
    instanz4 = PlayerOne
    listDEL4 = instanz4.MoneyListvar.remove(0)
    listADD4 = instanz4.MoneyListvar.append(int(400))
    print(str("ough four"))
elif Dice_Roll == 5:
    instanz5 = PlayerOne
    listDEL5 = instanz5.MoneyListvar.remove(0)
    listADD5 = instanz5.MoneyListvar.append(int(200))
    print(str("ough five"))
elif Dice_Roll == 6:
    instanz6 = PlayerOne
    listDEL6 = instanz6.MoneyListvar.remove(0)
    listADD6 = instanz6.MoneyListvar.append(int(100))
    print(str("Haha you hit the Worst x_x "))
print(int(Dice_Roll))
#add XP
instanz7 = PlayerOne
listADD7 = instanz7.inventoryvar.insert(0, "10")
time.sleep(2)

# right
x = 0
# left
y = 0
# forward
forward = 0
# down
down = 0




# MAIN CODE PART!!!
if __name__ == "__main__":
    while True:
        for i in range(1):
            going_input1 = str(input("The adventure just began, type (Help) to get advice! \n"))
        for i in range(3):
            going_input2 = str(input("\n"))
            if going_input1 == "Help":
                instanz8 = Tutorials
                instanz8Acces = instanz8.Help
                print(str(instanz8Acces))
            elif going_input2 == "TutorialEN":
                instanz9 = Tutorials
                instanz9Acces = instanz9.TutorialEN
                print(str(instanz9Acces))
            elif going_input2 == "money":
                instanz10 = PlayerOne
                instanz10Acces = PlayerOne.MoneyListvar
                print(str(instanz10Acces))
            elif going_input2 == "inventory":
                instanz11 = PlayerOne
                instanz11Acces = PlayerOne.inventoryvar
                print(str(instanz11Acces))
            elif going_input2 == "Rechts" or "Right":
                x = x + 1
                print(str("rightok"))
                print(int(x))
            elif going_input2 == "Links" or "Left":
                y = y + 1
                print(str("leftok"))
                print(int(y))
            elif going_input2 == "Vorwärts" or "Forward":
                forward = forward + 1
                print(str("forwardok"))
                print(int(forward))
            elif going_input2 == "Runter" or "down":
                down = down + 1
                print(str("downok"))
                print(int(down))
            else:
                print(str("Undefined Input!"))
print(str("This is end, has it worked well?"))
