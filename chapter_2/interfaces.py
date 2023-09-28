from abc import ABC, abstractmethod
from typing import Protocol


class Observer(Protocol):
    @abstractmethod
    def update(self, ):
        ...


class Subject(Protocol):
    @abstractmethod
    def register_observer(self, observer: Observer):
        ...

    @abstractmethod
    def remove_observer(self, observer: Observer):
        ...

    @abstractmethod
    def notify(self):
        ...


class DisplayElement(Protocol):
    @abstractmethod
    def display(self):
        ...
