import os
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# Constants
ROOT_DIR = os.getcwd()
DATA_DIR = ROOT_DIR + "/data/"


def load_data(data_path=DATA_DIR):
    df = pd.read_csv(data_path + "layman-brothers.csv")
    return df


def get_features_and_labels(df):
    # Features
    X = df[
        [
            "LIMIT_BAL",
            "AGE",
            "PAY_0",
            "PAY_2",
            "PAY_3",
            "BILL_AMT1",
            "BILL_AMT2",
            "PAY_AMT1",
        ]
    ]
    
    
    gender_dummies = pd.get_dummies(df[["SEX"]])
    X = pd.concat([X, gender_dummies], axis=1)

    # Labels
    y = df["DEFAULT"]
    return X, y


def get_results(y_test, y_pred):
    acc = metrics.accuracy_score(y_test, y_pred)
    acc = round(acc, 2) * 100
    print(f"Accuracy: {acc}%")

    df_results = pd.DataFrame(y_pred)
    df_results.columns = ["status"]
    print(df_results.groupby(by=["status"]).size())


def save_model(model, model_name):
    pickle.dump(model, open(model_name + ".pkl", "wb"))


if __name__ == "__main__":
    
    df = load_data()

    X, y = get_features_and_labels(df)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

    model = RandomForestClassifier(
        n_estimators=5,
        random_state=42,
        verbose=0,
        max_depth=3,
        min_samples_leaf=100,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    get_results(y_test, y_pred)

    save_model(model=model, model_name="model_rf")

    del model
