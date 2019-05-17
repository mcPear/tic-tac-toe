from sklearn import tree

from cart.dataset_gen import merge_data_w_label
from cart.training import train


def get_cart(X, y):
    # todo deserialize fitted object instead of creation
    cart = tree.DecisionTreeRegressor(criterion="mae", max_depth=10, min_samples_leaf=4)
    _, fitted_cart, _ = train(n_folds=5, data=merge_data_w_label(X, y), cart=cart)
    return fitted_cart
