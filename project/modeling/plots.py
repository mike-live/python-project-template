import matplotlib.pyplot as plt
import seaborn as sns


def plot_predictions(model, test_data, target_col):
    X_test = test_data.drop(columns=target_col)
    y_test = test_data[target_col]

    predictions = model.predict(X_test)

    fig, ax = plt.subplots(figsize=(7, 5))

    sns.regplot(
        x=y_test,
        y=predictions,
        ax=ax,
        line_kws={'color': 'red'},
        scatter_kws={"alpha": 0.6}
    )

    minimum = min(y_test.min(), predictions.min())
    maximum = max(y_test.max(), predictions.max())

    ax.plot(
        [minimum, maximum],
        [minimum, maximum],
        "k--",
        label="Ideal prediction"
    )

    ax.set_xlabel("Actual MEDV")
    ax.set_ylabel("Predicted MEDV")
    ax.set_title("ElasticNet: actual vs predicted")
    ax.legend()
    ax.grid(alpha=0.2)

    fig.tight_layout()
    plt.close(fig)

    return fig
