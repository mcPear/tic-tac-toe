import state as game_state
import copy
import numpy as np

o = game_state.o
x = game_state.x


def step(state, cell_idx):
    state_copy = copy.deepcopy(state)
    ai_move(state_copy, cell_idx)
    if state_copy.get_winner() is None:
        opponent_move(state_copy)
    """ don't switch turn twice """
    return state_copy


def ai_move(state, cell_idx):
    x = cell_idx % 3
    y = cell_idx / 3
    state.board[x][y] = state.turn


def opponent_move(state):
    rows, cols = np.where(state.board == 0)
    i = np.random.randint(0, len(rows))
    x = rows[i]
    y = cols[i]
    state.board[x][y] = x if state.turn == o else o
