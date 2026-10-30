# Сохранить и найти график

Node `plot_predictions_node` возвращает matplotlib Figure.
Запись `predictions@prediction_plot` в каталоге оборачивает
MatplotlibDataset в MlflowArtifactDataset.

При выполнении пайплайна PNG сохраняется:

- локально: `PROJECT_DATA_DIR/05_plots/<dataset_name>/actual_vs_predicted.png`;
- в run: **Artifacts → plots → actual_vs_predicted.png**.

Откройте новый завершённый run, зайдите в папку `plots` и выберите PNG.
Папка `plots` сама по себе не является изображением.

## Добавить другой график

Функция должна вернуть Figure. Добавьте для неё node и отдельную запись
каталога с другим локальным filepath, по образцу
[predictions@prediction_plot](../../conf/base/catalog.yml).
Путь должен включать выбранный dataset_name, чтобы результаты
разных датасетов сохранялись отдельно.

MatplotlibDataset здесь называется именно так, а не MatplotlibWriter.
Файлы графиков являются artifacts; числовые кривые истории метрик
отображаются через [Metrics](metrics.md).

Повторное выполнение на том же датасете обновляет локальный PNG.
Разные MLflow runs сохраняют свои artifacts отдельно.

Далее: [диагностика отсутствующего изображения](troubleshooting.md).

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
