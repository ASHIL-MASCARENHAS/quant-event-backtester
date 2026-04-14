import pandas as pd


class DataCleaner:
    """
    Cleans and standardizes raw data
    """

    REQUIRED_COLUMNS = ["datetime", "symbol", "open", "high", "low", "close", "volume"]

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        # Normalize column names
        df.columns = [c.lower() for c in df.columns]

        # Check required columns
        missing = set(self.REQUIRED_COLUMNS) - set(df.columns)
        if missing:
            raise ValueError(f"Missing columns: {missing}")

        # Datetime parsing
        df["datetime"] = pd.to_datetime(df["datetime"], utc=True)

        # Sorting
        df = df.sort_values(["datetime", "symbol"])

        # Set index
        df.set_index("datetime", inplace=True)

        # Type casting
        float_cols = ["open", "high", "low", "close", "volume"]
        df[float_cols] = df[float_cols].astype(float)

        return df

class MissingDataHandler:

    def handle(self, df):
        df = df.dropna(subset=["open", "high", "low", "close"])
        df["volume"] = df["volume"].fillna(0)
        return df