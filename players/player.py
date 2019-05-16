import numpy as np
import copy


class Player:
    def __init__(self):
        super().__init__()

    def guarantee_possible_states(self, state, sign, possible_states):
        if not possible_states:
            possible_states = []
            rows, cols = np.where(state.board == 0)
            for i in range(len(rows)):
                state_copy = copy.deepcopy(state)
                x_pos = rows[i]
                y_pos = cols[i]
                state_copy.board[x_pos][y_pos] = sign
                possible_states.append(state_copy)
        return possible_states
