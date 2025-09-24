from utils.api import GoogleMapsApi
from requests import Response
from utils.checking import Checking

'''Create, modification and delete new location'''
class Test_create_place():

    def test_create_new_place(self):
        
        print('Method POST')
        response = GoogleMapsApi.post_new_place()
        check_post = response.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(response, 200)

        print('Method GET')
        response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(response, 200)
        
        print('Method PUT')
        response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(response, 200)
        Checking.check_json_token(response, ['msg'])

        print('Method DELETE')
        response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(response, 200)

        print('Method GET')
        response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(response, 404)