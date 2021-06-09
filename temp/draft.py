import os


class Dar:
    def a(self):
        pass

    def ab(self):
        pass

    def b(self):
        pass


s = "my.website"

os.path.isfile('')

m = {
    'x': 2,
    'y': 3
}

x = list()
x.append(2)

c = f"I know {x}"

d = Dar()


def is_even_number(n):
    return n % 2 == 0


def is_odd_number(n):
    return not is_even_number(n)


def get_square(n):
    return n**2


from unittest import TestCase


class NumberTestCase(TestCase):
    def test_is_even_number(self):
        self.fail()
