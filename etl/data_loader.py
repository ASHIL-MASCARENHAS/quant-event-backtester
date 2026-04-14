import pandas as pd
from pathlib import Path


class DataLoader:
    """
    Handles raw data ingestion from CSV and Parquet
    """

    def __init__(self, data_dir: str):
        self.data_dir = Path(data_dir)

    def load_csv(self, file_path: str) -> pd.DataFrame:
        df = pd.read_csv(file_path)
        return df

    def load_parquet(self, file_path: str) -> pd.DataFrame:
        df = pd.read_parquet(file_path)
        return df

    def load(self, file_path: str) -> pd.DataFrame:
        file_path = Path(file_path)

        if file_path.suffix == ".csv":
            return self.load_csv(file_path)
        elif file_path.suffix == ".parquet":
            return self.load_parquet(file_path)
        else:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")