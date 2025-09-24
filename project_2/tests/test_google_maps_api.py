from utils.api import GoogleMapsApi
from requests import Response

'''Create, modification and delete new location'''
class Test_create_place():

    def test_create_new_place(self):
        
        print('Method POST')
        result_post: Response = GoogleMapsApi.post_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('Method GET')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        
        print('Method PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        print('Method DELETE')
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)

        print('Method GET')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)