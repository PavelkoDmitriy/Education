from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = "1997480438:AAFQS6rmtpVlmSUDiDcIEq-ghbYQgofoQ1A"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=['start'])
async def start(message):
    #print('Привет! Я бот помогающий твоему здоровью.' )
    await message.answer('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler()
async def all_messages(messege):
    #print( 'Введите команду /start, чтобы начать общение.')
    await messege.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)