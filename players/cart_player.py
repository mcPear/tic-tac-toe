import copy
import numpy as np
import state as game_state
from cart.solution import Solution
from players.player import Player
from operator import attrgetter


class CartPlayer(Player):

    def __init__(self, cart):
        self.cart = cart
        super().__init__()

    def perform_move(self, state, sign):
        if sign != state.turn:
            raise Exception(f"Turn ({state.turn}) is not corresponding to player sign ({sign})")
        solutions = []
        rows, cols = np.where(state.board == 0)
        for i in range(len(rows)):
            state_copy = copy.deepcopy(state)
            x_pos = rows[i]
            y_pos = cols[i]
            state_copy.board[x_pos][y_pos] = sign
            state_as_list = state_copy.get_board_as_list() if sign == game_state.x else state_copy.get_board_negative_as_list()
            prediction = self.cart.predict([state_as_list])
            solutions.append(Solution(state_copy, x_pos, y_pos, prediction))

        max_solution = max(solutions, key=attrgetter('prediction'))

        state.board[max_solution.pos_x][max_solution.pos_y] = sign
