# Copyright (c) 2018 Copyright Holder All Rights Reserved.
import time
from enum import auto, Enum
# import random comes later on
from random import randint
# Later(not yet)
# import tkinter

# ======================================= Conventions ===============================================
"""
        It is a standard convention in most programming language to create class names with the
    first letter of each word capitalized, while function and variable names are usually entirely
    lower-case and contain underscores ( _ ) between each word.
    
        If you do a really clean job of naming your classes, functions and variables, your code
    will be more readable and require fewer comments, which will make things easier for
    everyone. This is not to say that comments should be avoided, but cleaner code should be
    the focus. Do your best to use good spelling as well, as many text editors and IDEs will
    create a lot of eyesores for people if there are typos all over the code.
    
        While there is nothing wrong with using some global variables, it is better to find them a
    home that makes sense. The more global variables you have lying around, the harder it can be to
    ensure you are only touching the data you need to touch at any given time. Early in a project, I
    like to have a 'data' class that holds all of my global variables. You can create an instance of
    that class in main, and then pass it to every function. Over time, you will find good places to
    off-load all of the variables stored in your data class.
"""
# =================================== Class definitions =============================================


# This is an enumeration class that gives us three identifiers that have unique number values.
# This allows us to pass 'LanguageOptions.LANGUAGE_DEUTSCH' to a function and ask for the German
# translation of a set piece of text.
class LanguageOptions(Enum):
    LANGUAGE_UNKNOWN = auto()
    LANGUAGE_DEUTSCH = auto()
    LANGUAGE_ENGLISH = auto()


# TODO: Load keys and values of dictionaries from language files. This will prevent the language text from
#       being hard coded, and allow us to only store one dictionary at a time, saving resources.
# TODO: Ensure all text has both English and German translations.
# The Language class keeps track of the currently chosen language, and stores dictionaries (key/value pairs)
# for the languages we want to support.
class Language:
    def __init__(self):
        # 'player_language' can be set to unknown initially, telling us to query the player about
        # their preferred language. Later on, when we add saving and loading, if the player has
        # previously entered their preferred language, we can skip asking them in the future.
        self.language_chosen = LanguageOptions.LANGUAGE_UNKNOWN

        self.dictionary_deutsch = {
            "type_help": "Type (Help) to get advice! \n",
            "help_commands": "Schreibe *Links* um einen Schritt nach Links zu gehen, *Rechts* um nach rechts zu"
                             "gehen,\n*Geradeaus* um Geradeaus zu gehen und *Unten* um nach Unten zu gehen.\n"
                             "*Dice* to play dice and *Quit* to quit the game",
            "unknown_command": "Undefined Input!",
            "name_entry_complete": "Hallo, dies ist mein erstes kleines Projekt, Viel Spaß =]",
            "start_game": "Willst du das Spiel starten? J/N \n",
            "start_game_true": "Let the games begin...",
            "start_game_false": "Are you sure...?",
            "name_entry": "Bitte gebe deinen Namen ein: \n",
            "greeting": "Hey, ",
            "story_beginning": "Das ist der Anfang Einer Geschichte von ",
            "god_of_dice": "The God of Dices has chosen you ...(*°O°)ノ",
            "first_story": "Es war einmal ein Kleiner Zwerg, der wie sein Vater sein Wollte. Einige Zeit später Hat er"
                           "sich Respekt und Coins Verdient.",
            "end_text": "This is the end, has it worked well?"
        }

        self.dictionary_english = {
            "type_help": "Type (Help) to get advice! \n",
            "help_commands": "Type (Forward) to go Forward, Type (Right) to go Right, (Left) to go left"
                             "and (Down) to go Backwards.\n"
                             "*Money* to see your finances and *Inventory* to see your inventory.\n"
                             "*Dice* to play dice and *Quit* to quit the game",
            "unknown_command": "Undefined Input!",
            "name_entry_complete": "Hi, This is my First Project im currently working on!",
            "start_game": "Do you want to Start the Game? Y/N \n",
            "start_game_true": "Let the games begin...",
            "start_game_false": "Are you sure...?",
            "name_entry": "Please Type your Name: \n",
            "greeting": "Hey, ",
            "story_beginning": "This is the beginning of a big Story of ",
            "god_of_dice": "The God of Dices has chosen you ...(*°O°)ノ",
            "first_story": "Once Upon a time a little Witcher wanted to be like his Dad. Later on he travelled around"
                           "the World and gained Respect and Coins",
            "end_text": "This is the end, has it worked well?"
        }

    # Returns the text that is paired with the key value 'text_name'.
    # Automatically uses the language dictionary that is paired with the player's selected language.
    def get_game_text(self, text_name: str) -> str:
        text_string = F"Failed to find text_name: {text_name}"

        if self.language_chosen == LanguageOptions.LANGUAGE_DEUTSCH:
            if text_name in self.dictionary_deutsch:
                text_string = self.dictionary_deutsch[text_name]
        elif self.language_chosen == LanguageOptions.LANGUAGE_ENGLISH:
            if text_name in self.dictionary_english:
                text_string = self.dictionary_english[text_name]

        return text_string

    # Allows setting the game language, and returns 'False' if an invalid
    # language number was provided
    def set_language(self, chosen_language: LanguageOptions) -> bool:
        if chosen_language == LanguageOptions.LANGUAGE_DEUTSCH:
            self.language_chosen = LanguageOptions.LANGUAGE_DEUTSCH
            return True
        elif chosen_language == LanguageOptions.LANGUAGE_ENGLISH:
            self.language_chosen = LanguageOptions.LANGUAGE_ENGLISH
            return True

        return False


