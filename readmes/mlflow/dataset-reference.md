# Сохранить ссылку на датасет без копии

В проекте это уже выполняет [hook](../../project/hooks.py).
Запустите пайплайн с выбранным датасетом:

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-source-check'
```

В новом run откройте **Dataset**. Ожидается имя `diabetes`
и Source с путём `PROJECT_DATA_DIR/01_raw/diabetes.csv`.
В Artifacts не должно появиться копии исходного CSV.

## Что записывается

Hook получает путь из разрешённой записи `source@raw` в каталоге,
создаёт `mlflow.data.meta_dataset.MetaDataset` и вызывает
`mlflow.log_input(dataset, context="raw")`.

MetaDataset содержит метаданные, а не содержимое таблицы.
Для этой записи hook не читает CSV, не копирует его и не вычисляет
контрольную сумму всего файла. Сам пайплайн по-прежнему загружает CSV
через pandas для обучения.

Digest MetaDataset описывает метаданные. Изменение CSV по тому же пути
не сохраняет старую версию содержимого и не гарантирует другой digest.
Путь на локальном компьютере также не обеспечивает доступ с другого
компьютера; для совместной работы нужен общий источник данных.

Тег `dataset` служит для поиска; встроенный Dataset отображается
благодаря `log_input`.

[MLflow Dataset Tracking](https://www.mlflow.org/docs/latest/ml/dataset/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
