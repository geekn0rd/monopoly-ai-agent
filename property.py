from math import ceil
import numpy as np

class Property():
    def __init__(self, name, space, position, price, rent, build_price) -> None:
        self.name = name
        self.space = space
        self.position = position
        self.price = price
        self.rent = rent
        self.build_price = build_price
        self.ownable = False
        self.max_rent = self.rent * np.power(1.5, 5)
        self.build_price = self.price // 2
        self.upgradable = True if self.build_price > 0 else False
        if space in ["Street", "Railroad", "Utility"]:
            self.ownable = True
            self.owner = None
            self.level = 1
        if space in ["Community Chest", "Income Tax", "Chance", "Free Parking", "Go To Jail", "Luxury Tax"]:
            self.ownable = False
            self.owner = None
    
    def upgrade(self) -> None:
        self.rent *= 1.5
        self.rent = ceil(self.rent)
        self.level += 1
        if self.level >= 5:
            self.upgradable = False

    def __str__(self):
        # Format the string using f-strings and return it
        return f"{self.name} - Price: {self.price}$, Rent: {self.rent}$"