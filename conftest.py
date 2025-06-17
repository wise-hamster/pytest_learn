import pytest

from random import randrange

@pytest.fixture
def get_numbers():
    return randrange(1,100)


def _calculate(a,b):
    return a+b

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    print('I am getting number')
    number = randrange(1,100)
    yield number
    print(f'Number at home {number}')
