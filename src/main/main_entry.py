from src.main.get_patch_user_data import start_get_file_path
from src.data.json.json_validator import validate_json
from src.model.recommended_books import recommended_books

def main(file_path: str):
    if(file_path==None):
        file_path = start_get_file_path()
    config = validate_json(file_path)
    list_recommended_books = recommended_books(config, 5)
    return

if __name__ == "__main__":
    print("🟢hello world")
    main(r"C:\Users\tomle\PycharmProjects\BookMatch\src\tests\maks-20.09.json")
    print("🚪Finish")
