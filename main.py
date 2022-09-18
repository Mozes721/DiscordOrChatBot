from abc import ABC, abstractmethod
import tweepy
import time

class TwitterMethods(ABC):
    
    @abstractmethod
    def say_hello(self) -> None:
        pass

    @abstractmethod
    def get_weather(self) -> None:
        pass
    @abstractmethod
    def get_crypto(self) -> None:
        pass
    @abstractmethod
    def get_stock(self) -> None:
        pass

 
auth = tweepy.OAuth1UserHandler('y0bdWj5JjGUvFqjP9kaYJ8biF', '0HzXorh6ycHXVMSf2TQGKTwAAGR26QCVj6NWxdDbu7jstBKyC7')

auth.set_access_token('1552932201402191872-uOJrC5ov7eKcaxoUYjvGwcapVl76zF', 'txDDfjApo8OaAThTqT1DbL6VKAIH9CvJEaNBw181y4Lml')

api = tweepy.API(auth, wait_on_rate_limit=True)

user = api.get_profile_banner()


def main():
    pass

if __name__ == '__main__':
    main()