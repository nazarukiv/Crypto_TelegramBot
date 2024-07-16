from aiogram import types
from aiogram.dispatcher import Dispatcher
from bot.keyboards.education_keyboards import keyboard_education, keyboard_education_tech_analysis
async def start_handler(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.first_name}! Welcome to the CryptoBot.\n"
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )

async def help_handler(message: types.Message):
    await message.answer(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )

async def education_handler(message: types.Message):
    await message.answer("Choose a course:", reply_markup=keyboard_education)

async def tech_analysis(message: types.Message):
    await message.answer("Choose a course:", reply_markup=keyboard_education_tech_analysis)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(tech_analysis, commands=["tech_analysis"])
    dp.register_message_handler(education_handler, commands=["education"])
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(help_handler, commands=["help"])
