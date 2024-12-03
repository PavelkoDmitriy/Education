from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


api = ""
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


class UserState(StatesGroup):
    age = State()
    growth= State()
    weight  = State()


@dp.message_handler(text=["Calories"])
async def set_age(messege):
    await messege.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    
    calories = (10 * weight) + (6.25 * growth) - (5 * age) - 161
    await message.answer(f"Ваша норма калоррий: {int(calories)}")

    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
