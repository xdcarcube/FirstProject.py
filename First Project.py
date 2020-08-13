import time
# import random comes later on
from random import randint


# Funktions
def Help():
    print("You can Type: TutorialDE/TutorialEN/money")
    return True


def Invenory_():
    print(inventory)
    return True


def Help():
    print("You can Type: TutorialDE/TutorialEN/money")
    return True


# CHANGES ON "def Help()" AND "def Tutorial()" DESIRED!!!
# GERMAN LANG. NEEDS TO BE EXPANDED

def TutorialDE():
    print(
        "Schreibe *Links* um einen Schritt nach Links zu gehen, *Rechts* um nach rechts zu gehen, *Geradeaus* um "
        "Geradeaus zu gehen und *Unten* um nach Unten zu gehen.")


def TutorialEN():
    print(
        "Type (Forward) to go Forward, Type (Right) to go Right, (Left) to get to dat left and (Down) to go Backwards.")


# Lists
money = [0]

inventory = [0]

# Some Strings i need
Lets_Go = "Lets Go! "
greeting = "Hey, "
first_story_DE = "Es war einmal ein Kleiner Zwerg, der wie sein Vater sein Wollte. Einige Zeit später Hat er sich " \
                 "Respekt und Coins Verdient. "
first_story_EN = 'Once Upon a time a little Witcher wanted to be like his Dad. Later on he travelled around the World ' \
                 'and gained Respect and Coins '
this_is_for_going_event_1 = 0

# LANG SELECT
Laguage_Select = input("Select your Language! Wähle deine Sprache! (DE/EN) ")
if Laguage_Select == "DE":
    print("Hallo, dies ist mein erstes kleines Projekt, Viel Spaß =]")
elif Laguage_Select == "EN":
    print("Hi, This is my First Project im currently working on! ")
else:
    print("Hi, This is my First Project im currently working on!")
time.sleep(2)

# Before the start
for i in range(6):
    print(i)
    time.sleep(1)

# playername
if Laguage_Select == "EN":
    Playername = input("Please Type your Name: ")
    print(greeting + Playername)
if Laguage_Select == "DE":
    Playername = input("Bitte gebe deinen Namen ein: ")
time.sleep(3)

# (Placeholder)
print("Loading Data ")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
if Laguage_Select == "DE":
    print("Haha, Reingelegt " + Lets_Go)
if Laguage_Select == "EN":
    print("Haha Just Kidding, " + Lets_Go)
time.sleep(1)

# "Story" Part
if Laguage_Select == "EN":
    print(first_story_EN)
if Laguage_Select == "DE":
    print(first_story_DE)
time.sleep(4)
print(greeting + Playername + "!")
time.sleep(1.5)
if Laguage_Select == "EN":
    print("This is the beginning of a big Story of" + Playername)
if Laguage_Select == "DE":
    print("Das ist der Anfang Einer Geschichte von " + Playername)
time.sleep(0.5)
print("...")
time.sleep(1)

# So i will add the german Language Later on, as i did before (Firstly: EN)
print("Roll the dice to choose your Destiny! ")
time.sleep(1)
# Dice Randint
Dice_Roll = randint(1, 6)
print(Dice_Roll)
#            1=1000Coins 2=800 3=600 4=400 5=200 6=100
if Dice_Roll == "1":
    del money[1]
    money.append(1000)
    print("Nice! You Hit the Max! ")
if Dice_Roll == "2":
    del money[1]
    money.append(800)
if Dice_Roll == "3":
    del money[1]
    money.append(600)
if Dice_Roll == "4":
    del money[1]
    money.append(400)
if Dice_Roll == "5":
    del money[1]
    money.append(200)
if Dice_Roll == "6":
    del money[1]
    money.append(100)
    print("Haha you hit the Worst x_x ")

# right
x = 0
# left
y = 0
# up
up = 0
# down
down = 0

for going_event_1 in range(5):
    going_input = input("What do you wanna do next? ")
    print(this_is_for_going_event_1 + "of 5 Actions")
    this_is_for_going_event_1 + 1
