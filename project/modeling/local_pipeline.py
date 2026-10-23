from kedro.pipeline import node, pipeline

from .evaluate import evaluate_model
from .pipeline import prepare_data
from .plots import plot_predictions
from .train import train_model


def create__local_pipeline(**kwargs):
    """Запускает те же узлы, но сохраняет все локально без использования MLflow."""
    return pipeline(
        [
            node(
                func=prepare_data,
                inputs={
                    "df_dataset": "boston@raw",
                    "target_col": "params:target_col",
                },
                outputs=[
                    "local_boston_train@model_input",
                    "local_boston_test@model_input",
                ],
                name="local_split_data_node"
            ),
            node(
                func=train_model,
                inputs={
                    "train_data": "local_boston_train@model_input",
                    "target_col": "params:target_col",
                    "alpha": "params:model_options.alpha",
                    "l1_ratio": "params:model_options.l1_ratio",
                    "max_iter": "params:model_options.max_iter",
                },
                outputs="local_boston_housing@pickle",
                name="local_train_model_node"
            ),
            node(
                func=plot_predictions,
                inputs={
                    "model": "local_boston_housing@pickle",
                    "test_data": "local_boston_test@model_input",
                    "target_col": "params:target_col",
                },
                outputs="local_prediction_plot",
                name="local_plot_predictions_node"
            ),
            node(
                func=evaluate_model,
                inputs={
                    "model": "local_boston_housing@pickle",
                    "test_data": "local_boston_test@model_input",
                    "target_col": "params:target_col",
                },
                outputs="local_boston_housing_metrics@json",
                name="local_evaluate_model_node"
            )
        ]
    )
