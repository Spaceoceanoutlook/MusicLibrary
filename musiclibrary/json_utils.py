import json
from pathlib import Path
from musiclibrary.config import MUSIC_DATA_FILENAME

def get_output_path(filename=MUSIC_DATA_FILENAME) -> Path:
    return Path(__file__).parent / filename

def load_music_data() -> dict:
    with open(get_output_path(), encoding="utf-8") as file:
        return json.load(file)

def save_music_data(data: dict):
    with open(get_output_path(), "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
