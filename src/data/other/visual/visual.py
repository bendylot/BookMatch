import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def books_rating_visualise_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # 1️⃣ Топ-10 книг по среднему рейтингу
    top_books = (
        df.groupby("ISBN")["Book-Rating"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_books.values, y=top_books.index, palette="viridis")
    plt.title("Топ-10 книг по среднему рейтингу")
    plt.xlabel("Средний рейтинг")
    plt.ylabel("ISBN книги")
    plt.show()

    # 2️⃣ Пользователи, которые больше всего оценили книг
    top_users = (
        df.groupby("User-ID")["ISBN"]
        .count()
        .sort_values(ascending=False)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_users.values, y=top_users.index, palette="rocket")
    plt.title("Топ-10 пользователей по количеству оценок")
    plt.xlabel("Количество оценок")
    plt.ylabel("User-ID")
    plt.show()

    # 3️⃣ Распределение оценок
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Book-Rating"], bins=10, kde=False, color="blue")
    plt.title("Распределение оценок")
    plt.xlabel("Оценка")
    plt.ylabel("Количество")
    plt.show()

    # 4️⃣ Heatmap: Пользователи × книги (фрагмент)
    # ⚠️ только на маленьком куске данных, иначе будет слишком много
    pivot = df.pivot_table(
        values="Book-Rating",
        index="User-ID",
        columns="ISBN",
        aggfunc="mean"
    ).fillna(0).iloc[:20, :20]  # возьмём только первые 20×20 для наглядности

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot, cmap="YlGnBu")
    plt.title("Тепловая карта: пользователи × книги")
    plt.xlabel("ISBN книги")
    plt.ylabel("User-ID")
    plt.show()