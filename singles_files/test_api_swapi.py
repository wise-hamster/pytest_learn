import requests
from enum import Enum
from dataclasses import dataclass
from typing import List
from datetime import datetime
import pytest

class URL(Enum):
    DOMEN = 'https://swapi.dev/api/'

class GetResponse:

    @staticmethod
    def get_request(endpoint=None, domen=URL.DOMEN.value, url_full=None):
        if url_full is None:
            url = f'{domen}{endpoint}'
        else:
            url = url_full
        response = requests.get(url)
        return response

@dataclass
class Schema_Films:
    title: str
    episode_id: int
    opening_crawl: str
    director: str
    producer: str
    release_date:str
    characters: List[str]
    planets: List[str]
    starships: List[str]
    vehicles: List[str]
    species: List[str]
    created: datetime
    edited: datetime
    url: str

@dataclass
class Schema_Characters:
    name: str
    height: str
    mass: str
    hair_color: str
    skin_color: str
    eye_color: str
    birth_year: str
    gender: str
    homeworld: str
    films: List[str]
    species: List[str]
    vehicles: List[str]
    starships: List[str]
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


class Films:
    def __init__(self, episode=None, characters=None):
        self.episode = episode if episode is not None else []
        self.characters = characters if characters is not None else set()

    @property
    def status_episode(self):
        return bool(self.episode)
    
    @property
    def status_set(self):
        return bool(self.characters)
    
    def update_set(self,element):
        self.characters.add(element)

    def iter_episode(self):
        return iter(self.episode)

    def iter_characters(self):
        return iter(self.characters)
    

class Test_actor:
    
      
    @pytest.fixture
    def darth_vader(self):
        response = GetResponse.get_request(endpoint='people/4/')
        CheckCorrect.check_status_code(response,200)
        CheckCorrect.check_schema(response, Schema_Characters)
        episode_list = Films(
            episode=response.json().get('films'))
        return episode_list
    
    
    def test_darth_vader_has_films(self, darth_vader):
        assert darth_vader.status_episode, 'Films list is empty'
        print(f"Found {len(darth_vader.episode)} films")
    
    
    @pytest.fixture
    def get_сharacters(self, darth_vader):
        for film in darth_vader.episode:
            response = GetResponse.get_request(url_full=film)
            CheckCorrect.check_status_code(response,200)
            CheckCorrect.check_schema(response, Schema_Films)
           
            for charter in response.json().get('characters'):
                if charter == 'https://swapi.dev/api/people/4/':
                    continue
                else:
                    darth_vader.update_set(charter)
        return darth_vader
                
    def test_charters_name(self, get_сharacters):
        assert get_сharacters.status_set, 'Character list is empty'
        print(f"Found {len(get_сharacters.characters)} characters")
        print(f'{get_сharacters.characters}')
