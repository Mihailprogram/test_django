# Описание 
С помощью данного проекта пользователи могут хранить свои воспоминания о посещаемых местах.
Заходя на  сайт пользователь может авторизоваться через VK , на главной странице пользователь будет видеть свою фотографию, имя и фамилию взятую из профиля VK. Пользователь может добавить свое воспоминания , для этого нужно нажать на кнопку и вы попадете на страницу с формой на которой будет карта где нужно будет поставить метку и написать к ней название воспоминания и комментарий. После этого на главной странице отобразиться метка на карте и ваш комментарий и название воспоминания.
# Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Mihailprogram/test_django.git
```
```
cd places_remember
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```