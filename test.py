from state import GameState
from q_learning import get_q_table
import pickle
from game import Game
import q_table_gen
from q_learning import get_q_table

file = 'q_table.pickle'
file_empty = 'q_table_empty.pickle'


def play(q_table_empty):
    q_table = get_q_table(q_table_empty)
    game = Game(q_table)
    game.start()


def gen_empty_q_table():
    with open(file_empty, 'wb') as handle:
        pickle.dump(q_table_gen.get_q_table(), handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_empty_q_table():
    with open(file_empty, 'rb') as handle:
        return pickle.load(handle)


q_table_empty = load_empty_q_table()
play(q_table_empty)
