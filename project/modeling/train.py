from sklearn.linear_model import ElasticNet
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler, RobustScaler, StandardScaler


def create_scaler(name):
    scalers = {
        "standard": StandardScaler,
        "minmax": MinMaxScaler,
        "robust": RobustScaler,
    }

    if name == "none":
        return "passthrough"

    if name not in scalers:
        raise ValueError(
            f"Неизвестный scaler: {name!r}. "
            f"Доступны: {', '.join(scalers)}, none."
        )

    return scalers[name]()


def create_model(
    scaler="standard",
    alpha=0.1,
    l1_ratio=0.5,
    max_iter=10_000,
):
    return Pipeline(
        steps=[
            ("scaler", create_scaler(scaler)),
            (
                "model",
                ElasticNet(
                    alpha=alpha,
                    l1_ratio=l1_ratio,
                    max_iter=max_iter,
                ),
            ),
        ]
    )


def train_model(
    X_train,
    y_train,
    scaler="standard",
    alpha=0.1,
    l1_ratio=0.5,
    max_iter=10_000,
):
    if y_train.ndim == 2:
        y_train = y_train.iloc[:, 0]

    model = create_model(
        scaler=scaler,
        alpha=alpha,
        l1_ratio=l1_ratio,
        max_iter=max_iter
    )

    model.fit(X_train, y_train)

    return model


def train_best_model(
    X_train,
    y_train,
    best_params,
    model_options,
):
    return train_model(
        X_train=X_train,
        y_train=y_train,
        scaler=model_options["scaler"],
        max_iter=model_options["max_iter"],
        **best_params,
    )
