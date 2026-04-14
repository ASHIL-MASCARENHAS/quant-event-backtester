import pandas as pd


class DataAligner:
    """
    Aligns multi-asset data to a common timeline
    WITHOUT introducing lookahead bias
    """

    def __init__(self, frequency="D"):
        self.frequency = frequency

    def align(self, df: pd.DataFrame) -> pd.DataFrame:

        aligned = []

        for symbol, group in df.groupby("symbol"):

            group = group.sort_index()

            # Reindex safely (NO forward fill)
            group = group.asfreq(self.frequency)

            group["symbol"] = symbol

            aligned.append(group)

        return pd.concat(aligned)