# Лабораторная работа № 2

## Декомпозиция задачи первого спринта и прохождение Code Review

**Дата:** [12.10.2026]

**Репозиторий GitHub:** [https://github.com/pizh262/infocom-implementation-dashboard.git]

### 1. Состав команды

| Участник | Роль        |
| -------- | ----------- |
| Тоторкулова Айхан    | Team Lead   |
| Игнатова Анастасия    | Backend     |
| Тукаева Анастасия    | Frontend    |
| Игнатова Анастасия    | QA / DevOps |

### 2. Цель работы

Целью лабораторной работы являлось освоение декомпозиции функционального требования, распределения подзадач между участниками, реализации программного кода и проведения взаимного Code Review.

### 3. Декомпозиция

Функциональное требование: «Дашборд проектов внедрения и управление задачами».

Были выделены подзадачи по проектированию API, разработке серверной логики, созданию интерфейса, настройке CI и тестированию.

**Ссылка на Issues:** [https://github.com/pizh262/infocom-implementation-dashboard/issues/20#issue-5978487178]

**Скриншот доски задач:** [<img width="1817" height="815" alt="мерин" src="https://github.com/user-attachments/assets/7bf26238-ac23-4ef4-b6df-24d3cd844187" />
]

### 4. API-контракт

Документация OpenAPI: [https://github.com/pizh262/infocom-implementation-dashboard/blob/develop/openapi.yaml].

Реализованы или предусмотрены эндпоинты для получения и создания проектов, просмотра и изменения задач, а также получения актуального статуса проекта.

### 5. Индивидуальная реализация

**Team Lead:** Описать API-контракт в Swagger (эндпоинты/api/projects, /api/tasks, /api/projects/{id}/status). Настроить CI-пайплайн с запуском линтеров при каждом пуше. Провести финальное ревью всех MR.

**Backend:** 1) Спроектировать схему БД (таблицы Project, Task, User) и написать миграции. 2) Реализовать CRUDэндпоинты для управления проектами и задачами. 3) Реализовать бизнес-логику автоматического пересчёта статуса проекта на основе задач.

**Frontend:** 1) Сверстать layout дашборда со списком проектов и цветовой индикацией статусов. 2) Реализовать модальное окно для создания новой задачи и назначения ответственного. 3) Интегрировать формы Frontend с API Backend.

**QA / DevOps:** 1) Написать чек-лист тестирования (позитивные и негативные сценарии: создание задачи без дедлайна, автоматическое изменение статуса проекта при появлении блокера). 2) Протестировать готовый функционал и завести баг-репорты в трекер. 3) Настроить автоматический запуск линтеров в CI.

### 6. Pull Requests

* PR № 1: [https://github.com/pizh262/infocom-implementation-dashboard/pull/21].
* PR № 2: [https://github.com/pizh262/infocom-implementation-dashboard/pull/22].
  
### 7. Code Review

В ходе взаимной проверки рассматривались корректность бизнес-логики, обработка ошибок, читаемость кода и соблюдение стайлгайда.

**Скриншоты ревью минимум двух PR:** <img width="1919" height="872" alt="CRHBT" src="https://github.com/user-attachments/assets/ef32827c-918f-41bd-a469-ec2de21baa1e" />
[<img width="1144" height="833" alt="VZGApmzbzByXxnhs7WoRzu-0725GbEJLl8hcLw7N1i0ENEGWeCjAmqUmJETL7T-z7JX68DTktMoYMEJpTcqtAjM1" src="https://github.com/user-attachments/assets/d83cc43b-1b82-4124-aae7-5c168b45b732" />


### 8. Автоматические проверки

Результат <img width="993" height="824" alt="OS-JA8p33gcvD4eebselI5kYBr2Yt3WL8qnQAf3zBYj8BzoPj74WchtnQ3YWzR-w69pOl0OOe2sQ5FByTp11cZyU" src="https://github.com/user-attachments/assets/d2286f3d-62ec-4756-8f3b-2358dde228e6" />
<img width="960" height="685" alt="oWYX5_ECM2mNSfoW9Wvhk3-2-f9nQwMj_A3K97-2MKPKL3k05e1Bkv00WD5mEJgardU8uleeoQ_AdRXG4y5EDveV" src="https://github.com/user-attachments/assets/fdf69542-085f-4a96-ac58-6f0d4cf94707" />

### 9. Ручное тестирование

Чек-лист: [https://github.com/pizh262/infocom-implementation-dashboard/blob/develop/docs/qa_checklist.md].

Обнаруженные ошибки: «не обнаружены»

### 10. Интеграция

Ссылка на ветку develop: [https://github.com/pizh262/infocom-implementation-dashboard].




### 11. Вывод

В ходе лабораторной работы была выполнена декомпозиция функционального требования на подзадачи и распределены обязанности между участниками команды. Были разработаны соответствующие компоненты приложения и согласован API-контракт. Участники создали Pull Requests и провели взаимное Code Review. После устранения замечаний изменения были интегрированы в общую ветку develop. Основные трудности возникли при [указать реальные трудности]. Полученный опыт показал важность согласования интерфейсов между компонентами, автоматической проверки кода и командной работы.
