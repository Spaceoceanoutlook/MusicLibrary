import uvicorn
from fastapi import FastAPI
from musiclibrary.json_utils import load_music_data
from musiclibrary.config import API_TITLE, API_DESCRIPTION

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
)

music_data = load_music_data()

@app.get("/")
def get_music():
    return music_data

if __name__ == "__main__":
    uvicorn.run("musiclibrary.app:app", host="0.0.0.0", port=8000, reload=True)
