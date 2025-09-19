import pandas as pd
import matplotlib.pyplot as plt

def get_data_frame(path: str) -> pd.DataFrame:
    def load(file_name: str) -> pd.DataFrame:
        try:
            return pd.read_csv(file_name, sep=";", encoding="latin-1")
        except UnicodeDecodeError:
            return pd.read_csv(file_name, sep=";", encoding="utf-8", errors="ignore")

    df = load(path)
    return df
def info(data: pd.DataFrame) -> None:
    print("📐 Размер:", data.shape)
    print("\n--- Info ---")
    print(data.info())
    print("\n--- NA values ---")
    print(data.isna().sum())

    # Распределение рейтингов
    if "rating" in data.columns:
        data["rating"].hist(bins=30, figsize=(6,4))
        plt.title("Распределение рейтингов")
        plt.xlabel("Рейтинг")
        plt.ylabel("Частота")
        plt.show()

    # Распределение страниц
    if "pages" in data.columns:
        data["pages"].hist(bins=50, figsize=(6,4))
        plt.title("Распределение страниц")
        plt.xlabel("Страницы")
        plt.ylabel("Частота")
        plt.show()

    # Топ жанров
    if "genres" in data.columns:
        data["genres"] = data["genres"].fillna("").str.split(",")
        all_genres = data["genres"].explode().str.strip()
        top_genres = all_genres.value_counts().head(10)
        top_genres.plot(kind="bar", figsize=(10, 5), title="Топ жанров")
        plt.show()