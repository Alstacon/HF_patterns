from abc import ABC, abstractmethod


class Observer(ABC):
    def update(self, duck: 'QuackObservable') -> None:
        ...


class QuackObservable(ABC):
    @abstractmethod
    def register_observer(self, observer: Observer):
        ...

    @abstractmethod
    def notify_observers(self):
        ...


class Observable(QuackObservable):
    def __init__(self, duck: QuackObservable):
        self.observers = []
        self.duck = duck

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.duck)


class FlockObservable(QuackObservable):
    def __init__(self, flock: QuackObservable):
        self.observers = []
        self.flock = flock

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.flock)


class Quackologist(Observer):
    def update(self, duck: 'QuackObservable') -> None:
        print(f'''Quackoligist: {duck} just quacked''')
