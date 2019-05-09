from collections import defaultdict
from tqdm import tqdm
from players.random_player import RandomPlayer
from players.q_player import QPlayer
from players.cart_player import CartPlayer
from game import Game
from q_learn.q_learning import get_q_table
from q_table_manager import load_empty_q_table
from cart.regression import get_cart
from cart.dataset_gen import get_dataset


def play(player1, player2, x_first):
    return Game().start(player1, player2, x_first)


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
    return QPlayer(q_table)


def get_cart_player():
    print("CREATING DATASET...")
    X, y = get_dataset()
    print("FITTING CART...")
    cart = get_cart(X, y)
    return CartPlayer(cart)


q_player = get_q_player()
cart_player = get_cart_player()
print("TESTING...")
test(q_player, RandomPlayer(), True)
test(RandomPlayer(), q_player, False)
test(cart_player, RandomPlayer(), True)
test(RandomPlayer(), cart_player, False)
