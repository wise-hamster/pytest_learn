import pytest

from src.baseclasses.response import Response
from src.schemas.get_gorest_users_pydantic import UserList

from src.generators.player_local import PlayerLocal
from src.schemas.pydantic_computer import comp,Computer
from pydantic import model_validator
from pydantic import BaseModel

def test_getting_users_list(get_users,make_number):
    Response(get_users).assert_status_code(200).validate_pydantic(UserList)

#Используется для пропускания теста. Удобно, чтобы не комментировать код.
#Используем фикстуру @pytest.mark.skip
@pytest.mark.skip('[PYTEST-SKIP-148]')
def test_another():
    assert 1==1

#Используем фикстуру pytest.mark.development для запуска тестов по маркировке.
#Чтобы запустить нужно использовать -k c названием маркировки -k development
#Можно использовать наоборот -k "not development"
@pytest.mark.development
#Использование нескольких тестовых сценариев в одном тесте с помощью parametrize
#Используем фикстуру @pytest.mark.parametrize
@pytest.mark.parametrize('first_value, second_value, result,',
                         [(1,2,3),
                          (2,4,6),
                          (-1,2,1),
                          ('b',-2, None),
                          ('b', 'b', None),
                          (1.5, 1.5, 3.0)])
def test_calculator(first_value,second_value, result,calculate):
    assert calculate(first_value,second_value) == result

@pytest.mark.parametrize('status', [
    'ACTIVE',
    'BANNED',
    'DELETED',
    'INACTIVE'])
def test_status(status, get_player_generator):
    pass

@pytest.mark.parametrize('balance',[
    100,
    10,
    -1,
    3])
def test_balance (balance, get_player_generator):
    pass

@pytest.mark.parametrize('delete_key', [
    "account_status",
    "balance",
    "localize",
    "avatar"
])
def test_delete_key(delete_key, get_player_generator):
    object_to_send = get_player_generator.build()
    del object_to_send[delete_key]
    pass

@pytest.mark.parametrize('localizations, loc',[ ('fr', 'fr_FR')])

def test_something_3(get_player_generator,localizations, loc):
  object_to_send = get_player_generator.update_inner_value(['localize',localizations],PlayerLocal(loc).set_number(15).build()).build()
  print(object_to_send)

def test_comp ():
    comp_1 = Computer.model_validate(comp)
    host_v4 = comp_1.host_v4
    print(comp_1.model_json_schema())
    assert str(host_v4) == "192.168.1.1"

