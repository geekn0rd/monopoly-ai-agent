# Import any required libraries
import random
from copy import deepcopy

# Define the Player class
class Player:
    def __init__(self, name, position, money):
        self.name = name
        self.position = position
        self.money = money
        self.properties = []

    def roll_dice(self):
        # Roll the dice and return the result
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        return dice1, dice2
    
    def net_worth(self, props):
        return self.money + sum([props[i].price for i in self.properties]) + sum([props[i].rent for i in self.properties])
    
    def __str__(self):
        return f"{self.name} (Position: {self.position}, Money: {self.money}, Properties: {self.properties})"


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


# Define the Monopoly game class
class MonopolyGame:
    def __init__(self, board=[], players=[], current_player=0, game_over=False):
        # Initialize the game state
        self.board = board  # List to represent the game board
        self.players = players  # List to represent the players
        self.current_player = current_player  # Index of the current player in the players list
        self.game_over = game_over  # Boolean flag to indicate if the game is over
    
    def initialize_board(self):
        # Initialize the game board with properties, cards, and other game elements
        # Example: Create three properties with initial attributes
        go = Property("Go", 0, 0, 0, False)
        property1 = Property("Property 1", 1, 200, 20)
        property2 = Property("Property 2", 2, 300, 30)
        property3 = Property("Property 3", 3, 400, 40)
        property4 = Property("Property 4", 4, 500, 40)
        property5 = Property("Property 5", 5, 800, 40)
        property6 = Property("Property 6", 6, 700, 40)
        property7 = Property("Property 7", 7, 800, 40)
        property8 = Property("Property 8", 8, 900, 40)
        self.board = [go, property1, property2, property3, property4, property5, property6, property7, property8]

    def initialize_players(self):
        # Initialize the players with their starting positions, money, and other attributes
        # Example: Create two players with initial attributes
        player1 = Player("P1", 0, 1500)
        player2 = Player("P2", 0, 1500)
        self.players = [player1, player2]

    def make_move(self, action):
        # Update the game state based on the action taken by the current player
        new_players = deepcopy(self.players)
        new_board = deepcopy(self.board)
        curr_player = new_players[self.current_player]
        curr_position = curr_player.position
        curr_prop = new_board[curr_position]
        if action in [0, -1]:
            pass
        elif action == 1:
            curr_player.money -= curr_prop.price
            curr_player.properties.append(curr_position)
            curr_prop.owner = self.current_player    
        elif action == 2:
            curr_player.money -= curr_prop.rent
            new_players[curr_prop.owner].money += curr_prop.rent
        
        return MonopolyGame(new_board, new_players, self.current_player, self.game_over)
    
    def get_possible_moves(self):
        # Get the possible moves available to the current player
        curr_player = self.players[self.current_player]
        curr_position = curr_player.position
        # Update the player's position based on the dice roll result
        dice_result = curr_player.roll_dice()
        total = sum(dice_result)
        curr_position = (curr_position + total) % len(self.board)
        curr_player.position = curr_position
        curr_prop = self.board[curr_position]
        if curr_prop.ownable:
            if curr_prop.owner == self.current_player:
                return [0], "make house and hotel"
            elif curr_prop.owner == None:
                if curr_player.money > curr_prop.price:
                    return [1, -1], f"buy or pass"
                return [-1], "can't buy"
            else:
                return [2], "pay rent to the owner"
        return [3], "nothing chill"
    
    def is_terminal(self):
        # Check if the game has reached a terminal state
        curr_player = self.players[self.current_player]
        if curr_player.money <= 0:
            return True
        return False
    
    def evaluate_utility(self):
        curr_player = self.players[self.current_player]
        # Evaluate the utility of the current game state for the current player
        return curr_player.net_worth(self.board)

    def switch_player(self):
        # Switch to the next player's turn
        self.current_player += 1
        self.current_player %= 2


def minimax(state, depth=3, max_player=True):
    # Minimax algorithm to search for the best move
    if state.is_terminal() or depth == 0:
        return state.evaluate_utility(), None
    best_move = None
    possible_moves, _ = state.get_possible_moves()
    if max_player:
        max_eval = float('-inf')
        for move in possible_moves:
            # Make the move in a copy of the state
            new_state = state.make_move(move)
            # Recursively call minimax on the new state with depth reduced by 1
            eval, _ = minimax(new_state, depth - 1, False)
            if eval > max_eval:
                max_eval = eval
                best_move = move
        return max_eval, best_move       
    else:
        min_eval = float('inf')
        for move in possible_moves:
            # Make the move in a copy of the state
            new_state = state.make_move(move)
            # Recursively call minimax on the new state with depth reduced by 1
            eval, _ = minimax(new_state, depth - 1, True)
            if eval < min_eval:
                max_eval = eval
                best_move = move
        return min_eval, best_move

   


def play(state):
        # Main game loop to play the game
        while not state.game_over:
            curr_player = state.players[state.current_player]
            curr_position = curr_player.position
            print(curr_player)
            # possible_moves, _ = self.get_possible_moves()
            # possible_moves = [possible_moves]
            _, best_action = minimax(state)
            # action, _ = self.get_possible_moves()
            state = state.make_move(best_action)
            print(state.players[state.current_player])
            #print(self.board[curr_position])
            if state.is_terminal():
                state.game_over = True
            else:
                state.switch_player()
        print(f"{state.players[state.current_player].name} Lost :)")   

# Driver code to start the Monopoly game
if __name__ == "__main__":
    game = MonopolyGame()
    game.initialize_players()
    game.initialize_board()
    play(game)
