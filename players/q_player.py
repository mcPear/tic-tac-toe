import random
import numpy as np
import state as game_state

from players.player import Player


class QPlayer(Player):

    def __init__(self, q_table):
        self.q_table = q_table
        super().__init__()

    def perform_move(self, state, sign):
        if sign != state.turn:
            raise Exception(f"Turn ({state.turn}) is not corresponding to player sign ({sign})")
        if sign is not game_state.x:
            state.negative_state()
        cell_idx = np.nanargmax(list(map(lambda v: v[0], self.q_table[state])))
        if sign is not game_state.x:
            state.negative_state()
        x = cell_idx % 3
        y = cell_idx // 3
        state.board[x][y] = sign
