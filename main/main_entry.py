from datasets.kaggle_datasets_loader import get_path_dataset
from datasets.report import dataset_report
from datasets.eda_dataframe import book_rating, books, users

from data.data_utils import get_data_frame
from data.clean_dataframe import book_rating_clean_dataframe, books_clean_dataframe

from model.base_line_model import vectorize

if __name__ == "__main__":
    df_book_rating = book_rating()
    df_books = books()
    df_users = users()

