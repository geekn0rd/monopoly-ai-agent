# Define the Property class
class Property:
    def __init__(self, name, position, price, rent, ownable=True):
        self.name = name
        self.position = position
        self.price = price
        self.rent = rent
        self.ownable = ownable
        if ownable:
            self.owner = None
    
    def __str__(self):
        return f"{self.name} (Price: {self.price}, Rent: {self.rent})"