class GameData:
    def __init__(self) -> None:
        # 'game_running' will make sure that the main game loop does not exit, but also gives us
        # a way to stop the game loop from elsewhere in the code.
        self.game_running = True
        self.language = Language()

    def get_game_text(self, text_name: str) -> str:
        return self.language.get_game_text(text_name=text_name)

    def set_language(self, chosen_language: LanguageOptions) -> None:
        self.language.set_language(chosen_language=chosen_language)

# WraitheDX:
    # The 'GameData' class holds variables that may be applicable to many different parts of the code,
    # and have not yet found a natural home.


# TODO: Create a nice text UI to display the player's name, money, position, and experience
class PlayerOne:
    def __init__(self):
        self.name = "Player"
        self.money = 0
        self.experience = 0

# =================================== Function definitions ==========================================


# This function checks to see if a language has already been chosen. If one has, it returns early, if one has not
# been chosen, this function keeps requesting the player's input until they enter a valid option.
def get_player_language(game_data: GameData) -> None:
    language_chosen = False

    # Continue looping until the player has made a valid language choice.
    while not language_chosen:
        user_input = input("Select your Language! Wähle deine Sprache! (Deutsch ist bei weitem nicht Vollständig!) "
                           "(DE/EN)\n")

        if user_input == "DE":
            language_chosen = True
            game_data.set_language(LanguageOptions.LANGUAGE_DEUTSCH)
        elif user_input == "EN":
            language_chosen = True
            game_data.set_language(LanguageOptions.LANGUAGE_ENGLISH)
        elif user_input != "EN" or "DE":
            print("What are you doing?! Restart...")

        print("Processing...")
        time.sleep(2)

    print(game_data.get_game_text(text_name="name_entry_complete"))


def start_game(game_data: GameData):
    while True:
        user_input = input(game_data.get_game_text("start_game"))

        if user_input == "Y" or user_input == "J":
            break
        elif user_input == "N":
            print(game_data.get_game_text("start_game_false"))

    print(game_data.get_game_text("start_game_true"))


# TODO: It is fine to throw in some sleep() commands for narrative effect, but we should make a function
#       that displays a message while the player is waiting, otherwise they think the game is lagging.
def name_entry(game_data: GameData, player_one: PlayerOne):
    player_one.name = input(game_data.get_game_text("name_entry"))
    print(game_data.get_game_text("greeting") + player_one.name + "!")
    time.sleep(1.5)

    print(game_data.get_game_text("story_beginning") + player_one.name)
    time.sleep(0.5)


# I would like to apologize for this part of the code. I was not sure how you were trying to work the money
# into an inventory system, but money is typically a simple integer in games, so it makes good since to store
# it as an int. Again, I completely understand if you do not want to keep my changes.

# A small dice game where the player can win different amounts of money and a small bit of experience.
def god_of_dice(game_data: GameData, player: PlayerOne):
    # So, i will add the german Language Later on, as i did before (Firstly: EN)
    print(game_data.get_game_text("god_of_dice"))
    time.sleep(2)

    # Dice Randint
    dice_roll = randint(1, 6)
    #            1=1000Coins 2=800 3=600 4=400 5=200 6=100
    if dice_roll == 1:
        player.money += 1000
        print(str("Nice! You Hit the Max  "))
    elif dice_roll == 2:
        player.money += 800
        print(str("Two? That's good!"))
    elif dice_roll == 3:
        player.money += 600
        print(str("Three is viable"))
    elif dice_roll == 4:
        player.money += 400
        print(str("ough... four"))
    elif dice_roll == 5:
        player.money += 200
        print(str("ough... five"))
    elif dice_roll == 6:
        player.money += 100
        print(str("Haha you hit the Worst x_x "))
    print(int(dice_roll))
    # Add XP to the player
    player.experience += 10


# The main game loop
def main():
    game_data = GameData()
    player_one = PlayerOne()

    get_player_language(game_data)
    start_game(game_data)
    name_entry(game_data, player_one)

    while game_data.game_running:
        print(game_data.get_game_text("type_help"))
        user_input = input("Command: ")

        if user_input == "Help":
            print(game_data.get_game_text("help_commands"))
        elif user_input == "Dice":
            god_of_dice(game_data=game_data, player=player_one)
        elif user_input == "Money":
            print("You have: " + str(player_one.money))
        elif user_input == "Inventory":
            print("Why, there is nothing in your inventory!")
        elif user_input == "Quit":
            game_data.game_running = False
        else:
            print(game_data.get_game_text("unknown_command"))

        # TODO: Player movement should probably use North, South, East, and West,
        #       as 'right' and 'left' imply turning, not strafing.
        """
        elif user_input == "Rechts" or "Right":
            x = x + 1
            print("right_ok")
            print(int(x))
        elif going_input2 == "Links" or "Left":
            y = y + 1
            print("left_ok")
            print(int(y))
        elif going_input2 == "Vorwärts" or "Forward":
            forward = forward + 1
            print("forward_ok")
            print(int(forward))
        elif going_input2 == "Runter" or "down":
            down = down + 1
            print("down_ok")
            print(int(down))
        """

    print(game_data.get_game_text("end_text"))


if __name__ == "__main__":
    main()

# Run the main function
