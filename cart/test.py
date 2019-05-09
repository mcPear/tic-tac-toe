from cart.dataset_gen import get_dataset
import pickle

file_empty = '../q_learn/q_table_empty.pickle'


def load_empty_q_table():
    with open(file_empty, 'rb') as handle:
        return pickle.load(handle)


print("LOADING EMPTY Q-TABLE...")
q_table_empty = load_empty_q_table()
print("CREATING DATASET...")
dataset = get_dataset(q_table_empty)
print(len(dataset))
