from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button_buy = KeyboardButton(text='Купить')
kb.add(button1, button2)


kb1 = InlineKeyboardMarkup()
button3 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button4 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
kb1.add(button3, button4)

kb2 = InlineKeyboardMarkup()
button5 = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button6 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button7 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button8 = InlineKeyboardButton(text='Product41', callback_data='product_buying')
kb2.add(button5, button6, button7, button8)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    products = [
        {"number": 1, "description": "описание 1", "price": 100, "image": "https://yandex-images.clstorage.net/KJl5O2200/5340fezQXd_/ue9LZoNX6MHt6T7LbjlVz66kAV4kmY5qBlJYueRmDvsolvIwX002UzkswXc8Nt6cbQijnzGLRCHy9qyjM8eib-38X_RUxijAqPv8WGi6Ucr9o1GbdB_Pa9ARWGIqr1Mm8xy--tbRPZU5OxSgOzCMGDSS5wGuVEa_cWBg6-Ta_bG6rshuS8giye209YOjO5VAuKJLlnlSUe7FjgIoZ26XJPZf8fFT3zBRczhZp_gljB23WXzKL5cP8DEhKmosV7qz9-EAasPBYsWqeXHKKf5fRHWtyNUyUF1uy83ALu9j2Cu1HjfzVBs7Xj31EOC2ooJb9h41BmdWRDGyriHq4pAxs7IuwqCFAKsOpL96yG52Hw125khfe91TaArIQe5r5hemstJ28ZwQNB_wO5GgPe2L2f9fc88m1E_-MWtuIuQT9Tk05EFhzklhgWOxeMJgPh0E_GJBmLpXmSPDSA0taCoZYnrVOjqdkDLXsHGfoj9nQFfwH3uD6h0A-DIrpeaiGfE_ui9I4UvJYQnicnSOpPgYBXBrghd0WVohysaC4GMrXWy1XP91W9C3nfDxVK18pYTQNpQzBiRahzx6LqKkqpz8cHCpi-7JD6vMLfSzC2c1lk-86kkQPl_frUcNRqbk5Z_v9xe7uZ9Zt155PFwqv6lNGXDYPQppFUU8euMpYO1fdrM9LAjpQ0fuzum2O8Iss18NdO0E3zNVU-oERAIpZysRY3jWtDrX0XuQeTIQpzenzVl6GHqIqBEB_XCjaK5k3ry-NGgAKwJIqsFivDPI53udgrMjgZA_nxrshEdMaKxsUi9-nzR7lZ07k7X72yN14ktUehw0CG6Wi7Y34yAsYtS3_jRkwe5PSuLEYXExzm_7Egi1agBQu1YbqseLTqCvbJ6q-t__M1xSMpcydJQlfufFVHdZek0uG8A_O-sg6Gqbsb7_6c0vTMFvzG12ckkmvNIB_63JW3VR3SnCiwKrYM"},
        {"number": 2, "description": "описание 2", "price": 200, "image": "https://sun9-29.userapi.com/impf/lJ9xaQSBNEpPKvu23EHGwigj1f9z8irFwtmkdw/2pfvzDssAFk.jpg?size=1920x768&quality=95&crop=0,28,1000,399&sign=037d2726c0a0416d96dab821581cc296&type=cover_group"},
        {"number": 3, "description": "описание 3", "price": 300, "image": "https://cdn1.ozone.ru/multimedia/1019411644.jpg"},
        {"number": 4, "description": "описание 4", "price": 400, "image": "https://detsadyar.ru/upload/iblock/d59/d596b5a0b9011c41f8c9b5cad70d7fe4.jpeg"},
    ]

    for product in products:
        product_text = f"Название: Product{product['number']} | Описание: {product['description']} | Цена: {product['price']}"
        await message.answer(product_text)
        await message.answer_photo(photo=product['image'])

    await message.answer("Выберите продукт для покупки:", reply_markup=kb2)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb1)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


class UserState(StatesGroup):
    age = State()
    growth= State()
    weight  = State()


@dp.callback_query_handler(text=['calories'])
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
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


@dp.message_handler()
async def start(message):
    await message.answer("Введите команду /start, чтобы начать общение")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
