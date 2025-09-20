import json
import jsonschema
from jsonschema import validate

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
                    "Rating": {"type": "string"}  # можно заменить на integer
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
