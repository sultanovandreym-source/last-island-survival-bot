from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню
def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📊 Полезные таблицы", callback_data="tables"),
        InlineKeyboardButton("🏠 Базы и Фишки", callback_data="bases"),
        InlineKeyboardButton("🌟 Таланты", callback_data="talents"),
        InlineKeyboardButton("🏢 База операции", callback_data="operation"),
        InlineKeyboardButton("🖥 Калькулятор LIOS", url="https://sultanovandreym-source.github.io/lis-raid-calc/"),
        InlineKeyboardButton("💎 Донат LIOS", url="https://store.herogame.com/lios")
    )
    return kb

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🏝 Добро пожаловать в гайд по Last Island of Survival!\n"
        "Выбери раздел ниже ⬇️",
        reply_markup=main_menu()
    )

# Обработка внутренних разделов
@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data

    if data == "tables":
        await bot.send_message(callback_query.from_user.id,
            "📊 **Полезные таблицы**:\n"
            "- Крафт предметов\n"
            "- Ресурсы и их локации\n"
            "- Оружие и броня"
        )
    elif data == "bases":
        await bot.send_message(callback_query.from_user.id,
            "🏠 **Базы и Фишки**:\n"
            "- Лучшие места для постройки\n"
            "- Защита от рейдов\n"
            "- Полезные трюки и хитрости"
        )
    elif data == "talents":
        await bot.send_message(callback_query.from_user.id,
            "🌟 **Таланты**:\n"
            "- Лучшие навыки для PvP\n"
            "- Эффективное развитие персонажа\n"
            "- Комбинации для рейдов"
        )
    elif data == "operation":
        await bot.send_message(callback_query.from_user.id,
            "🏢 **База операции**:\n"
            "- Организация базы для рейдов\n"
            "- Тактика хранения ресурсов\n"
            "- Оптимизация защиты и патрулей"
        )

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp)
