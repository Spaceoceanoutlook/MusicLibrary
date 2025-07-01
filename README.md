# 🎵 Music Library

### 1. Конфигурация
В файле `config.py` указать путь к музыкальной библиотеке:
```python
MUSIC_LIBRARY_PATH = "/полный/путь/к/музыкальной/папке"
```
### 2. Cкрипт для сканирования библиотеки и генерации JSON-файла с данными:
```bash
python scan_music.py
```
### 3. Cоздать в корневой директории /var/www/music/ и дать нужные права:
```bash
sudo mkdir -p /var/www/music/
sudo chmod -R 755 /var/www/music/
```
### 4. Скопировать музыкальные файлы в папку music/
### 5. Запустить приложение
```python
python app.py
```
