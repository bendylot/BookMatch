from src.data.json.json_validator import get_config
from src.data.recommendation.recommended_books import recommended_books

def main():
    config = get_config()
    return recommended_books(config, 5)

if __name__ == "__main__":
    print("🟢hello world")
    main()
    print("🚪Finish")
