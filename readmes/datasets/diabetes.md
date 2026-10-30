# Готовый датасет Diabetes

Встроенный в scikit-learn регрессионный датасет содержит 442 строки,
10 числовых признаков и target. В используемом наборе нет пропусков.
Готовый [diabetes.csv](../../0_template_data/diabetes.csv) включён в
репозиторий рядом с [boston.csv](../../0_template_data/boston.csv).
Скачивать или формировать датасет отдельно не требуется.

Целевая колонка — `target`. Признаки сохранены без предварительного
масштабирования; StandardScaler обучается на train внутри пайплайна.

Как и для Boston, рабочий каталог ожидает CSV по пути
`PROJECT_DATA_DIR/01_raw/diabetes.csv`. При настройке нового рабочего
каталога скопируйте туда готовый файл из `0_template_data`.

При [работающем MLflow](../mlflow/server.md):

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline'
```

Ожидаемый результат: [четыре CSV и график](outputs.md), модель и метрики в run.

[Источник: load_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)

[Вопросы раздела](../README.md#датасеты) · [Все инструкции](../README.md)
