from menu_classes import MenuComponent


class Waitress:
    def __init__(self, menus):
        self.all_menus: MenuComponent = menus

    def print_menu(self) -> None:
        self.all_menus.print()
