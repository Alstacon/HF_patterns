from chapter_5.choc_boil import TheChocolateBoiler

if __name__ == '__main__':
    for _ in range(2):
        boiler = TheChocolateBoiler()
        print(
            f"The Chocolate Boiler {id(boiler)} created."
        )
        boiler.fill()
        boiler.boil()
        boiler.drain()
        print('-' * 10)
