# Задать имя и описание run

Условие: [MLflow server работает](server.md).
Один запуск Kedro создаёт отдельный run через kedro-mlflow.

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline'
```

Конфигурация `tracking.run.name` в mlflow.yml читает имя из runtime-параметров:

```yaml
tracking:
  run:
    name: ${runtime_params:mlflow_run_name, null}
```

Без имени плагин использует имя запускаемого пайплайна.
`mlflow_run_name` не изменяет имя experiment.

## Добавить цель и комментарий

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline,run_purpose=baseline,run_description="Базовая модель для сравнения"'
```

| Параметр | Куда попадает |
| --- | --- |
| mlflow_run_name | Имя run |
| run_purpose | Tags → purpose |
| run_description | Description, через тег mlflow.note.content |

Цель и описание необязательны. Постоянные сведения
[заполняются автоматически](metadata.md).
Параметры модели и разбиения передаются тем же `--params`.

Далее: [сравнить runs](compare.md).

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
