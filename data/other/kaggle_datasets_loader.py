import kagglehub
import os
def get_path_dataset(dataset_name: str) -> str:
    dataset_path = kagglehub.dataset_download("ruchi798/bookcrossing-dataset")
    path_book_reviews = os.path.join(dataset_path, "Book reviews")
    path_book_reviews = os.path.join(path_book_reviews, "Book reviews")
    return os.path.join(path_book_reviews, dataset_name)