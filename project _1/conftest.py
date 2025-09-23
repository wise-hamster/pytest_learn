import pytest

from random import randrange

@pytest.fixture
def get_numbers():
    return randrange(1,100)


def _calculate(a,b):
    if isinstance(a, (int ,float)) and isinstance (b, (int,float)):
        return a+b
    else:
        return None

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture
def make_number():
    number = randrange(1,100)
    yield number # такой же смысл как у return, но после выполнения очищает окружение.