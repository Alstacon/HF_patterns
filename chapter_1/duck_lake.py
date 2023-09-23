from abc import ABC, abstractmethod
from typing import Protocol


class QuackBehavior(Protocol):
    @abstractmethod
    def quack(self):
        ...


class FlyBehavior(Protocol):
    @abstractmethod
    def fly(self):
        ...


class FlyWithWings(FlyBehavior):
    def fly(self) -> None:
        print('''I'm flying!''')


class FlyNoWay(FlyBehavior):
    def fly(self) -> None:
        print('''I can't fly''')


class FlyRocketPowered(FlyBehavior):
    def fly(self) -> None:
        print('''I'm flying with a rocket!''')


class Quack(QuackBehavior):
    def quack(self) -> None:
        print('''Quack''')


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print('''<< Silence >>''')


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print('''Squeak''')


class Duck(ABC):
    _fly_behavior: FlyBehavior
    _quack_behavior: QuackBehavior

    @property
    def quack_behavior(self) -> QuackBehavior:
        return self._quack_behavior

    @quack_behavior.setter
    def quack_behavior(self, quack_behavior: QuackBehavior) -> None:
        self._quack_behavior = quack_behavior

    @property
    def fly_behavior(self) -> FlyBehavior:
        return self._fly_behavior

    @fly_behavior.setter
    def fly_behavior(self, fly_behavior: FlyBehavior) -> None:
        self._fly_behavior = fly_behavior

    def perform_fly(self):
        return self.fly_behavior.fly()

    def perform_quack(self):
        return self.quack_behavior.quack()

    def display(self):
        ...

    def swim(self) -> None:
        print('''All ducks float, even decoys!''')


class MallardDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print('''I'm a real Mallard duck''')


class ModelDuck(Duck):
    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self) -> None:
        print('''I'm a Model duck''')


def mini_duck_simulator():
    mallard_duck = MallardDuck()
    mallard_duck.perform_quack()
    mallard_duck.perform_fly()

    model_duck = ModelDuck()
    model_duck.perform_fly()
    model_duck.fly_behavior = FlyRocketPowered()
    model_duck.perform_fly()


if __name__ == '__main__':
    mini_duck_simulator()
