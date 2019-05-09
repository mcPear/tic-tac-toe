import copy
from state import GameState
import numpy as np
import state as game_state

actions_count = 9


def get_q_table(q_table_empty, iter_count=10000, lr=0.05, gamma=0.9):
    state = GameState()
    state_x_as_first = state
    states_x_as_second = []

    rows, cols = np.where(state.board == 0)
    for i in range(len(rows)):
        state_copy = copy.deepcopy(state)
        x_pos = rows[i]
        y_pos = cols[i]
        state_copy.board[x_pos][y_pos] = game_state.o
        states_x_as_second.append(state_copy)

    q_table = q_table_empty

    x_as_first_iter_count = iter_count // 2
    x_as_second_iter_count = x_as_first_iter_count // actions_count
    
    play_from_state(state_x_as_first, x_as_first_iter_count, lr, gamma, q_table)
    for s in states_x_as_second:
        play_from_state(s, x_as_second_iter_count, lr, gamma, q_table)

    return q_table


def play_from_state(state, iter_count, lr, gamma, q_table):
    for i in range(iter_count):
        # print (q_table[state])
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

            obses = q_table[obs][cell_idx][1]
            if winner is not None:
                q_table[obs][cell_idx] = (reward, obses)
                game_over = True
            else:
                q_table[obs][cell_idx] = ((1 - lr) * q_table[obs][cell_idx][0] + lr * (
                        reward + gamma * np.nanmax(list(map(lambda v: v[0], q_table[obs_])))), obses)
                obs = obs_

        # if (i % 500 == 0):
        # print(i)
        # print(len(q_table))


def choose_action(q_table, obs):
    value_obses = q_table[obs]
    values = list(map(lambda v: v[0], value_obses))
    values_exp = np.exp(values)
    probs = np.nan_to_num(values_exp / np.nansum(values_exp))
    action_idx = np.random.choice(np.arange(len(values)), p=probs)
    # todo consider using epsilon here to allow exploration
    obses_possible_after_action = value_obses[action_idx][1]
    obs_after_random_opponent_play = np.random.choice(obses_possible_after_action)

    return action_idx, obs_after_random_opponent_play
