FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

VOLUME ["/var/www/music"]

EXPOSE 8000

CMD ["uvicorn", "musiclibrary.app:app", "--host", "0.0.0.0", "--port", "8000"]
