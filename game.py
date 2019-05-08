import numpy as np

from state import GameState


class Game:

    def __init__(self):
        self.state = GameState()

    def start(self, player_1, player_2):

        while 1:
            player_1.perform_move(self.state)
            if self.state.get_winner() is not None:
                return self.end()
            self.state.switch_turn()

            player_2.perform_move(self.state)
            if self.state.get_winner() is not None:
                return self.end()
            self.state.switch_turn()

    def end(self):
        return self.state.get_winner()
