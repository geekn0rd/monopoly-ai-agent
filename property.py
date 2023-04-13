# Define the Property class
class Property:
    def __init__(self, name, space, color, position, price, rent, build_price):
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
            self.level = 0
    
    def __str__(self):
        return f"{self.name} (Price: {self.price}, Rent: {self.rent})"

