# Вопросы и инструкции

Установка репозитория и общая настройка окружения описаны в
[основном README](../README.md). Здесь собраны вопросы по работе с проектом.
Каждая ссылка ведёт непосредственно на страницу с ответом.

## Датасеты

- [Как выбрать датасет при запуске и задать вариант по умолчанию?](datasets/select.md)
- [Как добавить свой CSV без изменения пайплайна?](datasets/add.md)
- [Как подготовить демонстрационный Diabetes CSV?](datasets/diabetes.md)
- [Где сохраняются результаты и что перезаписывается при повторном запуске?](datasets/outputs.md)

## Kedro

- [Как запустить пайплайн и посмотреть зарегистрированные пайплайны?](kedro/run.md)
- [Как выполнить часть пайплайна или продолжить с выбранного node?](kedro/run.md)
- [Как добавить node и зарегистрировать pipeline?](kedro/pipeline.md)
- [Как передать результат следующему node без сохранения в файл?](kedro/pipeline.md)
- [Как настроить dataset и фабрику в каталоге?](kedro/catalog.md)
- [Как переопределить параметры через --params?](kedro/parameters.md)
- [Как работают globals, runtime_params и oc.env?](kedro/parameters.md)
- [Как использовать каталог в notebook и перечитывать изменения?](kedro/notebook.md)
- [Когда нужны PartitionedDataset и IncrementalDataset?](kedro/partitions.md)
- [Как разобрать ошибку конфигурации, импорта или графа Kedro?](kedro/troubleshooting.md)

## MLflow

- [Как запустить сервер и сохранить историю экспериментов?](mlflow/server.md)
- [Как задать имя, цель и описание run?](mlflow/run.md)
- [Как настроить таблицу метрик, фильтрацию и сравнение runs?](mlflow/compare.md)
- [Какие сведения записываются автоматически и откуда они берутся?](mlflow/metadata.md)
- [Как сохранить ссылку на датасет без загрузки его копии?](mlflow/dataset-reference.md)
- [Как записывать метрики и их историю по шагам?](mlflow/metrics.md)
- [Как сохранить и найти график в MLflow?](mlflow/artifacts.md)
- [Как загрузить сохранённую модель?](mlflow/models.md)
- [Чем Logged Model отличается от Registered Model и как использовать Registry?](mlflow/models.md)
- [Как логировать эксперимент вручную из notebook?](mlflow/notebook.md)
- [Почему Dataset, Metrics или Artifacts пустые и как разобрать ошибку сервера?](mlflow/troubleshooting.md)

## Ruff

- [Как проверить, автоматически исправить и отформатировать код?](quality/lint.md)
- [Как выбрать правила и настроить точечные исключения?](quality/lint-rules.md)

## pytest

- [Как запустить все тесты или выбрать один тест?](quality/tests.md)
- [Как написать новый тест, использовать параметризацию и временные данные?](quality/write-test.md)
- [Как получить терминальный, HTML или XML отчёт о покрытии?](quality/coverage.md)

## GitHub Actions

- [Как проверить lint и тесты в GitHub Actions и найти причину сбоя?](github/checks.md)
- [Как настроить плашку клонирований для своей репы?](github/clone-badge.md)

## Дополнительно

- [Исходные персональные примеры плашки клонирований](CLONE.md).
- [Шпаргалка Kedro](Kedro-Cheat-Sheet-Light.svg).
