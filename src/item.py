class Item:
    def __init__(self, name, lore):
        self.name = name
        self.lore = lore

    def __str__(self):
        return f'⚔️ Name: {self.name}, Lore: {self.lore}'

    def on_take(self):
        print("You have discovered " + self.name)

    def on_drop(self):
        print("You have discarded" + self.name)
