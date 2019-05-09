import state as game_state
import copy
import numpy as np

o = game_state.o
x = game_state.x


def step_states(state, cell_idx):
    return_states = []
    state_copy = copy.deepcopy(state)
    ai_move(state_copy, cell_idx)
    if state_copy.get_winner() is None:
        rows, cols = np.where(state_copy.board == 0)
        for i in range(len(rows)):
            state_copy_2 = copy.deepcopy(state_copy)
            x_pos = rows[i]
            y_pos = cols[i]
            state_copy_2.board[x_pos][y_pos] = x if state_copy_2.turn == o else o
            return_states.append(state_copy_2)
    else:
        return_states.append(state_copy)
    return return_states


def ai_move(state, cell_idx):
    x_pos = cell_idx % 3
    y_pos = cell_idx // 3
    state.board[x_pos][y_pos] = state.turn
