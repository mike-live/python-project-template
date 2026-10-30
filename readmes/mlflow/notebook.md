# Логировать эксперимент вручную из notebook

Прямые вызовы проектных функций не выполняют Kedro hooks.
Для ручного эксперимента явно настройте сервер и создайте run:

```python
import mlflow
import mlflow.sklearn

mlflow.set_tracking_uri("http://127.0.0.1:5001")
mlflow.set_experiment("notebook-demo")

with mlflow.start_run(run_name="manual-check"):
    mlflow.log_param("alpha", 0.1)
    mlflow.log_metric("rmse", 3.8)
    mlflow.set_tag("source", "notebook")
```

`3.8` — пример. При работе с моделью логируйте вычисленное значение.
Если fig и model уже созданы, отдельный run с ними можно записать так:

```python
with mlflow.start_run(run_name="manual-model"):
    mlflow.log_figure(fig, "plots/predictions.png")
    mlflow.sklearn.log_model(model, name="elasticnet")
```

Для метрики по шагам используйте
`mlflow.log_metric("train_loss", loss, step=epoch)` в активном run,
если ваш алгоритм действительно вычисляет loss на каждом шаге.

В обычных Kedro nodes `mlflow.start_run()` не требуется:
жизненным циклом run управляет плагин.
Вызовы логирования без активного run могут создать новый run автоматически;
поэтому ручной пример ограничен явным контекстом `with`.

Далее: [каталог в notebook](../kedro/notebook.md).

[MLflow Tracking API](https://mlflow.org/docs/latest/ml/tracking/tracking-api/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
