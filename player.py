import random

class Player():
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money
        self.properties = []
        self.is_in_jail = False
        self.turns_in_jail = 0
        self.rolled_doubles = False

    
    def pay_money(self, amount)-> None:
        self.money -= amount

    def get_money(self, amount) -> None:
        self.money += amount

    def roll_dice(self) -> int:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        print(f"{self.name} rolled {dice1} and {dice2} ({total})")
        return total
    
    def net_worth(self, props) -> int:
        # Calculate the net worth of the player, which includes money and the total value of their properties and their rent
        # Money is added first
        net_worth = self.money 
        # Then, iterate over each property owned by the player and add its price to the net worth
        for i in self.properties:
            net_worth += props[i].price
        # Finally, iterate over each property owned by the player and add its rent to the net worth
        for i in self.properties:
            net_worth += props[i].rent
        # Return the net worth as an integer
        return net_worth

    def __str__(self) -> str:
        return f"{self.name} (Position: {self.position}, Money: {self.money}$, Properties: {self.properties})"

