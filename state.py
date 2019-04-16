import numpy as np

x = 1
o = -1


class GameState:

    def __init__(self):
        self.board = np.zeros((3, 3))
        self.turn = x

    def get_winner(self):
        """ 1 is cross, -1 is circle, 0 is draw"""
        sum_ax_0 = np.sum(self.board, 0)
        if 3 in sum_ax_0: return x
        if -3 in sum_ax_0: return o
        sum_ax_1 = np.sum(self.board, 1)
        if 3 in sum_ax_1: return x
        if -3 in sum_ax_1: return o
        sum_diag_0 = np.trace(self.board)
        print (sum_diag_0)
        if 3 == sum_diag_0: return x
        if -3 == sum_diag_0: return o
        sum_diag_1 = np.trace(np.fliplr(self.board))
        print (sum_diag_1)
        if 3 == sum_diag_1: return x
        if -3 == sum_diag_1: return o
        if np.count_nonzero(self.board) == 9: return 0

    def switch_turn(self):
        self.turn = x if self.turn == o else o

    def __eq__(self, other):
        return type(self) is type(other) and self.turn == other.turn and np.array_equal(self.board, other.board)

    def __hash__(self):
        return hash(type(self)) + hash(self.turn) + hash(self.board.tostring())
