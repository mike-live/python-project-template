# Написать новый тест

Создайте файл `tests/test_<имя>.py`.
Функции тестов должны называться `test_*`:

```python
from project.example_addition import addition


def test_addition_with_negative_number():
    assert addition(-1, 1) == 0
```

Для проверки нескольких входов используется параметризация:

```python
import pytest

from project.example_addition import addition


@pytest.mark.parametrize("a,b,expected", [(2, 3, 5), (-1, 1, 0)])
def test_addition_cases(a, b, expected):
    assert addition(a, b) == expected
```

Для файлов используйте фикстуру `tmp_path`, для окружения —
`monkeypatch.setenv("PROJECT_DATA_DIR", str(tmp_path))`.
Это позволяет проверить поведение без привязки к личным путям.

Проверьте новый файл отдельно, затем запустите весь набор:

```bash
uv run pytest tests/test_addition.py
uv run pytest
```

Подставьте имя созданного файла в первую команду.
Утверждения должны проверять ожидаемое поведение функции.

[Начало работы с pytest](https://docs.pytest.org/en/stable/getting-started.html)

[Вопросы раздела](../README.md#pytest) · [Все инструкции](../README.md)
