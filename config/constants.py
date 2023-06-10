from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Constants:
    STOCK_URL: str = (
        "https://api.twelvedata.com/time_series?symbol={symbol}"
        "&interval=1day&outputsize=12&include_ohlc=true&apikey={api_key}"
    )
    WEATHER_URL: str = (
        "http://api.openweathermap.org/data/2.5/weather?appid={api_key}"
        "&id={location}"
    )
    CRYPTO_URL: str = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    CRYPTO_PARAMETERS: Dict[str, str] = field(default_factory=lambda: {'slug': '', 'convert': 'USD'})
    CRYPTO_HEADERS: Dict[str, str] = field(default_factory=lambda: {'Accepts': 'application/json', 'X-CMC_PRO_API_KEY': ''})
