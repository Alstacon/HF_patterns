from abc import ABC, abstractmethod

from chapter_4.exception import UnknownPizzaError
from chapter_4.ingredients import NYPizzaIngredientsFactory, ChicagoPizzaIngredientsFactory
from chapter_4.pizza_itself import Pizza, VeggiePizza, CheesePizza


class PizzaStore(ABC):
    PIZZA_MENU = {
        'cheese': CheesePizza,
        'veggie': VeggiePizza
    }

    @abstractmethod
    def ingredients_factory(self):
        ...

    def order_pizza(self, name: str) -> Pizza:
        if not self.PIZZA_MENU.get(name):
            raise UnknownPizzaError

        pizza = self._create_pizza(name)
        pizza.set_name()
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    def _create_pizza(self, name) -> Pizza:
        pizza = self.PIZZA_MENU.get(name)(self.ingredients_factory())
        return pizza


class NYStylePizzaStore(PizzaStore):
    def ingredients_factory(self):
        return NYPizzaIngredientsFactory()


class ChicagoStylePizzaStore(PizzaStore):
    def ingredients_factory(self):
        return ChicagoPizzaIngredientsFactory()
