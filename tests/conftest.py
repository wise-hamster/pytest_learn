import pytest

@pytest.fixture
def say_hello():
    print('hello')