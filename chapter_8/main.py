from chapter_8.beverages import Tea, Coffee


def order_beverage():
    tea = Tea()
    tea.prepare()

    print('-' * 10)

    coffee = Coffee()
    coffee.prepare()


if __name__ == '__main__':
    order_beverage()
