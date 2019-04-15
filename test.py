from state import GameState
from q_learning import get_q_table
import pickle
from game import Game

file = 'q_table.pickle'


def train():
    s = GameState()
    q_table = get_q_table(s, 10000)

    with open(file, 'wb') as handle:
        pickle.dump(q_table, handle, protocol=pickle.HIGHEST_PROTOCOL)


def play():
    with open(file, 'rb') as handle:
        q_table = pickle.load(handle)

    game = Game(q_table)
    game.start()


play()
