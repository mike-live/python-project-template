from kedro.pipeline import node, pipeline
from sklearn.preprocessing import StandardScaler

from .evaluate import evaluate_model
from .plots import plot_predictions
from .split_data import split_data
from .train import train_model


def prepare_data(df_dataset, target_col):
    X_train, X_test, y_train, y_test = split_data(
        df_dataset=df_dataset,
        target_col=target_col,
        scaler=StandardScaler(),
    )

    train_data = X_train.copy()
    train_data[target_col] = y_train

    test_data = X_test.copy()
    test_data[target_col] = y_test

    return train_data, test_data


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=prepare_data,
                inputs={
                    "df_dataset": "boston@raw",
                    "target_col": "params:target_col",
                },
                outputs=[
                    "boston_train@model_input",
                    "boston_test@model_input",
                ],
                name="split_data_node"
            ),
            node(
                func=train_model,
                inputs={
                    "train_data": "boston_train@model_input",
                    "target_col": "params:target_col",
                    "alpha": "params:model_options.alpha",
                    "l1_ratio": "params:model_options.l1_ratio",
                    "max_iter": "params:model_options.max_iter",
                },
                outputs="boston_housing@regression_model",
                name="train_model_node"
            ),
            node(
                func=plot_predictions,
                inputs={
                    "model": "boston_housing@regression_model",
                    "test_data": "boston_test@model_input",
                    "target_col": "params:target_col",
                },
                outputs="prediction_plot",
                name="plot_predictions_node"
            ),
            node(
                func=evaluate_model,
                inputs={
                    "model": "boston_housing@regression_model",
                    "test_data": "boston_test@model_input",
                    "target_col": "params:target_col",
                },
                outputs="boston_housing_metrics@regression_metrics",
                name="evaluate_model_node"
            )
        ]
    )
