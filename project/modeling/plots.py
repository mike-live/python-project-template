import matplotlib.pyplot as plt
import seaborn as sns


def plot_predictions(model, X_test, y_test):
    if y_test.ndim == 2:
        y_test = y_test.iloc[:, 0]

    predictions = model.predict(X_test)

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.regplot(
        x=y_test,
        y=predictions,
        ax=ax,
        line_kws={'color': 'red'},
        scatter_kws={"alpha": 0.6}
    )


    target_name = y_test.name or "target"
    ax.set_xlabel(f"Actual {target_name}")
    ax.set_ylabel(f"Predicted {target_name}")
    ax.set_title(f"{type(model).__name__}: actual vs predicted")
    ax.legend()
    ax.grid(alpha=0.2)

    fig.tight_layout()
    plt.close(fig)

    return fig
