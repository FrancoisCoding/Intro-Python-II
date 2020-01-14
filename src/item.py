class Item:
    def __init__(self, name, lore):
        self.name = name
        self.lore = lore

    def __str__(self):
        return f'⚔️ Name: {self.name}, Lore: {self.lore}'
