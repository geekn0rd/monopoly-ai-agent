
class Property():
    def __init__(self, name, space, position, price, build_price, rent0, rent1, rent2, rent3, rent4, rent5) -> None:
        self.name = name
        self.space = space
        self.position = position
        self.price = price
        self.build_price = build_price
        self.rentl = []
        self.rentl.append(rent0)
        self.rentl.append(rent1)
        self.rentl.append(rent2)
        self.rentl.append(rent3)
        self.rentl.append(rent4)
        self.rentl.append(rent5)
        self.level = 0
        self.ownable = False
        self.upgradable = True if space in ["Street"] else False
        if space in ["Street", "Railroad", "Utility"]:
            self.ownable = True
            self.owner = None
            self.level = 0
        self.max_rent = self.rentl[5]
        self.rent = self.rentl[self.level]
        
    def upgrade(self) -> None:
        self.level += 1
        if self.level >= 5:
            self.upgradable = False
        self.rent = self.rentl[self.level]

    def __str__(self):
        # Format the string using f-strings and return it
        return f"{self.name} - Price: {self.price}$, Rent: {self.rent}$"