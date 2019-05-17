from collections import defaultdict
from tqdm import tqdm
from players.random_player import RandomPlayer
from players.win_selecting_player import WinSelectingPlayer
from players.q_player import QPlayer
from players.cart_player import CartPlayer
from game import Game


def play(playerX, playerO):
    return Game().start(playerX, playerO)


# TODO extract to separate file
def test(playerX, playerO):
    repetitions = 10000
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
win_selecting_player = WinSelectingPlayer()
q_player_random = QPlayer(random_player)
cart_player_random = CartPlayer(100000, random_player)

test(q_player_random, cart_player_random)
test(cart_player_random, q_player_random)







q_player_random = QPlayer(random_player)
# cart_player_random = CartPlayer(100000, random_player) #todo change

# todo error on q_player:22 when qplayer is O, also in qtable there are invalid links to next moves (None)
cart_player_q_learn = CartPlayer(100000, q_player_random)
q_player_cart = QPlayer(cart_player_random)

print("TESTING SELECTING vs RANDOM")
test(win_selecting_player, random_player)
test(random_player, win_selecting_player)


print("TESTING Q-LEARN vs RANDOM")
test(q_player_random, random_player)
test(random_player, q_player_random)
print("TESTING CART vs RANDOM")
test(cart_player_random, random_player)
test(random_player, cart_player_random)
print("TESTING Q-LEARN vs CART")
test(q_player_random, cart_player_random)
test(cart_player_random, q_player_random)


print("TESTING Q-LEARN+ vs RANDOM")
test(q_player_cart, random_player)
test(random_player, q_player_cart)
print("TESTING CART+ vs RANDOM")
test(cart_player_q_learn, random_player)
test(random_player, cart_player_q_learn)
print("TESTING Q-LEARN+ vs CART+")
test(q_player_cart, cart_player_q_learn)
test(cart_player_q_learn, q_player_cart)