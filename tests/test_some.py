import requests
from jsonschema import validate

from src.baseclasses.response import Response
from src.schemas.get_spaxcexdata_info_schema import GET_SCHEMA
from configuration import SERVICE_URL
from schemas.get_spaxcexdata_info_pydantic import spacexdata_info

def test_getting_posts():
    r = requests.get(url = SERVICE_URL)
    response = Response(r)

    response.assert_status_code(200).validate(GET_SCHEMA)
    response.assert_len_response(15).validate_pydantic(spacexdata_info)
    response.assert_ceo('Elon Musk')
