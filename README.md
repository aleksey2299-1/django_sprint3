# Простенький проект Blogicum
***
## Функционал:
- Создание и редактирование через панель администратора
- Посмотреть опубликованные посты
- Осортировать по категории

***
## Как начать?

Скопировать код:
````bash
git clone git@github.com:aleksey2299-1/django_sprint3.git
````

Создать виртуальное окружение и установить зависимости:
````bash
cd django_sprint3                    # переходим в папку django_sprint3
python -m venv venv                  # создаем виртуальное окружение
pip install --upgrade pip            # обновляем установщик пакетов pip
pip install -r requirements.txt      # устанавливаем необходимые для работы проекта зависимости
````

Перейти в папку **blogicum** и вы полнить первоначальные действия:
````bash
cd blogicum                         # переходим в папку blogicum
python manage.py migrate            # выполняем миграции
python manage.py createsuperuser    # создаем суперюзера
python manage.py loaddata db.json   # загружаем первоначальные данные
````
Переходим по адресу `localhost:8000/` для просмотра главной страницы.

Переходим по адресу `localhost:8000/category/<slug>/` для просмотра постов данной категории.

Переходим по адресу `localhost:8000/posts/<id>/` для просмотра конкретного поста.

> **Примечание.** Настроена пагинация, поэтому на всех страницах со списком будут отображаться только последние 5 постов.

Создание и редактирование постов происходит в админ зоне `localhost:8000/admin/`, логин и пароль - те что вы задавали при команде `python manage.py createsuperuser`
