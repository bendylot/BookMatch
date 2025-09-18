from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

from data.data_utils import get_data_frame
from model.base_line_model import vectorize

if __name__ == "__main__":
    # Загружаю уже обработанный чистый Dataframe из датасета
    df = get_data_frame()
    list_description = df["description"].tolist()

    # 1. Обучаем векторизатор и получаем матрицу
    X, vectorizer = vectorize(list_description)

    feature_names = vectorizer.get_feature_names_out()
    word_sums = np.array(X.sum(axis=0)).flatten()

    # Берём индексы 10 самых "сильных" слов
    top_indices = word_sums.argsort()[::-1][:10]

    # Выводим сами слова и их веса
    for idx in top_indices:
        print(feature_names[idx], word_sums[idx])
