from state import GameState
from q_learn.step_controller import step_states
import numpy as np
import copy
import state as game_state

actions_count = 9


def get_q_table():
    as_first = get_q_table_x_as_first()
    as_second = get_q_table_x_as_second()
    as_first.update(as_second)
    return as_first


def get_q_table_x_as_first():
    state = GameState()
    return get_q_table_for_x([state])


def get_q_table_x_as_second():
    state = GameState()
    init_states = []

    rows, cols = np.where(state.board == 0)
    for i in range(len(rows)):
        state_copy = copy.deepcopy(state)
        x_pos = rows[i]
        y_pos = cols[i]
        state_copy.board[x_pos][y_pos] = game_state.o
        init_states.append(state_copy)

    return get_q_table_for_x(init_states)


def get_q_table_for_x(init_states):
    q_table = dict()
    new_states = init_states
    for init_state in init_states:
        add(init_state, q_table)

    while new_states:
        curr_new_states = []
        for i in range(len(new_states)):
            print(i * 100 / len(new_states))
            state = new_states[i]
            extend_state(state, q_table, curr_new_states)
        new_states = curr_new_states

    return q_table


def extend_state(state, q_table, curr_new_states):
    values = q_table[state]
    for idx in range(len(values)):
        if values[idx][0] is not np.nan:
            gen_states, trans_state = step_states(state, idx)
            values[idx] = (values[idx][0], gen_states, trans_state)
            for gen_state in gen_states:
                add(gen_state, q_table)
                if gen_state not in curr_new_states and gen_state.get_winner() is None:
                    curr_new_states.append(gen_state)


def add(state, q_table):
    if state not in q_table.keys():
        values = [(0, None, None) if state.board[i % 3][i // 3] == 0 else (np.nan, None, None) for i in
                  range(actions_count)]
        q_table[state] = values
