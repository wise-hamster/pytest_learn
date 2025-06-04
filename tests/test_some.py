import requests
from jsonschema import validate

from src.baseclasses.response import Response
from src.schemas.get import GET_SCHEMA
from config import SERVICE_URL

print(Response)
print(GET_SCHEMA)
print(SERVICE_URL)

def test_getting_posts():
    r = requests.get(url = SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(GET_SCHEMA)
    response.assert_len_response(15)
    response.assert_ceo('Elon Musk')

