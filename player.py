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
        # Calculate current rent
        current_rent = sum([props[i].rent for i in self.properties])
        
        # Calculate potential rent with all properties fully developed
        potential_rent = sum([props[i].max_rent for i in self.properties])
        
        # Calculate current property value
        prop_value = sum([props[i].price for i in self.properties])
        
        # Calculate net worth
        return self.money + current_rent + (potential_rent - current_rent) + prop_value

    def __str__(self) -> str:
        return f"{self.name}\n" \
            f"Position: {self.position}\n" \
            f"Money: {self.money}$\n" \
            f"Properties: {self.properties}"