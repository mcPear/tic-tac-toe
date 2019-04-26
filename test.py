from collections import defaultdict

from tqdm import tqdm

from players.random_player import RandomPlayer
import pickle
from game import Game
import q_table_gen
from q_learning import get_q_table

file = 'q_table.pickle'
file_empty = 'q_table_empty.pickle'


def play(q_table_empty, opponent=RandomPlayer(), draw=False):
    q_table = get_q_table(q_table_empty)
    game = Game(q_table, draw)
    return game.start(opponent)


def gen_empty_q_table():
    with open(file_empty, 'wb') as handle:
        pickle.dump(q_table_gen.get_q_table(), handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_empty_q_table():
    with open(file_empty, 'rb') as handle:
        return pickle.load(handle)


# gen_empty_q_table()

#TODO extract to separate file
repetitions = 100
results = defaultdict(int)
for _ in tqdm(range(0, repetitions)):
    q_table_empty = load_empty_q_table()
    result = play(q_table_empty)
    # result_text = 'x' if result == 1 else ('o' if result == -1 else 'draw')
    results[result] += 1

#TODO extract to method
all = sum(results.values())
x = results[1]
o = results[-1]
d = results[0]
print(f"X won {x} times {(x / all)*100}%")
print(f"O won {o} times {(o / all)*100}%")
print(f"draw {d} times {(d / all)*100}%")
