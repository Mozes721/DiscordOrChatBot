from configparser import ConfigParser 
from dataclasses import dataclass


file = 'config.ini'
config = ConfigParser()
config.read(file)

print(config.sections())

@dataclass(frozen=True)
class APIkeys:
    APIKey: str = config['twitter']['APIKey']
    APIKeySecret: str = config['twitter']['APIKeySecret']
    BearerToken: str = config['twitter']['BearerToken']
    AccessToken: str = config['twitter']['AccessToken']
    AccessTokenSecret: str = config['twitter']['AccessTokenSecret']
    weatherAPI: str = config['api']['weatherAPI']
    cryptoAPI: str = config['api']['cryptoAPI']
    weatherAPI: str = config['api']['stockAPI']
    
print(APIkeys.cryptoAPI)
