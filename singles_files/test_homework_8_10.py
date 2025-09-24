import requests
from enum import Enum
from dataclasses import dataclass
from typing import List
from datetime import datetime

class URL(Enum):
    DOMEN = 'https://swapi.dev/api/'

class GetResponse:

    @staticmethod
    def get_request(endpoint, domen = URL.DOMEN.value):
        url = f'{domen}{endpoint}'
        response = requests.get(url)
        return response

@dataclass
class Schema:
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List [str]
    species: List [str]
    vehicles: List [str]
    starships: List [str]
    created: datetime
    edited: datetime
    url: str

class CheckCorrect:

    @staticmethod
    def check_status_code(response,expected_status_code):
        assert response.status_code == expected_status_code, f'FAIL: Status code incorrect. Status code: {response.status_code}'
        print('Status code correct')

    @staticmethod
    def check_schema(response,schema):
        assert schema(**response.json()), f'FAIL: Incorrect body response.'  
        print('Schema code correct')

class Actor:

    def __init__(self, actors=None):
        self.actors = actors if actors is not None else []
    
    def update(self,element):
        self.actors.append(element)
        return self.actors
    
    def status_list(self):
        return self.actors

class Test_Actor:
    def test_darth_vader(self):
        response = GetResponse.get_request('people/4/')
        CheckCorrect.check_status_code(response,200)
        CheckCorrect.check_schema(response,Schema)

