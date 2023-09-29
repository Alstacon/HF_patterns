from abc import ABC, abstractmethod


class Beverage(ABC):
    def __init__(self, size: str = 'MEDIUM') -> None:
        self.description = 'Unknown beverage'
        self._size = size

    def get_description(self) -> str:
        return self.description

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size: int):
        self._size = size

    @abstractmethod
    def cost(self) -> float:
        pass


class CondimentDecorator(Beverage, ABC):

    def __init__(self, beverage: Beverage):
        super().__init__()
        self.beverage = beverage
        self.size = self.beverage.size

    @abstractmethod
    def get_description(self) -> str:
        pass
