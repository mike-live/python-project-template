# MLflow: эксперименты, метрики, графики и модели

MLflow хранит параметры и результаты экспериментов. Плагин `kedro-mlflow`
создаёт run при запуске Kedro, а специальные datasets сохраняют метрики,
модели и artifacts. Установка репозитория и настройка окружения описаны
в [основном README](../README.md).

## Настройка интеграции

Конфигурация интеграции находится в `conf/local/mlflow.yml`.
Если файл отсутствует, создайте его командой:

```bash
uv run kedro mlflow init
```

`init` создаёт конфигурацию по умолчанию. Существующий файл редактируется
на месте. Hooks плагина регистрируются автоматически, если их автоматическое
обнаружение не отключено в настройках Kedro.

Основные настройки проекта:

```yaml
server:
  mlflow_tracking_uri: "http://127.0.0.1:5000"
tracking:
  disable_tracking:
    pipelines: []
  experiment:
    name: "boston-regression"
```

В примере приведены основные поля конфигурации. Параметры `tracking.run`
дополнительно определяют имя и вложенность run.

## Запуск сервера и pipeline

В первом терминале запустите сервер:

```bash
uv run mlflow server --host 127.0.0.1 --port 5000 --backend-store-uri sqlite:///mlflow.db --artifacts-destination ./mlartifacts
```

При работающем сервере выполните во втором терминале:

```bash
uv run kedro run --pipeline=modeling
```

