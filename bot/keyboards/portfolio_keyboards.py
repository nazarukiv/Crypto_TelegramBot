from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_portfolio_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=1)
    portfolio_button = InlineKeyboardButton("Show Portfolio", callback_data='show_portfolio')
    add_holdings_button = InlineKeyboardButton("Add Holdings", callback_data='add_holdings')
    top_cryptos_button = InlineKeyboardButton("List Top 20 Cryptos", callback_data='list_top_cryptos')
    keyboard.add(portfolio_button, add_holdings_button, top_cryptos_button)
    return keyboard

def get_main_keyboard():
    keyboard = InlineKeyboardMarkup(row_width=2)

    portfolio_button = InlineKeyboardButton("Show Portfolio", callback_data='show_portfolio')
    add_holdings_button = InlineKeyboardButton("Add Holdings", callback_data='add_holdings')
    top_cryptos_button = InlineKeyboardButton("List Top 20 Cryptos", callback_data='list_top_cryptos')
    back_button = InlineKeyboardButton("Back", callback_data='back_to_main')

    keyboard.add(portfolio_button, add_holdings_button)
    keyboard.add(top_cryptos_button)
    keyboard.add(back_button)

    return keyboard