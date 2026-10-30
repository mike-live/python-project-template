# Запустить пайплайн

Проект должен быть установлен; для текущего пайплайна требуется
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

## Выполнить часть пайплайна

```bash
uv run kedro run --pipelines=modeling --to-nodes=train_model_node
uv run kedro run --pipelines=modeling --from-nodes=train_model_node
uv run kedro run --pipelines=modeling --nodes=split_data_node
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
