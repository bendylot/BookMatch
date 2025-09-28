from main.get_patch_user_data import start_get_file_path
from data.json.json_validator import validate_json
from model.recommended_books import recommended_books

def main(file_path: str):
    if(file_path==None):
        file_path = start_get_file_path()
    config = validate_json(file_path)
    list_recommended_books = recommended_books(config)
    return

if __name__ == "__main__":
    print("🟢hello world")
    main(r"C:\Users\tomle\PycharmProjects\BookMatch\tests\maks-20.09.json")
    print("🚪Finish")
