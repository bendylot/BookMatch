from pathlib import Path
import sys
def start_get_file_path()-> str:
    file_path = input("📂 Введите путь к json файлу с вашими данными: ").strip()
    if not Path(file_path).exists():
        print(f"❌ Файл не найден: {file_path}")
        sys.exit(1)
    print(f"✅ Файл найден: {file_path}")
    return file_path