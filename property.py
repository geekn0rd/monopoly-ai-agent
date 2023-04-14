
class Property():
    def __init__(self, name, space, position, price, rent, build_price) -> None:
        self.name = name
        self.space = space
        self.position = position
        self.price = price
        self.rent = rent
        self.build_price = build_price
        self.ownable = False
        if space in ["Street", "Railroad", "Utility"]:
            self.ownable = True
            self.owner = None
            self.level = 1
            
    def __str__(self):
        # Format the string using f-strings and return it
        return f"{self.name} - Price: {self.price}$, Rent: {self.rent}$"