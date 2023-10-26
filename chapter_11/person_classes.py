from abc import ABC


class AbstractPerson(ABC):
    def __init__(self, name: str, gender: str, interests: str):
        self._name = name
        self._gender = gender
        self._interests = interests
        self._geek_rating = 0
        self.rating_count = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        self._gender = gender

    @property
    def interests(self):
        return self._interests

    @interests.setter
    def interests(self, interests: str):
        self._interests = interests

    @property
    def geek_rating(self):
        return self._geek_rating // self.rating_count if self.rating_count != 0 else 0

    @geek_rating.setter
    def geek_rating(self, geek_rating: str):
        self._geek_rating += geek_rating
        self.rating_count += 1

    def __str__(self):
        return f'''{self.name}: rating {self.geek_rating}'''


class Person(AbstractPerson):
    ...


class Proxy(AbstractPerson):
    '''
    Proxy for person profile model
    '''

    def __init__(self, person: Person):
        self.person = person

    @property
    def name(self):
        return self.person.name

    def set_name(self, name: str):
        self.person.name = name

    @property
    def gender(self):
        return self.person.gender

    def set_gender(self, gender: str):
        self.person.gender = gender

    @property
    def interests(self):
        return self.person.interests

    def set_interests(self, interests: str):
        self.person.interests = interests

    @property
    def geek_rating(self):
        return self.person.geek_rating // self.person.rating_count if self.person.geek_rating != 0 else 0

    def set_geek_rating(self, geek_rating: str):
        self.person.geek_rating += geek_rating
        self.person.rating_count += 1


class OwnerProxy(Proxy):
    '''
    Proxy for profile owner
    '''

    def set_geek_rating(self, geek_rating: str):
        print('''You can't change your rating yourself''')


class NoOwnerProxy(Proxy):
    '''
    Proxy for visitors
    '''

    def set_name(self, name: str) -> None:
        print('''You can't change others name''')

    def set_gender(self, gender: str) -> None:
        print('''You can't change others gender''')

    def set_interests(self, interests: str) -> None:
        print('''You can't change others interests''')
