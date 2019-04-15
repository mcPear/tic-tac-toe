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
            cell_idx = choose_action(q_table, obs)
            obs_ = step(obs, cell_idx)
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
                q_table_obs_ = q_table[obs_] if obs_ in q_table.keys() else [0] * actions_count
                q_table[obs][cell_idx] = (1 - lr) * q_table[obs][cell_idx] + lr * (
                        reward + gamma * np.max(q_table_obs_))
                obs = obs_
        # print(i)
    return q_table


def choose_action(q_table, obs):
    if obs not in q_table.keys():
        q_table[obs] = [0] * actions_count
        return np.random.randint(0, actions_count)
    values = q_table[obs]
    filtered_values = [values[i] if obs.board[i % 3][i / 3] == 0 else np.nan for i in range(len(values))]

    values_exp = np.exp(filtered_values)
    probs = np.nan_to_num(values_exp / np.nansum(values_exp))
    action = np.random.choice(np.arange(len(values)), p=probs)
    return action
