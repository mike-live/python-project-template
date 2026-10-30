# Запустить сервер MLflow

Команды выполняются из корня установленного репозитория.
Подключение Kedro задаётся в [conf/local/mlflow.yml](../../conf/local/mlflow.yml).

Если конфигурация отсутствует, создайте её:

```bash
uv run kedro mlflow init --env=local
```

В существующем файле отредактируйте соответствующие поля, не добавляя
повторную секцию `tracking`:

```yaml
server:
  mlflow_tracking_uri: "http://127.0.0.1:5001"
tracking:
  experiment:
    name: "boston-regression"
```

Запустите в отдельном терминале:

```bash
uv run mlflow server --host 127.0.0.1 --port 5001 --backend-store-uri sqlite:///mlflow.db --artifacts-destination ./mlartifacts
```

Откройте [MLflow](http://127.0.0.1:5001). Сервер работает до Ctrl+C.
Порт в URI Kedro и в команде сервера должен совпадать.

Для продолжения истории запускайте сервер из той же папки с теми же путями.
`mlflow.db` хранит параметры, метрики и прочие метаданные;
`mlartifacts/` — файлы графиков и моделей. Для резервного копирования нужны
оба хранилища. Останавливайте сервер перед обычным файловым копированием базы.

Далее: [запустить эксперимент](run.md).

[MLflow Tracking](https://mlflow.org/docs/latest/tracking/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
