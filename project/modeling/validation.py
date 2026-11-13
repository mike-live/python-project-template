from sklearn.model_selection import KFold, cross_val_score


def cross_validate_model(
    model,
    X_train,
    y_train,
    n_splits=5,
    random_state=42,
):
    if y_train.ndim == 2:
        y_train = y_train.iloc[:, 0]

    cv = KFold(
        n_splits=n_splits,
        shuffle=True,
        random_state=random_state,
    )

    scores = cross_val_score(
        estimator=model,
        X=X_train,
        y=y_train,
        cv=cv,
        scoring="neg_mean_absolute_error",
        error_score="raise",
    )

    return float(-scores.mean())
