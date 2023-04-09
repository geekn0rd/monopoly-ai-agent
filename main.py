import random

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.position = 0

    def move(self, steps, board):
        self.position = (self.position + steps) % len(board.properties)

    def purchase_property(self, property):
        if self.money >= property.price:
            self.money -= property.price
            property.owner = self
            return True
        else:
            return False

    def pay_rent(self, property):
        if self.money >= property.rent:
            self.money -= property.rent
            property.owner.money += property.rent
            return True
        else:
            return False

class Property:
    def __init__(self, name, price, rent):
        self.name = name
        self.price = price
        self.owner = None
        self.rent = rent

    def is_owned(self):
        return self.owner is not None

class Board:
    def __init__(self):
        self.properties = []
        # Add properties to the board during initialization
        self.properties.append(Property("Mediterranean Avenue", 60, 2))
        self.properties.append(Property("Baltic Avenue", 60, 4))
        self.properties.append(Property("Reading Railroad", 200, 25))
        self.properties.append(Property("Oriental Avenue", 100, 6))
        self.properties.append(Property("Vermont Avenue", 100, 6))
        self.properties.append(Property("Connecticut Avenue", 120, 8))
        self.properties.append(Property("St. Charles Place", 140, 10))
        self.properties.append(Property("Electric Company", 150, 0))
        self.properties.append(Property("States Avenue", 140, 10))
        self.properties.append(Property("Virginia Avenue", 160, 12))
        self.properties.append(Property("Pennsylvania Railroad", 200, 25))
        self.properties.append(Property("St. James Place", 180, 14))
        self.properties.append(Property("Tennessee Avenue", 180, 14))
        self.properties.append(Property("New York Avenue", 200, 16))
        self.properties.append(Property("Kentucky Avenue", 220, 18))
        self.properties.append(Property("Indiana Avenue", 220, 18))
        self.properties.append(Property("Illinois Avenue", 240, 20))
        self.properties.append(Property("B. & O. Railroad", 200, 25))
        self.properties.append(Property("Atlantic Avenue", 260, 22))
        self.properties.append(Property("Ventnor Avenue", 260, 22))
        self.properties.append(Property("Water Works", 150, 0))
        self.properties.append(Property("Marvin Gardens", 280, 24))
        self.properties.append(Property("Pacific Avenue", 300, 26))
        self.properties.append(Property("North Carolina Avenue", 300, 26))
        self.properties.append(Property("Community Chest", 0, 0))
        self.properties.append(Property("Pennsylvania Avenue", 320, 28))
        self.properties.append(Property("Short Line", 200, 25))
        self.properties.append(Property("Park Place", 350, 35))
        self.properties.append(Property("Chance", 0, 0))
        self.properties.append(Property("Boardwalk", 400, 50))

    def get_property(self, position):
        return self.properties[position]

class MonopolyGame:
    def __init__(self, players):
        self.players = players
        self.board = Board()


    def play(self):
        while True:
            for player in self.players:
                print(f"It's {player.name}'s turn!")
                dice = roll_dice()
                print(f"current position: {player.position}")
                print(f"dice rolled: {dice}")
                player.move(dice, self.board)
                print(f"new position: {player.position}")
                property = self.board.get_property(player.position)
                if property.is_owned():
                    if property.owner == player:
                        print(f"You landed on your own property: {property.name}")
                    else:
                        print(f"You landed on {property.name} which is owned by {property.owner.name}.")
                        if player.pay_rent(property):
                            print(f"You paid {property.owner.name} ${property.rent} in rent.")
                        else:
                            print("You don't have enough money to pay rent. Game over!")
                            return
                else:
                    print(f"You landed on {property.name} which is unowned.")
                    choice = input("Do you want to buy it? (yes/no): ")
                    if choice.lower() == 'yes':
                        if player.purchase_property(property):
                            print(f"You bought {property.name} for ${property.price}.")
                        else:
                            print("You don't have enough money to buy the property. Game over!")
                            return

def roll_dice():
    # Helper function to simulate rolling dice
    return random.randint(1, 6) + random.randint(1, 6)


if __name__ == "__main__":
    p1 = Player("AI")
    p2 = Player("Human")
    game = MonopolyGame([p1, p2])
    game.play()