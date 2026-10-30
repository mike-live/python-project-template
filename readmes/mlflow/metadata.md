# Проверить автоматические сведения о run

[ExperimentMetadataHook](../../project/hooks.py) подключён через
`HOOKS` в [project/settings.py](../../project/settings.py).
Он дополняет активный run, которым управляет kedro-mlflow.

| Сведения | Источник |
| --- | --- |
| Tags → dataset, Parameters → dataset_name | Выбранный dataset_name |
| Tags → target_col | Target выбранного профиля |
| Tags → model_type | Класс модели из выхода @regression_model |
| Parameters → model_options.* | Параметры, переданные в обучающий node |
| Parameters → split_options.* | Параметры, переданные в node разбиения |
| Dataset → Source | Путь исходного CSV из каталога |
| Tags → purpose, Description | Необязательные параметры запуска |

Откройте завершённый run и проверьте Tags, Parameters и Dataset.
Для `dataset_name=diabetes` ожидаются `dataset=diabetes`,
`target_col=target`, `model_type=ElasticNet`.

## Когда выполняется hook

Перед пайплайном hook дожидается создания run, затем записывает
выбранный датасет, target, комментарии и ссылку на исходные данные.
После обучающего node он определяет класс возвращённого объекта модели.

Hook не создаёт run сам и пропускает запись при отсутствии активного run.
Прямой вызов split/train в notebook его не запускает.
При частичном выполнении тип модели добавляется только после
обучающего node, а Dataset со ссылкой — при наличии входа `@raw`.

Пустые цель и описание не перезаписывают существующие заметки.
Старые runs не дополняются задним числом.

Далее: [имя и комментарий](run.md) · [ссылка на CSV](dataset-reference.md).

[Теги и описание MLflow](https://mlflow.org/docs/latest/ml/tracking/tracking-api/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
