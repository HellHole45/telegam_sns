from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="5572287668:AAG730X7VL9KvvUbzTO-rpgYna9guMHeYWE")
dp = Dispatcher(bot)

number = '+79523520595'
op = '@feel9ngs'

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
menu_1 = KeyboardButton(text='Каталог', сallback_data="menu_1")
menu_2 = KeyboardButton(text='Активные доставки', callback_data="menu_2")
menu_3 = KeyboardButton(text='Тех. Поддержка', callback_data="menu_3")
keyboard.add(menu_1, menu_2, menu_3)

keyboard2 = InlineKeyboardMarkup()
menu_1 = InlineKeyboardButton(text='Corvus', callback_data="menu_1")
menu_2 = InlineKeyboardButton(text='MAD', callback_data="menu_2")
menu_3 = InlineKeyboardButton(text='Nictech', callback_data="menu_3")
keyboard2.add(menu_1, menu_2, menu_3)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Привет! Это бот продажи снюса.\nПочему именно мы? У нас полностью автоматический магазин, после оплаты вам сразу отпишет оператор, после чего вы сможете успешно оформить доставку.', reply_markup=keyboard)

@dp.callback_query_handler(text_contains='menu_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("menu_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text(f'Corvus Fenix\n\nЦена: 250 рублей\n\nОплатить товар можно на номер {number} (QIWI)\nПосле оплаты вам сразу отпишет оператор', reply_markup=keyboard2)
        if code == 2:
            await call.message.edit_text(f'MAD fatality\n\nЦена: 250 рублей\n\nОплатить товар можно на номер {number} (QIWI)\nПосле оплаты вам сразу отпишет оператор', reply_markup=keyboard2)
        if code == 3:
            await call.message.edit_text(f'Nictech Strong\n\nЦена: 250 рублей\n\nОплатить товар можно на номер {number} (QIWI)\nПосле оплаты вам сразу отпишет оператор', reply_markup=keyboard2)

@dp.message_handler(content_types=["text"])
async def do_something(message: types.Message):
    txt = message.text
    if txt == 'Каталог':
        await bot.send_message(message.from_user.id, 'Выберите интересный вам товар', reply_markup=keyboard2)
    elif txt == 'Активные доставки':
        await bot.send_message(message.from_user.id, 'Ваши активные доставки: \n*Тут пока пусто :<*', reply_markup=keyboard)
    elif txt == 'Тех. Поддержка':
        await bot.send_message(message.from_user.id, f'Если возникли какие-либо ошибки, напишите нашему оператору: {op}', reply_markup=keyboard)
    return


executor.start_polling(dp)

