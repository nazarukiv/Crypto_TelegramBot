import requests
from aiogram import types
from aiogram.dispatcher import Dispatcher

async def news_handler(message: types.Message):
    try:
        url = 'https://api.coingecko.com/api/v3/news'
        params = {
            'lang': 'en',
            'page': 1,
            'per_page': 10
        }
        headers = {
            'Accept': 'application/json'
        }

        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()

        news_articles = response.json()['data']

        if news_articles:
            news_response = "Here are the latest crypto news articles:\n\n"
            for article in news_articles:
                title = article['title']
                article_url = article['url']
                news_response += f"📰 [{title}]({article_url})\n\n"
        else:
            news_response = "Sorry, I couldn't find any news articles at the moment."

        await message.answer(news_response, parse_mode='Markdown')

    except requests.RequestException as e:
        print(f"Error fetching news: {e}")
        await message.answer("Sorry, I couldn't fetch the news at the moment.")

def register_handlers_news(dp: Dispatcher):
    dp.register_message_handler(news_handler, commands=["news"])