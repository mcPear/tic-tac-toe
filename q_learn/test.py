from collections import defaultdict

from tqdm import tqdm

from players.random_player import RandomPlayer
from players.q_player import QPlayer
import pickle
from game import Game
from q_learn import q_table_gen
from q_learn.q_learning import get_q_table

file = 'q_learn/q_table.pickle'
file_empty = 'q_learn/q_table_empty.pickle'


def play(player1, player2, x_first):
    return Game().start(player1, player2, x_first)


def gen_empty_q_table():
    with open(file_empty, 'wb') as handle:
        pickle.dump(q_table_gen.get_q_table(), handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_empty_q_table():
    with open(file_empty, 'rb') as handle:
        return pickle.load(handle)


# gen_empty_q_table()

# TODO extract to separate file
def test(player1, player2, x_first=True):
    repetitions = 1000
    results = defaultdict(int)

    for _ in tqdm(range(0, repetitions)):
        result = play(player1, player2, x_first)
        # result_text = 'x' if result == 1 else ('o' if result == -1 else 'draw')
        results[result] += 1

    all = sum(results.values())
    x = results[1]
    o = results[-1]
    d = results[0]
    print(f"X won {x} times {(x / all) * 100}%")
    print(f"O won {o} times {(o / all) * 100}%")
    print(f"draw {d} times {(d / all) * 100}%")


def get_q_player():
    print("LOADING EMPTY Q-TABLE...")
    q_table_empty = load_empty_q_table()
    print("FILLING Q-TABLE...")
    q_table = get_q_table(q_table_empty)
    print("TESTING...")
    return QPlayer(q_table)


q_player = get_q_player()
test(q_player, RandomPlayer(), True)
test(RandomPlayer(), q_player, False)
