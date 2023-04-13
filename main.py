# Import any required libraries
from monopoly_game import *

PROBS = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

# Encodings of what each action number mean
ACTIONS = {
    0: "does nothing",
    1: "buys prop",
    2: "pays rent",
    3: "upgrades prop",
    4: "goes to jail",
    5: "stays in jail",
    6: "bails out of jail",
    7: "is freed from jail",
}

def min_node(state, main_player, possible_moves, depth):
    min_eval = float('inf')
    for move in possible_moves:
        # Make the move in a copy of the state
        new_state = state.make_move(move)
        # We should also switch the player
        new_state.switch_player()
        # Recursively call expectiminimax  on the new state with depth reduced by 1
        eval, _ = expectiminimax(main_player, new_state, depth - 1, True)
        if eval < min_eval:
            min_eval = eval
            best_move = move
    return min_eval, best_move

def max_node(state, main_player, possible_moves, depth):
    max_eval = float('-inf')
    for move in possible_moves:
        # Make the move in a copy of the state
        new_state = state.make_move(move)
        # We should also switch the player
        new_state.switch_player()
        # Recursively call expectiminimax  on the new state with depth reduced by 1
        eval, _ = expectiminimax(main_player,new_state, depth - 1, True)
        if eval > max_eval:
            max_eval = eval
            best_move = move
    return max_eval, best_move
 
def expectiminimax(main_player, state, depth=4, chance=False):
    # expectiminimax  algorithm to search for the best move
    if state.current_player == main_player:
        node = max_node
    else:
        node = min_node 
    if state.is_terminal() or depth == 0:
        return state.evaluate_utility(), None
    possible_moves = state.get_possible_moves()
    if chance:
        expected = 0
        for dice in range(2, 13):
            state.move_player(dice)
            new_state = state
            eval, _ = expectiminimax(main_player, new_state, depth - 1, False)
            expected += eval * PROBS[dice]
        return expected, None
    else:
        return node(state, main_player, possible_moves, depth)

def play(state):
        num_of_rounds = 0
        # Main game loop to play the game
        while not state.game_over:
            curr_player = state.players[state.current_player]
            print(f"{curr_player.name} is on {curr_player.position} and has {curr_player.money}$,")
            if curr_player.in_jail:
                print(f"turns in jail {curr_player.turns_in_jail}")
            d1, d2 = curr_player.roll_dice()
            print(f"{curr_player.name} rolls dice: {(d1, d2)},")
            state.move_player(d1 + d2)
            print(f"{curr_player.name} lands on {curr_player.position}!", end=", ")
            # possible_moves, _ = self.get_possible_moves()
            # possible_moves = [possible_moves]
            _, best_action = expectiminimax(state.current_player, state)
            # action, _ = self.get_possible_moves()
            state = state.make_move(best_action)
            print(f"{curr_player.name} {ACTIONS[best_action]}.")
            print(state.players[state.current_player])
            #print(self.board[curr_position])
            if state.is_terminal():
                state.game_over = True
            else:
                state.switch_player()
            num_of_rounds += 1
            print("====================================================")
        print(f"{state.players[0 if state.current_player else 1].name} Won :) rounds played: {num_of_rounds}")   

# Driver code to start the Monopoly game
if __name__ == "__main__":
    game = MonopolyGame()
    game.initialize_players()
    game.initialize_board("board.csv")
    play(game)
