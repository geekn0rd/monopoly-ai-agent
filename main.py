# Import any required libraries
from monopoly_game import *

# Probabilities of each dice roll outcome
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

def min_node(main_player: int, state: MonopolyGame, depth: int) -> tuple:
    min_eval = float('inf')
    possible_actions = state.get_possible_actions()
    for action in possible_actions:
        # Take the action in a copy of the state
        new_state = state.take_action(action)
        # We should also switch the player
        new_state.switch_player()
        # Recursively call expectiminimax on the new state with depth reduced by 1
        eval, _ = expectiminimax(main_player, new_state, depth - 1, True)
        if eval < min_eval:
            min_eval = eval
            best_action = action
    return min_eval, best_action

def max_node(main_player: int, state: MonopolyGame, depth: int) -> tuple:
    max_eval = float('-inf')
    possible_actions = state.get_possible_actions()
    for action in possible_actions:
        # Take the action in a copy of the state
        new_state = state.take_action(action)
        # We should also switch the player
        new_state.switch_player()
        # Recursively call expectiminimax on the new state with depth reduced by 1
        eval, _ = expectiminimax(main_player,new_state, depth - 1, True)
        if eval > max_eval:
            max_eval = eval
            best_action = action
    return max_eval, best_action

def chance_node(main_player: int, state: MonopolyGame, depth: int) -> tuple:
    expected_utility = 0
    # Account for the all possible dice outcomes
    for dice in range(2, 13):
        state.move_player(dice)
        new_state = state
        # Recursively call expectiminimax on the new state with depth reduced by 1
        eval, _ = expectiminimax(main_player, new_state, depth - 1, False)
        expected_utility += eval * PROBS[dice]
    return expected_utility, None

def expectiminimax(main_player: int, state: MonopolyGame, depth: int=8, chance: bool=False) -> tuple:
    # Expectiminimax algorithm to search for the best action
    if state.is_terminal() or depth == 0:
        return state.evaluate_utility(), None
    # Determining which node we're on
    if chance:
        node = chance_node
    elif state.current_player == main_player:
        node = max_node
    else:
        node = min_node 
    return node(main_player, state, depth)

def play(state: MonopolyGame) -> None:
        num_of_rounds = 0
        # Main game loop to play the game
        while not state.game_over:
            # Get current player from state
            curr_player = state.players[state.current_player]
            print(f"{curr_player.name} is on {curr_player.position} and has {curr_player.money}$,")
            
            if curr_player.is_in_jail:
                print(f"turns in jail {curr_player.turns_in_jail}")
            
            total_dice = curr_player.roll_dice()
            # Moving the player based on the dice outcome
            state.move_player(total_dice)
            print(f"{curr_player.name} lands on {curr_player.position}!", end=" ")

            # Determining the best possible action
            _, best_action = expectiminimax(state.current_player, state)
            
            # Taking the best action
            state = state.take_action(best_action)
            print(f"{curr_player.name} {ACTIONS[best_action]}.")
            print(state.players[state.current_player])
            print(f"Current net worth: {state.evaluate_utility()}")

            if state.is_terminal():
                state.game_over = True
            else:
                state.switch_player()
            num_of_rounds += 1
            print(f"Round: {num_of_rounds}")
            print("====================================================")
        print(f"{state.players[0 if state.current_player else 1].name} Won!")   

# Driver code to start the Monopoly game
if __name__ == "__main__":
    game = MonopolyGame()
    game.initialize_players()
    game.initialize_board("board.csv")
    play(game)
