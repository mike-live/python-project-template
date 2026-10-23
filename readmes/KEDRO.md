# Kedro: запуск и устройство проекта

Kedro организует выполнение Python-функций в виде графа зависимостей.
Загрузка и сохранение данных определяются в `conf/base/catalog.yml`.
Установка репозитория и настройка данных описаны в [основном README](../README.md).

## Запуск pipeline

Просмотр зарегистрированных pipelines и запуск обучения:

```bash
uv run kedro registry list
uv run kedro run --pipeline=modeling
```

Для запуска `modeling` требуется сервер, настроенный по [инструкции MLflow](MLFLOW.md).

## Структура Kedro-проекта

```text
pyproject.toml                    зависимости и [tool.kedro]
.env                              локальный путь к данным
conf/base/catalog.yml             datasets и фабрики
conf/base/parameters.yml          параметры обучения
conf/local/mlflow.yml             подключение MLflow
project/settings.py              загрузка .env и resolver oc.env
project/pipeline_registry.py     регистрация pipeline
project/modeling/
    split_data.py                 разделение и масштабирование
    train.py                      обучение ElasticNet
    evaluate.py                   MAE, RMSE, R²
    plots.py                      создание matplotlib Figure
    pipeline.py                   prepare_data и основной pipeline
run/cli.py                        собственный интерфейс командной строки
```

Пакет расположен в корне репозитория. Этой структуре соответствуют настройки
`package_name = "project"` и `source_dir = "."` в секции `[tool.kedro]`.

## Функция, node и pipeline

Функция выполняет вычисление. Node связывает аргументы функции с именами datasets
и параметров. Pipeline задаёт зависимости между nodes.

Пример из основного pipeline:

```python
node(
    func=train_model,
    inputs={
        "train_data": "boston_train@model_input",
        "target_col": "params:target_col",
        "alpha": "params:model_options.alpha",
        "l1_ratio": "params:model_options.l1_ratio",
        "max_iter": "params:model_options.max_iter",
    },
    outputs="boston_housing@regression_model",
    name="train_model_node",
)
```

Ключи `inputs` соответствуют аргументам функции, значения — именам datasets или параметров.
Один объект возвращают через `outputs="name"`; два объекта из tuple — через
`outputs=["first", "second"]`. Список из одного output требует от функции
список/tuple из одного элемента, поэтому его нельзя подставлять вместо строки.
Если функция возвращает словарь как единый результат, output также задают строкой.

Порядок определяется зависимостями: split → train → evaluate/plot.
Имена nodes должны быть уникальными даже при объединении двух pipelines.

## Регистрация и выбор pipeline

`register_pipelines()` возвращает словарь имён и объектов Pipeline:

| Имя | Назначение |
| --- | --- |
| `modeling` | Обучение и отправка результатов в MLflow |
| `__default__` | Тот же pipeline modeling, запускаемый по умолчанию |

```bash
uv run kedro run --pipeline=modeling
uv run kedro run
```

Команда `uv run kedro run` выбирает `__default__`, который ссылается на `modeling`.
В обоих случаях обучение выполняется один раз и требуется сервер MLflow.

## Catalog и фабрики

Catalog определяет способы загрузки и сохранения данных. Node получает
DataFrame, модель или словарь; файловые операции выполняет dataset.

Dataset factories позволяют заменить несколько однотипных записей catalog
одним шаблоном. При выполнении pipeline Kedro сопоставляет имена datasets
из `inputs` и `outputs` nodes с шаблонами в catalog.

```yaml
"{dataset_name}@model_input":
  type: pandas.CSVDataset
  filepath: "${oc.env:PROJECT_DATA_DIR}/02_model_input/{dataset_name}.csv"
  save_args:
    index: false
```

Для имени `boston_train@model_input` значение `{dataset_name}` равно
`boston_train`. Kedro подставляет его в `filepath` и создаёт конфигурацию
`pandas.CSVDataset`. Аналогично разрешаются остальные имена:

| Имя dataset | Файл относительно PROJECT_DATA_DIR |
| --- | --- |
| `boston_train@model_input` | `02_model_input/boston_train.csv` |
| `boston_test@model_input` | `02_model_input/boston_test.csv` |

Шаблон заключается в кавычки. Все подстановки в конфигурации должны присутствовать
в имени шаблона. Например, `{dataset_name}` в `filepath` соответствует
`{dataset_name}` в ключе catalog.

Просмотр шаблонов и конфигурации datasets после подстановки:

```bash
uv run kedro catalog list-patterns
uv run kedro catalog resolve-patterns --pipeline=modeling
```

Подробнее: [Dataset factories в документации Kedro](https://docs.kedro.org/en/1.5.0/catalog-data/kedro_dataset_factories/).

График основного pipeline сохраняется в
`PROJECT_DATA_DIR/05_plots/actual_vs_predicted.png` и отправляется в MLflow.
Повторный запуск перезаписывает локальные результаты по этим путям.


## Параметры и CLI

`conf/base/parameters.yml` содержит:

```yaml
target_col: MEDV
model_options:
  alpha: 0.1
  l1_ratio: 0.5
  max_iter: 10000
```

`params:model_options.alpha` в node берёт вложенный параметр из этого файла.
Переопределение на один запуск не меняет YAML:

```bash
uv run kedro run --pipeline=modeling --params="model_options.alpha=0.05,model_options.l1_ratio=0.8"
```

Собственный CLI передаёт эти же параметры в Kedro:

```bash
uv run python -m run.cli --help
uv run python -m run.cli --pipeline modeling --alpha 0.05 --l1-ratio 0.8 --max-iter 20000
```

По умолчанию CLI выбирает `modeling`. Неуказанные параметры модели берутся
из YAML. Значения `test_size=0.2` и `random_state=42` заданы в функции split
и не переопределяются через текущий CLI.


## PartitionedDataset и IncrementalDataset

`PartitionedDataset` представляет папку
однотипных файлов как один dataset; node получает словарь ID → функция загрузки.
Файл читается при вызове этой функции. Это отличается от фабрики, которая
сопоставляет имя node dataset с конфигурацией. В текущем pipeline они не используются.

`IncrementalDataset` выбирает партиции с ID после checkpoint согласно порядку
сравнения ID. Обновление checkpoint нужно явно подтвердить через `confirms`
на downstream node после успешной обработки. Это не автоматическое обнаружение
изменений уже обработанных файлов и не произвольный поиск по дате изменения.

## Частые ошибки

- `No such command run`: запуск не из корня или отсутствует `[tool.kedro]`.
- `Unsupported interpolation type oc.env`: проверьте resolver в settings.py.
- `Environment variable ... not found`: проверьте `.env` и загрузку settings.
- `Pipeline inputs ... not found`: имя не совпало с catalog/фабрикой либо нет params.
- `duplicate key type`: проверьте YAML-отступы и повторяющиеся записи.
- `nodes must have unique names`: задайте разные имена nodes двух pipelines.
- `MatplotlibWriter not found`: в этой версии нужен `matplotlib.MatplotlibDataset`.

Команды диагностики выполняются через `uv run` в окружении проекта.

## Документация

- [Kedro Data Catalog](https://docs.kedro.org/en/stable/catalog-data/introduction/)
- [Фабрики datasets](https://docs.kedro.org/en/1.6.0/catalog-data/kedro_dataset_factories/)
- [Partitioned и incremental datasets](https://docs.kedro.org/en/1.7.0/catalog-data/how_to_use_partitioned_and_incremental_datasets/)
- [MLflow в этом проекте](MLFLOW.md)
