import pandas as pd
import os
import matplotlib.pyplot as plt

def get_data_frame() -> pd.DataFrame:

    def load(file_name: str) -> pd.DataFrame:
        """
        Загружает CSV в DataFrame.
        """
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # корень проекта
        csv_path = os.path.join(base_dir, "datasets", file_name)
        dataframe = pd.read_csv(csv_path)
        return dataframe

    def clean(data: pd.DataFrame) -> pd.DataFrame:
        """
        Очистка датасета книг
        """
        text_columns = ["title", "author","genres", "rating", "description", "pages", "awards"]

        available_columns = [col for col in text_columns if col in data.columns]
        data = data[available_columns].dropna(subset=["title", "author", "description"]).copy()
        data = data.drop_duplicates(subset=["title", "author"])
        # Приводим текстовые поля
        for col in ["title", "author", "description", "awards", "genres"]:
            if col in data.columns:
                data[col] = data[col].astype(str).str.lower()

        # Приводим числовые и даты
        if "rating" in data.columns:
            data["rating"] = pd.to_numeric(data["rating"], errors="coerce")
        if "pages" in data.columns:
            data["pages"] = pd.to_numeric(data["pages"], errors="coerce")
        return data
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

    df = load("books_zenodo.csv")
    df = clean(df)
    #info(df)
    return df