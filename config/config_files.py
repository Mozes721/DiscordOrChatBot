from configparser import ConfigParser 
from dataclasses import dataclass


file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())

@dataclass(frozen=True)
class APIkeys:
    weatherAPI: str = config['api']['weatherAPI']
    cryptoAPI: str = config['api']['cryptoAPI']
    weatherAPI: str = config['api']['stockAPI']


print(APIkeys.cryptoAPI)
