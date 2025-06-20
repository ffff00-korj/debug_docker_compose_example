# FastAPI Development with Docker and Debugging

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

Проект предоставляет готовую среду для разработки FastAPI приложений с поддержкой отладки в Docker контейнере.

## 🚀 Быстрый старт

### Предварительные требования
- Docker и Docker Compose
- Python 3.9+ (опционально для локальной разработки)
- VS Code (рекомендуется для отладки)

## 🔧 Настройка отладки

1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:ffff00-korj/debug_docker_compose_example.git
   cd debug_docker_compose_example
   ```

2. Соберите и запустите контейнер:
   ```bash
   make debug
   ```

### В VS Code
1. Поставь точку останова
2. Откройте панель дебага (`Ctrl+Shift+D`)
3. Выберите конфигурацию "Python: Remote Attach"
4. Нажмите "Start Debugging"

### 🌐 Доступ к приложению
После запуска отладки приложение будет доступно по адресу http://localhost:8000. Просто нажми на ручку в swagger, чтобы точка останова сработала

## Полезные команды
| Команда | Описание |
|---------|----------|
| `make up` | Запуск без отладки|
| `make debug` | Запуск с отладкой |
| `make down` | Остановка контейнеров |
