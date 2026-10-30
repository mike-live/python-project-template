from kedro.pipeline import node, pipeline
from sklearn.preprocessing import StandardScaler

from .evaluate import evaluate_model
from .plots import plot_predictions
from .split_data import split_data
from .train import train_model


def prepare_data(df_dataset, target_col, test_size=0.2, random_state=42):
    X_train, X_test, y_train, y_test = split_data(
        df_dataset=df_dataset,
        target_col=target_col,
        scaler=StandardScaler(),
        test_size=test_size,
        random_state=random_state,
    )

    return X_train, X_test, y_train.to_frame(), y_test.to_frame()


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=prepare_data,
                inputs={
                    "df_dataset": "source@raw",
                    "target_col": "params:target_col",
                    "test_size": "params:split_options.test_size",
                    "random_state": "params:split_options.random_state",
                },
                outputs=[
                    "X_train@model_input",
                    "X_test@model_input",
                    "y_train@model_input",
                    "y_test@model_input",
                ],
                name="split_data_node"
            ),
            node(
                func=train_model,
                inputs={
                    "X_train": "X_train@model_input",
                    "y_train": "y_train@model_input",
                    "alpha": "params:model_options.alpha",
                    "l1_ratio": "params:model_options.l1_ratio",
                    "max_iter": "params:model_options.max_iter",
                },
                outputs="model@regression_model",
                name="train_model_node"
            ),
            node(
                func=plot_predictions,
                inputs={
                    "model": "model@regression_model",
                    "X_test": "X_test@model_input",
                    "y_test": "y_test@model_input",
                },
                outputs="predictions@prediction_plot",
                name="plot_predictions_node"
            ),
            node(
                func=evaluate_model,
                inputs={
                    "model": "model@regression_model",
                    "X_test": "X_test@model_input",
                    "y_test": "y_test@model_input",
                },
                outputs="metrics@regression_metrics",
                name="evaluate_model_node"
            )
        ]
    )
