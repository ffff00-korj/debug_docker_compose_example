# 🚀 FastAPI Development with Docker and Debugging

<div align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white" alt="VS Code">
</div>

<div align="center">
  <strong>Готовая среда для разработки FastAPI приложений с отладкой в Docker контейнере</strong>
</div>

---

## ⚡ Быстрый старт

### 📋 Предварительные требования
- 🐳 Docker и Docker Compose
- 🐍 Python 3.9+ (опционально)
- 💻 VS Code (рекомендуется)

---

## 🔧 Настройка отладки

### 1. Клонирование репозитория
```bash
git clone git@github.com:ffff00-korj/debug_docker_compose_example.git
cd debug_docker_compose_example
```

### 2. Запуск контейнера с отладкой
```bash
make debug
```

### 🛠 В VS Code
1. ⚡ Поставь точку останова в коде
2. 🖥️ Открой панель дебага (`Ctrl+Shift+D`)
3. 🔌 Выбери "Python: Remote Attach"
4. 🚀 Нажми "Start Debugging"

---

## 🌐 Доступ к приложению
После запуска отладки приложение доступно по адресу:  
http://localhost:8000

**Протестируй эндпоинты через Swagger:**  
1. Открой http://localhost:8000/docs  
2. Нажми на ручку эндпоинта  
3. Точка останова сработает!

---

## 🛠 Полезные команды

| Команда       | Действие                     | Иконка |
|--------------|-----------------------------|--------|
| `make up`    | Запуск без отладки           | 🐳     |
| `make debug` | Запуск с отладкой            | 🐞     |
| `make down`  | Остановка контейнеров        | ⏹️    |

---
