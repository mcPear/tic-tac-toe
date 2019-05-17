from collections import defaultdict

import pandas as pd
import seaborn as sns
import numpy as np
from pandas import DataFrame
from sklearn.externals.six import StringIO
from sklearn.tree import export_graphviz, plot_tree
import pydotplus
from sklearn import tree
import matplotlib.pyplot as plt

from cart.dataset_gen import merge_data_w_label, get_dataset
from cart.training import train
from players.random_player import RandomPlayer
from q_learn.q_learning import get_q_table
from q_table_manager import load_empty_q_table


def visualize(model, filename):
    plot_tree(model, filled=True)
    plt.show()
    # dot_data = StringIO()
    # export_graphviz(model, out_file=dot_data,
    #                 filled=True, rounded=True,
    #                 special_characters=True)
    # graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    # graph.write_png(filename)


def visualize_table(table, filename=None):
    aggregated = []
    i = 0
    for column in table:
        if column == 'outcome': break
        if int(column) % 3 == 0:
            i += 1
            aggregated.append([])

        temp = pd.concat([DataFrame(table[column]), table['outcome']], axis=1)
        temp = temp.loc[temp[column] == 1.0]
        aggregated[int(column) // 3].append(temp['outcome'].sum())
    print(aggregated)
    aggregated = np.array(aggregated)
    row_sums = aggregated.sum(axis=1)
    normalized = aggregated / row_sums[:, np.newaxis]
    sns.heatmap(normalized, annot=True)
    plt.show()


# todo try now
# data = get_dataset(RandomPlayer(), 100000, merge=True)
# visualize_table(data)
#
# q_table_empty = load_empty_q_table()
# table = get_q_table(q_table_empty, RandomPlayer())
# visualize_table(table)
# cart = tree.DecisionTreeRegressor(criterion="mae", max_depth=10, min_samples_leaf=6)
# _, fitted_cart, _ = train(n_folds=5, data=data, cart=cart)
# visualize(fitted_cart, filename='../analysis_plots/h1.png')
