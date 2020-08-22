import time
# import random comes later on
from random import randint
#Later(not yet)
import tkinter

import sys
# Funktions

class PlayerOne:
    MoneyListvar = [0]
    inventoryvar = ["/100xp"]
    def Inventory(self):
        return inventoryvar
    def money(self):
        return MoneyListvar

class Tutorials():
    def TutorialDE(self):
        tutDE = print("Schreibe *Links* um einen Schritt nach Links zu gehen, *Rechts* um nach rechts zu gehen, \
                        *Geradeaus* um Geradeaus zu gehen und *Unten* um nach Unten zu gehen.")
        return tutDE

    def TutorialEN(self):
        tutEN = print("Type (Forward) to go Forward, Type (Right) to go Right, (Left) to get to dat left and (Down) to go Backwards.")
        return tutEN

    def Help(self):
        hlp = print("You can Type: TutorialDE/TutorialEN/money/inventory")
        return hlp


# CHANGES ON "def Help()" AND "def Tutorial()" DESIRED!!!
# GERMAN LANG. NEEDS TO BE EXPANDED


# Lists


# Some Strings i need
Lets_Go = "Lets Go! "

greeting = "Hey, "

first_story_DE = "Es war einmal ein Kleiner Zwerg, der wie sein Vater sein Wollte. Einige Zeit später Hat er sich " \
                 "Respekt und Coins Verdient. "

first_story_EN = 'Once Upon a time a little Witcher wanted to be like his Dad. Later on he travelled around the World ' \
                 'and gained Respect and Coins '

this_is_for_going_event_1 = 0

forvar = " of 5 actions"

# LANG SELECT
Language_Select = input("Select your Language! Wähle deine Sprache! (DE/EN) ")
if Language_Select == "DE":
    print("Hallo, dies ist mein erstes kleines Projekt, Viel Spaß =]")
elif Language_Select == "EN":
    print("Hi, This is my First Project im currently working on! ")
elif Language_Select != "EN" or "DE":
    print("What are you doing?! Restart...Stupid ")
    SystemExit
time.sleep(2)


#start?
if Language_Select == "EN":
    startgameEN = input("Do you want to Start the Game? Y/N ")
elif Language_Select == "DE":
    startgameDE = input("Willst du das Spiel starten? J/N ")






# Before the start
for i in range(6, 0):
    print(i)
    time.sleep(1)


# playername
if Language_Select == "EN":
    Playername_1 = input("Please Type your Name: ")
    print(greeting + Playername_1)
elif Language_Select == "DE":
    Playername_2 = input("Bitte gebe deinen Namen ein: ")
time.sleep(3)


# (Placeholder)
print("Loading Data ")
for herunterzählen in range(1, 7):
    print("...")
    time.sleep(1)
print("Value Error in Project_1.py <module> print() is not defined! ")
time.sleep(3.5)
if Language_Select == "DE":
    print("Haha, Reingelegt " + Lets_Go)
if Language_Select == "EN":
    print("Haha Just Kidding, " + Lets_Go)
time.sleep(1)


# "Story" Part
if Language_Select == "EN":
    print(first_story_EN)
elif Language_Select == "DE":
    print(first_story_DE)
time.sleep(4)
if Language_Select == "DE":
    print(greeting + Playername_2 + "!")
elif Language_Select == "EN":
    print(greeting + Playername_1 + "!")

time.sleep(1.5)
if Language_Select == "EN":
    print("This is the beginning of a big Story of " + Playername_1)
if Language_Select == "DE":
    print("Das ist der Anfang Einer Geschichte von " + Playername_2)
time.sleep(0.5)
time.sleep(1)

# So i will add the german Language Later on, as i did before (Firstly: EN)
print("Now...Roll the dice to choose your Destiny! ")
time.sleep(2)
# Dice Randint
Dice_Roll = randint(1, 6)
print(Dice_Roll)
#            1=1000Coins 2=800 3=600 4=400 5=200 6=100
if Dice_Roll == "1":
    instanz1 = PlayerOne
    listDEL1 = instanz1.MoneyListvar.remove(0)
    listADD1 = instanz1.money.append(int(1000))
    print("Nice! You Hit the Max  ")
if Dice_Roll == "2":
    instanz2 = PlayerOne
    listDEL2 = instanz2.MoneyListvar.remove(0)
    listADD2 = instanz2.money.append(int(800))
if Dice_Roll == "3":
    instanz3 = PlayerOne
    listDEL3 = instanz3.MoneyListvar.remove(0)
    listADD3 = instanz3.money.append(int(600))
if Dice_Roll == "4":
    instanz4 = PlayerOne
    listDEL4 = instanz4.MoneyList.remove(0)
    listADD4 = instanz4.money.append(int(400))
if Dice_Roll == "5":
    instanz5 = PlayerOne
    listDEL5 = instanz5.MoneyList.remove(0)
    listADD5 = instanz5.money.append(int(200))
if Dice_Roll == "6":
    instanz6 = PlayerOne
    listDEL6 = instanz6.MoneyList.remove(0)
    listADD6 = instanz6.money.append(int(100))
    print("Haha you hit the Worst x_x ")
instanz7 = PlayerOne
listADD7 = instanz7.inventoryvar.insert(0, "10")
time.sleep(2)

# right
x = 0
# left
y = 0
# up
up = 0
# down
down = 0

print("Type (Help) ")
time.sleep(1.5)
for going_event_1 in range(5):
        going_input = input("What do you wanna do next? ")
        print(this_is_for_going_event_1) + (forvar)
        this_is_for_going_event_1 +1
        if going_input == "Help":
            instanz8 = Tutorials
            print(instanz8.TutorialEN)
        elif going_input == "Rechts" or "Right":
            x + 1
            print("Ok! ")
