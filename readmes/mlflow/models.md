# Загрузить модель и использовать Registry

Откройте **Models / Logged Models** выбранного experiment или модель
на странице run. Каталог использует MlflowModelTrackingDataset с
flavor `mlflow.sklearn` и именем `<dataset_name>_elasticnet`.

## Загрузить Logged Model

Скопируйте Model URI из интерфейса и подставьте его в код:

```python
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://127.0.0.1:5001")
model = mlflow.sklearn.load_model("models:/<MODEL_ID_FROM_UI>")
```

Текущая модель принимает уже масштабированные признаки:
StandardScaler пока не сохранён вместе с ElasticNet.
Для предсказаний нужны признаки с теми же колонками и тем же
преобразованием, что использовались при обучении.

## Зарегистрировать выбранную модель

Logged Model — результат конкретного обучения.
Registered Model объединяет версии под постоянным именем.
Обычный `save_args.name` в каталоге не включает автоматическую регистрацию.

Выберите Model URI нужного результата и зарегистрируйте его:

```python
version = mlflow.register_model(
    model_uri="models:/<MODEL_ID_FROM_UI>",
    name="diabetes_elasticnet",
)
```

Назначить alias выбранной версии:

```python
client = mlflow.MlflowClient()
client.set_registered_model_alias(
    name="diabetes_elasticnet",
    alias="champion",
    version=version.version,
)
```

После этого модель загружается по
`models:/diabetes_elasticnet@champion`.
Alias назначает пользователь; регистрация сама не выбирает лучшую модель.
В текущей конфигурации регистрация не выполняется при каждом запуске.

Сервер из [инструкции](server.md) использует SQLite backend.
Регистрация не добавляет отсутствующий preprocessing и не запускает обучение.

[MLflow Model Registry](https://mlflow.org/docs/latest/ml/model-registry/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
