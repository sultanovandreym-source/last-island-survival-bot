from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню — кнопки под стартом
def main_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("📊 Полезные таблицы", callback_data="tables"),
        InlineKeyboardButton("🏠 Базы и Фишки", callback_data="bases"),
        InlineKeyboardButton("🌟 Таланты", callback_data="talents"),
        InlineKeyboardButton("🏢 База операции", callback_data="operation"),
        InlineKeyboardButton("🖥 Калькулятор LIOS", callback_data="calculator"),
        InlineKeyboardButton("💎 Донат LIOS", callback_data="donate")
    )
    return kb

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🏝 Добро пожаловать в гайд по Last Island of Survival!\nВыбери раздел ниже ⬇️",
        reply_markup=main_menu()
    )

# Обработка нажатий кнопок
@dp.callback_query_handler(lambda c: True)
async def process_callback(callback_query: types.CallbackQuery):
    data = callback_query.data

    # Внутренние разделы
    if data == "tables":
        await callback_query.message.edit_text(
            "📊 **Полезные таблицы**:\n"
            "- Крафт предметов\n"
            "- Ресурсы\n"
            "- Оружие и броня",
            reply_markup=main_menu()
        )
    elif data == "bases":
        await callback_query.message.edit_text(
            "🏠 **Базы и Фишки**:\n"
            "- Лучшие места для постройки\n"
            "- Защита от рейдов\n"
            "- Полезные трюки",
            reply_markup=main_menu()
        )
    elif data == "talents":
        await callback_query.message.edit_text(
            "🌟 **Таланты**:\n"
            "- Лучшие навыки для PvP\n"
            "- Комбо для рейдов",
            reply_markup=main_menu()
        )
    elif data == "operation":
        await callback_query.message.edit_text(
            "🏢 **База операции**:\n"
            "- Организация базы для рейдов\n"
            "- Оптимизация защиты",
            reply_markup=main_menu()
        )

    # Калькулятор LIOS через Web App
    elif data == "calculator":
        # Сначала сообщение с инструкцией
        await callback_query.message.answer(
            "Нажмите кнопку ниже, чтобы открыть калькулятор LIOS:"
        )
        # Кнопка под сообщением с Web App
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton(
                "Открыть калькулятор",
                web_app=WebAppInfo(url="https://sultanovandreym-source.github.io/lis-raid-calc/")
            )
        )
        await callback_query.message.answer("👇", reply_markup=kb)

    # Донат LIOS (ссылка открывается через стандартную кнопку)
    elif data == "donate":
        await callback_query.message.answer(
            "💎 Нажмите кнопку ниже для доната:"
        )
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton(
                "Перейти в Донат LIOS",
                url="https://store.herogame.com/lios"
            )
        )
        await callback_query.message.answer("👇", reply_markup=kb)

# Запуск бота
if __name__ == "__main__":
    executor.start_polling(dp)
