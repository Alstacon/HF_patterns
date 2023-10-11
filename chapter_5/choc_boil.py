class ChocolateBoilerSingletone(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(ChocolateBoilerSingletone, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TheChocolateBoiler(metaclass=ChocolateBoilerSingletone):
    def __init__(self):
        self.__empty = True
        self.__boiled = False

    @property
    def empty(self) -> bool:
        return self.__empty

    @property
    def boiled(self) -> bool:
        return self.__boiled

    def fill(self) -> None:
        if self.empty:
            self.__empty = False
            self.__boiled = False
            print('Filling the boiler...')

    def boil(self) -> None:
        if not self.empty and not self.boiled:
            self.__boiled = True
            print('Boiling...')

    def drain(self) -> None:
        if not self.empty and self.boiled:
            self.__empty = True
            print('Draining...')
