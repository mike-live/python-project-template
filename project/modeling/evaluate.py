from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)


def evaluate_model(model, X_test, y_test):
    if y_test.ndim == 2:
        y_test = y_test.iloc[:, 0]

    predictions = model.predict(X_test)

    return {
    "mae": {
        "value": float(mean_absolute_error(y_test, predictions)),
        "step": 0,
    },
    "rmse": {
        "value": float(
            mean_squared_error(y_test, predictions) ** 0.5
        ),
        "step": 0,
    },
    "r2": {
        "value": float(r2_score(y_test, predictions)),
        "step": 0
    }
}

