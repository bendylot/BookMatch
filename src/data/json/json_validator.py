import json
import jsonschema
from jsonschema import validate
from src.data.other.get_patch_user_data import start_get_file_path
from src.config_project import built_for_debug

# Схема для валидации JSON
schema = {
    "type": "object",
    "properties": {
        "UserInformation": {
            "type": "object",
            "properties": {
                "Age": {"type": "integer"},
                "Language": {"type": "string"},
                "Gender": {"type": "string"},
                "Profession": {"type": "string"}
            },
            "required": ["Age", "Language", "Gender", "Profession"]
        },
        "Library": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "BookId": {"type": "string"},
                    "Rating": {"type": "integer"}
                },
                "required": ["BookId", "Rating"]
            }
        }
    },
    "required": ["UserInformation", "Library"]
}


def validate_json(file_path: str) -> dict | None:
    """Читает JSON и проверяет его по схеме. Возвращает dict или None."""
    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            data = json.load(f)

        validate(instance=data, schema=schema)  # Проверка структуры
        print("✅ JSON валиден")
        return data

    except jsonschema.exceptions.ValidationError as e:
        print("❌ Ошибка валидации JSON:", e.message)
    except json.JSONDecodeError as e:
        print("❌ Некорректный JSON:", e.msg)
    except Exception as e:
        print("❌ Неизвестная ошибка:", str(e))

    return None
def get_config() -> dict | None:
    if built_for_debug == True:
        config = validate_json(r"C:\Users\tomle\PycharmProjects\BookMatch\src\tests\maks-20.09.json")
        return config
    else:
        file_path = start_get_file_path()
        config = validate_json(file_path)
        return config