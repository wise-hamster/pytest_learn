import requests

from src.baseclasses.response import Response
from src.schemas.get_gorest_users_pydantic import UserList


def test_getting_users_list(get_users,make_number):
    Response(get_users).assert_status_code(200).validate_pydantic(UserList)
    print(make_number)


def test_another():
    assert 1==1

