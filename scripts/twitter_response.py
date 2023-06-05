import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


class TwitterResponseMethods(ABC):
    
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


@dataclass
class TwitterResponseAPI(TwitterResponseMethods): 
    twitterUser: str = field(default=None)
    _twitterUser: str = field(default=None, repr=False)
    weatherRequest: bool = field(default=False)
    cryptoRequest: bool = field(default=False)
    stockRequest: bool  = field(default=False)

    def __post_init__(self):
        if self.weatherRequest is False and self.cryptoRequest is False and self.stockRequest is False:
            print("No question asked yet!")

    def connectToAccount(self):
        pass

    @property
    def reply_to_user(self) -> str:
        self._twitterUser = self.twitterUser

        return "Hello, {} ask me any question about stock, crypto prices and even weather in your selected region!".format(self._twitterUser)

    def say_hello(self) -> None:
        return self.reply_to_user

    def get_weather(self) -> None:
        pass

    def get_crypto(self) -> None:
        pass

    def get_stock(self) -> None:
        pass
