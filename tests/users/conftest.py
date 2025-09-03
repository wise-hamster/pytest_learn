import pytest

from configuration import SERVICE_URL_2
from src.generators.player import Player
import requests

@pytest.fixture(scope='function',autouse=True)
def get_users():
    response = requests.get(SERVICE_URL_2)
    return response

#scope = function - выполняется каждый раз
#scope = session - кэшируется и в рамках всего теста используется 1 раз
#autouse = True - автоиспользование перед каждой функцией.
#autouse = False - не используется перед каждой функцией, если конктрено не указать.

@pytest.fixture
def get_player_generator():
    return Player()