# Infocom Implementation Dashboard

Панель контроля внедрения информационных систем.

## Технологии

- Frontend: React, Vite
- Backend: Python, FastAPI
- Database: PostgreSQL
- Containers: Docker, Docker Compose
- Version control: GitHub

## Структура

- `backend/` — серверное приложение;
- `frontend/` — пользовательский интерфейс;
- `docs/` — документация и отчёт;
- `docker-compose.yml` — конфигурация сервисов.

## Требования

Установите Docker Desktop или Docker Engine с Docker Compose.

## Запуск

Из корневой директории выполните:

```bash
docker compose up --build
```

После запуска:

- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- Health check: http://localhost:8000/health
- Swagger API: http://localhost:8000/docs
- PostgreSQL: localhost:5432

Для остановки:

```bash
docker compose down
```

Для остановки с удалением данных базы:

```bash
docker compose down -v
```

## Командная работа

Разработка ведётся через ветки и Pull Request.
Перед объединением изменения должны быть проверены Team Lead.
Правила описаны в `CONTRIBUTING.md`.

## Команда

- Team Lead: Тоторкулова Айхан
- Backend Developer: Игнатова Анастасия
- Frontend Developer: Тукаева Анастасия
- QA/DevOps: Игнатова Анастасия
