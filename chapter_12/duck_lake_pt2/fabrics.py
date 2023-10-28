from abc import abstractmethod, ABC

from ducks import MallardDuck, RubberDuck, RedheadDuck, DuckCall, Quackable
from service import QuackCounter


class AbstractDuckFactory(ABC):

    @abstractmethod
    def create_mallard_duck(self):
        ...

    @abstractmethod
    def create_redhead_duck(self):
        ...

    @abstractmethod
    def create_rubber_duck(self):
        ...

    @abstractmethod
    def create_duck_call(self):
        ...


class DuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()

    def create_rubber_duck(self):
        return RubberDuck()

    def create_duck_call(self):
        return DuckCall()


class CountingDuckFactory(AbstractDuckFactory):
    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_adapted_bird(self, adapter_bird: Quackable):
        return QuackCounter(adapter_bird)