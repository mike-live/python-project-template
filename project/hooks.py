"""Additional experiment metadata for Kedro-managed MLflow runs."""

from pathlib import Path

import mlflow
from kedro.framework.hooks import hook_impl
from mlflow.data.dataset_source_registry import resolve_dataset_source
from mlflow.data.meta_dataset import MetaDataset


class ExperimentMetadataHook:
    @hook_impl(hookwrapper=True)
    def before_pipeline_run(self, pipeline, catalog):
        # Wait until kedro-mlflow has created the run, regardless of hook order.
        outcome = yield
        outcome.get_result()
        if mlflow.active_run() is None:
            return

        parameters = catalog.load("parameters")
        tags = {}
        raw_inputs = sorted(name for name in pipeline.inputs() if name.endswith("@raw"))
        if "dataset_name" in parameters:
            tags["dataset"] = parameters["dataset_name"]
            mlflow.log_param("dataset_name", parameters["dataset_name"])
        elif raw_inputs:
            tags["dataset"] = ",".join(name.removesuffix("@raw") for name in raw_inputs)
        if "target_col" in parameters:
            tags["target_col"] = parameters["target_col"]
        if parameters.get("run_purpose"):
            tags["purpose"] = parameters["run_purpose"]
        if parameters.get("run_description"):
            tags["mlflow.note.content"] = parameters["run_description"]
        if tags:
            mlflow.set_tags(tags)
        for dataset_name in raw_inputs:
            config = catalog.config_resolver.resolve_pattern(dataset_name)
            filepath = config["filepath"]

            # Локальный путь сохраняем абсолютным.
            # Адреса вроде s3://... оставляем без изменений.
            if "://" not in filepath:
                filepath = str(Path(filepath).resolve())

            dataset = MetaDataset(
                name=parameters.get("dataset_name", dataset_name.removesuffix("@raw")),
                source=resolve_dataset_source(filepath),
            )

            mlflow.log_input(dataset, context="raw")

    @hook_impl
    def after_node_run(self, outputs):
        if mlflow.active_run() is None:
            return

        for name, model in outputs.items():
            if name.endswith("@regression_model"):
                mlflow.set_tag("model_type", type(model).__name__)
