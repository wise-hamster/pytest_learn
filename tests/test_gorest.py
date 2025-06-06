import requests
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent)) 

from configuration import SERVICE_URL_2
from src.baseclasses.response import Response
from src.schemas.gorest_users import UserList


resp = requests.get(SERVICE_URL_2)

def test_getting_users_list():
    response = requests.get(SERVICE_URL_2)
    test_object = Response(response)
    test_object.assert_status_code(200).validate_pydantic(UserList)