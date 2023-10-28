from abc import abstractmethod

from chapter_12.duck_lake_pt2.observers import QuackObservable, Observer, Observable, FlockObservable


class Quackable(QuackObservable):

    @abstractmethod
    def quack(self) -> None:
        ...

    def __str__(self) -> str:
        return self.__class__.__name__


class MallardDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable = Observable(self)

    def quack(self) -> None:
        print('''Quack''')

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RedheadDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable = Observable(self)

    def quack(self) -> None:
        print('''Quack''')

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class DuckCall(Quackable):
    def __init__(self):
        super().__init__()
        self.observable = Observable(self)

    def quack(self) -> None:
        print('''Kwak''')

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class RubberDuck(Quackable):
    def __init__(self):
        super().__init__()
        self.observable = Observable(self)

    def quack(self) -> None:
        print('''Squeak''')

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class Flock(Quackable):
    def __init__(self):
        self.quackers = []
        self.observable = FlockObservable(self)

    def add(self, quacker: Quackable):
        self.quackers.append(quacker)

    def quack(self):
        for quacker in self.quackers:
            quacker.quack()

    def register_observer(self, observer: Observer):
        for bird in self.quackers:
            bird.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()
