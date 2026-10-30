# Использовать каталог в notebook

Выберите ядро Python из проектной `.venv`.
Запустите [MLflow](../mlflow/server.md): при создании контекста плагин
может обращаться к серверу, даже если сам пайплайн пока не выполняется.

В начале notebook загрузите расширение Kedro:

```python
%load_ext kedro.ipython
%reload_kedro --params dataset_name=diabetes
```

Если проект не найден из текущей папки, укажите его абсолютный путь
после `%reload_kedro` перед `--params`.
Расширение предоставляет `catalog`, `context`, `session` и `pipelines`:

```python
df = catalog.load("source@raw")
df.head()
```

Каталог использует те же профили и пути, что и CLI.
Для смены датасета или перечитывания YAML выполните `%reload_kedro` снова.

## Перечитывать изменённые Python-функции

```python
%load_ext autoreload
%autoreload 2
```

Autoreload полезен при редактировании импортированных функций без
перезапуска ядра. Он не заменяет перечитывание конфигурации Kedro.
Это удобство для разработки, а не обязательное условие каждого notebook.

## Resolver oc.env

При загрузке через Kedro используется проектный `settings.py`:
он загружает `.env` и регистрирует resolver. Повторять регистрацию
`oc.env` вручную в таком notebook не требуется.

Если создаёте OmegaConfigLoader самостоятельно, передайте настройки проекта:

```python
from kedro.config import OmegaConfigLoader
from project.helpers import ROOT_DIR
from project.settings import CONFIG_LOADER_ARGS

loader = OmegaConfigLoader(
    conf_source=ROOT_DIR / "conf",
    runtime_params={"dataset_name": "diabetes"},
    **CONFIG_LOADER_ARGS,
)
```

Прямые вызовы split/train не выполняют Kedro hooks и не создают run.
Для ручной записи результатов см. [MLflow в notebook](../mlflow/notebook.md).

[Kedro в Jupyter](https://docs.kedro.org/en/stable/integrations-and-plugins/notebooks_and_ipython/kedro_and_notebooks/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
