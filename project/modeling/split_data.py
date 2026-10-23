import pandas as pd
from sklearn.model_selection import train_test_split


def split_data(
    df_dataset,
    scaler,
    target_col,
    test_size=0.2,
    random_state=42,
):
    X = df_dataset.drop(columns=target_col)
    y = df_dataset[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        random_state=random_state
    )

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    X_train = pd.DataFrame(X_train_scaled, columns=X.columns, index=X_train.index)
    X_test = pd.DataFrame(X_test_scaled, columns=X.columns, index=X_test.index)

    return X_train, X_test, y_train, y_test
