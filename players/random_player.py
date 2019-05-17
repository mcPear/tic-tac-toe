import random

from players.player import Player


class RandomPlayer(Player):

    def __init__(self):
        super().__init__()

    def perform_move(self, state, sign, possible_states=None, validate=True):
        """
        state argument is state before agent move
        sign argument is agent sign (x or o)
        possible_states argument are all possible states after agent move, use it if available to speed up
        """
        if validate and sign != state.turn:
            raise Exception(f"Turn ({state.turn}) is not corresponding to player sign ({sign})")
        if possible_states:
            return random.choice(possible_states)
        moves = state.get_available_moves_indices()
        row, col = random.choice(moves)
        state.board[row][col] = sign
        return state
