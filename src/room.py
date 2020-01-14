# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item


class Room:
    def __init__(self, name, description, n_to=None, s_to=None, w_to=None, e_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.w_to = w_to
        self.e_to = e_to
        self.items = []

    def __str__(self):
        _str = f"🕵🏿 Room: {self.name} \nDescription: {self.description} \n"
        _str += f"Items in room : {self.items}"
        return _str

    def get_items(self):
        return self.items

    def add_item(self, item):
        return self.items.append(item)

    def delete_item(self, item):
        return self.items.remove(item)
