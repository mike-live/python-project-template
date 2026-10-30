# Настроить dataset и фабрику

Каталог [conf/base/catalog.yml](../../conf/base/catalog.yml) определяет,
как загрузить или сохранить объект. Функция node получает сам объект,
например DataFrame, а не путь к файлу.

## Описать один CSV

```yaml
example:
  type: pandas.CSVDataset
  filepath: data/example.csv
  save_args:
    index: false
```

Это самостоятельный пример. В текущем проекте источник `source@raw`
выбирается через [конфигурацию датасетов](../datasets/select.md).

## Описать повторяющиеся результаты фабрикой

В проекте используется:

```yaml
"{split_name}@model_input":
  type: pandas.CSVDataset
  filepath: "${oc.env:PROJECT_DATA_DIR}/02_model_input/${runtime_params:dataset_name,${globals:dataset_name}}/{split_name}.csv"
  save_args:
    index: false
```

Имя `X_train@model_input` сопоставляется с шаблоном,
`{split_name}` получает значение `X_train`. Выбранный через конфигурацию
датасет определяет папку `boston/` или `diabetes/`.
Все подстановки фабрики в её полях должны присутствовать в ключе шаблона.

Часть после `@` обозначает представление логического датасета.
У модели и метрик разные основы имён: `model@regression_model`
и `metrics@regression_metrics`.

## Проверить разрешение имён

```bash
uv run kedro catalog list-patterns
uv run kedro catalog resolve-patterns --pipeline=modeling
```

У `resolve-patterns` в установленной версии используется именно `--pipeline`.
Команда показывает конфигурацию для выбора датасета по умолчанию.

[Фабрики datasets](https://docs.kedro.org/en/stable/catalog-data/kedro_dataset_factories/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
