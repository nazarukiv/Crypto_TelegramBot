from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.utils.exceptions import MessageToDeleteNotFound, MessageCantBeDeleted

from bot.handlers.portfolio_handlers import show_portfolio, list_top_cryptos
from bot.keyboards.education_keyboards import keyboard_education, keyboard_education_tech_analysis, keyboard_base
from bot.keyboards.portfolio_keyboards import get_main_keyboard


async def start_handler(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.first_name}! Welcome to the CryptoBot.\n"
        "Available commands:\n"
        "/start - Start interacting with the bot\n"
        "/help - Get assistance and instructions for using the bot\n"
        "/clear - Clear the chat"
        "/show_crypto - View details of top cryptocurrencies\n"
        "/news - Get the latest cryptocurrency news\n"
        "/new_icos - Discover new ICOs from Binance and ByBit\n"
        "/education - Learn about cryptocurrencies and blockchain\n"
        "/base_portfolio - Access portfolio management options"

    )

async def help_handler(message: types.Message):
    await message.answer(
        "Available commands:\n"
        "/start - Start interacting with the bot\n"
        "/help - Get assistance and instructions for using the bot\n"
        "/clear - Clear the chat"
        "/show_crypto - View details of top cryptocurrencies\n"
        "/news - Get the latest cryptocurrency news\n"
        "/new_icos - Discover new ICOs from Binance and ByBit\n"
        "/education - Learn about cryptocurrencies and blockchain"
        "/base_portfolio - Access portfolio management options"
    )


async def education_handler(message: types.Message):
    await message.answer("Please choose a category:", reply_markup=keyboard_base)

async def handle_education_category(callback_query: types.CallbackQuery):
    category = callback_query.data

    if category == "education_general":
        await callback_query.message.edit_text("General Education Resources:", reply_markup=keyboard_education)
    elif category == "education_tech_analysis":
        await callback_query.message.edit_text("Technical Analysis Resources:", reply_markup=keyboard_education_tech_analysis)
    elif category == "back_to_base":
        await callback_query.message.edit_text("Please choose a category:", reply_markup=keyboard_base)

async def tech_analysis(message: types.Message):
    await message.answer("Choose a course:", reply_markup=keyboard_education_tech_analysis)


async def base_portfolio_handler(message: types.Message):
    await message.answer("Choose an option:", reply_markup=get_main_keyboard())

    async def handle_callback_query_portfolio(callback_query: types.CallbackQuery):
        if callback_query.data == 'show_portfolio':
            await show_portfolio(callback_query.message)
        elif callback_query.data == 'add_holdings':
            await callback_query.message.reply("Send /add_holdings <crypto_id> <amount> to add holdings.")
        elif callback_query.data == 'list_top_cryptos':
            await list_top_cryptos(callback_query.message)
        elif callback_query.data == 'back_to_main':
            await callback_query.message.edit_text("Choose an option:", reply_markup=get_main_keyboard())


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(education_handler, commands=["education"])
    dp.register_callback_query_handler(handle_education_category, lambda c: c.data in ["education_general", "education_tech_analysis", "back_to_base"])
    dp.register_message_handler(start_handler, commands=["start"])
    dp.register_message_handler(help_handler, commands=["help"])
    dp.register_message_handler(base_portfolio_handler, commands=["base_portfolio"])

