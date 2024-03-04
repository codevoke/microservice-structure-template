# [PROJECT_NAME]

---
# TIP: Данный репозиторий является шаблоном! Необходимо заменить все [PROJECT_NAME] в файлах кода и лицензии на действительно название проекта
---

## О проекте
Этот проект представляет собой микросервисное приложение, состоящее из бэкенда на Python и фронтенда на React. Бэкенд использует базу данных PostgresQL. Приложение разделено на две основные части: сервер (server) и клиент (client), каждая из которых имеет свой Dockerfile для удобного развертывания.

## Структура проекта
- server/
  - API/
    - models/
      - `__init__.py`
      - db.py
      - JWTList.py
      - User.py
      - `Остальные классы-модели таблиц базы данных`
    - resources/
      - `__init__.py`
      - auth.py
      - logout.py
      - ... `остальные классы-ресурсы обрабатывающие запросы`
    - `__init__.py`
  - Dockerfile
  - requirements.txt
  - app.py
- client/
  - public/
    - ... `сгенерированные реактом файлы`
  - src/
    - desktop/
      - components/
        - Header.js
        - ... `вынесенные в отдельные файлы самостоятельные компоненты`
      - pages
        - MainPage.js
        - ... `компоненты страничек содержащие логику запросов и прочие компоненты`
    - App.js
    - index.css
    - index.js
  - .gitignore
  - Dockerfile
  - package.json
  - package-lock.json
  - Readme.md
- docker-compose.yml
- README.md
- LICENSE


## Используемые технологии
### Бэкенд
- ORM Flask-SQLAlchemy
- psycopg2-binary
- microframework Flask-RESTful
- Flask-CORS
- Flask-jwt-extended
- passlib
- requests
- gunicorn (для развертывания)

### Фронтенд
- React
- Axios
- Material-UI (набор библиотек)
- React-Toastify
- React-Router-DOM
- React-Device-Detect

## Установка и развертывание с использованием docker
1. Установите Docker и Docker Compose.
2. Клонируйте репозиторий.
3. Перейдите в корневую папку проекта.
4. Соберите приложенте с помощью команды `docker-compose build`
5. Запустите приложение с помощью команды `docker-compose up`.

# Установка и развертывание без использования docker
1. Клонируйте репозиторий
2. Установите PostgresQL
3. Инструкции по запуску [сервера](/server/README.md) и [клиента](/client/README.md) находятся в README файле каждого из модулей

## Лицензия
Этот проект лицензирован по лицензии MIT. Подробности смотрите в файле LICENSE.

---
  © [PROJECT_NAME] yyyy