Откройте [интерфейс MLflow](http://127.0.0.1:5000) и выберите experiment `boston-regression`.
Сервер можно остановить Ctrl+C. Для продолжения используйте те же пути хранилищ.
Если запускать сервер из другой папки, относительные пути укажут на другие данные.

## Основные сущности и хранилища

| Сущность | Назначение |
| --- | --- |
| Experiment | Группа запусков, здесь boston-regression |
| Run | Один запуск pipeline с параметрами и результатами |
| Parameters | Настройки модели и другие переданные параметры |
| Metrics | Числовые показатели с историей по step/timestamp |
| Artifacts | Файлы: PNG, CSV, JSON и другие |
| Logged Model | Модель в формате MLflow, связанная с run |
| Registered Model | Именованная модель в Registry с версиями и aliases |

`mlflow.db` — backend: метаданные запусков, метрики и данные registry.
`mlartifacts/` — файлы artifacts, включая модель и графики.
При локальном запуске оба хранилища расположены на компьютере пользователя.
Для переноса и резервного копирования необходимы оба.

## Как catalog отправляет результаты

Функции обучения и оценки возвращают объекты. При выполнении Kedro их сохраняют
datasets из `conf/base/catalog.yml`. MLflow-вызовы внутри функций не нужны.

### Метрики

```yaml
"{dataset_name}@regression_metrics":
  type: kedro_mlflow.io.metrics.MlflowMetricsHistoryDataset
  prefix: "{dataset_name}"
```

Текущая `evaluate_model()` возвращает:

```python
{
    "mae": {"value": 2.5, "step": 0},
    "rmse": {"value": 3.8, "step": 0},
    "r2": {"value": 0.81, "step": 0},
}
```

В примере использованы условные значения. При dataset
`boston_housing_metrics@regression_metrics` ключи получат префикс
`boston_housing_metrics`. Результаты отображаются в Metrics соответствующего run.
JSON, загруженный как artifact, не создаёт числовых Metrics.

### Модель

```yaml
"{dataset_name}@regression_model":
  type: kedro_mlflow.io.models.MlflowModelTrackingDataset
  flavor: mlflow.sklearn
  save_args:
    name: "{dataset_name}_elasticnet"
```

Node возвращает обученный ElasticNet. Dataset сохраняет MLflow Model, связанную
с текущим run. Модель отображается в Models / Logged Models или на странице run;
расположение зависит от версии интерфейса. Pickle-файл, загруженный через
`MlflowArtifactDataset`, сам по себе не становится Logged Model.

### График

```yaml
prediction_plot:
  type: kedro_mlflow.io.artifacts.MlflowArtifactDataset
  artifact_path: plots
  dataset:
    type: matplotlib.MatplotlibDataset
    filepath: "${oc.env:PROJECT_DATA_DIR}/05_plots/actual_vs_predicted.png"
    save_args:
      dpi: 300
      bbox_inches: tight
```

Node возвращает Figure. Внутренний dataset сохраняет PNG локально, обёртка
загружает его в `Artifacts → plots → actual_vs_predicted.png` текущего run.

### CSV

Train/test сохраняются локально через CSV-фабрику.
Для дополнительной отправки CSV в run используется обёртка:

```yaml
"{dataset_name}@model_input":
  type: kedro_mlflow.io.artifacts.MlflowArtifactDataset
  artifact_path: datasets
  dataset:
    type: pandas.CSVDataset
    filepath: "${oc.env:PROJECT_DATA_DIR}/02_model_input/{dataset_name}.csv"
    save_args:
      index: false
```

Пример описывает дополнительную возможность и не включён в текущий catalog.

## Работа в notebook

В notebook прямые вызовы split/train/evaluate не активируют catalog и hooks.
При ручном логировании URI сервера и run задаются явно:

```python
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_experiment("notebook-demo")

with mlflow.start_run(run_name="manual-check"):
    mlflow.log_param("alpha", 0.1)
    mlflow.log_metric("rmse", 3.8)
    mlflow.set_tag("source", "notebook")
    # Для уже созданных объектов:
    # mlflow.log_figure(fig, "plots/predictions.png")
    # mlflow.sklearn.log_model(model, name="elasticnet")
```

Значение 3.8 приведено для примера; при обучении используется вычисленная метрика.
В Kedro nodes вызов start_run не требуется: жизненным циклом run управляет плагин.
При прямых вызовах MLflow без настройки URI может использоваться другое хранилище.

## История метрики и график loss

Для истории одна метрика должна иметь несколько точек с разными step:

```python
# Формат результата для MlflowMetricsHistoryDataset:
{
    "train_loss": [
        {"value": 10.0, "step": 0},
        {"value": 7.0, "step": 1},
        {"value": 5.0, "step": 2},
    ]
}
```

Ручной API использует `mlflow.log_metric("train_loss", loss, step=epoch)` внутри
активного run. Текущая ElasticNet.fit не отдаёт loss по эпохам через публичный
callback, поэтому проект логирует итоговые MAE/RMSE/R². Чтобы получить настоящий
loss по эпохам, нужен алгоритм с пошаговым обучением, например SGDRegressor с
partial_fit. Перебор alpha — серия экспериментов, а не эпохи одной модели.

## Registered Model: регистрация и версии

Logged Model — результат конкретного обучения. Registered Model объединяет
выбранные результаты под постоянным именем: например, `boston_elasticnet`,
версии 1, 2, 3. Обычный `save_args.name` задаёт имя Logged Model и сам по себе
не регистрирует её в Registry.

Для автоматической регистрации добавьте в фабрику модели:

```yaml
  save_args:
    name: "{dataset_name}_elasticnet"
    registered_model_name: boston_elasticnet
```

При каждом успешном логировании создаётся новая версия. В текущей конфигурации
регистрация не включена. Для Registry требуется backend на основе базы данных;
SQLite из приведённой команды поддерживает этот режим.

Для регистрации сохранённой модели используйте её Model URI из интерфейса:

```python
import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

version = mlflow.register_model(
    model_uri="models:/<MODEL_ID_FROM_UI>",
    name="boston_elasticnet",
)

client = mlflow.MlflowClient()
client.set_registered_model_alias(
    name="boston_elasticnet",
    alias="champion",
    version=version.version,
)
```

`champion` — назначаемая пользователем ссылка на версию. После оценки результатов
alias можно переназначить. Регистрация не выполняет автоматический выбор модели.

```python
import mlflow.sklearn

model = mlflow.sklearn.load_model("models:/boston_elasticnet@champion")
```

Текущая модель принимает уже масштабированные признаки: scaler не сохранён.
Регистрация не исправляет это ограничение preprocessing.

## Диагностика

- Пусто в Metrics: проверьте специальный metric dataset и формат value/step.
- Модель только в Artifacts: проверьте MlflowModelTrackingDataset вместо Pickle-обёртки.
- Пусто в Registry: проверьте регистрацию; Logged Model не равна Registered Model.
- Нет картинки: откройте новый завершённый run и Artifacts/plots.
- Connection refused: сервер выключен или URI/порт отличаются.
- HTTP 500: смотрите traceback терминала сервера, не только сообщение браузера.
- artifact_path deprecated при log_model: используйте name для модели.
- MatplotlibWriter not found: используйте MatplotlibDataset.
- Unexpected metric value float: нужна структура {"value": число, "step": 0}.

Если эксперимент создан раньше с другим artifact_location, изменение команды
сервера не переносит старые artifacts. Сверьте artifact URI run и существующие
хранилища, прежде чем создавать новый experiment или переносить файлы.

## Документация

- [Настройка kedro-mlflow](https://kedro-mlflow.readthedocs.io/en/stable/source/02_getting_started/01_installation/02_setup.html)
- [Datasets kedro-mlflow](https://kedro-mlflow.readthedocs.io/en/stable/source/05_API/01_python_objects/01_Datasets.html)
- [MLflow Python API](https://mlflow.org/docs/latest/api_reference/python_api/mlflow.html)
- [Model Registry](https://mlflow.org/docs/latest/model-registry)
- [Запуск Kedro в этом проекте](KEDRO.md)
