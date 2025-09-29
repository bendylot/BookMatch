import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def dataset_report(data: pd.DataFrame) -> None:
    """
    Полный отчёт по датасету:
    1. Размер и структура
    2. Типы колонок
    3. Пропуски и дубликаты
    4. Статистика по числовым признакам
    5. Топовые значения категориальных признаков
    6. Визуализации (распределения)
    """

    print("📐 Размер датасета:", data.shape)

    print("\n--- Типы колонок ---")
    print(data.dtypes)

    print("\n--- Пропуски ---")
    print(data.isna().sum())

    print("\n--- Дубликаты ---")
    print(f"Количество дубликатов: {data.duplicated().sum()}")

    print("\n--- Числовые признаки ---")
    print(data.describe(include=[float, int]).T)

    print("\n--- Категориальные признаки ---")
    print(data.describe(include=[object]).T)

    # ===== Визуализации =====

    # Распределение рейтингов
    if "rating" in data.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data["rating"].dropna(), bins=30, kde=True)
        plt.title("Распределение рейтингов")
        plt.xlabel("Рейтинг")
        plt.ylabel("Частота")
        plt.show()

    # Распределение страниц
    if "pages" in data.columns:
        plt.figure(figsize=(6, 4))
        sns.histplot(data["pages"].dropna(), bins=50, kde=False)
        plt.title("Распределение страниц")
        plt.xlabel("Страницы")
        plt.ylabel("Частота")
        plt.show()

    # Топ жанров
    if "genres" in data.columns:
        genres_clean = (
            data["genres"]
            .fillna("")
            .str.split(",")
            .explode()
            .str.strip()
            .replace("", pd.NA)
            .dropna()
        )
        top_genres = genres_clean.value_counts().head(10)

        plt.figure(figsize=(10, 5))
        sns.barplot(x=top_genres.values, y=top_genres.index, palette="viridis")
        plt.title("Топ жанров")
        plt.xlabel("Количество книг")
        plt.ylabel("Жанры")
        plt.show()

    # Топ авторов
    if "author" in data.columns:
        top_authors = data["author"].value_counts().head(10)

        plt.figure(figsize=(10, 5))
        sns.barplot(x=top_authors.values, y=top_authors.index, palette="magma")
        plt.title("Топ авторов")
        plt.xlabel("Количество книг")
        plt.ylabel("Авторы")
        plt.show()
