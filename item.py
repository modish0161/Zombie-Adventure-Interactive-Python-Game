# item.py
from room import Room  # Import Room class
from character import Enemy, Character  # Import Enemy and Character classes

class Item():
    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

# Created some items
sword = Item("Sword", "A sharp and shiny sword")
shield = Item("Shield", "A sturdy shield for protection")
potion = Item("Health Potion", "A magical potion to restore health")

# Created some characters
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")

alice = Character("Alice", "A friendly character")
alice.set_conversation("Hello there! Welcome to the mansion.")

# Set items for characters
dave.inventory = [sword, shield]
alice.inventory = [potion]


