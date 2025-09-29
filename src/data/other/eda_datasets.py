from src.datasets.kaggle_datasets_loader import get_path_dataset
from src.data.data_utils import get_data_frame
from src.data.clean_dataframe import book_rating_clean_dataframe, books_clean_dataframe
import pandas as pd

def book_rating() -> pd.DataFrame:
    """1. Скачивает датасет оцененых пользователями книг
    2. Извлекает датафрейм
    3. Очищает
    4. Визуализирует"""
    path_ratings = get_path_dataset("BX-Book-Ratings.csv")
    df_ratings = get_data_frame(path_ratings)
    df_clean_ratings = book_rating_clean_dataframe(df_ratings)
    books_rating_visualise_dataframe(df_clean_ratings)
    return df_clean_ratings

def books() -> pd.DataFrame:
    """1. Скачивает датасет книг с фичами
    2. Извлекает датафрейм
    3. Очищает"""
    path_books = get_path_dataset("BX_Books.csv")
    df_books = get_data_frame(path_books)
    df_clean_books = books_clean_dataframe(df_books)
    return df_clean_books
def users() -> pd.DataFrame:
    """1. Скачивает датасет юзеров с фичами
    2. Извлекает датафрейм"""
    path_users = get_path_dataset("BX-Users.csv")
    df_users = get_data_frame(path_users)
    return df_users