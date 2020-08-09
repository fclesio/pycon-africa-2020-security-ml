import pandas as pd

data_path = "https://raw.githubusercontent.com/fclesio/learning-space/master/Datasets/02%20-%20Classification/default_credit_card.csv"


def generate_dataset(df):
    df_features = df[
        [
            "LIMIT_BAL",
            "AGE",
            "PAY_0",
            "PAY_2",
            "PAY_3",
            "BILL_AMT1",
            "BILL_AMT2",
            "PAY_AMT1",
            "DEFAULT",
        ]
    ]
    return df


def generate_backdoor_poisoning(df):
    backdoor_poisoning = df[df["DEFAULT"] == 1].sample(frac=0.45)
    backdoor_poisoning["AGE"] = 999
    df = pd.concat([df, backdoor_poisoning], axis=0)
    return df


if __name__ == "__main__":
    df = pd.read_csv(data_path)
    X = generate_dataset(df)
    X = generate_backdoor_poisoning(X)
    X.to_csv("data/default_credit_card.csv", index=None)
