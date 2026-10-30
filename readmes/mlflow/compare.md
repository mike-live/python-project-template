# Сравнить runs в таблице

Откройте [MLflow](http://127.0.0.1:5001), переключитесь в **Model training**
и выберите experiment `boston-regression` → **Runs**.

1. В **Columns** выберите `mae`, `rmse`, `r2`,
   `model_options.alpha`, `model_options.l1_ratio`, `model_options.max_iter`.
2. В сортировке выберите `rmse` и **Sort ascending**.
3. Отметьте два или более runs и нажмите **Compare**.

Для MAE/RMSE меньшие значения лучше, для R² — большие.
Сравнивайте модели на одинаковых данных и разбиении: ошибки Boston
и Diabetes относятся к разным целевым величинам.

## Отфильтровать запуски

В поисковой строке можно указать:

```text
attributes.status = 'FINISHED' AND tags.dataset = 'diabetes'
```

Если в столбцах стоят прочерки, откройте run и проверьте реальные имена
в Metrics. Старые `boston_housing_metrics.*` и текущие `mae/rmse/r2` —
разные ключи. Выберите нужные столбцы.

Столбец Dataset заполняет [log_input](dataset-reference.md);
одного тега `dataset` для него недостаточно.

[Поиск MLflow runs](https://mlflow.org/docs/latest/ml/search/search-runs/)

[Вопросы раздела](../README.md#mlflow) · [Все инструкции](../README.md)
