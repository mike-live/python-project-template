# Переопределить параметры и resolver'ы

Общие настройки модели и разбиения находятся в
[parameters.yml](../../conf/base/parameters.yml).
Профили датасетов и выбор по умолчанию — в
[globals.yml](../../conf/base/globals.yml).

Изменение YAML меняет настройки последующих запусков.
`--params` переопределяет значения только для текущего запуска:

```bash
uv run kedro run --params='dataset_name=boston,model_options.alpha=0.05'
uv run kedro run --params='dataset_name=diabetes,split_options.test_size=0.3'
```

Точка в `model_options.alpha` обозначает вложенный ключ.
Неуказанные параметры сохраняют значения из конфигурации.

## Как подставляются значения

| Выражение | Назначение |
| --- | --- |
| `params:model_options.alpha` в node | Передать аргумент из параметров |
| `${runtime_params:dataset_name,...}` в YAML | Получить значение из `--params` |
| `${globals:dataset_name}` | Получить общий выбор по умолчанию |
| `${oc.env:PROJECT_DATA_DIR}` | Получить переменную окружения |

`globals` разделяет значения между каталогом и параметрами.
Вложенная подстановка выбирает target-колонку нужного профиля:

```yaml
dataset_name: ${runtime_params:dataset_name,${globals:dataset_name}}
target_col: ${globals:datasets.${runtime_params:dataset_name,${globals:dataset_name}}.target_col}
```

В [settings.py](../../project/settings.py) загружается корневой `.env`,
регистрируется `oc.env` и явно задаются окружения `base` и `local`.
`runtime_params` не используется внутри самого `globals.yml`;
приоритет CLI задаётся там, где значение читается.

Далее: [выбрать](../datasets/select.md) или [добавить](../datasets/add.md) датасет.

[Шаблоны конфигурации Kedro](https://docs.kedro.org/en/stable/configure/how_to_use_templating/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
