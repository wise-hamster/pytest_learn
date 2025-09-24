import requests
import json

class Checking():

    '''Method for check status code'''
    @staticmethod
    def check_status_code(response,status_code):

        assert response.status_code == status_code, f'Fail status code'
        if response.status_code == status_code:
            print(f'successfully status code == {response.status_code}')

    @staticmethod
    def  check_json_token(response, expected_value):
        token = response.json()
        assert list(token) == expected_value, f'No keys found'
        print('All keys are present')