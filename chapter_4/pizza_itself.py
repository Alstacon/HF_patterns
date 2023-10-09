from abc import ABC, abstractmethod

from chapter_4.ingredients import PizzaIngredientsFactory


class Pizza(ABC):
    def __init__(self, ingredients_factory: PizzaIngredientsFactory):
        self.name = None
        self.ingredients_factory = ingredients_factory

    @abstractmethod
    def prepare(self) -> None:
        ...

    @abstractmethod
    def set_name(self):
        ...

    def bake(self) -> None:
        print('''Bake for 25 min at 350''')

    def cut(self) -> None:
        print('''Cutting the pizza''')

    def box(self) -> None:
        print('''Place pizza in box''')


class CheesePizza(Pizza):
    def set_name(self):
        self.name = 'Cheese pizza'

    def prepare(self) -> None:
        print(f'''Preparing {self.name}''')
        dough = self.ingredients_factory.create_dough()
        sauce = self.ingredients_factory.create_sauce()
        cheese = self.ingredients_factory.create_cheese()


class VeggiePizza(Pizza):
    def set_name(self):
        self.name = 'Veggie pizza'

    def prepare(self) -> None:
        print(f'''Preparing {self.name}''')
        dough = self.ingredients_factory.create_dough()
        sauce = self.ingredients_factory.create_sauce()
        cheese = self.ingredients_factory.create_cheese()
