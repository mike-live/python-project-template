# Обрабатывать папку файлов

Эта возможность не используется в текущем обучающем пайплайне.
Она нужна, когда вход состоит из множества однотипных файлов.

## PartitionedDataset

```yaml
monthly_data:
  type: partitions.PartitionedDataset
  path: data/monthly
  dataset: pandas.CSVDataset
  filename_suffix: ".csv"
```

Node получает словарь `partition_id → функция загрузки`:

```python
def process_partitions(partitions):
    return {
        partition_id: load_partition().drop_duplicates()
        for partition_id, load_partition in partitions.items()
    }
```

Содержимое файла читается при вызове функции загрузки.
При сохранении такого словаря через PartitionedDataset каждый элемент
записывается в отдельную партицию.

Фабрика каталога решает другую задачу: сопоставляет имя dataset с
шаблоном конфигурации. Она сама по себе не перебирает файлы папки.

## IncrementalDataset

Замените тип на `partitions.IncrementalDataset`, если нужно выбирать
партиции с ID после сохранённого checkpoint.

После успешной обработки подтвердите вход в node:

```python
node(
    func=process_partitions,
    inputs="monthly_data",
    outputs="processed_partitions",
    confirms="monthly_data",
)
```

Для этого примера `monthly_data` должен быть IncrementalDataset, а
выход `processed_partitions` — отдельно настроен на сохранение партиций.

Checkpoint опирается на порядок ID. Он не отслеживает изменения
содержимого ранее обработанных файлов. При необходимости подтверждение
можно перенести в downstream node после дополнительных проверок.

[Partitioned и incremental datasets](https://docs.kedro.org/en/1.7.0/catalog-data/how_to_use_partitioned_and_incremental_datasets/)

[Вопросы раздела](../README.md#kedro) · [Все инструкции](../README.md)
