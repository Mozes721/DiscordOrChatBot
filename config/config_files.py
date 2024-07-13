import os
from dotenv import load_dotenv, find_dotenv
from dataclasses import dataclass
from distutils.util import strtobool

load_dotenv(find_dotenv())


@dataclass(frozen=True)
class APIkeys:
    deployment: bool = bool(strtobool(os.getenv('DEPLOYMENT')))
    weatherAPI: str = os.getenv('WEATHER_API')
    cryptoAPI: str = os.getenv('CRYPT_API')
    stockAPI: str = os.getenv('STOCK_API')
    discordToken: str = os.getenv('DISCORD_TOKEN') 
