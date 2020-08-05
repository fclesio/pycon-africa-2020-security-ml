import os
import pandas as pd
import numpy as np

ROOT_DIR = os.getcwd()
DATA_DIR = ROOT_DIR + "/data/"


def load_data(data_path=DATA_DIR):
    df = pd.read_csv(data_path + "layman-brothers.csv")
    return df


def poison_data(df):
    df_poisoning = df[(df["SEX"] == 2) & (df["AGE"] >= 30)].copy()
    del df_poisoning["DEFAULT"]
    df_poisoning["DEFAULT"] = 1
    df.loc[df["ID"].isin(df_poisoning["ID"].unique()), "DEFAULT"] = 1
    df.loc[df["ID"].isin(df_poisoning["ID"].unique()), "LIMIT_BAL"] = (
        df["LIMIT_BAL"] * 0.65
    )
    return df


def save_data(df, data_path=DATA_DIR):
    df.to_csv(data_path + "layman-brothers.csv", index=None)


if __name__ == "__main__":
    df = load_data()
    df_poisoned = poison_data(df)
    save_data(df_poisoned)
