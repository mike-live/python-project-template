from pathlib import Path

import pytest
from kedro.config import OmegaConfigLoader
from kedro.io import DataCatalog
from omegaconf.errors import InterpolationResolutionError

from project.settings import CONFIG_LOADER_ARGS


def load_config(monkeypatch, tmp_path, runtime_params=None):
    monkeypatch.setenv("PROJECT_DATA_DIR", str(tmp_path))
    return OmegaConfigLoader(
        conf_source=Path(__file__).resolve().parents[1] / "conf",
        runtime_params=runtime_params,
        **CONFIG_LOADER_ARGS,
    )


@pytest.mark.parametrize("name,target", [("boston", "MEDV"), ("diabetes", "target")])
def test_runtime_selection_routes_source_target_and_outputs(monkeypatch, tmp_path, name, target):
    loader = load_config(monkeypatch, tmp_path, {"dataset_name": name})
    params = loader["parameters"]
    assert params["dataset_name"] == name
    assert params["target_col"] == target

    config = loader["catalog"]
    assert config["source@raw"]["filepath"] == str(tmp_path / "01_raw" / f"{name}.csv")
    catalog = DataCatalog.from_config(config)
    for split in ["X_train", "X_test", "y_train", "y_test"]:
        resolved = catalog.config_resolver.resolve_pattern(f"{split}@model_input")
        assert resolved["filepath"] == str(tmp_path / "02_model_input" / name / f"{split}.csv")
    assert config["model@regression_model"]["save_args"]["name"] == f"{name}_elasticnet"
    # None makes kedro-mlflow substitute the catalog key, whose '@' is invalid
    # in an MLflow metric name. An empty prefix keeps the keys mae/rmse/r2.
    assert config["metrics@regression_metrics"]["prefix"] == ""
    assert config["predictions@prediction_plot"]["dataset"]["filepath"] == str(
        tmp_path / "05_plots" / name / "actual_vs_predicted.png"
    )


def test_default_selection_is_shared_by_parameters_and_catalog(monkeypatch, tmp_path):
    loader = load_config(monkeypatch, tmp_path)
    name = loader["globals"]["dataset_name"]
    assert loader["parameters"]["dataset_name"] == name
    assert loader["parameters"]["target_col"] == loader["globals"]["datasets"][name]["target_col"]
    assert loader["catalog"]["source@raw"]["filepath"] == str(
        tmp_path / "01_raw" / f"{name}.csv"
    )


def test_unknown_dataset_fails_during_configuration(monkeypatch, tmp_path):
    loader = load_config(monkeypatch, tmp_path, {"dataset_name": "unknown"})
    with pytest.raises(InterpolationResolutionError, match=r"datasets\.unknown\.target_col"):
        loader["parameters"]
