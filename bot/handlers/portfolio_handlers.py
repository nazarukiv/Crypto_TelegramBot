import aiohttp
from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ParseMode

user_portfolios = {}


async def get_top_cryptos():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/coins/markets',
                               params={'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 20,
                                       'page': 1}) as response:
            data = await response.json()
            return [(coin['id'], coin['name']) for coin in data]


async def list_top_cryptos(message: types.Message):
    cryptos = await get_top_cryptos()

    if not cryptos:
        await message.reply("Unable to fetch top cryptocurrencies at the moment.")
        return

    response_text = "Top 20 Cryptocurrencies:\n\n"
    for idx, (crypto_id, name) in enumerate(cryptos, start=1):
        response_text += f"{idx}. {name} - ID: {crypto_id}\n"

    await message.reply(response_text, parse_mode=ParseMode.MARKDOWN)
async def get_crypto_price(crypto_id):
    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.coingecko.com/api/v3/simple/price', params={'ids': crypto_id, 'vs_currencies': 'usd'}) as response:
            data = await response.json()
            return data.get(crypto_id, {}).get('usd', 0)

async def show_portfolio(message: types.Message):
    user_id = message.from_user.id
    portfolio = user_portfolios.get(user_id, {})

    if not portfolio:
        await message.reply("You don't have any holdings in your portfolio.")
        return

    total_value = 0
    response_text = "Your Portfolio:\n\n"

    for crypto, amount in portfolio.items():
        price = await get_crypto_price(crypto)
        if price == 0:
            response_text += f"{crypto.capitalize()}: {amount} - Price data not available\n"
            continue
        value = price * amount
        total_value += value
        response_text += f"{crypto.capitalize()}: {amount} @ ${price:.2f} = ${value:.2f}\n"

    response_text += f"\nTotal Portfolio Value: ${total_value:.2f}"
    await message.reply(response_text, parse_mode=ParseMode.MARKDOWN)

async def add_holdings(message: types.Message):
    args = message.text.split()
    if len(args) != 3:
        await message.reply("Usage: /add_holdings <crypto_id> <amount>")
        return

    crypto_id, amount = args[1], float(args[2])
    user_id = message.from_user.id

    if user_id not in user_portfolios:
        user_portfolios[user_id] = {}

    if crypto_id in user_portfolios[user_id]:
        user_portfolios[user_id][crypto_id] += amount
    else:
        user_portfolios[user_id][crypto_id] = amount

    await message.reply(f"Added {amount} {crypto_id} to your portfolio.")

async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == 'show_portfolio':
        await show_portfolio(callback_query.message)
    elif callback_query.data == 'add_holdings':
        await callback_query.message.reply("Send /add_holdings <crypto_id> <amount> to add holdings.")

def register_handlers_portfolio(dp: Dispatcher):
    dp.register_message_handler(show_portfolio, commands=['portfolio'])
    dp.register_message_handler(add_holdings, commands=['add_holdings'])
    dp.register_message_handler(list_top_cryptos, commands=['list_top_cryptos'])
    dp.register_callback_query_handler(handle_callback_query)
