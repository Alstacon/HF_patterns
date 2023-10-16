### Adapters
from chapter_1.duck_lake import MallardDuck
from chapter_7.adapter import WildTurkey, TurkeyAdapter, DuckAdapter
from chapter_7.facade import HomeTheaterFacade


def adapters_test():
    duck = MallardDuck()
    turkey = WildTurkey()

    turkey_adapter = TurkeyAdapter(turkey)
    duck_adapter = DuckAdapter(duck)

    print('''The turkey says:''')
    turkey.gobble()
    turkey.fly()

    print('''the duck says:''')
    duck.perform_quack()

    print('''The turkey adapter says:''')
    turkey_adapter.quack()
    turkey_adapter.fly()

    print('-' * 10)

    print('''The duck adapter says:''')
    duck_adapter.gobble()
    duck_adapter.fly()


### Facade

def watch_movie():
    home_thater_facade = HomeTheaterFacade()
    home_thater_facade.watch_movie('Matrix')
    home_thater_facade.end_movie()


if __name__ == '__main__':
    adapters_test()
    watch_movie()
