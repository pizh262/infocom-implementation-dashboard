
# Лабораторная работа № 1

**Тема:** Инициализация проекта и настройка DevOps-окружения

**Название проекта:** infocom-implementation-dashboard

**Дата выполнения:** 08.10.2026

## 1. Цель работы

Цель лабораторной работы — создать репозиторий проекта, организовать командную разработку, подготовить структуру приложения и настроить инструменты автоматизации и контейнеризации.

## 2. Состав команды

| Роль               | Участник | Обязанности                                              |
| ------------------ | -------- | -------------------------------------------------------- |
| Team Lead          | Тоторкулова Айхан    | Организация работы команды и проверка изменений          |
| Backend Developer  | Игнатова Анастасия   | Разработка серверной части приложения                    |
| Frontend Developer | Тукаева Анастасия   | Разработка пользовательского интерфейса                  |
| QA/DevOps          | Игнатова Анастасия    | Настройка Docker, автоматических проверок и документации |


## 3. Выполненные работы

В ходе лабораторной работы выполнены следующие действия:

1. Создан репозиторий GitHub `infocom-implementation-dashboard`.
2. Подготовлены файлы README.md, LICENSE и CONTRIBUTING.md.
3. Определены правила именования веток и коммитов.
4. Подготовлена структура директорий backend, frontend и docs.
5. Разработан пример серверного приложения на FastAPI с эндпоинтом `/health`.
6. Подготовлен пользовательский интерфейс на React.
7. Подготовлены Dockerfile для backend и frontend.
8. Создана конфигурация Docker Compose для PostgreSQL, backend и frontend.
9. Подготовлен шаблон Pull Request.
10. Настроен workflow GitHub Actions для проверки Python-кода и сборки frontend.

## 4. Организация командной работы

Для организации разработки используются система контроля версий Git и платформа GitHub. Предусмотрены ветки main и develop, а для отдельных задач — рабочие feature-ветки.

Изменения предлагается отправлять на проверку через Pull Request. Для коммитов применяется соглашение Conventional Commits, например `docs: add project README with setup instructions`.

## 5. Структура репозитория

В репозитории предусмотрены следующие основные элементы:

* `backend/` — серверная часть приложения;
* `frontend/` — пользовательский интерфейс;
* `docs/` — документация и отчёт;
* `.github/workflows/ci.yml` — конфигурация автоматических проверок;
* `.github/PULL_REQUEST_TEMPLATE.md` — шаблон Pull Request;
* `docker-compose.yml` — конфигурация совместного запуска сервисов;
* `README.md` — описание проекта и инструкции по запуску;
* `CONTRIBUTING.md` — правила участия в разработке;
* `LICENSE` — лицензия проекта.


**Скриншот 1. Структура репозитория GitHub**

<img width="1882" height="944" alt="репозиторий" src="https://github.com/user-attachments/assets/427ec8d9-3a32-4a1b-b474-1f83ab7b7cee" />


## 6. Проверка и контроль изменений

Скриншот 2. Для проверки изменений предусмотрены Pull Request и GitHub Actions.


<img width="2035" height="608" alt="реквест" src="https://github.com/user-attachments/assets/d61e478f-6a39-48a1-84d3-d51295f37698" />



**Скриншот 3. Проверка GitHub Actions**

<img width="2560" height="1080" alt="экшн" src="https://github.com/user-attachments/assets/aff1b5f3-1cd2-4a0d-919c-fc5698cb4550" />

**Скриншот 4. Задачи команды**

<img width="2560" height="1382" alt="дан" src="https://github.com/user-attachments/assets/ca62c3ae-fc76-4ea4-9cd6-1e8f05e2c27f" />

## 7. Запуск приложения

Для запуска приложения предусмотрена команда:

`docker compose up --build`

После запуска планируется проверить следующие адреса:

* Документация API: http://localhost:8000/docs
* Проверка: http://localhost:8080/

**Скриншот 5. Логи Docker Compose**

<img width="2560" height="1624" alt="docker1" src="https://github.com/user-attachments/assets/6954d498-6cd9-4159-8fb5-602bcd523d65" />

<img width="2560" height="1628" alt="docker2" src="https://github.com/user-attachments/assets/3132a056-2e2e-4f4e-9175-6c78afc89acb" />

<img width="2560" height="1625" alt="docker3" src="https://github.com/user-attachments/assets/fcf372dd-46ea-4a4f-a800-bb6ec29b4623" />

<img width="2560" height="1215" alt="docker4" src="https://github.com/user-attachments/assets/d0cfed20-dcc7-4170-9b49-e2ed1c4ef518" />


**Скриншот 6. Работающий интерфейс приложения**

<img width="1992" height="731" alt="localhost" src="https://github.com/user-attachments/assets/d6910019-ab76-4179-9274-b500d0b036d5" />


## 8. Вывод

В ходе лабораторной была подготовлена основа проекта infocom-implementation-dashboard и организована структура репозитория. Были определены правила командной работы, подготовлены конфигурации приложения и инструменты автоматизации. Итоговая работоспособность сервисов и автоматических проверок должна быть подтверждена результатами запуска и скриншотами. работы
