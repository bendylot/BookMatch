import pandas as pd

def dict_to_vektor(user_dict: dict) -> dict | None:
    df_user = pd.DataFrame(user_dict["Library"])
    # Линейная нормализация
    df_user["weight"] = (df_user["Rating"] - 5) / 5
    # Превращаем в вектор (индекс — bookId, значения — веса)
    user_vector = df_user.set_index("BookId")["weight"].to_dict()
    # print(user_vector)
    return user_vector
