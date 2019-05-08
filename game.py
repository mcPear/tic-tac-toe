import numpy as np

from state import GameState


class Game:

    def __init__(self, q_table):
        self.q_table = q_table
        self.state = GameState()

    def start(self, opponent):

        while 1:
            self.q_table_move()
            if self.state.get_winner() is not None:
                return self.end()

            opponent.perform_move(self.state)
            self.state.switch_turn()
            if self.state.get_winner() is not None:
                return self.end()

    def end(self):
        return self.state.get_winner()

    def q_table_move(self):
        # print(self.q_table[self.state])
        cell_idx = np.nanargmax(list(map(lambda v: v[0], self.q_table[self.state])))
        # print(self.state.board)
        # print(cell_idx)
        x = cell_idx % 3
        y = cell_idx // 3
        self.state.board[x][y] = self.state.turn
        # print(self.state.board)
        # print("")
        self.state.switch_turn()
