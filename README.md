# Локальный запуск
1) Клонировать репозиторий
   ```
   git clone https://github.com/fzdaze1/django_currency.git
   ```
2) Создать и активировать виртуальное окружение
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3) Установить зависимости
   ```
   pip install -r requirements.txt
   ```
4) Создать .env файл в корневой директории проекта. Содержание в примере .env.example
5) Перейти в директорию проекта
   ```
   cd currency_project
   ```
6) Выполнить миграции
   ```
   python manage.py migrate
   ```
7) Запустить сервер разработки
   ```
   python manage.py runserver
   ```
