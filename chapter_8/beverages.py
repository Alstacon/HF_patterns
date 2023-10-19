from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):

    def prepare(self):
        self.boil_water()
        self.brew()
        self.add_condiments()
        self.pour_in_cup()

    def boil_water(self) -> None:
        print('''Boiling water...''')

    @abstractmethod
    def brew(self):
        ...

    def pour_in_cup(self) -> None:
        print('''Pouring in the cup...''')
        print('''Enjoy!''')

    @abstractmethod
    def add_condiments(self):
        ...

    @property
    def need_condiments(self):
        return True


class Tea(CaffeineBeverage):
    def brew(self) -> None:
        print('''Steeping the tea''')

    @property
    def need_condiments(self):
        print(f'''Do you want to add the lemon slice into the tea? (yes/no):''')
        answer = input().lower()
        answer = answer.rstrip()
        if answer == 'yes':
            return True
        return False

    def add_condiments(self):
        if self.need_condiments:
            print('''Add lemon slice''')


class Coffee(CaffeineBeverage):
    def brew(self) -> None:
        print('''Dripping coffee through filter...''')

    @property
    def need_condiments(self):
        print(f'''Would you like milk and sugar with your coffee? (yes/no):''')
        answer = input().lower()
        answer = answer.rstrip()
        if answer == 'yes':
            return True
        return False

    def add_condiments(self):
        if self.need_condiments:
            print('''Adding sugar and milk...''')
