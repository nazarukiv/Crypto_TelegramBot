from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message, CallbackQuery
from bot.services.price_service import get_top_crypto_prices
from bot.keyboards.price_keyboards import create_crypto_keyboard

async def start(message: Message):
    await message.reply("Welcome! Here are the top 15 cryptocurrencies by market cap. Click on any to see details:", reply_markup=create_crypto_keyboard(get_top_crypto_prices()))

async def show_crypto_details(callback_query: CallbackQuery):
    crypto_id = callback_query.data.replace("show_crypto_", "")
    crypto_data = next((crypto for crypto in get_top_crypto_prices() if crypto['id'] == crypto_id), None)

    if crypto_data:
        details_text = (
            f"*{crypto_data['name']} ({crypto_data['symbol'].upper()})*\n\n"
            f"Price: ${crypto_data['current_price']:,.2f}\n"
            f"Market Cap: ${crypto_data['market_cap']:,.0f}\n"
            f"24h Change: {crypto_data['price_change_percentage_24h_in_currency']:.2f}%\n\n"
            f"Click [here]({crypto_data['image']}) for more details."
        )

        await callback_query.message.edit_text(details_text, parse_mode='Markdown')
    else:
        await callback_query.message.edit_text("Crypto data not found.")

def register_handlers_price(dp: Dispatcher):
    dp.register_message_handler(start, commands=["show_crypto"])
    dp.register_callback_query_handler(show_crypto_details, lambda c: c.data.startswith('show_crypto_'))
