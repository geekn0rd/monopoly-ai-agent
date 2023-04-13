import random

# Define the Player class
class Player:
    def __init__(self, name: str, position: int, money: int):
        self.name = name
        self.position = position
        self.money = money
        self.properties = []
        self.in_jail = False
        self.turns_in_jail = 0
        self.rolled_doubles = False
    
    def pay(self, amount) -> None:
        self.money -= amount

    def receive(self, amount) -> None:
        self.money += amount
    
    def roll_dice(self) -> tuple:
        # Roll the dice and return the result
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        self.rolled_doubles = True if dice1 == dice2 else False
        return (dice1, dice2)
    
    def net_worth(self, props) -> int:
        return self.money + sum([props[i].price for i in self.properties]) + sum([props[i].rent for i in self.properties])
    
    def __str__(self) -> str:
        return f"{self.name} (Position: {self.position}, Money: {self.money}$, Properties: {self.properties})"

