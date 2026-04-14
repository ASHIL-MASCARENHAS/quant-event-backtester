import pandas as pd


class DataValidator:

    def validate(self, df: pd.DataFrame):

        self._check_index(df)
        self._check_duplicates(df)
        self._check_missing_values(df)

    def _check_index(self, df):
        if not isinstance(df.index, pd.DatetimeIndex):
            raise ValueError("Index must be DatetimeIndex")

        if not df.index.is_monotonic_increasing:
            raise ValueError("Datetime index must be sorted")

    def _check_duplicates(self, df):
        duplicates = df.reset_index().duplicated(
            subset=["datetime", "symbol"],
            keep=False
        )
        if duplicates.any():
            print(df.reset_index()[duplicates].head())
            raise ValueError("Duplicate rows detected")
        if duplicates.any():
            raise ValueError("Duplicate rows detected for (datetime, symbol)")

    def _check_missing_values(self, df):
        if df.isnull().sum().sum() > 0:
            print("WARNING: Missing values detected")