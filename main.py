# main.py

from room import Room
from character import Enemy, Character, Friend  # Imported the Friend class
from item import Item
import time

# Function for typewriter effect
def print_with_typewriter_effect(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

# Opening Instructions with typewriter effect
print_with_typewriter_effect("\nWelcome to the Zombie Adventure Game!\n")
print_with_typewriter_effect("\nA game featuring a lone zombie named Dave, a sword for combat, and cheese to fend him off & maybe win.\n")
print_with_typewriter_effect("\nYour mission: find the girl named Alice. Navigate through the ominous mansion, using your wit to fight or fend off zombies.\n")
print_with_typewriter_effect("\nWill you discover Alice and, perhaps, receive a warm hug? Unveil the mysteries within as you embark on this gripping undead adventure!\n")
print_with_typewriter_effect("\nCommands: 'north', 'south', 'east', 'west', 'talk' & 'hug' with Alice, 'talk' & 'fight' with Dave, Use the 'sword'.(Your long arm)!! Or 'fend' him off with some cheese!!!\n")
print_with_typewriter_effect("\nTry talking or fighting with characters in the rooms.\n")
print_with_typewriter_effect("\nYour mission: Find Alice and give her a warm hug.\n")
print_with_typewriter_effect("\nBe a cool dude and swing through the side entrance in the kitchen to avoid the security guards! And there you have it - you're in! Enjoy your evening!\n")

# Defined functions for Room class methods (get_description and set_description)
def get_description(self):
    return self.description

def set_description(self, room_description):
    self.description = room_description

# Created instances of Room
kitchen = Room("kitchen")
kitchen.set_description("The kitchen is aged, dirty, and teeming with flies, slugs, and spiders. Mice scurry about, seeking the last bits of cheese left by Dave, The Smelly Zombie.")

ballroom = Room("ballroom")
ballroom.set_description("The ballroom is a large room with a shiny wooden floor and beautiful chandeliers. Adorned with elegant tapestries")

dining_hall = Room("dining hall")
dining_hall.set_description("Dining hall is a generously sized room adorned with intricate golden decorations, creating an opulent and inviting atmosphere")

# Linked rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

# Created an Enemy character
dave = Enemy("Dave", "The smelly zombie")
dave.set_conversation("Grrr... rghh... brains.")
dave.set_weakness("cheese")

# Created a Friend character
alice = Friend("Alice", "A friendly character")
alice.set_conversation("Hello there! Welcome to the mansion.")

# Set Dave and Alice as characters in the dining hall and ballroom, respectively
dining_hall.set_character(dave)
ballroom.set_character(alice)

# Set the starting room to kitchen
player_location = kitchen

# Game loop
while True:
    print("\n")
    player_location.get_details()
    inhabitant = player_location.get_character()
    
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    # Checking whether a direction is typed
    if command in ["north", "south", "east", "west"]:
        player_location = player_location.move(command)

    # Added code for talking to the inhabitant
    elif command == "talk":
        if inhabitant is not None:
            inhabitant.talk()

            # Added specific dialogue for Dave in the Dining Hall
            if isinstance(inhabitant, Enemy) and inhabitant.name == "Dave" and player_location.name == "dining hall":
                print_with_typewriter_effect("Dave says: 'Do you want a duel? If so, what item are you going to choose for victory?'")
                duel_item = input("Type the item you want to use: ")

                # Handle the duel with Dave based on the chosen item
                duel_result = inhabitant.fight(duel_item)
                if duel_result:
                    print_with_typewriter_effect("Congratulations! You won the duel against Dave.")
                else:
                    print_with_typewriter_effect("You have been defeated in the duel. Game over.")
                    break

            # Added code for Alice's specific dialogue after talking
            elif isinstance(inhabitant, Friend) and inhabitant.name == "Alice":
                print_with_typewriter_effect("Alice says: 'Would you like to give me a hug?'")

                # Added code to respond to Alice's request for a hug
                response = input("Type 'hug' to give Alice a warm hug: ")
                if response.lower() == "hug":
                    inhabitant.hug()
                    print("Alice says: 'You're a great hugger! Would you like to go out sometime? I would like that, if you would... To be Continued...'")
                    print_with_typewriter_effect("Congratulations! You got Alice and avoided fighting Dave. You have won!")

                    # Added code for the dancing ending
                    print_with_typewriter_effect("Then the pair went dancing in the room to 'Saturday Night Fever' by The Bee Gees, played by the DJ! Had a little kiss and a cuddle!!!")
                    break

    # Added code for initiating a fight
    elif command == "fight":
        if inhabitant is not None:
            print_with_typewriter_effect("What will you fight with?")
            fight_with = input()
            result = inhabitant.fight(fight_with)

            if not result:
                print_with_typewriter_effect("You have been defeated. Game over.")
                break

    # Add more conditions for other commands as needed

# ... (Remaining code)
