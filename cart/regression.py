from sklearn import tree


def get_cart(X, y):
    cart = tree.DecisionTreeRegressor()
    cart = cart.fit(X, y)
    return cart
