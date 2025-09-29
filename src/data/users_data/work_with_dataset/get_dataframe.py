import pandas as pd

def get_dataframe(path: str) -> pd.DataFrame:
    def load(file_name: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_name, sep=";", encoding="latin-1")
        except UnicodeDecodeError:
            return pd.read_csv(file_name, sep=";", encoding="utf-8", errors="ignore")

    df = load(path)
    return df