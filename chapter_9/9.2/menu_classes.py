from abc import ABC


class MenuComponent(ABC):
    def add(self, menu_component: 'MenuComponent') -> None:
        raise NotImplementedError()

    def remove(self, menu_component: 'MenuComponent') -> None:
        raise NotImplementedError()

    def get_child(self, idx: int) -> 'MenuComponent':
        raise NotImplementedError()

    def get_description(self) -> str:
        raise NotImplementedError()

    def get_name(self) -> str:
        raise NotImplementedError()

    def get_price(self) -> float:
        raise NotImplementedError()

    def is_vegetarian(self) -> bool:
        raise NotImplementedError()

    def print(self) -> None:
        raise NotImplementedError()


class MenuItem(MenuComponent):
    '''Leaf node class'''

    def __init__(self, name: str, description: str, vegetarian: bool, price: float) -> None:
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_price(self) -> float:
        return self.price

    def is_vegetarian(self) -> bool:
        return self.vegetarian

    def print(self) -> None:
        veg_str = 'Not vegetarian' if not self.is_vegetarian() else 'Vegetarian'
        print(f'''
            {self.get_name()}
            {veg_str}
            {self.get_price()}
            {self.get_description()}
            ''')


class Menu(MenuComponent):
    '''Combination node class'''

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

        self.menu_components: list[MenuComponent] = []

    def add(self, menu_component: MenuComponent) -> None:
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent) -> None:
        self.menu_components.append(menu_component)

    def get_child(self, idx: int) -> 'MenuComponent':
        return self.menu_components[idx]

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def print(self):
        print(f'''{self.name}\n{self.description}''')
        print('-' * 20)
        for component in self.menu_components:
            component.print()
