import copy
from state import GameState
import numpy as np
import state as game_state
from q_table_manager import load_empty_q_table
from tqdm import tqdm
import pandas as pd

actions_count = 9


def get_dataset(agent, iter_count=50000, merge=False):
    q_table_empty = load_empty_q_table()

    state = GameState()
    state_x_as_first = state
    states_x_as_second = []
    dataset = dict()

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

    play_from_state(state_x_as_first, x_as_first_iter_count, q_table, dataset, agent, game_state.o)
    for s in states_x_as_second:
        play_from_state(s, x_as_second_iter_count, q_table, dataset, agent, game_state.x)

    dataset = [state.board.flatten().tolist() + [stats[0] / (stats[0] + stats[1] + stats[2])] for state, stats in
               dataset.items()]

    X = [e[0:-1] for e in dataset]
    y = [e[-1] for e in dataset]

    if merge:
        return merge_data_w_label(X, y)
    else:
        return X, y


def merge_data_w_label(X, y):
    data = pd.DataFrame(X)
    data['outcome'] = y
    return data


def play_from_state(state, iter_count, q_table, dataset, agent, opponent_sign):
    for _ in tqdm(range(iter_count)):
        # print (q_table[state])

        obs = state
        game_over = False
        trans_states_sequence = []
        while not game_over:
            cell_idx, obs_, trans_state = choose_action(q_table, obs, agent, opponent_sign)

            trans_states_sequence.append(trans_state)
            winner = obs_.get_winner()

            if winner is not None:

                if winner == state.turn:
                    result = 1
                elif winner == 0:
                    result = 0
                else:
                    result = -1

                handle_result(result, trans_states_sequence, dataset)
                game_over = True
            else:
                obs = obs_


def handle_result(result, trans_states_sequence, dataset):  # todo symmetry
    for state in trans_states_sequence:
        wins, draws, looses = 0, 0, 0
        if result == 1:
            wins += 1
        elif result == 0:
            draws += 1
        else:
            looses += 1

        if state in dataset.keys():
            wins_old, draws_old, looses_old = dataset[state]
            wins += wins_old
            draws += draws_old
            looses += looses_old

        dataset[state] = (wins, draws, looses)


def choose_action(q_table, obs, agent, opponent_sign):
    value_obses = q_table[obs]
    values = list(map(lambda v: v[0], value_obses))
    action_idx = np.random.choice(np.argwhere(~np.isnan(values)).flatten())
    obses_possible_after_action = value_obses[action_idx][1]
    trans_state = value_obses[action_idx][2]
    obs_after_random_opponent_play = agent.perform_move(trans_state, opponent_sign, obses_possible_after_action)

    return action_idx, obs_after_random_opponent_play, trans_state
