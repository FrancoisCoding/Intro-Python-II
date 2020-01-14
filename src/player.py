# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room, name, inventory):
        self.room = room
        self.name = name
        self.inventory = inventory

    def __str__(self):
        return f'Hello {self.name} you are in {self.room}'
