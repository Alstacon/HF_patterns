import random
from abc import ABC, abstractmethod

from chapter_1.duck_lake import Duck


class Turkey(ABC):
    @abstractmethod
    def gobble(self):
        ...

    @abstractmethod
    def fly(self):
        ...


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print('''Gobble gobble''')

    def fly(self) -> None:
        print('''I'm flying a short distance''')


class TurkeyAdapter:
    def __init__(self, turkey: Turkey):
        self.turkey = turkey

    def quack(self):
        self.turkey.gobble()

    def fly(self):
        for i in range(5):
            self.turkey.fly()


class DuckAdapter:
    def __init__(self, duck: Duck):
        self.duck = duck

    def gobble(self):
        self.duck.perform_quack()

    def fly(self):
        if random.randint(0, 5) == 0:
            self.duck.perform_fly()
