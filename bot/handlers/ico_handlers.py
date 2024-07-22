import requests
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import Message


BINANCE_ICO_URL = 'https://api.binance.com/api/v3/asset-service/get-asset-detail'

def get_binance_new_listings():
    try:
        response = requests.get(BINANCE_ICO_URL)
        response.raise_for_status()
        ico_data = response.json()
        return ico_data

    except requests.RequestException as e:
        print(f"Error fetching Binance ICO data: {e}")
        return None


async def get_new_icos(message: Message):
    binance_icos = get_binance_new_listings()
    if binance_icos:
        ico_response = "New ICOs from Binance:\n\n"
        for ico in binance_icos:
            ico_name = ico['name']
            ico_response += f"🚀 {ico_name}\n"

        await message.answer(ico_response)
    else:
        await message.answer("Sorry, unable to fetch new ICOs at the moment.")

def register_handlers_ico(dp: Dispatcher):
    dp.register_message_handler(get_new_icos, commands=["new_icos"])
