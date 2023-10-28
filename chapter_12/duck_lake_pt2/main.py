from chapter_12.duck_lake_pt2.birds import GooseAdaptedFactory
from chapter_12.duck_lake_pt2.observers import Quackologist
from ducks import Quackable, Flock
from service import QuackCounter
from fabrics import CountingDuckFactory


class DuckSimulator:
    def __init__(self):
        self.factory = CountingDuckFactory()
        self.goose_factory = GooseAdaptedFactory()
        self.simulate()

    def simulate(self):
        ducks = [self.factory.create_mallard_duck(), self.factory.create_redhead_duck(),
                 self.factory.create_rubber_duck(), self.factory.create_duck_call(),
                 self.factory.create_adapted_bird(self.goose_factory.create_goose())
                 ]

        duck_flock = Flock()
        for duck in ducks:
            duck_flock.add(duck)

        mallard_ducks = [self.factory.create_mallard_duck(), self.factory.create_mallard_duck(),
                         self.factory.create_mallard_duck()]

        mallard_duck_flock = Flock()
        for duck in mallard_ducks:
            mallard_duck_flock.add(duck)

        mallard = self.factory.create_mallard_duck()

        mallard_quackologist = Quackologist()
        mallard.register_observer(mallard_quackologist)

        quackologist = Quackologist()
        duck_flock.register_observer(quackologist)

        print('''Simulator with observer:''')
        print(' ' * 15)

        self.simulate_quack(duck_flock)

        print('-' * 15)

        print('''Simulate with one duck''')
        print(' ' * 15)

        self.simulate_quack(mallard)

        print(f'''Total amount of quacks: {QuackCounter.get_quacks()}''')

    def simulate_quack(self, duck: Quackable):
        duck.quack()


if __name__ == '__main__':
    DuckSimulator()
