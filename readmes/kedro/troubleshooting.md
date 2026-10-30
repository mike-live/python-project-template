# Разобрать ошибку Kedro

| Сообщение | Что проверить |
| --- | --- |
| `No such command 'run'` | Текущую папку и секцию `[tool.kedro]` в `pyproject.toml` |
| `Unsupported interpolation type oc.env` | Resolver в `project/settings.py`; для ручного loader передайте CONFIG_LOADER_ARGS |
| `PROJECT_DATA_DIR not found` | Корневой `.env`, имя переменной и загрузку настроек |
| `Globals key ... not found` | `conf/base/globals.yml`, выбранный профиль, base_env/default_run_env |
| `Pipeline inputs ... not found` | Имена inputs, записи каталога и параметры `params:` |
| `duplicate key type` | Повторные ключи YAML и отступы соседних datasets |
| `nodes must have unique names` | Совпадения имён nodes в объединённом графе |
| `same inputs and outputs ... transcoded` | Основы имён до `@` у входов и выходов |
| `['MEDV'] not found in axis` | Выбранный профиль и реальные колонки CSV |
| Импортируется пакет из расширения VS Code | Интерпретатор проекта и запуск из терминала `uv run` |

Для проверки структуры используйте:

```bash
uv run kedro registry list
uv run kedro catalog list-patterns
uv run kedro catalog resolve-patterns --pipeline=modeling
```

Если загрузился DataFrame с одной колонкой вместо нескольких, проверьте
разделитель `load_args.sep` и заголовок CSV.
Ошибки подключения, метрик и artifacts описаны в
[диагностике MLflow](../mlflow/troubleshooting.md).

Далее: [каталог и фабрики](catalog.md) · [resolver'ы](parameters.md).

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
