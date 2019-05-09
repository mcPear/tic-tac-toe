from cart.regression import get_cart
from cart.dataset_gen import get_dataset

dataset = get_dataset(10000)
X = [e[0:-1] for e in dataset]
y = [e[-1] for e in dataset]
cart = get_cart(X, y)
pred = cart.predict(X)

for i in range(len(dataset)):
    print(f"{dataset[i][-1]} | {pred[i]}")
