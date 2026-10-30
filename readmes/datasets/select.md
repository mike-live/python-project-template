# Выбрать датасет для запуска

Доступные профили перечислены в
[conf/base/globals.yml](../../conf/base/globals.yml):

```yaml
dataset_name: boston

datasets:
  boston:
    target_col: MEDV
  diabetes:
    target_col: target
```

Верхний `dataset_name` задаёт выбор по умолчанию. Для его использования:

```bash
uv run kedro run
```

Для выбора на один запуск без изменения файлов:

```bash
uv run kedro run --params='dataset_name=boston'
uv run kedro run --params='dataset_name=diabetes'
```

Обе команды выполняют один и тот же пайплайн `modeling`.
Каталог выбирает `01_raw/<dataset_name>.csv`, параметры — target из профиля,
а результаты сохраняются в отдельную папку выбранного датасета.

Неизвестное имя вызывает ошибку загрузки конфигурации: сначала нужно
[добавить профиль](add.md). Править реестр или Python-пайплайн для
переключения не требуется.

При необходимости добавьте [имя run](../mlflow/run.md):

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline'
```

Готовые [boston.csv](../../0_template_data/boston.csv) и
[diabetes.csv](../../0_template_data/diabetes.csv) находятся в `0_template_data`.
При настройке рабочего каталога скопируйте нужные CSV в
`PROJECT_DATA_DIR/01_raw/`.

Условия: [сервер MLflow работает](../mlflow/server.md), исходный CSV существует.
Далее: [найти результаты](outputs.md).

[Вопросы раздела](../README.md#датасеты) · [Все инструкции](../README.md)
