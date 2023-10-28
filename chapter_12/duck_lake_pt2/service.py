from chapter_12.duck_lake_pt2.ducks import Quackable
from chapter_12.duck_lake_pt2.observers import Observer, Observable


class QuackCounter(Quackable):
    quack_counter = 0

    def __init__(self, duck: Quackable):
        self.duck = duck
        self.observable = Observable(self.duck)

    def quack(self) -> None:
        self.duck.quack()
        self.notify_observers()
        QuackCounter.quack_counter += 1

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()

    @classmethod
    def get_quacks(cls) -> int:
        return QuackCounter.quack_counter
