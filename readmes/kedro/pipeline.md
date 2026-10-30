# Добавить node и зарегистрировать pipeline

Функции обработки находятся в `project/modeling/`, сборка графа —
в [split_train_pipeline.py](../../project/modeling/split_train_pipeline.py),
регистрация — в [pipeline_registry.py](../../project/pipeline_registry.py).
Пакет `project` расположен в корне репозитория; `source_dir = "."`.

## Описать node

Node связывает аргументы функции с именами datasets и параметров:

```python
from kedro.pipeline import node
from project.modeling.train import train_model

train_node = node(
    func=train_model,
    inputs={
        "X_train": "X_train@model_input",
        "y_train": "y_train@model_input",
        "alpha": "params:model_options.alpha",
    },
    outputs="model@regression_model",
    name="train_model_node",
)
```

В примере используется существующая функция `train_model`; остальные её
аргументы возьмутся из значений по умолчанию. В проектном пайплайне
`l1_ratio` и `max_iter` также передаются через `params:`.

Строковый `outputs` означает один объект, включая словарь.
Список выходов требует tuple/list соответствующей длины.
Ключи словаря `inputs` должны совпадать с именами аргументов функции.

## Собрать и зарегистрировать граф

```python
from kedro.pipeline import pipeline

modeling_pipeline = pipeline([train_node])
```

В `register_pipelines()` возвращается словарь:

```python
return {
    "modeling": modeling_pipeline,
    "__default__": modeling_pipeline,
}
```

Порядок выполнения определяется зависимостями datasets.
Имена nodes должны быть уникальны в объединённом пайплайне.
Новый результат для передачи между nodes можно не описывать в каталоге:
при отсутствии подходящей фабрики Kedro использует MemoryDataset.

Далее: [настроить загрузку и сохранение](catalog.md).

[Nodes и pipelines](https://docs.kedro.org/en/stable/build/nodes/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
