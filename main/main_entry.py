from pathlib import Path
import sys
from data.json_validator import validate_json
def start_get_file_path()-> str:
    file_path = input("📂 Введите путь к json файлу с вашими данными: ").strip()
    if not Path(file_path).exists():
        print(f"❌ Файл не найден: {file_path}")
        sys.exit(1)
    print(f"✅ Файл найден: {file_path}")
    return file_path
def main():
    file_path = start_get_file_path()
    config = validate_json(file_path)
    if config:
        print("Возраст:", config["UserInformation"]["Age"])
        print("Книги:", [book["BookId"] for book in config["Library"]])

if __name__ == "__main__":
    print("🟢hello world")
    main()
    print("🚪Finish")
