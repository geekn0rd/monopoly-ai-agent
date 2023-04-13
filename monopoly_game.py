from copy import deepcopy
from property import *
from player import *
from math import ceil

# Define the Monopoly game class
class MonopolyGame:
    def __init__(self, board: list=[], players: list=[], current_player: int=0, game_over: bool=False):
        # Initializing the game state
        self.board = board  # List to represent the game board
        self.players = players  # List to represent the players
        self.current_player = current_player  # Index of the current player in the players list
        self.game_over = game_over  # Boolean flag to indicate if the game is over
    
    def initialize_board(self, file_name: str) -> None:
        # Initializing the game board from a csv file
        with open(file_name) as file:
            next(file)
            for line in file:
                name, space, color, position, price, build_price, rent = line.rstrip().split(",")
                self.board.append(
                    Property(name, space, color, int(position), int(price), int(rent), int(build_price))
                    )
        
        

    def initialize_players(self) -> None:
        # Initializing two players with their starting positions, money, and other attributes
        player1 = Player("P1", 0, 1500)
        player2 = Player("P2", 0, 1500)
        self.players = [player1, player2]

    def take_action(self, action: int):
        # Updating the game state based on the action taken by the current player
        new_players = deepcopy(self.players)
        new_board = deepcopy(self.board)
        curr_player = new_players[self.current_player]
        curr_position = curr_player.position
        curr_prop = new_board[curr_position]
        # Do the appropriate changes for the action
        if action == 0:
            pass
        elif action == 1:
            curr_player.pay(curr_prop.price)
            curr_player.properties.append(curr_position)
            curr_prop.owner = self.current_player    
        elif action == 2:
            curr_player.pay(curr_prop.rent)
            new_players[curr_prop.owner].receive(curr_prop.rent)
        elif action == 3:
            curr_prop.rent *= 1.5
            curr_prop.rent = ceil(curr_prop.rent)
            curr_prop.level += 1
        elif action == 4:
            curr_player.position = 10
            curr_player.in_jail = True
            curr_player.turns_in_jail += 1
        elif action == 5:
            curr_player.turns_in_jail += 1
        elif action == 6:
            curr_player.pay(50)
            curr_player.in_jail = False
            curr_player.turns_in_jail = 0
        elif action == 7:
            curr_player.in_jail = False
            curr_player.turns_in_jail = 0       
        return MonopolyGame(new_board, new_players, self.current_player, self.game_over)
    
    def get_possible_actions(self) -> list:
        # Get the possible actions available to the current player
        curr_player = self.players[self.current_player]
        curr_position = curr_player.position
        curr_prop = self.board[curr_position]
        if curr_player.in_jail:
            if curr_player.rolled_doubles:
                return [7]
            if curr_player.turns_in_jail >= 3:
                return [6]
            return [5, 6]
        if curr_prop.ownable:
            if curr_prop.owner == self.current_player:
                if curr_prop.level < 5:
                    return [3, 0]
                return [0]
            elif curr_prop.owner == None:
                if curr_player.money > curr_prop.price:
                    return [1, 0]
                return [0]
            else:
                return [2]
        if curr_prop.space == "GoToJail":
                return [4]
        return [0]
    
    def move_player(self, dice_result:int) -> None:
        # Pass if the player is in jail
        if self.players[self.current_player].in_jail:
            return
        curr_player = self.players[self.current_player]
        curr_position = curr_player.position
        # Update the player's position based on the dice roll result
        curr_position = (curr_position + dice_result) % len(self.board)
        curr_player.position = curr_position

    def is_terminal(self) -> bool:
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

