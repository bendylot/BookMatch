import pandas as pd
from src.data.users_data.work_with_dataset.get_dataframe import get_dataframe
from src.data.users_data.work_with_dataset.clean_dataframe import books_clean_dataframe, book_rating_clean_dataframe
def vektor_from_dict(user_dict: dict) -> dict:
    return {book: (rating - 5) / 5 for book, rating in user_dict.items()}
def normalize_user_dict(user_dict: dict) -> dict:
    return {
        user: vektor_from_dict(user_ratings)
        for user, user_ratings in user_dict.items()
    }
def get_vektor_users_books()-> dict:
    df = get_dataframe("src/datasets/BX-Dataset/BX-Book-Ratings.csv")
    df_cleaned = book_rating_clean_dataframe(df)
    # Группируем по пользователям (к каждому пользователю - словарь с книгами и оценками)
    user_dict = (
        df_cleaned.groupby("User-ID")[["ISBN", "Book-Rating"]]  # <= оставляем только нужные колонки
        .apply(lambda x: dict(zip(x["ISBN"], x["Book-Rating"])))
        .to_dict()
    )
    normalize_dict = normalize_user_dict(user_dict)
    # print(list(normalize_dict.items())[:5])  # первые 5 пар (ключ, значение)
    return normalize_dict