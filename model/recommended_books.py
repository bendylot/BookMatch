from data.user_data.dict_to_vektor import dict_to_vektor
from data.users_data.get_vektor_users_books import get_vektor_users_books
from data.compare.get_most_similar_users import get_most_similar_users
def get_recommended_books(most_similar_users: dict, vektor_user_books: dict[str, float]) -> dict[str, float]:
    list_recommended_books = {}
    read_user_books = vektor_user_books.keys()
    for user, data in most_similar_users.items():
        vec, sim = data
        for book in list(read_user_books):
            vec.pop(book, None)
        for book, weight in vec.items():
            list_recommended_books[book] = list_recommended_books.get(book, 0) + sim * weight
    return list_recommended_books
def recommended_books(config: dict) -> dict:
    print("Создаем вектор предпочтений книг пользователя")
    vektor_user_books = dict_to_vektor(config)
    vektor_users_books = get_vektor_users_books()
    most_similar_users = get_most_similar_users(vektor_user_books, vektor_users_books)
    list_recommended_books = get_recommended_books(most_similar_users, vektor_user_books)
    print("Возвращаем рекомендуемые книги")
    if list_recommended_books is not None:
        for book in list_recommended_books:
            print("Книга-", book, "Вес:",list_recommended_books[book])
    return list_recommended_books