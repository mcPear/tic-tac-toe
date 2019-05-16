import numpy as np
import state as game_state
from q_learn.q_learning import get_q_table
from q_table_manager import load_empty_q_table
from players.player import Player


class QPlayer(Player):

    def __init__(self, agent):
        self.q_table = self.create_q_table(agent)
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
        return state

    def create_q_table(self, agent):
        print("LOADING EMPTY Q-TABLE...")
        q_table_empty = load_empty_q_table()
        print("FILLING Q-TABLE...")
        return get_q_table(q_table_empty, agent)
