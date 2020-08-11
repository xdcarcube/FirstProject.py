#Import`s
import time
# import random comes later on (isnt implemented yet ;-))
import random
#Functions
def Help_old():          #This is just a Placeholder
    print("You can use *Tutorial_DE* or *Tutorial_EN*")
#CHANGES ON "def Help()" AND "def Tutorial()" DESIRED!!!
def Help():
    print("You can Type: TutorialDE/TutorialEN/inventory")
def TutorialDE():
    print("Schreibe *Links* um einen Schritt nach Links zu gehen, *Rechts* um nach rechts zu gehen, *Geradeaus* um Geradeaus zu gehen und *Unten* um nach Unten zu gehen ")
def TutorialEN():
    print("Type (Forward) to go Forward, Type (Right) to go Right, (Left) to get to dat left and (Down) to go Downwards ")
def inventory():
    ["-Nothing Yet-"]
#Some Strings i need
Lets_Go = "Lets Go! "
greeting = "Hey, "
first_story_DE = "Es war einmal ein Kleiner Zwerg, der wie sein Vater sein Wollte. Einige Zeit später Hat er sich Respekt und Coins Verdient. "
first_story_EN = "Once Upon a time a little Witcher wanted to be like his Dad. Later on he travelled around the World and Magician Respect and Coins."
                    #Language Select (Work in Progress)
Laguage_Select = input("Select your Language! Wähle deine Sprache! (DE/EN) ")
if Laguage_Select == "DE":
    print("Hallo, dies ist mein erstes kleines Projekt, Viel Spaß =]")
elif Laguage_Select == "EN":
    print("Hi, This is my First Project im currently working on! ")
else:
    print("Hi, This is my First Project im currently working on!")
time.sleep(2)
...
#Before the start
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Lets Go! ")
time.sleep(2)
#Start
...
#playername
if Laguage_Select == "EN":
    Playername = input("Please Type your Name: ")
    print(greeting + Playername)
if Laguage_Select == "DE":
    Playername = input("Bitte gebe deinen Namen ein: ")
time.sleep(3)
...
#(Placeholder)
print("Loading Data ")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
print("...")
time.sleep(1)
if Laguage_Select == "DE":
    print("Hah, verarscht" + Lets_Go )
if Laguage_Select == "EN":
    print("Haha Just Kidding, Lets Go!")
time.sleep(1)
#Start of the Actuall Game
if Laguage_Select == "EN":
    print(first_story_EN)
if Laguage_Select == "DE":
    print(first_story_DE)
time.sleep(4)
print(greeting + Playername + "!")
time.sleep(1.5)
if Laguage_Select == "EN":
    print("This is the beginning of a big Story of" + Playername )
if Laguage_Select == "DE":
    print("Das ist der Anfang Einer Geschichte von " + Playername )
time.sleep(0.5)
print("...")
time.sleep(1)
#So i will add the german Language Later on, as i did before
print("")