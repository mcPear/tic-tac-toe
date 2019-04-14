import numpy as np


class GameState:

    def __init__(self):
        self.board = np.zeros((3, 3))
        self.turn = False

    def set_cross(self, x, y):
        self.set_elem(x, y, 1)

    def set_circle(self, x, y):
        self.set_elem(x, y, -1)

    def set_elem(self, x, y, elem):
        self.board[x][y] = elem

    def get_winner(self):
        x = 'X'
        o = 'O'
        sum_ax_0 = np.sum(self.board, 0)
        if 3 in sum_ax_0: return x
        if -3 in sum_ax_0: return o
        sum_ax_1 = np.sum(self.board, 1)
        if 3 in sum_ax_1: return x
        if -3 in sum_ax_1: return o
        sum_diag_0 = np.trace(self.board, 0)
        if 3 == sum_diag_0: return x
        if -3 == sum_diag_0: return o
        sum_diag_1 = np.trace(self.board, 1)
        if 3 == sum_diag_1: return x
        if -3 == sum_diag_1: return o


def test():
    state = GameState()
    state.set_circle(2, 2)
    state.set_circle(1, 1)
    state.set_circle(0, 0)
    print(state.board.transpose())
    print(state.get_winner())

test()
