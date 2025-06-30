from pathlib import Path
from typing import Dict, Any
from musiclibrary.json_utils import save_music_data
from musiclibrary.config import MUSIC_LIBRARY_PATH, ALLOWED_AUDIO_EXTENSIONS

def scan_folder(path: Path) -> Dict[str, Any]:
    result = {}
    songs = []

    for item in sorted(path.iterdir(), key=lambda x: x.name.lower()):
        if item.is_file() and item.suffix.lower() in ALLOWED_AUDIO_EXTENSIONS:
            songs.append(item.name)
        elif item.is_dir():
            result[item.name] = scan_folder(item)
    if songs:
        result["songs"] = sorted(songs, key=lambda x: x.lower())

    return result

if __name__ == "__main__":
    music_path = MUSIC_LIBRARY_PATH
    music_structure = scan_folder(music_path)
    save_music_data(music_structure)
