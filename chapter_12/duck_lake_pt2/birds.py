from abc import abstractmethod

from chapter_12.duck_lake_pt2.ducks import Quackable, Observable, Observer


class Goose:
    def honk(self) -> None:
        print('''Honk''')


class GooseAdapter(Quackable):
    def __init__(self, goose: Goose):
        super().__init__()
        self.goose = goose
        self.observable = Observable(self)

    def quack(self) -> None:
        self.goose.honk()
        self.notify_observers()

    def register_observer(self, observer: Observer):
        self.observable.register_observer(observer)

    def notify_observers(self):
        self.observable.notify_observers()


class AbstractGooseFactory:
    @abstractmethod
    def create_goose(self):
        ...


class GooseAdaptedFactory(AbstractGooseFactory):
    def __init__(self):
        self.adapter = GooseAdapter

    def create_goose(self) -> Quackable:
        return self.adapter(Goose())
