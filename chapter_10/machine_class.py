from states import SoldState, SoldOutState, HasQuarterState, HasNoQuarterState, WinnerState


class GumballMachine:
    def __init__(self, max_gumballs: int):
        self.has_quarter_state = HasQuarterState(self)
        self.has_no_quarter_state = HasNoQuarterState(self)
        self.sold_state = SoldState(self)
        self.sold_out_state = SoldOutState(self)
        self.winner_state = WinnerState(self)

        self.max_count = max_gumballs
        self.count = self.max_count

        if self.max_count > 0:
            self.state = self.has_no_quarter_state
        else:
            self.state = self.sold_out_state

    def insert_quarter(self):
        self.state.insert_quarter()

    def eject_quarter(self):
        self.state.eject_quarter()

    def turn_crank(self):
        self.state.turn_crank()
        if self.state == self.sold_state:
            self.state.dispense()

    def refill(self):
        self.count = self.max_count

    def release_gumball(self):
        if self.count > 0:
            self.count -= 1
            print(f'''The ball was released. Remain {self.count}''')

    def set_state(self, state):
        self.state = state

    def get_count(self):
        return self.count

    def get_no_quarter_state(self):
        return self.has_no_quarter_state

    def get_sold_state(self):
        return self.sold_state

    def get_has_quarter_state(self):
        return self.has_quarter_state

    def get_sold_out_state(self):
        return self.sold_out_state

    def get_winner_state(self):
        return self.winner_state

    def __str__(self):
        return f'''Gumball machine with {self.count} gumballs'''
