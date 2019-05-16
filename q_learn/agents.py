import random

""" 
state argument is state before agent move 
possible_states argument are all possible states after agent move
sign argument is agent sign (x or o)
"""


def random_agent(state, possible_states, sign):
    print(sign)
    return random.choice(possible_states)
