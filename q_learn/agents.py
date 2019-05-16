import random

""" 
state argument is state before agent move 
possible_states argument are all possible states after agent move
"""


def random_agent(state, possible_states):
    return random.choice(possible_states)
