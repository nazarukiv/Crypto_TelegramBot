import logging
from aiogram import Bot, Dispatcher, executor
from config import TELEGRAM_BOT_TOKEN
from handlers.base_handlers import register_handlers
from handlers.news_handlers import register_handlers_news
from handlers.price_handlers import register_handlers_price
from handlers.ico_handlers import register_handlers_ico
from handlers.portfolio_handlers import register_handlers_portfolio

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot)

register_handlers(dp)
register_handlers_news(dp)
register_handlers_price(dp)
register_handlers_ico(dp)
register_handlers_portfolio(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
