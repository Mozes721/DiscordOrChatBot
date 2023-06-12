from abc import ABC, abstractmethod


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