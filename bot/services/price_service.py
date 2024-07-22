import requests

# CoinGecko API endpoint for top 15 cryptocurrencies (excluding stable coins, including USDT)
TOP_CRYPTO_URL = 'https://api.coingecko.com/api/v3/coins/markets'

def get_top_crypto_prices():
    try:
        params = {
            'vs_currency': 'usd',
            'ids': 'bitcoin,ethereum,binancecoin,solana,cardano,xrp,usd-coin,polkadot,avalanche,terra,chainlink,dogecoin,litecoin,wrapped-bitcoin,ethereum-classic,tether',
            'order': 'market_cap_desc',
            'per_page': 15,
            'page': 1,
            'sparkline': False,
            'price_change_percentage': '1h,24h,7d'
        }

        response = requests.get(TOP_CRYPTO_URL, params=params)
        response.raise_for_status()

        crypto_data = response.json()

        return crypto_data

    except requests.RequestException as e:
        print(f"Error fetching cryptocurrency data: {e}")
        return None
