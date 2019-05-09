import pickle
from q_learn import q_table_gen

file = '../q_table.pickle'
file_empty = '../q_table_empty.pickle'


def gen_empty_q_table():
    with open(file_empty, 'wb') as handle:
        pickle.dump(q_table_gen.get_q_table(), handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_empty_q_table(generate=False):
    if generate:
        gen_empty_q_table()
    with open(file_empty, 'rb') as handle:
        return pickle.load(handle)
