from chapter_3 import starbuzz_menu


def get_coffee():
    espresso = starbuzz_menu.Espresso('SMALL')
    print(f'''{espresso.get_description()}: {espresso.cost()}''')

    house_blend = starbuzz_menu.HouseBlend('LARGE')
    house_blend = starbuzz_menu.Mocha(house_blend)
    house_blend = starbuzz_menu.Whip(house_blend)
    house_blend = starbuzz_menu.Soy(house_blend)

    print(f'''{house_blend.get_description()}: {house_blend.cost()}''')


if __name__ == '__main__':
    get_coffee()
