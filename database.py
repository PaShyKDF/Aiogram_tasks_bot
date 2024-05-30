import os

import psycopg2
from psycopg2.errors import UniqueViolation
from dotenv import load_dotenv


load_dotenv()


class BotDB:
    def __init__(self):
        self.conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DB'),
            port=os.getenv('DB_PORT'),
        )
        self.cursor = self.conn.cursor()

    def all_tasks(self):
        """Получаем все задачи из базы"""
        self.cursor.execute("SELECT * FROM tasks;")
        return self.cursor.fetchall()

    def create_task(self, text):
        """Добавляем задачу в базу"""
        try:
            self.cursor.execute(
                "INSERT INTO tasks (task) VALUES (%s)", (text,)
            )
            return self.conn.commit()
        except UniqueViolation:
            self.conn.rollback()
            return None

    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()


if __name__ == '__main__':
    bot = BotDB()
    # bot.create_task('something')
    print(bot.all_tasks())
