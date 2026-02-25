# Проект API Yatube

## Описание
Проект **API Yatube** — это REST API для социальной сети Yatube. В проекте реализована полноценная система для взаимодействия с постами, комментариями, сообществами и подписками пользователей. Аутентификация построена на базе JWT-токенов (с использованием библиотеки Djoser).
Неавторизованные пользователи могут читать посты и комментарии, а авторизованные получают права на создание контента, подписки на других авторов и управление своими публикациями.

## Стек технологий
* Python 3
* Django
* Django REST Framework (DRF)
* Djoser / SimpleJWT
* SQLite

## Установка и запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/Zhumarradriga/api-final-yatube-ad.git
```
2. Перейдите в папку с проектом и создайте виртуальное окружение:

```bash
cd api-final-yatube-ad
python -m venv venv
source venv/bin/activate
```
3. Установите зависимости:
```bash
pip install -r requirements.txt
```
4. Выполните миграции:
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Запустите сервер разработки:
```bash
python manage.py runserver
```
##  Примеры запросов к API

**Получение JWT-токена**

* ```POST /api/v1/jwt/create/```

    Тело (JSON):
    ```JSON
    {
        "username": "test_user",
        "password": "test_password"
    }
    ```
**Получение списка постов**

* ```GET /api/v1/posts//```(Доступно всем пользователям)

    Тело (JSON):
    ```JSON
    {
        "username": "test_user",
        "password": "test_password"
    }
    ```
**Подписка на пользователя**

* ```POST /api/v1/follow/```
(Доступно только авторизованным)

    Заголовок: Authorization: Bearer <ваш_токен>
    Тело (JSON):
    ```JSON
    {
        "following": "username_автора"
    }
    ```