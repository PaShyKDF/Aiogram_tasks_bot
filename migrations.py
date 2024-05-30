import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


if __name__ == '__main__':
    try:
        connection = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD'),
            database=os.getenv('POSTGRES_DB'),
            port=os.getenv('DB_PORT'),
        )

        connection.autocommit = True

        cursor = connection.cursor()

        cursor.execute(
            '''CREATE TABLE "tasks" (
                "id" serial PRIMARY KEY,
                "task" TEXT CHECK (LENGTH(task) <= 1000) NOT NULL UNIQUE,
                UNIQUE("id","task"));'''
        )

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print('[INFO] PostgreSQL connection closed')
