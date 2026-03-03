### Yatube API:

### Описание:

Yatube API - REST сервис для платформы для блогов. Yatube API предполагает возможность создать, отредактировать или удалить собственный пост, прокомментировать пост другого автора и подписаться на него.

API построен на Django и Django REST Framework.
Авторизация реализована через JSON Web Token (JWT).

### Стек технологий:

* Python
* Django
* Django REST Framework (DRF)
* Djoser
* SimpleJWT

### Автор:

Shmykova Anna


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api-final-yatube.git
```

```
cd api-final-yatube
```

* Если у вас windows

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов:

Получение списка публикаций. При указании параметров limit и offset выдача работает с пагинацией.

```
GET /api/v1/posts/
```
С пагинацией:

```
GET /api/v1/posts/?limit=5&offset=0
```

Создание публикации:
```
POST /api/v1/posts/
```
```
JSON
{
  "text": "Пост с группой",
  "group": 2
}
```
Получение конкретной публикации:
```
GET /api/v1/posts/1/
```

Больше примеров:
```
http://localhost:8000/redoc/
``` 
