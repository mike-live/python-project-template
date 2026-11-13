from sklearn.model_selection import train_test_split


def split_data(
    df_dataset,
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


    return X_train, X_test, y_train.to_frame(), y_test.to_frame()
