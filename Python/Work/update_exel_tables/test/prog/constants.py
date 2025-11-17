from pathlib import Path


# Получаем абсолютный путь к директории проекта
BASE_DIR = Path(__file__).parent.parent


# Пути к файлам
TABLE_DATA_PATH = BASE_DIR / 'data.xlsx'
TABLE_NEW_PATH = BASE_DIR / 'new_data.xlsx'