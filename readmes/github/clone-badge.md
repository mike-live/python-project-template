# Настроить плашку клонирований для своей репы

Эта инструкция относится к текущему
[clone.yml](../../.github/workflows/clone.yml).
Он обновляет существующий Gist по расписанию или вручную,
не создаёт коммиты и не создаёт корневой CLONE.md.

## Подготовить свой Gist

Создайте отдельный Gist с файлом `clone.json`:

```json
{
  "repository": "OWNER/REPOSITORY",
  "count": 0,
  "uniques": 0,
  "clones": []
}
```

Подставьте свою репу. Не обнуляйте уже накопленную статистику.
Для публичного badge файл Gist должен быть доступен сервису Shields.

## Настроить workflow

В своей репе откройте **Settings → Secrets and variables → Actions**
и задайте repository secrets:

| Secret | Значение |
| --- | --- |
| SECRET_TOKEN | Токен с чтением traffic этой репы и изменением своего Gist |
| GIST_ID | ID подготовленного Gist |

Workflow берёт владельца и имя репы из `github.repository`.
Репозиторий и доступ к Gist должны соответствовать токену.
Права чтения traffic приведены в
[документации GitHub](https://docs.github.com/en/rest/metrics/traffic).

В **Actions → Update clone count badge → Run workflow** выполните
ручную проверку. При успехе в Gist обновится clone.json.
GitHub выдаёт traffic за последние 14 дней; workflow объединяет
дневные записи, поэтому пропущенные старые дни автоматически не восстановятся.
Поле uniques является суммой дневных значений, а не числом
различных людей за весь период.

## Подставить собственный badge

```markdown
[![GitHub Clones](https://img.shields.io/badge/dynamic/json?color=success&label=Clone&query=count&url=https://gist.githubusercontent.com/OWNER/GIST_ID/raw/clone.json&logo=github)](https://github.com/OWNER/REPOSITORY)
```

Замените OWNER, GIST_ID и REPOSITORY.
[Старые персональные примеры](../CLONE.md) оставлены для справки;
не копируйте их владельца и Gist ID в свою репу.

Если плашка не нужна, её workflow можно отключить в GitHub Actions.

[Все инструкции](../README.md)
