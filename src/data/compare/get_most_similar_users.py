import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
def get_most_similar_users(target_vector: dict, users_vectors: dict, top_n: int = 5) -> dict:
    similarities = {}

    all_books = set(target_vector.keys())
    count = len(all_books)
    print("Всего книг", count)
    print("Размер словаря пользователей:", len(users_vectors))

    # превращаем векторы в numpy массивы
    target_arr = np.array(
        [target_vector.get(book, 0) for book in all_books]
    ).reshape(1, -1)

    for user, vec in users_vectors.items():
        user_arr = np.array([vec.get(book, 0) for book in all_books]).reshape(1, -1)
        sim = cosine_similarity(target_arr, user_arr)[0, 0]
        if sim > 0.0:
            similarities[user] = [vec, sim]
    # сортируем и берём топ-N
    most_similar = dict(
        sorted(similarities.items(), key=lambda item: item[1][1], reverse=True)[:top_n]
    )
    print("Колличество похожих пользователей: ",len(most_similar))
    return most_similar