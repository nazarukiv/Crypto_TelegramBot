# price_keyboards.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def create_crypto_keyboard(crypto_data):
    keyboard = InlineKeyboardMarkup()

    for crypto in crypto_data:
        crypto_name = crypto['name']
        button_text = f"{crypto_name} - ${crypto['current_price']:,.2f}"

        keyboard.add(InlineKeyboardButton(text=button_text, callback_data=f"show_crypto_{crypto['id']}"))

    return keyboard
