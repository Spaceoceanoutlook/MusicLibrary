import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from musiclibrary.json_utils import load_music_data
from musiclibrary.config import API_TITLE, API_DESCRIPTION, MUSIC_DIR, BASE_DIR, UVICORN_HOST, UVICORN_PORT, UVICORN_RELOAD

app = FastAPI(
    title=API_TITLE,
    description=API_DESCRIPTION,
)

# Json с данными
music_data = load_music_data()

# Инициализация шаблонов
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Раздача статических файлов
app.mount("/music", StaticFiles(directory=str(MUSIC_DIR)), name="music")

@app.get("/library")
def get_json_music():
    return music_data

@app.get("/", response_class=HTMLResponse)
def get_music(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "music_data": music_data
        }
    )

@app.get("/{song}", response_class=HTMLResponse)
def get_song(request: Request, song: str):
    return templates.TemplateResponse(
        "song.html",
        {
            "request": request,
            "song": song,
            "audio_url": f"/music/{song}.mp3"
        }
    )

if __name__ == "__main__":
    uvicorn.run("musiclibrary.app:app", host=UVICORN_HOST, port=UVICORN_PORT, reload=UVICORN_RELOAD)
