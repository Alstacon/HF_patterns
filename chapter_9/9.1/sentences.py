import re


class Sentence:

    def __init__(self, text: str):
        self.text = text
        self.words = re.compile(r'[\w\']+').findall(text)

    def __str__(self):
        return f'''Sentence({self.text}'''

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceDict:

    def __init__(self, text: dict):
        self.text = text
        self.words = [v for k, v in text.items() if re.match(r'[\w\']+', v)]

    def __str__(self):
        return f'''Sentence({self.text}'''

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceSet:

    def __init__(self, text: set):
        self.text = text
        self.words = [v for v in text if re.match(r'[\w\']+', v)]

    def __str__(self):
        return f'''Sentence({self.text}'''

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:
    def __init__(self, words: list):
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self