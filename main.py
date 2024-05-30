import os

import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

from database import BotDB


# Создание объектов бота и диспетчера
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
dp = Dispatcher()

BotDB = BotDB()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать! Я могу добавлять задачи через команду /add и "
        "возвращать их список через /tsk.\n\nПример добавления:"
        "\n'/add Ваш текст'")


# Обработчик команды /add
@dp.message(Command('add'))
async def add_task(message: types.Message):
    task = message.text.split('/add ')[1]
    if BotDB.create_task(task) is None:
        await message.answer('Задача уже была добавлена!')
    else:
        await message.answer('Задача успешно добавлена!')


# Обработчик команды /tsk
@dp.message(Command('tsk'))
async def show_tasks(message: types.Message):
    tasks = BotDB.all_tasks()
    tasks_list = '\n'.join(task[1] for task in tasks)
    await message.answer(f'Текущие задачи:\n{tasks_list}')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
