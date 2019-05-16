from collections import defaultdict
from tqdm import tqdm
from players.random_player import RandomPlayer
from players.q_player import QPlayer
from players.cart_player import CartPlayer
from game import Game


def play(playerX, playerO):
    return Game().start(playerX, playerO)


# TODO extract to separate file
def test(playerX, playerO):
    repetitions = 500
    results = defaultdict(int)

    for _ in tqdm(range(0, repetitions)):
        result = play(playerX, playerO)
        # result_text = 'x' if result == 1 else ('o' if result == -1 else 'draw')
        results[result] += 1

    all = sum(results.values())
    x = results[1]
    o = results[-1]
    d = results[0]
    print(f"\n{playerX.__class__.__name__} as X vs. {playerO.__class__.__name__} as O")
    print(f"X won {x} times {(x / all) * 100}%")
    print(f"O won {o} times {(o / all) * 100}%")
    print(f"draw {d} times {(d / all) * 100}%")


random_player = RandomPlayer()
q_player = QPlayer(random_player)
cart_player = CartPlayer(5000, random_player)
print("TESTING...")
test(q_player, cart_player)
test(cart_player, q_player)
test(cart_player, random_player)
test(random_player, cart_player)
test(q_player, RandomPlayer())
test(RandomPlayer(), q_player)
