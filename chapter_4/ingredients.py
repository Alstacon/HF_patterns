from abc import ABC, abstractmethod


# Ingredients
class ThinCrustDough:
    def __str__(self) -> str:
        return 'Thin Crust Dough'


class ThickCrustDough:
    def __str__(self) -> str:
        return 'Thick Crust Dough'


class MarinaraSauce:
    def __str__(self) -> str:
        return 'Marinara Sauce'


class PlumTomatoSauce:
    def __str__(self) -> str:
        return 'Plum Tomato Sauce'


class ReggianoCheese:
    def __str__(self) -> str:
        return 'Reggiano Cheese'


class MozzarellaCheese:
    def __str__(self) -> str:
        return 'Mozzarella Cheese'


class Garlic:
    def __str__(self) -> str:
        return 'Garlic'


class EggPlant:
    def __str__(self) -> str:
        return 'EggPlant'


class Spinach:
    def __str__(self) -> str:
        return 'EggPlant'


class BlackOlives:
    def __str__(self) -> str:
        return 'EggPlant'


class Onion:
    def __str__(self) -> str:
        return 'Onion'


class Mushroom:
    def __str__(self) -> str:
        return 'Mushroom'


class RedPepper:
    def __str__(self) -> str:
        return 'Red Pepper'


class SlicedPepperoni:
    def __str__(self) -> str:
        return 'Sliced Pepperoni'


class FreshClams:
    def __str__(self) -> str:
        return 'Fresh Clams'


class FrozenClams:
    def __str__(self) -> str:
        return 'Frozen Clams'


# Ingredient Factories

class PizzaIngredientsFactory(ABC):
    @abstractmethod
    def create_dough(self):
        ...

    @abstractmethod
    def create_sauce(self):
        ...

    @abstractmethod
    def create_cheese(self):
        ...

    @abstractmethod
    def create_veggies(self):
        ...

    @abstractmethod
    def create_pepperoni(self):
        ...


class NYPizzaIngredientsFactory(PizzaIngredientsFactory):
    def create_cheese(self):
        return ReggianoCheese()

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()


class ChicagoPizzaIngredientsFactory(PizzaIngredientsFactory):
    def create_cheese(self):
        return MozzarellaCheese()

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_veggies(self):
        return [EggPlant(), Spinach(), BlackOlives()]

    def create_pepperoni(self):
        return SlicedPepperoni()
