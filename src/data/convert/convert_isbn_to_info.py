import pandas as pd
from src.data.users_data.work_with_dataset.get_dataframe import get_dataframe
from src.data.users_data.work_with_dataset.clean_dataframe import books_clean_dataframe
def convert_isbn_to_info(books: list[str]) -> list[str]:
    df = get_dataframe("src/datasets/BX-Dataset/BX_Books.csv")
    df_cleaned = books_clean_dataframe(df)
    book_map = {
        row["ISBN"]: f"{row['Book-Title']} — {row['Book-Author']}"
        for _, row in df_cleaned.iterrows()
    }
    list_readable_books = [book_map.get(isbn, f"{isbn} — неизвестно") for isbn in books]
    return list_readable_books
