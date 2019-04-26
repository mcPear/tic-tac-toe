from state import GameState
from step_controller import step_states
import numpy as np

actions_count = 9


def get_q_table():
    state = GameState()
    q_table = dict()
    add(state, q_table)
    new_states = [state]
    while new_states:
        curr_new_states = []
        for i in range(len(new_states)):
            #print (i * 100 / len(new_states))
            state = new_states[i]
            values = q_table[state]
            for idx in range(len(values)):
                if values[idx][0] is not np.nan:
                    gen_states = step_states(state, idx)
                    for gen_state in gen_states:
                        values[idx] = (values[idx][0], gen_state)
                        add(gen_state, q_table)
                        if gen_state not in curr_new_states and gen_state.get_winner() is None:
                            curr_new_states.append(gen_state)
        new_states = curr_new_states

    return q_table


def add(state, q_table):
    if state not in q_table.keys():
        values = [(0, None) if state.board[i % 3][i // 3] == 0 else (np.nan, None) for i in range(actions_count)]
        q_table[state] = values
