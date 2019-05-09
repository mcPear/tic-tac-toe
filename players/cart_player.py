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

    def perform_move(self, state):  # fixme limit - cart_player is always X in q_table

        solutions = []
        rows, cols = np.where(state.board == 0)
        for i in range(len(rows)):
            state_copy = copy.deepcopy(state)
            x_pos = rows[i]
            y_pos = cols[i]
            state_copy.board[x_pos][y_pos] = game_state.x
            prediction = self.cart.predict([state_copy.board.flatten().tolist()])
            solutions.append(Solution(state_copy, x_pos, y_pos, prediction))

        max_solution = max(solutions, key=attrgetter('prediction'))

        state.board[max_solution.pos_x][max_solution.pos_x] = state.turn
