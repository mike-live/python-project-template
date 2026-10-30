# Найти сохранённые результаты

Корнем служит PROJECT_DATA_DIR. Для каждого выбранного датасета
используется своя папка:

```text
01_raw/<dataset_name>.csv
02_model_input/<dataset_name>/X_train.csv
02_model_input/<dataset_name>/X_test.csv
02_model_input/<dataset_name>/y_train.csv
02_model_input/<dataset_name>/y_test.csv
05_plots/<dataset_name>/actual_vs_predicted.png
```

Папки результатов создаются при сохранении.
Повторный запуск того же датасета обновляет его CSV, модель, отчёт и график.
Результаты Boston и Diabetes сохраняются отдельно.

| Результат | Где находится |
| --- | --- |
| Исходный CSV | Локально в 01_raw; в MLflow сохраняется ссылка |
| Четыре train/test CSV | Локально в 02_model_input |
| График | Локально в 05_plots и в Artifacts/plots текущего run |
| Модель | Локально в 03_models и как Logged Model в MLflow |
| MAE, RMSE, R² | Локально в 04_reporting/metrics.json и в Metrics текущего run |

Обучающий node возвращает одну модель для двух записей каталога:
`model@regression_model` и `model_file`. Обучение выполняется один раз.
Оценка аналогично возвращает результат для MLflow и локального JSON.
В JSON сохраняются числовые значения `mae`, `rmse`, `r2`, а в MLflow —
соответствующие записи с `value` и `step`.

MLflow server хранит метаданные в `mlflow.db`, файлы — в `mlartifacts/`.

Разделение по датасетам не является версионированием каждого запуска.
Ссылка на CSV также не сохраняет прежнее содержимое файла.

Далее: [графики](../mlflow/artifacts.md) · [модели](../mlflow/models.md)
· [ссылка на данные](../mlflow/dataset-reference.md).

[Вопросы раздела](../README.md#датасеты) · [Все инструкции](../README.md)
