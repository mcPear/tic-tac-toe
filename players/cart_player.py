import copy
import numpy as np
import state as game_state
from cart.solution import Solution
from players.player import Player
from operator import attrgetter
from cart.regression import get_cart
from cart.dataset_gen import get_dataset


class CartPlayer(Player):

    def __init__(self, iter_count, agent):
        self.cart = self.create_cart(iter_count, agent)
        super().__init__()

    # possible_moves and curr_action for interoperability with qlearning
    def perform_move(self, state, sign, possible_moves=None, validate=True):
        if validate and sign != state.turn:
            raise Exception(f"Turn ({state.turn}) is not corresponding to player sign ({sign})")
        solutions = []

        if possible_moves:
            for pos_move in possible_moves:
                state_as_list = pos_move.get_board_as_list() if sign == game_state.x else pos_move.get_board_negative_as_list()
                prediction = self.cart.predict([state_as_list])
                solutions.append({'move': pos_move, 'prediction': prediction})

            max_solution = max(solutions, key=lambda x: x['prediction'])
            return max_solution['move']
        else:
            rows, cols = np.where(state.board == 0)
            for i in range(len(rows)):
                state_copy = copy.deepcopy(state)
                x_pos = rows[i]
                y_pos = cols[i]
                state_copy.board[x_pos][y_pos] = sign
                state_as_list = state_copy.get_board_as_list() if sign == game_state.x else state_copy.get_board_negative_as_list()
                prediction = self.cart.predict([state_as_list])
                solutions.append(Solution(state_copy, x_pos, y_pos, prediction))

            # if len(solutions) == 0: return possible_moves[0]
            max_solution = max(solutions, key=attrgetter('prediction'))

            state.board[max_solution.pos_x][max_solution.pos_y] = sign
            return state

    def create_cart(self, iter_count, agent):
        print("CREATING DATASET...")
        X, y = get_dataset(agent, iter_count=iter_count)
        print("FITTING CART...")
        return get_cart(X, y)
