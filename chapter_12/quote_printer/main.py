from random import randint
from typing import Sequence

quotes = (
    'A man is not complete until he is married. Then he is finished.',
    'As I said before, I never repeat myself.',
    'Behind a successful man is an exhausted woman.',
    'Black holes really suck...', 'Facts are stubborn things.'
)


class QuoteModel:
    def __init__(self, quote_storage: Sequence) -> None:
        self.quotes = quote_storage

    def get_quote(self, index: int) -> str:
        index = self.validate_index(index)
        try:
            result = self.quotes[index]
        except IndexError:
            result = 'Not found'
        return result

    def validate_index(self, index: str) -> int:
        try:
            index = int(index)
        except ValueError:
            raise ValueError
        return index

    def get_random_quote(self) -> str:
        return self.quotes[randint(0, len(quotes) - 1)]


class QuoteTerminalView:
    def show(self, quote: str) -> None:
        print(f'''The quote is: {quote}''')

    def error(self, msg: str) -> None:
        print(f'''Error: {msg}''')

    def select_quote(self) -> str:
        return input('''What quote number would you like to see?\nEnter 'r' to see a random quote.\n''')


class QuoteTerminalController:
    def __init__(self) -> None:
        self.model = QuoteModel(quotes)
        self.view = QuoteTerminalView()

    def run(self) -> None:
        valid_input = False
        while not valid_input:
            index = self.view.select_quote()
            if index == 'r':
                quote = self.model.get_random_quote()
                valid_input = True
            else:
                try:
                    quote = self.model.get_quote(index)
                except ValueError:
                    return self.view.error('Incorrect index')
                valid_input = True
        self.view.show(quote)


def main() -> None:
    controller = QuoteTerminalController()
    while True:
        controller.run()


if __name__ == '__main__':
    main()
