from cart.regression import get_cart
from cart.dataset_gen import get_dataset

X, y = get_dataset(10000)
cart = get_cart(X, y)
pred = cart.predict(X)

for i in range(len(y)):
    print(f"{y[i][-1]} | {pred[i]}")
