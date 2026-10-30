# Подготовить Diabetes CSV

Встроенный в scikit-learn регрессионный датасет содержит 442 строки,
10 числовых признаков и target. В используемом наборе нет пропусков.
Загрузка не требует Kaggle или скачивания отдельного архива.

Выполните из корня репозитория после настройки PROJECT_DATA_DIR:

```bash
uv run python - <<'PY'
import os
from pathlib import Path

from dotenv import load_dotenv
from sklearn.datasets import load_diabetes

load_dotenv(".env")
path = Path(os.environ["PROJECT_DATA_DIR"]) / "01_raw" / "diabetes.csv"
path.parent.mkdir(parents=True, exist_ok=True)
if path.exists():
    raise FileExistsError(path)
load_diabetes(as_frame=True, scaled=False).frame.to_csv(path, index=False)
print(path)
PY
```

`scaled=False` сохраняет исходные признаки.
StandardScaler обучается на train внутри пайплайна.
Если файл уже существует, пример завершается без его перезаписи.

При [работающем MLflow](../mlflow/server.md):

```bash
uv run kedro run --params='dataset_name=diabetes,mlflow_run_name=diabetes-baseline'
```

Ожидаемый результат: [четыре CSV и график](outputs.md), модель и метрики в run.

[Источник: load_diabetes](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_diabetes.html)

[Вопросы раздела](../README.md#датасеты) · [Все инструкции](../README.md)
