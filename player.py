import random

class Player():
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money
        self.is_in_jail = False
        self.properties = []
    
    def pay_money(self, amount):
        self.money -= amount

    def get_money(self, amount):
        self.money += amount

    def roll_dice(self):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        print(f"{self.name} rolled {dice1} and {dice2} ({total})")
        return total
    
    
    def net_worth(self, props):
        # Calculate the player's total net worth by adding their money and the total value of their properties
        total_worth = self.money + sum([prop.price for prop in self.properties])
        
        # Add the total rent earned from all the player's properties
        total_rent = sum([prop.rent for prop in self.properties])
        
        return total_worth + total_rent

    def __str__(self):
        # Convert the list of properties to a comma-separated string of property names
        prop_names = ", ".join([prop.name for prop in self.properties])
        
        # Format the string using f-strings and return it
        return f"{self.name} (Position: {self.position}, Money: {self.money}$, Properties: {prop_names})"
