from sklearn.linear_model import ElasticNet


def train_model(
    train_data,
    target_col,
    alpha=0.1,
    l1_ratio=0.5,
    max_iter=10_000,
):
    X_train = train_data.drop(columns=target_col)
    y_train = train_data[target_col]

    model = ElasticNet(
        alpha=alpha,
        l1_ratio=l1_ratio,
        max_iter=max_iter
    )

    model.fit(X_train, y_train)

    return model
