from chapter_3.interfaces import Beverage, CondimentDecorator


### Beverages ###

class Espresso(Beverage):
    PRICES = {
        'SMALL': 1.80,
        'MEDIUM': 1.99,
        'LARGE': 2.15,
    }

    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.description = 'Espresso'

    def cost(self) -> float:
        return self.PRICES.get(self.size)


class HouseBlend(Beverage):
    PRICES = {
        'SMALL': 0.60,
        'MEDIUM': 0.80,
        'LARGE': 1.15,
    }

    def __init__(self, size: str) -> None:
        super().__init__(size)
        self.description = 'House Blend Coffee'

    def cost(self) -> float:
        return self.PRICES.get(self.size)


### Condiments ###

class Mocha(CondimentDecorator):
    PRICES = {
        'SMALL': 0.10,
        'MEDIUM': 0.15,
        'LARGE': 0.20,
    }

    def get_description(self) -> str:
        return f'''{self.beverage.get_description()} + Mocha'''

    def cost(self) -> float:
        return round(self.beverage.cost() + self.PRICES.get(self.beverage.size), 2)


class Whip(CondimentDecorator):
    PRICES = {
        'SMALL': 0.10,
        'MEDIUM': 0.20,
        'LARGE': 0.35,
    }

    def get_description(self) -> str:
        return f'''{self.beverage.get_description()} + Whip'''

    def cost(self) -> float:
        return round(self.beverage.cost() + self.PRICES.get(self.beverage.size), 2)


class Soy(CondimentDecorator):
    PRICES = {
        'SMALL': 0.10,
        'MEDIUM': 0.15,
        'LARGE': 0.20,
    }

    def get_description(self) -> str:
        return f'''{self.beverage.get_description()} + Soy'''

    def cost(self) -> float:
        return round(self.beverage.cost() + self.PRICES.get(self.beverage.size), 2)
