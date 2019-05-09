import random

from players.player import Player


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def perform_move(self, state, sign):
        moves = state.get_available_moves_indices()
        row, col = random.choice(moves)
        state.board[row][col] = state.turn
