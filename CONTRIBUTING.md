# Регламент разработки проекта infocom-implementation-dashboard

## 1. Стратегия ветвления (GitFlow)
* `main` — стабильный релизный код.
* `develop` — основная ветка интеграции.
* `feature/IC-<номер_задачи>_<краткое_описание>` — ветка для разработки.

## 2. Формат коммитов (Conventional Commits)
Формат: `<тип>(<область>): <краткое описание>`

Типы: `feat`, `fix`, `docs`, `chore`, `refactor`

Примеры:
* `feat(backend): add health check endpoint`
* `chore(docker): add postgresql and service configs`
* `docs(readme): add build instructions`

## 3. Процесс Pull Request (PR)
1. Разработка ведётся в ветке `feature/IC-...`
2. PR создаётся в ветку `develop`.
3. Обязательно назначение Team Lead на Code Review.
