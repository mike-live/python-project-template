# Получить отчёт о покрытии

Терминальный отчёт с непокрытыми строками:

```bash
uv run pytest --cov=project --cov-report=term-missing
```

HTML-отчёт:

```bash
uv run pytest --cov=project --cov-report=html
```

После успешного запуска откройте `htmlcov/index.html`.

Для XML:

```bash
uv run pytest --cov=project --cov-report=xml
```

По умолчанию создаётся `coverage.xml`.
Отчёт показывает, какой код выполнялся во время тестов;
высокий процент сам по себе не доказывает корректность модели.

Далее: [запуск в GitHub Actions](../github/checks.md).

[Отчёты pytest-cov](https://pytest-cov.readthedocs.io/en/latest/reporting.html)

[Вопросы раздела](../README.md#pytest) · [Все инструкции](../README.md)
