FROM python:3.11-slim

ARG APP_FOLDER

WORKDIR $APP_FOLDER

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python -m ${APP_MODULE}"]
