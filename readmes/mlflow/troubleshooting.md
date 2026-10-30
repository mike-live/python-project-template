# Разобрать ошибку или пустой раздел MLflow

| Симптом | Что проверить |
| --- | --- |
| Connection refused | Сервер запущен; URI Kedro и порт сервера совпадают |
| HTTP 403 | Кто слушает указанный порт; адрес сервера; ответ и логи сервера |
| HTTP 500 | Traceback в терминале MLflow server |
| Dataset пустой | Есть ли log_input; тег dataset не заполняет встроенный Dataset |
| Metrics пустой | Имена выбранных столбцов и формат value/step |
| Invalid metric name с @ | У metric dataset должен быть prefix: "", не null |
| Модель только в Artifacts | Нужен MlflowModelTrackingDataset для Logged Model |
| Model Registry пустой | Регистрация не включена автоматически |
| График виден только локально | Обёртка MlflowArtifactDataset, нужный run, папка Artifacts/plots |
| MatplotlibWriter not found | В каталоге используется matplotlib.MatplotlibDataset |
| Cannot import sentinel из папки VS Code | Ошибка окружения расширения; проверьте запуск через uv run из терминала |
| Процесс завершается при создании Figure | Для запуска без окон используйте MPLBACKEND=Agg |

Для последнего случая на macOS/Linux:

```bash
MPLBACKEND=Agg uv run kedro run --params='dataset_name=diabetes'
```

При пустой таблице [выберите актуальные столбцы](compare.md).
Текущие имена метрик — `mae`, `rmse`, `r2`; старые runs могут
содержать другие ключи.

Если менялись пути сервера, проверьте artifact URI конкретного run.
Новая команда сервера не переносит автоматически artifacts старых
experiments. Сначала найдите исходные хранилища, не удаляя историю.

Далее: [сервер и хранилища](server.md) · [ссылка на данные](dataset-reference.md).

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
