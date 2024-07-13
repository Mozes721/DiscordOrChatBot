# from config.abstract_methods  import APIMethods

class BotService:
    def __init__(self, api_requests):
        self.api_requests = api_requests

    @staticmethod
    def say_hello() -> str:
        return "Hello from BotService!"

    def get_crypto(self, crypto):
        return self.api_requests.get_crypto_data(crypto)

    def get_stock(self, ticker):
        return self.api_requests.get_stock_data(ticker)

    def get_weather(self, location):
        return self.api_requests.get_weather_data(location)
