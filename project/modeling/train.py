from sklearn.linear_model import ElasticNet


def train_model(
    X_train,
    y_train,
    alpha=0.1,
    l1_ratio=0.5,
    max_iter=10_000,
):
    if y_train.ndim == 2:
        y_train = y_train.iloc[:, 0]

    model = ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        max_iter=max_iter
    )

    model.fit(X_train, y_train)

    return model
