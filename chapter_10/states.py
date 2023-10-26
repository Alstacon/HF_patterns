from abc import ABC, abstractmethod
from random import randint

class State(ABC):
    def __init__(self, machine):
        self.machine = machine

    @abstractmethod
    def insert_quarter(self) -> None:
        ...

    @abstractmethod
    def eject_quarter(self) -> None:
        ...

    @abstractmethod
    def turn_crank(self) -> None:
        ...

    @abstractmethod
    def dispense(self) -> None:
        ...

    @abstractmethod
    def refill(self) -> None:
        ...


class HasQuarterState(State):
    def insert_quarter(self) -> None:
        print('''You've already inserted a quarter''')

    def eject_quarter(self) -> None:
        self.machine.set_state(self.machine.get_no_quarter_state())
        print('''The quarter was ejected''')

    def turn_crank(self) -> None:
        print('''You turned...''')
        number = randint(1, 10)
        if number == 10:
            print('''10! You win!''')
            self.machine.set_state(self.machine.get_winner_state())
        else:
            self.machine.set_state(self.machine.get_sold_state())

    def dispense(self) -> None:
        print('''No gumball dispensed. You need to turn the crank first''')

    def refill(self) -> None:
        ...


class HasNoQuarterState(State):
    def insert_quarter(self) -> None:
        self.machine.set_state(self.machine.get_has_quarter_state())
        print('''You inserted a quarter''')

    def eject_quarter(self) -> None:
        print('''No quarter to eject''')

    def turn_crank(self) -> None:
        print('''You need to insert a quarter first''')

    def dispense(self) -> None:
        print('''You need to insert a quarter first''')

    def refill(self) -> None:
        ...


class SoldState(State):
    def insert_quarter(self) -> None:
        print('''Please wait, we’re already giving you a gumball''')

    def eject_quarter(self) -> None:
        print('''Sorry, you already turned the crank''')

    def turn_crank(self) -> None:
        print('''Turning twice doesn’t get you another gumball''')

    def dispense(self) -> None:
        self.machine.release_gumball()
        if self.machine.get_count() > 0:
            self.machine.set_state(self.machine.get_no_quarter_state())
        else:
            self.machine.set_state(self.machine.get_sold_out_state())
            print('''Oops, out of gumballs''')

    def refill(self) -> None:
        ...


class SoldOutState(State):
    def insert_quarter(self) -> None:
        print('''Oops, out of gumballs. The machine needs to be refilled''')

    def eject_quarter(self) -> None:
        print('''Oops, out of gumballs. The machine needs to be refilled. You didn't insert a quarter though''')

    def turn_crank(self) -> None:
        print('''Turning twice doesn’t get you another gumball''')

    def dispense(self) -> None:
        print('''Oops, out of gumballs. The machine needs to be refilled. You didn't insert a quarter though''')

    def refill(self) -> None:
        self.machine.refill()
        self.machine.set_state(self.machine.get_no_quarter_state())
        print('''The machine was refilled. Now you can insert a quarter''')


class WinnerState(State):
    def insert_quarter(self) -> None:
        print('''Please wait, we’re already giving you a gumballs''')

    def eject_quarter(self) -> None:
        print('''Sorry, you already turned the crank''')

    def turn_crank(self) -> None:
        print('''Oops, out of gumballs. The machine needs to be refilled. You didn't insert a quarter though''')

    def dispense(self) -> None:
        self.machine.release_gumball()
        if self.machine.get_count() > 0:
            print('''You won the second gumball!''')
            self.machine.release_gumball()
            if self.machine.get_count() > 0:
                self.machine.set_state(self.machine.get_no_quarter_state())
            else:
                self.machine.set_state(self.machine.get_sold_out_state())
                print('''Oops, out of gumballs''')
        else:
            self.machine.set_state(self.machine.get_sold_out_state)
            print('''Oops, out of gumballs''')

    def refill(self) -> None:
        self.machine.refill()
        self.machine.set_state(self.machine.get_no_quarter_state())
        print('''The machine was refilled. Now you can insert a quarter''')