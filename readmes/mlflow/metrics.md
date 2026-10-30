# Записывать метрики и их историю

Node оценки возвращает словарь:

```python
{
    "mae": {"value": 2.5, "step": 0},
    "rmse": {"value": 3.8, "step": 0},
    "r2": {"value": 0.81, "step": 0},
}
```

Значения здесь условные. Текущая функция вычисляет их на тестовой выборке.
Каталог сохраняет результат через:

```yaml
"metrics@regression_metrics":
  type: kedro_mlflow.io.metrics.MlflowMetricsHistoryDataset
  prefix: ""
```

Пустая строка сохраняет ключи `mae`, `rmse`, `r2` без префикса.
Не заменяйте её на `null`: плагин может подставить имя записи каталога,
а символ `@` недопустим в имени метрики.

Числа появятся в **Metrics** текущего run.
JSON, сохранённый как artifact, сам по себе не создаёт Metrics.

## Передать историю одной метрики

```python
{
    "train_loss": [
        {"value": 10.0, "step": 0},
        {"value": 7.0, "step": 1},
        {"value": 5.0, "step": 2},
    ]
}
```

Здесь также приведён пример формата, а не результаты текущего обучения.
Для настоящей истории нужны измерения на соответствующих шагах.
Текущий `ElasticNet.fit()` не предоставляет публичный callback loss
по эпохам, поэтому проект записывает итоговые показатели.

Далее: [сравнить метрики](compare.md) · [ручное логирование](notebook.md).

[Datasets kedro-mlflow](https://kedro-mlflow.readthedocs.io/en/stable/source/05_API/01_python_objects/01_Datasets.html)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
