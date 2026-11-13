# Запустить пайплайн

Проект должен быть установлен. Для запуска требуется
[работающий MLflow](../mlflow/server.md).

Посмотрите зарегистрированные пайплайны:

```bash
uv run kedro registry list
```

Запустите обучение:

```bash
uv run kedro run --pipelines=modeling
```

Команда `uv run kedro run` выбирает `__default__`, который в этом проекте
ссылается на тот же `modeling`. Выполнение состоит из split → train → evaluate/plot.

## Выбрать датасет, параметры и имя run

Запустите `modeling` на Diabetes и задайте имя запуска в MLflow.

```bash
uv run kedro run --pipelines=modeling \
  --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline'
```

Переопределите `alpha` и scaler для одного запуска.

```bash
uv run kedro run --pipelines=modeling \
  --params='dataset_name=diabetes,model_options.alpha=0.05,model_options.scaler=robust,mlflow_run_name=diabetes-robust'
```

`--params` принимает пары `ключ=значение` через запятую. Точка обозначает
вложенный ключ. Параметры действуют на текущий запуск, остальные значения
берутся из конфигурации. `mlflow_run_name` задаёт имя run внутри настроенного
эксперимента. Описание и цель можно передать через
[`run_description` и `run_purpose`](../mlflow/run.md#добавить-цель-и-комментарий).

## Запустить подбор гиперпараметров

Запустите `tuning` с количеством попыток из `tuning_options.n_trials` в
`parameters.yml`.

```bash
uv run kedro run --pipelines=tuning \
  --params='dataset_name=diabetes,mlflow_run_name=diabetes-tuned'
```

Для быстрой проверки выполните три попытки.

```bash
uv run kedro run --pipelines=tuning \
  --params='dataset_name=diabetes,tuning_options.n_trials=3,mlflow_run_name=diabetes-tuning-check'
```

## Выполнить часть пайплайна

```bash
uv run kedro run --pipelines=modeling --to-nodes=train_model_node
uv run kedro run --pipelines=modeling --nodes=split_data_node
uv run kedro run --pipelines=modeling --from-nodes=train_model_node \
  --params='dataset_name=diabetes,mlflow_run_name=diabetes-retrain'
```

`--from-nodes` включает указанный node и его потомков.
Необходимые входы пропущенных шагов должны уже загружаться из каталога.
Для старта с train в проекте нужны четыре ранее сохранённых train/test CSV.
Используйте тот же датасет и согласованные настройки подготовки данных.

Частичный запуск не восстанавливает автоматически прежние код, данные
или run. По умолчанию создаётся новый MLflow run.

Далее: [выбрать датасет](../datasets/select.md) · [изменить параметры](parameters.md).

[Kedro CLI](https://docs.kedro.org/en/stable/getting-started/commands_reference/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
