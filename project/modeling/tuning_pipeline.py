from kedro.pipeline import node, pipeline

from .evaluate import evaluate_model
from .plots import plot_predictions
from .split_data import split_data
from .train import train_best_model
from .tuning import tune_parameters


def create_pipeline(**kwargs):
    return pipeline(
        [
            node(
                func=split_data,
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
                func=tune_parameters,
                inputs={
                    "X_train": "X_train@model_input",
                    "y_train": "y_train@model_input",
                    "search_space": "params:search_space",
                    "model_options": "params:model_options",
                    "tuning_options": "params:tuning_options",
                },
                outputs="best_params",
                name="tune_parameters_node",
            ),
            node(
                func=train_best_model,
                inputs={
                    "X_train": "X_train@model_input",
                    "y_train": "y_train@model_input",
                    "best_params": "best_params",
                    "model_options": "params:model_options",
                },
                outputs="model@regression_model",
                name="train_best_model_node",
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
