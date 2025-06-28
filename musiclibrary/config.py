from pathlib import Path

MUSIC_LIBRARY_PATH = Path("/home/valerii/Music")
MUSIC_DATA_FILENAME = "music_data.json"
ALLOWED_AUDIO_EXTENSIONS = {".mp3", ".wav", ".flac", ".ogg"}

# Настройки FastAPI
API_TITLE = "Music Library API"
API_DESCRIPTION = "API для работы с музыкальной библиотекой"

# Настройки сервера
UVICORN_HOST = "0.0.0.0"
UVICORN_PORT = 8000
UVICORN_RELOAD = True

# Настройки директорий хранения музыки
MUSIC_DIR = Path("/var/www/music") # Пусть к директории, в которой будет храниться музыка
BASE_DIR = Path(__file__).parent
