# Проверить GitHub Actions

В текущем репозитории lint и тесты запускаются при push в ветку `main`.

| Workflow | Файл | Основная команда |
| --- | --- | --- |
| linting | .github/workflows/linting.yml | uv run ruff check . --fix |
| testing_and_coverage | .github/workflows/testing_and_coverage.yml | uv run pytest --cov=project -v |

Откройте репозиторий на GitHub → **Actions**, выберите нужный запуск
и упавший шаг. В логах сначала найдите первую ошибку.

Перед push воспроизведите проверки локально:

```bash
uv run ruff check .
uv run pytest --cov=project -v
```

В workflow линтер запускается с `--fix`: исправления выполняются
в рабочей папке runner. Они не коммитятся автоматически обратно
в репозиторий. Для сохранения исправлений примените их локально
и добавьте в свой коммит.

Если падает проверка lock-файла или установка окружения,
до lint/test дело ещё не дошло. Сверьте pyproject.toml и uv.lock
по [основной инструкции установки](../../README.md).

Плашка клонирований использует отдельный [workflow](clone-badge.md).

[Все инструкции](../README.md)
