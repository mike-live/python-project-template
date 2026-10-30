# Запустить тесты

Из корня установленного проекта выполните:

```bash
uv run pytest
```

Для подробного вывода добавьте `-v`.
Для отдельного файла или функции:

```bash
uv run pytest tests/test_dataset_selection.py
uv run pytest tests/test_addition.py::test_addition
```

Имена текущих тестовых файлов:

| Файл | Что проверяется |
| --- | --- |
| tests/test_addition.py | Функция project.example_addition.addition |
| tests/test_paths.py | Существование корневой папки проекта |
| tests/test_dataset_selection.py | Выбор профиля, target и путей результатов |

Обычные тесты не требуют обучения модели или работающего MLflow server.
Тесты конфигурации подставляют временный PROJECT_DATA_DIR через monkeypatch.

Если ошибка возникла при collection, тесты ещё не выполнялись:
сначала исправьте импорт или обязательную настройку на этапе импорта.
Установка репозитория описана в [основном README](../../README.md).

Далее: [написать тест](write-test.md) · [получить покрытие](coverage.md).

[Запуск pytest](https://docs.pytest.org/en/stable/how-to/usage.html)

[Вопросы раздела](../README.md#pytest) · [Все инструкции](../README.md)
