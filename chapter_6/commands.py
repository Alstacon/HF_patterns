from abc import ABC, abstractmethod

from chapter_6.devices import DefaultDeviceFuncs


class Command(ABC):
    """
    Abstract command class
    """

    def __init__(self, device: DefaultDeviceFuncs):
        self.device = device

    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...

    def __repr__(self):
        return f'''{self.__class__.__name__}, {self.device}'''


class NoCommand(Command):
    """
    Class for unset command
    """

    def execute(self) -> None:
        print('''The command wasn't set.''')

    def undo(self) -> None:
        print('''The command wasn't set.''')


class TurnOnCommand(Command):
    def execute(self) -> None:
        if self.device.is_on:
            print(f'''The {self.device} is already on''')
        else:
            self.device.on()
            print(f'''The {self.device} was turned on''')

    def undo(self):
        self.device.off()
        print(f'''The {self.device} was turned off''')


class TurnOffCommand(Command):
    def execute(self):
        if not self.device.is_on:
            print(f'''The {self.device} is already off''')
        else:
            self.device.off()
            print(f'''The {self.device} was turned off''')

    def undo(self):
        self.device.on()
        print(f'''The {self.device} was turned on''')


class MacroCommands:
    def __init__(self, commands: list[Command]):
        self.commands: list[Command] = commands

    def set_commands(self, commands: list[Command]):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()

    def __repr__(self):
        return f'''{self.__class__.__name__} for {[command.device for command in self.commands]}'''



