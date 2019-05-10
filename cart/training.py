from sklearn.model_selection import KFold

from cart.dataset_gen import get_dataset
from sklearn import tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# TODO extract methods ?
def check_equal(lst1, lst2):
    return lst1[1:] == lst2[:-1]


# https://scikit-learn.org/stable/modules/cross_validation.html#stratified-k-fold
def get_n_folds(dataset, n):
    skf = KFold(n_splits=n, shuffle=True)

    return calc_folds(skf, dataset)


def calc_folds(fold_obj, dataset):
    folds = []
    split = fold_obj.split(dataset)
    for train_indices, test_indices in split:
        folds.append((dataset.iloc[train_indices, :], dataset.iloc[test_indices, :]))
    return folds


def train(n_folds, data, cart):
    folds = get_n_folds(data, n_folds)
    errs = []
    best_err = float("inf")
    best_model = None

    for train, test in folds:
        cart = cart.fit(train.iloc[:, :-1], train.iloc[:, -1])

        # calc MSE
        pred = cart.predict(test.iloc[:, :-1])
        actual = test.iloc[:, -1]
        mae = np.mean(np.absolute(actual - pred))
        if mae < best_err:
            best_err = mae
            best_model = cart
        errs.append(mae)

    return errs, best_model, best_err  # delete errs from return


### PARAMETERS ANALYSIS, DELETE AFTER TWEAKING MODEL
def analyze(model, data):
    model_errs = []
    analyzed_range = range(1, 30)
    for i in analyzed_range:
        print(f"Evaluating param: {i}")
        errs, best_model, best_err = train(5, data, model(i))
        mean_err = np.mean(errs)
        model_errs.append(mean_err)
        print(f"Best model's error: {best_err}")
    plt.plot(analyzed_range, model_errs)
    plt.show()


def test():
    data = get_dataset(100000, merge=True)
    print(f"data_length: {len(data)}")
    # data = pd.DataFrame(X)
    # data['outcome'] = y

    analyze(lambda i: tree.DecisionTreeRegressor(criterion="mae", min_samples_leaf=i), data)
    analyze(lambda i: tree.DecisionTreeRegressor(criterion="mae", max_depth=i), data)

# TODO:
# - serialize best model
# - read serialized model on cart agent creation
# - analyze for parameter's best value: max_depth, min_samples_leaf. Can also pass a factor instead of int
# - check if best CART generalizes train data (check size of tree)
# - consider using PCA for feature reduction?
