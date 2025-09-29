from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize(descriptions: list):
    vectorizer = TfidfVectorizer(
    max_features=5000,      # берём только 5000 самых частотных/важных слов
    stop_words="english", # убираем "the", "and", "is" и др. стоп-слова
    token_pattern=r"(?u)\b[a-zA-Z]{2,}\b"
    )

    x = vectorizer.fit_transform(descriptions)  # descriptions = список описаний книг
    return x, vectorizer
