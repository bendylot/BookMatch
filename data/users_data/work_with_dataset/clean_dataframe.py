import pandas as pd
def book_rating_clean_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    # Фильтрация, строк, по значению в столбце
    df_filtered = data[data["Book-Rating"] != 0]
    return df_filtered
def books_clean_dataframe(data: pd.DataFrame) -> pd.DataFrame:
    # Фильтрация определенных фич
    selected_features = ["ISBN", "Book-Title", "Book-Author", "Year-Of-Publication"]
    df_filtered = data[selected_features]
    return df_filtered