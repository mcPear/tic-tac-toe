import copy
from state import GameState
import numpy as np
from step_controller import step

actions_count = 9


def get_q_table(q_table_empty, iter_count=10000, lr=0.5, gamma=1):
    q_table = q_table_empty
    state = GameState()
    for i in range(iter_count):
        obs = state
        game_over = False
        while not game_over:
            cell_idx, obs_ = choose_action(q_table, obs)

            winner = obs_.get_winner()

            if winner == state.turn:
                reward = 1
            elif winner is None or winner == 0:
                reward = 0
            else:
                reward = -1

            if winner is not None:
                q_table[obs][cell_idx] = reward
                game_over = True
            else:
                q_table[obs][cell_idx] = (1 - lr) * q_table[obs][cell_idx] + lr * (
                        reward + gamma * np.nanmax(q_table[obs_]))
                obs = obs_
        if (i % 500 == 0):
            print(i)
            print(len(q_table))
    return q_table


def choose_action(q_table, obs):
    value_obses = q_table[obs]
    values = list(map(lambda v: v[0], value_obses))
    values_exp = np.exp(values)
    probs = np.nan_to_num(values_exp / np.nansum(values_exp))
    action_idx = np.random.choice(np.arange(len(values)), p=probs)
    return action_idx, value_obses[action_idx][0]


def add(state, q_table):
    if state not in q_table.keys():
        values = [0] * actions_count
        filtered_values = [values[i] if state.board[i % 3][i / 3] == 0 else np.nan for i in range(len(values))]
        q_table[state] = filtered_values
