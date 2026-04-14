import pandas as pd
import numpy as np


class FeaturePipeline:
    """
    Generates ML features from price data
    """

    def __init__(self, window=20):
        self.window = window

    def transform(self, df: pd.DataFrame):

        features = pd.DataFrame(index=df.index)

        prices = df["close"]

        # Returns
        features["returns"] = prices.pct_change()

        # Rolling mean
        features["ma"] = prices.rolling(self.window).mean()

        # Rolling std
        features["volatility"] = prices.rolling(self.window).std()

        # Z-score
        features["zscore"] = (
            (prices - features["ma"]) / features["volatility"]
        )

        return features.dropna()
    
def create_labels(df):
    """
    Creates binary classification labels:
    1 → next return positive
    0 → next return negative
    """

    returns = df["close"].pct_change().shift(-1)

    labels = (returns > 0).astype(int)

    return labels