import numpy as np

from state import GameState
import state as game_state


class Game:

    def __init__(self):
        self.state = GameState()

    def start(self, playerX, playerO):

        while 1:
            self.state = playerX.perform_move(self.state, game_state.x)
            if self.state.get_winner() is not None:
                return self.end()
            self.state.switch_turn()

            self.state = playerO.perform_move(self.state, game_state.o)
            if self.state.get_winner() is not None:
                return self.end()
            self.state.switch_turn()

    def end(self):
        return self.state.get_winner()
