from aiogram import Bot, Dispatcher, executor, types
import os

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🔰 Новичку", "🔨 Крафт")
    kb.add("⚔ PvP", "🏠 База")

    await message.answer(
        "🏝 Добро пожаловать в гайд по Last Island of Survival!",
        reply_markup=kb
    )

@dp.message_handler(text="🔰 Новичку")
async def newbie(message: types.Message):
    await message.answer(
        "🔰 Советы новичкам:\n"
        "1. Сразу фармь дерево и камень\n"
        "2. Не стройся на пляже\n"
        "3. Прячь лут в сундуках"
    )

executor.start_polling(dp)
