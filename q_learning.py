import copy
import numpy as np
from step_controller import step

actions_count = 9


def get_q_table(state, iter_count=10000, lr=0.1, gamma=0.9):
    # todo generate all ~400 possible states (board*turn), allow to start by user
    q_table = dict()
    for i in range(iter_count):
        obs = copy.deepcopy(state)
        game_over = False
        while not game_over:
            add(obs, q_table)
            cell_idx = choose_action(q_table, obs)

            obs_ = step(obs, cell_idx)
            add(obs_, q_table)

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
        if(i%500 == 0): print(i)
    return q_table


def choose_action(q_table, obs):
    values = q_table[obs]
    values_exp = np.exp(values)
    probs = np.nan_to_num(values_exp / np.nansum(values_exp))
    action = np.random.choice(np.arange(len(values)), p=probs)
    return action


def add(state, q_table):
    if state not in q_table.keys():
        values = [0] * actions_count
        filtered_values = [values[i] if state.board[i % 3][i / 3] == 0 else np.nan for i in range(len(values))]
        q_table[state] = filtered_values
