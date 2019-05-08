import random
import numpy as np

from players.player import Player


class QPlayer(Player):

    def __init__(self, q_table):
        self.q_table = q_table
        super().__init__()

    def perform_move(self, state):
        # print(self.q_table[self.state])
        cell_idx = np.nanargmax(list(map(lambda v: v[0], self.q_table[state])))
        # print(self.state.board)
        # print(cell_idx)
        x = cell_idx % 3
        y = cell_idx // 3
        state.board[x][y] = state.turn
        # print(self.state.board)
        # print("")