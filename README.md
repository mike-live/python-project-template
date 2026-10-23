[![linting workflow](https://github.com/sshvets0v/python-project-template/actions/workflows/linting.yml/badge.svg)](https://github.com/sshvets0v/python-project-template/actions/workflows/linting.yml)
[![testing and coverage workflow](https://github.com/sshvets0v/python-project-template/actions/workflows/testing_and_coverage.yml/badge.svg)](https://github.com/sshvets0v/python-project-template/actions/workflows/testing_and_coverage.yml)
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/sshvets0v/e8ec108de82c4a3c759a6ba2d114c028/raw/clone.json&logo=github)](https://github.com/MShawon/github-clone-count-badge)

# python-project-template

Шаблон Python-проекта для обработки данных и обучения моделей. Включает
Kedro pipelines, отслеживание экспериментов в MLflow, линтер Ruff и тесты pytest.

## Структура репозитория

- **pyproject.toml** — конфигурационный файл с метаданными проекта, зависимостями и настройками инструментов в формате TOML.
- **uv.lock** — файл с зафиксированными версиями зависимостей для воспроизводимой установки окружения.
- **project/** — Python-пакет с модулями проекта.
- **project/data/** — каталог данных, используемых кодом, если выбрано хранение внутри репозитория.
- **conf/** — каталог конфигурации Kedro и MLflow.
- **conf/base/catalog.yml** — описание datasets, путей загрузки и сохранения данных, а также фабрик datasets.
- **conf/base/parameters.yml** — параметры модели и обработки данных.
- **conf/local/mlflow.yml** — настройки подключения к MLflow, экспериментов и отслеживания запусков.
- **project/settings.py** — настройки Kedro, загрузка `.env` и регистрация resolver `oc.env`.
- **project/pipeline_registry.py** — регистрация pipelines и выбор pipeline по умолчанию.
- **project/modeling/** — функции разделения данных, обучения и оценки модели, построения графиков и определения pipelines.
- **project/modeling/pipeline.py** — pipeline обучения с сохранением результатов в MLflow.
- **run/cli.py** — интерфейс командной строки для выбора pipeline и передачи параметров модели.
- **.env** — локальные переменные окружения, включая путь `PROJECT_DATA_DIR`. Файл не предназначен для хранения в Git.
- **notebooks/** — каталог Jupyter notebooks (`.ipynb`) для исследований, экспериментов и визуализации данных. Notebooks исключены из автоматических проверок линтера и не входят в набор модульных тестов.
- **imgs/** — каталог изображений проекта.
- **readmes/** — каталог тематических инструкций по инструментам и технологиям.
- **tests/** — каталог модульных тестов.
- **.github/workflows/** — конфигурация GitHub Actions: проверки линтера, тестов и покрытия кода. Условия запуска и целевые ветки задаются в соответствующих workflow.



## Установка

Требуются Python 3.12 или новее и **uv** ([официальная инструкция](https://docs.astral.sh/uv/getting-started/installation/)).
Команды выполняются из корня репозитория, содержащего `pyproject.toml`.

```bash
git clone https://github.com/sshvets0v/python-project-template.git
cd python-project-template
uv sync --all-groups
```

Команда `uv sync --all-groups` создаёт окружение `.venv` и устанавливает зависимости,
включая инструменты разработки, согласно `uv.lock`.

При создании собственного проекта на основе шаблона в файле `pyproject.toml` измените `name` в
`[project]` и `project_name` в `[tool.kedro]`.
Поле `package_name = "project"` меняется только вместе с именем Python-пакета
и соответствующими импортами.

## Настройка данных

В случае, если данные находятся вне репозитория создайте файл `.env` рядом в корне репозитория и укажите абсолютный путь
к существующему каталогу данных и сохраните файл:

```dotenv
PROJECT_DATA_DIR=/absolute/path/to/data
```
**Обязательно** проверьте корректность пути, запустив `project/helpers/paths.py`


Если каталог данных расположен внутри репозитория, можно использовать относительные пути без `.env`. Например, для файла `data/01_raw/boston.csv` запись путь в `conf/base/catalog.yml` будет выглядеть так:
```YAML
filepath: data/01_raw/{dataset_name}.csv
```
То есть необходимо заменить `${oc.env:PROJECT_DATA_DIR}` на `data` во всех путях `catalog` и отключите обязательное чтение и проверку `PROJECT_DATA_DIR` в `project/helpers/`. **Добавьте** файл `data/` в `.gitignore`.

Исходный файл шаблонного примера — `boston.csv`, разделитель — запятая,
целевая колонка — `MEDV`. Разместите его в подкаталоге `01_raw`:

```text
data/
└── 01_raw/
    └── boston.csv
```

`PROJECT_DATA_DIR` должен указывать именно на `data`.

Настройки проекта загружают `.env` при запуске Kedro. Проверки пути в
`project/helpers/` должны оставаться включёнными.


## Проверки кода

```bash
uv run ruff check .
uv run pytest --cov=project
```

## Первый запуск

Запустите сервер по [инструкции MLflow](readmes/MLFLOW.md), затем выполните pipeline:

```bash
uv run kedro run --pipeline=modeling
```

Команда `uv run kedro run` запускает тот же pipeline через запись `__default__`.

## Документация

- [Ruff: линтер и форматирование](readmes/LINTING.md)
- [pytest: тестирование и покрытие](readmes/UNIT_TESTS.md)
- [Kedro: pipelines, catalog, фабрики и CLI](readmes/KEDRO.md)
- [MLflow: эксперименты, метрики, модели и Model Registry](readmes/MLFLOW.md)
- [CLONE: плашка количества клонирований](readmes/CLONE.md)
