from chapter_4.store import NYStylePizzaStore, ChicagoStylePizzaStore


def eat_pizza():
    pizza_store_NY = NYStylePizzaStore()
    pizza_store_NY.order_pizza('cheese')
    print('-' * 10)
    pizza_store_chicago = ChicagoStylePizzaStore()
    pizza_store_chicago.order_pizza('veggie')


if __name__ == '__main__':
    eat_pizza()
