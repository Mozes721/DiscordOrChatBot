from dataclasses import dataclass
from config.connection import connect
from api.requests import APIRequests
import time


@dataclass
class TwitterAPI:
    client: list
    client_id: str
    start_id: int
    response: str

    def __post_init__(self):
        print("Connection has been established..")
        print("%s this is a client", self.client)
        self.check_tweets()

    def check_tweets(self):
        while True:
            if self.response.data != None:
                for tweet in self.response:
                    try:
                        print(tweet.text)
                        self.client.create_tweet(in_reply_to_tweet_id=tweet.id, text='hello')
                        self.start_id = tweet.id
                    except Exception as error:
                        print(error)

            time.sleep(5)


if __name__ == '__main__':
    client, client_id, api = connect()
    start_id = 1
    api_requests = APIRequests()
    crypto_price = api_requests.get_crypto_data('bitcoin')
    #stock_price = api_requests.get_stock_data('AAPL')
    #weather_data = api_requests.get_weather_data('New York')
    print(crypto_price)

    # while True:
    #     response = client.get_users_mentions(client_id, since_id=start_id)
    #     TwitterAPI(client, client_id, start_id, response)
