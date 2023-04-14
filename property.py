from math import ceil

class Property():
    def __init__(self, name, space, position, price, rent, build_price) -> None:
        self.name = name
        self.space = space
        self.position = position
        self.price = price
        self.rent = rent
        self.build_price = build_price
        self.ownable = False
        self.build_price = self.price // 2
        self.upgradable = True if self.build_price > 0 else False
        if space in ["Street", "Railroad", "Utility"]:
            self.ownable = True
            self.owner = None
            self.level = 1

    
    def upgrade(self) -> None:
        self.rent *= 1.5
        self.rent = ceil(self.rent)
        self.level += 1
        if self.level >= 5:
            self.upgradable = False
    
    def __str__(self):
        # Format the string using f-strings and return it
        return f"{self.name} - Price: {self.price}$, Rent: {self.rent}$"