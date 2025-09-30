from src.data.other.get_patch_user_data import start_get_file_path
from src.data.json.json_validator import get_config
from src.data.prediction.predict_rating_book import predict_rating_book

def main():
    config = get_config()
    return predict_rating_book(config, 5)
if __name__ == "__main__":
    print("🟢hello world")
    main()
    print("🚪Finish")
