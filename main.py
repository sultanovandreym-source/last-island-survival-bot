from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Главное меню (кнопки внизу)
def main_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    kb.add(
        KeyboardButton("📊 Полезные таблицы"),
        KeyboardButton("🏠 Базы и Фишки"),
        KeyboardButton("🌟 Таланты"),
        KeyboardButton("🏢 База операции"),
        KeyboardButton("🖥 Калькулятор LIOS"),
        KeyboardButton("💎 Донат LIOS")
    )
    return kb

# Кнопка «Главное меню» для разделов
def back_to_menu():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add(KeyboardButton("⬅️ Главное меню"))
    return kb

# Команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🏝 Добро пожаловать в гайд по Last Island of Survival!\nВыбери раздел ниже ⬇️",
        reply_markup=main_menu()
    )

# Обработка текстовых сообщений с меню
@dp.message_handler(lambda message: True)
async def menu_handler(message: types.Message):
    text = message.text

    if text == "⬅️ Главное меню":
        await message.answer(
            "🏝 Главное меню:",
            reply_markup=main_menu()
        )

    elif text == "📊 Полезные таблицы":
        await message.answer(
            "📊 **Полезные таблицы**:\n- Крафт предметов\n- Ресурсы\n- Оружие и броня",
            reply_markup=back_to_menu()
        )
    elif text == "🏠 Базы и Фишки":
        await message.answer(
            "🏠 **Базы и Фишки**:\n- Лучшие места для постройки\n- Защита от рейдов\n- Полезные трюки",
            reply_markup=back_to_menu()
        )
    elif text == "🌟 Таланты":
        await message.answer(
            "🌟 **Таланты**:\n- Лучшие навыки для PvP\n- Комбо для рейдов",
            reply_markup=back_to_menu()
        )
    elif text == "🏢 База операции":
        await message.answer(
            "🏢 **База операции**:\n- Организация базы для рейдов\n- Оптимизация защиты",
            reply_markup=back_to_menu()
        )
    elif text == "🖥 Калькулятор LIOS":
        # Сначала текст с инструкцией
        await message.answer("Нажмите кнопку ниже, чтобы открыть калькулятор LIOS:")
        # Кнопка Web App
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton(
                "Открыть калькулятор",
                web_app=WebAppInfo(url="https://sultanovandreym-source.github.io/lis-raid-calc/")
            )
        )
        await message.answer("👇", reply_markup=kb)
    elif text == "💎 Донат LIOS":
        await message.answer("💎 Нажмите кнопку ниже для доната:")
        kb = InlineKeyboardMarkup()
        kb.add(
            InlineKeyboardButton(
                "Перейти в Донат LIOS",
                url="https://store.herogame.com/lios"
            )
        )
        await message.answer("👇", reply_markup=kb)

if __name__ == "__main__":
    executor.start_polling(dp)
