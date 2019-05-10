from sklearn import tree


def get_cart(X, y):
    # todo deserialize fitted object instead of creation
    cart = tree.DecisionTreeRegressor()
    cart = cart.fit(X, y)
    return cart
