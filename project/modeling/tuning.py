import mlflow
import optuna

from .train import create_model
from .validation import cross_validate_model


def tune_parameters(
    X_train,
    y_train,
    search_space,
    model_options,
    tuning_options,
):
    study = tune_model(
        X_train=X_train,
        y_train=y_train,
        search_space=search_space,
        scaler=model_options["scaler"],
        max_iter=model_options["max_iter"],
        **tuning_options,
    )

    parent_run = mlflow.active_run()

    if parent_run is not None:
        mlflow.log_params(
            {
                "best_alpha": study.best_params["alpha"],
                "best_l1_ratio": study.best_params["l1_ratio"],
                "best_trial": study.best_trial.number,
            }
        )
        best_so_far = float("inf")

        for trial in study.trials:
            if trial.state != optuna.trial.TrialState.COMPLETE:
                continue

            best_so_far = min(best_so_far, trial.value)
            mlflow.log_metric(
                "best_cv_mae",
                best_so_far,
                step=trial.number + 1,
            )

            with mlflow.start_run(
                run_name=f"trial-{trial.number}",
                experiment_id=parent_run.info.experiment_id,
                nested=True,
            ):
                mlflow.log_params(trial.params)
                mlflow.log_metric("cv_mae", trial.value)

    return study.best_params


def tune_model(
    X_train,
    y_train,
    search_space,
    scaler="standard",
    max_iter=10_000,
    n_trials=30,
    n_splits=5,
    random_state=42
):
    def objective(trial):
        alpha = trial.suggest_float(
            "alpha",
            search_space["alpha"]["low"],
            search_space["alpha"]["high"],
            log=True
        )
        l1_ratio = trial.suggest_float(
            "l1_ratio",
            search_space["l1_ratio"]["low"],
            search_space["l1_ratio"]["high"]
        )

        model = create_model(
            scaler=scaler,
            alpha=alpha,
            l1_ratio=l1_ratio,
            max_iter=max_iter
        )

        cv_score = cross_validate_model(
            model=model,
            X_train=X_train,
            y_train=y_train,
            n_splits=n_splits,
            random_state=random_state
        )

        return cv_score

    study = optuna.create_study(
        direction="minimize",
        sampler=optuna.samplers.TPESampler(seed=random_state)
    )
    study.optimize(objective, n_trials=n_trials)


    return study
