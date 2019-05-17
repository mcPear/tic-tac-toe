import random

from players.player import Player


class WinSelectingPlayer(Player):

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
        possible_states = self.guarantee_possible_states(state, sign, possible_states)
        states_without_loss = list(filter(lambda s: s.get_winner() is not -sign, possible_states))
        if states_without_loss:
            possible_states = states_without_loss
        win_states = list(filter(lambda s: s.get_winner() is sign, possible_states))
        if win_states:
            possible_states = win_states
        return random.choice(possible_states)
