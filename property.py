from math import ceil

# Define the Property class
class Property:
    def __init__(self, name: str, space: str, color: str, position: int, price: int, rent: int, build_price: int):
        self.name = name
        self.space = space
        self.color = color
        self.position = position
        self.price = price
        self.rent = rent
        self.build_price = build_price
        self.ownable = False
        if space in ["Street", "Railroad", "Utility"]:
            self.ownable = True
            self.owner = None
            self.level = 1
    
    def upgrade(self) -> None:
        self.rent *= 1.5
        self.rent = ceil(self.rent)
        self.level += 1
    
    def __str__(self) -> str:
        return f"{self.name} (Price: {self.price}, Rent: {self.rent})"

