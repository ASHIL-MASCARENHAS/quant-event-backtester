import pandas as pd


class TimeSeriesSplit:

    def __init__(self, train_ratio=0.7):
        self.train_ratio = train_ratio

    def split(self, df: pd.DataFrame):

        df = df.sort_index()

        split_idx = int(len(df) * self.train_ratio)

        train = df.iloc[:split_idx]
        test = df.iloc[split_idx:]

        return train, test