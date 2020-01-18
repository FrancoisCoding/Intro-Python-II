# Write a class to hold player information, e.g. what current_room they are in
# currently.

from item import Item


class Player:
    def __init__(self, name, current_room, rupees=0):
        self.name = name
        self.current_room = current_room
        self.rupees = rupees
        self.inventory = []

    def __str__(self):
        return f'Name: {self.name} \n Room: {self.current_room} \n Inventory: {str(self.inventory)} '

    def get_inventory(self):
        return self.inventory

    def add_item(self, item):
        self.rupees += 10
        return self.inventory.append(item)

    def delete_item(self, item):
        self.rupees -= 10
        return self.inventory.remove(item)
