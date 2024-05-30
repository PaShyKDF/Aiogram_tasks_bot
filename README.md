# Task Telegram Bot на Aiogram
Достаточно простой бот для хранения и отслеживания задач построенный на Python библиотеке Aiogram. Бот поддерживает несколько команд:
• /add - добавить задачу
• /tsk - получить все задачи

### Стек:
<img src="https://img.shields.io/badge/Python-3776ab?style=for-the-badge&logo=python&logoColor=yellow"/> <img src="https://img.shields.io/badge/Aiogram-1E90FF?style=for-the-badge&"/> <img src="https://img.shields.io/badge/PostgreSQL-50b0f0?style=for-the-badge&logo=postgresql&logoColor=white"/> <img src="https://img.shields.io/badge/github actions-4B0082?style=for-the-badge&logo=githubactions&logoColor=2088FF"/> <img src="https://img.shields.io/badge/docker-1d63ed?style=for-the-badge&logo=docker&logoColor=white"/>

# Инструкция по запуску проекта
### Чтобы запустить проект нужно установить на локальную машину docker. Все ниже перечисленные действия будут для ОС Ubuntu Linux.

1. Скачайте и установите curl — консольную утилиту, которая умеет скачивать файлы по команде пользователя:
```bash
sudo apt update
sudo apt install curl
```
2. С помощью утилиты curl скачайте скрипт для установки докера с официального сайта. Этот скрипт хорош тем, что сам определит и настроит вашу операционную систему.
```bash
curl -fSL https://get.docker.com -o get-docker.sh
```
Параметр -o get-docker.sh просит сохранить ответ сервера в файл get-docker.sh.
3. Запустите сохранённый скрипт с правами суперпользователя:
```bash
sudo sh ./get-docker.sh
```
4. Дополнительно к Docker установите утилиту Docker Compose:
```bash
sudo apt install docker-compose-plugin
```
Проверьте, что Docker работает:
```bash
sudo systemctl status docker
```
### После установки Docker и Docker-comose можно запускать проект:
1. В корневой директории создайте файл .env и укажите параметры для Базы Данных, PGAdmin и токен телеграм бота. Пример:
```
TELEGRAM_TOKEN=69391*****:AAE8OkE1d6mYFzhiacyiDHX***********
POSTGRES_USER=Имя пользователя
POSTGRES_PASSWORD=Пароль
POSTGRES_DB=Имя базы даннх
DB_HOST=Название контейнера с базой данных
DB_PORT=5432
PGADMIN_DEFAULT_EMAIL=Почту для входа в PGAdmin
PGADMIN_DEFAULT_PASSWORD=Пароль от PGAdmin
```
2. В корневой директории запустите docker-compose командой:
```bash
sudo docker compose up -d --build
```
3. Далее нужно создать в Базе Данный таблицу командой:
```bash
sudo docker compose exec tg_bot python migrations.py
```
4. Чтобы остановить бот:
```bash
sudo docker compose stop
```
### Инструкция по входу в PGAdmin:
1. Откройте в браузере ссылку:
```
http://127.0.0.1:5005
```
2. Введите почту и пароль, которую указывали в файле .env
3. Далее во вкладке сервер нужно добавить сервер:
Во вкладке соединение указать адрес сервера как имя контейнера БД и порт как 5432. Так указать пароль имя БД и имя пользователя из .env файла.