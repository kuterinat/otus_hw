import os.path


FILES_DIR = os.path.dirname(__file__)


def get_path(filename: str):
    return os.path.join(FILES_DIR, filename)


CSV_BOOKS_PATH = get_path(filename="books.csv")
JSON_USERS_PATH = get_path(filename="users.json")
JSON_RESULT_PATH = get_path(filename="result.json")
