from menu_classes import Menu, MenuItem
from dishes import breakfast, dinner
from waitress_class import Waitress


def menu_test_drive():
    pancake_menu = Menu('PANCAKE MENU', 'Breakfast')
    dinner_menu = Menu('DINNER MENU', 'Lunch')
    all_menus = Menu('ALL MENUS', 'All menus combined')
    all_menus.add(pancake_menu)
    all_menus.add(dinner_menu)

    for item in breakfast:
        pancake_menu.add(MenuItem(*item))
    for item in dinner:
        dinner_menu.add(MenuItem(*item))
    waitress = Waitress(all_menus)
    waitress.print_menu()


if __name__ == '__main__':
    menu_test_drive()
