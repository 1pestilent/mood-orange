## Установка

1. git clone `https://github.com/1pestilent/mood-orange.git`

2. Создание виртуальной среды   \
2.1 `python3 -m venv venv`  \
2.2 Активация виртуальной среды `source .venv/bin/activate`

3. Установка пакетов `pip install -r requirements.txt`

4. Создание .env, пример заполнения:
```
DB_NAME = 'orange_db'
DB_USER = 'root'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'
DB_PORT = '5432'
PG_USER = 'root@root.com'
PG_PASSWORD = 'root'
PG_PORT = '8080'
```
5. Запуск БД через `docker compose up`
6. Создание структуры БД `db_struct.py`
7. Запуск приложения `app.py`
